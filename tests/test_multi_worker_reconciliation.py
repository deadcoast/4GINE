import unittest
from collections.abc import Mapping, MutableMapping
from dataclasses import replace
from typing import cast

from spinaltap.contract_kernel import (
    ContractRef,
    GateRef,
    RefusalCode,
    SignalBundle,
    TimePacket,
    refuse,
)
from spinaltap.reconciliation import SpinalReconciliationHarness, WorkerUpdate
from spinaltap.signal_spine import SignalConstraintSpine
from spinaltap.vertebra_delta import VertebraDeltaWorker


def fixed_step() -> TimePacket:
    return TimePacket(0.016, 0.016, 1, 0.0, 0.0, None)


def update(owner: str, key: str, value: float, *, hook: str = "VG03") -> WorkerUpdate:
    return WorkerUpdate(
        worker=VertebraDeltaWorker({key}),
        owner=owner,
        channel="motion.delta",
        constraint_set={"max_delta": 2.0},
        proposed_delta={key: value},
        validation_hook=hook,
    )


class MultiWorkerReconciliationTests(unittest.TestCase):
    def test_worker_cannot_modify_the_scheduled_local_snapshot(self):
        class MutatingWorker(VertebraDeltaWorker):
            def propose(self, **kwargs):
                kwargs["local_state_slice"]["x"] = -100
                return super().propose(**kwargs)

        job = replace(update("worker:x", "x", 1), worker=MutatingWorker({"x"}))
        result = SpinalReconciliationHarness().reconcile_step(
            state={"x": 0},
            time_packet=fixed_step(),
            updates=[job],
        )
        self.assertIsNone(result.next_state)
        self.assertEqual(result.ordered_bundles, ())
        assert result.refusal is not None
        self.assertEqual(result.refusal.code, RefusalCode.VALIDATION_FAILED)

    def test_worker_cannot_substitute_a_different_accepted_proposal(self):
        class SubstitutingWorker(VertebraDeltaWorker):
            def propose(self, **kwargs):
                packet = super().propose(**kwargs)
                return replace(packet, bounded_delta={"x": 2})

        job = replace(update("worker:x", "x", 1), worker=SubstitutingWorker({"x"}))
        result = SpinalReconciliationHarness().reconcile_step(
            state={"x": 0},
            time_packet=fixed_step(),
            updates=[job],
        )
        self.assertIsNone(result.next_state)
        self.assertEqual(result.ordered_bundles, ())
        assert result.refusal is not None
        self.assertEqual(result.refusal.code, RefusalCode.INVALID_PAYLOAD)

    def test_disjoint_workers_produce_one_read_only_candidate_in_declared_order(self):
        source = {"x": 0.0, "y": 10.0, "untouched": 4.0}
        result = SpinalReconciliationHarness().reconcile_step(
            state=source,
            time_packet=fixed_step(),
            updates=[update("worker:y", "y", -2), update("worker:x", "x", 1)],
        )
        self.assertIsNone(result.refusal)
        self.assertIsNone(result.failed_owner)
        self.assertEqual(result.next_state, {"x": 1.0, "y": 8.0, "untouched": 4.0})
        self.assertEqual(
            [bundle.owner for bundle in result.ordered_bundles],
            ["worker:y", "worker:x"],
        )
        self.assertEqual(source, {"x": 0.0, "y": 10.0, "untouched": 4.0})
        assert result.next_state is not None
        with self.assertRaises(TypeError):
            cast(MutableMapping[str, float], result.next_state)["x"] = 9
        source["x"] = 50
        self.assertEqual(result.next_state["x"], 1.0)

    def test_reordering_disjoint_updates_changes_bundle_order_but_not_candidate(self):
        harness = SpinalReconciliationHarness()
        jobs = [update("worker:x", "x", 1), update("worker:y", "y", -1)]
        first = harness.reconcile_step(
            state={"x": 0, "y": 0}, time_packet=fixed_step(), updates=jobs
        )
        second = harness.reconcile_step(
            state={"x": 0, "y": 0}, time_packet=fixed_step(), updates=jobs[::-1]
        )
        self.assertEqual(first.next_state, second.next_state)
        self.assertEqual(
            [bundle.owner for bundle in first.ordered_bundles], ["worker:x", "worker:y"]
        )
        self.assertEqual(
            [bundle.owner for bundle in second.ordered_bundles],
            ["worker:y", "worker:x"],
        )

    def test_all_workers_read_the_original_step_snapshot(self):
        observed = []

        def capture(bundle: SignalBundle):
            observed.append(dict(bundle.ordered_signal_bundle[0].local_state_slice))

        harness = SpinalReconciliationHarness(
            SignalConstraintSpine(validation_hooks={"capture": capture})
        )
        jobs = [
            replace(
                update("worker:x", "x", 1, hook="capture"),
                worker=VertebraDeltaWorker({"x", "y"}),
            ),
            replace(
                update("worker:y", "y", 2, hook="capture"),
                worker=VertebraDeltaWorker({"x", "y"}),
            ),
        ]
        result = harness.reconcile_step(
            state={"x": 3, "y": 4}, time_packet=fixed_step(), updates=jobs
        )
        self.assertEqual(result.next_state, {"x": 4, "y": 6})
        self.assertEqual(observed, [{"x": 3, "y": 4}, {"x": 3, "y": 4}])

    def test_overlapping_writes_are_refused_before_hooks_even_for_equal_values(self):
        observed = []

        def capture(bundle):
            observed.append(bundle)

        harness = SpinalReconciliationHarness(
            SignalConstraintSpine(validation_hooks={"capture": capture})
        )
        result = harness.reconcile_step(
            state={"x": 0},
            time_packet=fixed_step(),
            updates=[
                update("worker:first", "x", 1, hook="capture"),
                update("worker:second", "x", 1, hook="capture"),
            ],
        )
        self.assertIsNone(result.next_state)
        self.assertEqual(result.ordered_bundles, ())
        assert result.refusal is not None
        self.assertEqual(result.refusal.code, RefusalCode.WRITE_CONFLICT)
        self.assertIn("x", result.refusal.reason)
        self.assertIn("worker:first", result.refusal.reason)
        self.assertIn("worker:second", result.refusal.reason)
        self.assertEqual(observed, [])

    def test_duplicate_owner_is_refused_even_with_disjoint_writes(self):
        result = SpinalReconciliationHarness().reconcile_step(
            state={"x": 0, "y": 0},
            time_packet=fixed_step(),
            updates=[update("worker", "x", 1), update("worker", "y", 1)],
        )
        self.assertIsNone(result.next_state)
        assert result.refusal is not None
        self.assertEqual(result.refusal.code, RefusalCode.INVALID_PAYLOAD)

    def test_late_worker_refusal_discards_prior_accepted_bundle(self):
        source = {"x": 0.0, "y": 0.0}
        result = SpinalReconciliationHarness().reconcile_step(
            state=source,
            time_packet=fixed_step(),
            updates=[update("worker:x", "x", 1), update("worker:y", "y", 3)],
        )
        self.assertIsNone(result.next_state)
        self.assertEqual(result.ordered_bundles, ())
        self.assertEqual(result.failed_owner, "worker:y")
        assert result.refusal is not None
        self.assertEqual(result.refusal.code, RefusalCode.CONSTRAINT_VIOLATION)
        self.assertEqual(source, {"x": 0, "y": 0})

    def test_late_hook_refusal_or_exception_discards_the_entire_step(self):
        def rejecting(bundle):
            return refuse(
                ContractRef.DC03,
                GateRef.VG03,
                RefusalCode.VALIDATION_FAILED,
                "channel closed",
            )

        def raising(bundle):
            raise RuntimeError("hook failed")

        for hook in (rejecting, raising):
            with self.subTest(hook=hook.__name__):
                source = {"x": 0.0, "y": 0.0}
                harness = SpinalReconciliationHarness(
                    SignalConstraintSpine(validation_hooks={"late": hook})
                )
                result = harness.reconcile_step(
                    state=source,
                    time_packet=fixed_step(),
                    updates=[
                        update("worker:x", "x", 1),
                        update("worker:y", "y", 1, hook="late"),
                    ],
                )
                self.assertIsNone(result.next_state)
                self.assertEqual(result.ordered_bundles, ())
                self.assertEqual(result.failed_owner, "worker:y")
                self.assertEqual(source, {"x": 0, "y": 0})

    def test_raw_time_refusal_precedes_worker_execution(self):
        result = SpinalReconciliationHarness().reconcile_step(
            state={"x": 0},
            time_packet=cast(TimePacket, 0.016),
            updates=[update("worker", "x", 1)],
        )
        self.assertIsNone(result.next_state)
        assert result.refusal is not None
        self.assertEqual(result.refusal.code, RefusalCode.RAW_DT)

    def test_missing_state_key_cannot_be_created_by_a_worker(self):
        result = SpinalReconciliationHarness().reconcile_step(
            state={"x": 0},
            time_packet=fixed_step(),
            updates=[update("worker", "y", 1)],
        )
        self.assertIsNone(result.next_state)
        assert result.refusal is not None
        self.assertEqual(result.refusal.code, RefusalCode.OUTSIDE_LOCAL_SLICE)

    def test_invalid_scalar_state_is_refused_without_a_candidate(self):
        for state in (
            None,
            {"x": True},
            {"x": "1"},
            {"x": float("nan")},
            {"x": float("inf")},
            {"x": 10**1000},
            {"x": {"nested": 1}},
            {1: 0},
            {" ": 0},
        ):
            with self.subTest(state=repr(state)[:60]):
                result = SpinalReconciliationHarness().reconcile_step(
                    state=cast(Mapping[str, float], state),
                    time_packet=fixed_step(),
                    updates=[],
                )
                self.assertIsNone(result.next_state)
                assert result.refusal is not None
                self.assertEqual(result.refusal.code, RefusalCode.INVALID_PAYLOAD)

    def test_nonfinite_candidate_addition_refuses_all_updates(self):
        large = replace(
            update("worker:y", "y", 1e308), constraint_set={"max_delta": 1e308}
        )
        result = SpinalReconciliationHarness().reconcile_step(
            state={"x": 0, "y": 1e308},
            time_packet=fixed_step(),
            updates=[update("worker:x", "x", 1), large],
        )
        self.assertIsNone(result.next_state)
        self.assertEqual(result.ordered_bundles, ())
        assert result.refusal is not None
        self.assertEqual(result.refusal.code, RefusalCode.INVALID_PAYLOAD)

    def test_empty_ordered_batch_is_a_valid_snapshot_noop(self):
        result = SpinalReconciliationHarness().reconcile_step(
            state={"x": 4},
            time_packet=fixed_step(),
            updates=[],
        )
        self.assertEqual(result.next_state, {"x": 4})
        self.assertIsNone(result.refusal)
        self.assertEqual(result.ordered_bundles, ())

    def test_bad_update_metadata_is_refused_during_preflight(self):
        valid = update("worker", "x", 1)
        for job in (
            None,
            replace(valid, owner=" "),
            replace(valid, channel=""),
            replace(valid, validation_hook=""),
            replace(valid, proposed_delta=cast(Mapping[str, object], None)),
            replace(valid, constraint_set={1: 2}),
        ):
            with self.subTest(job=job):
                result = SpinalReconciliationHarness().reconcile_step(
                    state={"x": 0},
                    time_packet=fixed_step(),
                    updates=[cast(WorkerUpdate, job)],
                )
                self.assertIsNone(result.next_state)
                self.assertIsNotNone(result.refusal)

    def test_unordered_or_lazy_batches_are_refused(self):
        for jobs in ({}, set(), iter([]), "workers"):
            with self.subTest(jobs=jobs):
                result = SpinalReconciliationHarness().reconcile_step(
                    state={"x": 0},
                    time_packet=fixed_step(),
                    updates=cast(list[WorkerUpdate], jobs),
                )
                self.assertIsNone(result.next_state)
                self.assertIsNotNone(result.refusal)

    def test_update_mappings_are_snapshotted_before_any_hook_runs(self):
        second_delta = {"y": 1.0}

        def mutate_caller_payload(bundle):
            second_delta["y"] = 999.0

        harness = SpinalReconciliationHarness(
            SignalConstraintSpine(validation_hooks={"mutate": mutate_caller_payload})
        )
        second = replace(update("worker:y", "y", 1), proposed_delta=second_delta)
        result = harness.reconcile_step(
            state={"x": 0, "y": 0},
            time_packet=fixed_step(),
            updates=[
                update("worker:x", "x", 1, hook="mutate"),
                second,
            ],
        )
        self.assertEqual(second_delta["y"], 999.0)
        self.assertEqual(result.next_state, {"x": 1, "y": 1})

    def test_worker_exception_does_not_expose_a_partial_result(self):
        class RaisingWorker(VertebraDeltaWorker):
            def propose(self, **kwargs):
                raise RuntimeError("solver failed")

        second = replace(update("worker:y", "y", 1), worker=RaisingWorker({"y"}))
        result = SpinalReconciliationHarness().reconcile_step(
            state={"x": 0, "y": 0},
            time_packet=fixed_step(),
            updates=[update("worker:x", "x", 1), second],
        )
        self.assertIsNone(result.next_state)
        self.assertEqual(result.ordered_bundles, ())
        assert result.refusal is not None
        self.assertEqual(result.refusal.code, RefusalCode.VALIDATION_FAILED)


if __name__ == "__main__":
    unittest.main()
