"""Adversarial fixtures for planning integrity; runtime specimens stay separate."""

from __future__ import annotations

from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from check_planning import main, validate


def markdown(body: str, *, requirements: tuple[str, ...] = ()) -> str:
    markers = ("DOC", *requirements)
    index = ", ".join(f"[{marker}]" for marker in markers)
    definitions = "\n\n".join(
        f'[{marker}]: CONTEXT_{marker}\n  "Fixture context for {marker}."'
        for marker in markers
    )
    return (
        "# Fixture [DOC]\n\n" + body.strip() + "\n\n"
        "## (Y) Link-complete usage index\n\n" + index + "\n\n"
        "## (Z) Context-Citations\n\n" + definitions + "\n"
    )


def card(
    identifier: str,
    *,
    status: str = "ready",
    phase: str = "P1",
    requirements: str = "REQ01",
    dependencies: str = "none",
    evidence: str = "Pending implementation.",
) -> str:
    return (
        f"### {identifier}: Bounded implementation\n\n"
        f"- Status: {status}\n"
        f"- Phase: {phase}\n"
        f"- Requirements: {requirements}\n"
        f"- Depends on: {dependencies}\n"
        "- Acceptance: Valid values pass and invalid values are refused.\n"
        "  Failures preserve the previously accepted state.\n"
        f"- Evidence: {evidence}\n"
    )


class PlanningValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = TemporaryDirectory(prefix="4gine-planning-tests-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        (self.root / "docs/todos").mkdir(parents=True)
        self.write("README.md", markdown("[Queue](TODO.md)"))
        self.write("TODO.md", markdown("Next task: ST-001"))
        self.write(
            "docs/requirements.md",
            markdown("Requirements", requirements=("REQ01", "REQ02")),
        )
        self.write(
            "docs/global_plan.md", markdown("## P1: Baseline\n\n## P2: Application")
        )
        self.set_cards()

    def write(self, name: str, text: str) -> None:
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def set_cards(self, first: str | None = None, second: str | None = None) -> None:
        self.write(
            "docs/todos/work.md",
            markdown(
                (first or card("ST-001"))
                + "\n"
                + (
                    second
                    or card(
                        "ST-002",
                        status="planned",
                        phase="P2",
                        requirements="REQ02",
                        dependencies="ST-001",
                    )
                )
            ),
        )

    def messages(self) -> list[str]:
        return [issue.message for issue in validate(self.root).issues]

    def assert_issue(self, fragment: str) -> None:
        self.assertTrue(
            any(fragment in message for message in self.messages()), self.messages()
        )

    def test_valid_catalogue_has_coverage_and_independent_root(self) -> None:
        result = validate(self.root)
        self.assertEqual(result.issues, [])
        self.assertEqual((result.tasks, result.phases, result.requirements), (2, 2, 2))
        output = StringIO()
        with redirect_stdout(output):
            self.assertEqual(main(["--root", str(self.root)]), 0)
        self.assertIn("PASS:", output.getvalue())

    def test_unknown_dependency_and_self_dependency_fail(self) -> None:
        self.set_cards(first=card("ST-001", dependencies="ST-999, ST-001"))
        self.assert_issue("unknown dependency ST-999")
        self.assert_issue("self dependency")

    def test_dependency_cycle_is_reported_without_recursing_forever(self) -> None:
        self.set_cards(
            first=card("ST-001", status="planned", dependencies="ST-002"),
            second=card(
                "ST-002", status="planned", requirements="REQ02", dependencies="ST-001"
            ),
        )
        self.assert_issue("dependency cycle")

    def test_duplicate_task_identifier_across_files_fails(self) -> None:
        self.write("docs/todos/duplicate.md", markdown(card("ST-001")))
        self.assert_issue("duplicate task ID: ST-001")

    def test_unknown_phase_and_requirement_fail(self) -> None:
        self.set_cards(first=card("ST-001", phase="P9", requirements="REQ99"))
        self.assert_issue("unknown phase 'P9'")
        self.assert_issue("unknown requirement 'REQ99'")
        self.assert_issue("requirement has no task coverage: REQ01")

    def test_ready_dependency_requires_done_and_cannot_point_to_later_phase(
        self,
    ) -> None:
        self.set_cards(first=card("ST-001", dependencies="ST-002"))
        self.assert_issue("dependency ST-002 is not done")
        self.assert_issue("dependency ST-002 belongs to a later phase")

    def test_done_requires_evidence_and_queue_must_advance(self) -> None:
        self.set_cards(first=card("ST-001", status="done"))
        self.assert_issue("done requires non-pending evidence detail")
        self.assert_issue("next task is not ready or in_progress")

    def test_done_with_evidence_unlocks_ready_dependency(self) -> None:
        self.set_cards(
            first=card(
                "ST-001",
                status="done",
                evidence="PASS: fixture acceptance and refusal checks observed.",
            ),
            second=card(
                "ST-002",
                status="ready",
                phase="P2",
                requirements="REQ02",
                dependencies="ST-001",
            ),
        )
        self.write("TODO.md", markdown("Next task: ST-002"))
        self.assertEqual(self.messages(), [])

    def test_missing_required_field_and_unknown_status_fail(self) -> None:
        first = card("ST-001", status="almost_done").replace(
            "- Acceptance:", "- Notes:"
        )
        self.set_cards(first=first)
        self.assert_issue("missing field Acceptance")
        self.assert_issue("unknown status 'almost_done'")

    def test_fenced_invalid_examples_are_not_live_definitions_or_links(self) -> None:
        self.write(
            "README.md",
            markdown(
                "```md\n[GL00]\n[DOC]: DUPLICATE\n[bad](missing.md)\n```\n\n[Queue](TODO.md)"
            ),
        )
        self.assertEqual(self.messages(), [])

    def test_citation_duplicates_missing_unused_and_zero_placeholders_fail(
        self,
    ) -> None:
        content = markdown("[MISSING] [GL00]")
        content += (
            '\n[doc]: DUPLICATE\n  "Duplicate."\n\n[UNUSED]: UNUSED\n  "Unused."\n'
        )
        self.write("README.md", content)
        self.assert_issue("duplicate reference definition: doc")
        self.assert_issue("unresolved pseudo-citation: missing")
        self.assert_issue("unused reference definition: unused")
        self.assert_issue("active zero placeholder: GL00")

    def test_definition_above_registry_and_missing_usage_index_fail(self) -> None:
        content = markdown('[EARLY]: EARLY\n  "Wrong place."\n\n[EARLY]')
        self.write(
            "README.md", content.replace("## (Y) Link-complete usage index", "## Index")
        )
        self.assert_issue("reference definition outside the final registry")
        self.assert_issue("expected one (Y) usage index")

    def test_relative_file_and_heading_links_are_checked(self) -> None:
        self.write(
            "README.md",
            markdown("[Missing](missing.md)\n\n[Fragment](docs/global_plan.md#absent)"),
        )
        self.assert_issue("missing local link target: missing.md")
        self.assert_issue("missing heading fragment: docs/global_plan.md#absent")

    def test_setext_headings_and_percent_escaped_paths_resolve(self) -> None:
        self.write(
            "README.md",
            "CURRENT STATE:\n==============\n\n[DOC]\n\n"
            "[Space](docs/a%20file.md#section-name)\n\n"
            "[Angle](<docs/a file.md#section-name>)\n\n"
            "(Y) Link-complete usage index\n-----------------------------\n\n[DOC]\n\n"
            '(Z) Context-Citations\n---------------------\n\n[DOC]: DOCUMENT\n  "Fixture."\n',
        )
        self.write(
            "docs/a file.md", markdown("Section name\n------------\n\nContents.")
        )
        self.assertEqual(self.messages(), [])

    def test_changelog_is_link_checked_but_control_directories_are_excluded(
        self,
    ) -> None:
        self.write("docs/logs/CHANGELOG.md", "# History\n\nPlain historical text.\n")
        self.write(".agents/broken.md", "[bad](absent.md)")
        self.write(".user_notes/broken.md", "[bad](absent.md)")
        self.assertEqual(self.messages(), [])
        self.write("docs/logs/CHANGELOG.md", "# History\n\n[bad](absent.md)\n")
        self.assert_issue("missing local link target: absent.md")

    def test_lowercase_category_destinations_are_not_file_links(self) -> None:
        self.write(
            "README.md",
            markdown("Category [DOC]").replace("CONTEXT_DOC", "nervous_system"),
        )
        self.assertEqual(self.messages(), [])

    def test_malformed_task_heading_is_not_silently_ignored(self) -> None:
        self.set_cards(first=card("ST-001").replace("ST-001:", "ST-1:"))
        self.assert_issue("malformed task heading")

    def test_failure_exit_code_and_output_are_deterministic(self) -> None:
        self.write("README.md", markdown("[bad](absent.md)"))
        first = StringIO()
        second = StringIO()
        with redirect_stdout(first):
            self.assertEqual(main(["--root", str(self.root)]), 1)
        with redirect_stdout(second):
            self.assertEqual(main(["--root", str(self.root)]), 1)
        self.assertEqual(first.getvalue(), second.getvalue())


if __name__ == "__main__":
    unittest.main()
