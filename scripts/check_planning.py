"""Check local planning integrity, not runtime, research or acceptance correctness.

The standard-library parser handles fenced examples, ATX/Setext headings,
ordinary inline/reference links and this repository's explicit task-card schema.
It is deliberately not a complete CommonMark implementation: HTML links,
reference labels containing brackets and dynamically generated content are out
of scope. External URLs are not fetched. .agents and .user_notes are excluded;
historical CHANGELOG files receive link checks but no pseudo-citation checks.
Markdownlint remains a separate required check.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
from html import unescape
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


STATUSES = {"planned", "ready", "in_progress", "blocked", "done", "deferred"}
REQUIRED_FIELDS = {
    "Status",
    "Phase",
    "Requirements",
    "Depends on",
    "Acceptance",
    "Evidence",
}
MARKER = re.compile(r"\[([A-Za-z][A-Za-z0-9]*)\]")
DEFINITION = re.compile(r"^ {0,3}(?:>\s*)?\[([^]\n]+)\]:\s*(<[^>]+>|\S+)")
FIELD = re.compile(r"^- ([A-Za-z][A-Za-z ]+):\s*(.*)$")
TASK_HEADING = re.compile(r"ST-\d{3,}:\s+\S.*")
PENDING = re.compile(
    r"^(?:none|pending|todo|tbd|n/a|not run|unverified|not yet|planned|deferred)\b",
    re.IGNORECASE,
)


@dataclass(frozen=True, order=True)
class Issue:
    path: str
    line: int
    message: str


@dataclass(frozen=True)
class Heading:
    level: int
    title: str
    line: int


@dataclass
class Document:
    path: Path
    text: str
    visible: list[str]
    headings: list[Heading]
    anchors: set[str]


@dataclass
class Task:
    identifier: str
    path: Path
    line: int
    fields: dict[str, str]
    dependencies: list[str] = field(default_factory=list)


@dataclass
class Result:
    issues: list[Issue] = field(default_factory=list)
    documents: int = 0
    tasks: int = 0
    phases: int = 0
    requirements: int = 0


def visible_lines(text: str) -> list[str]:
    """Keep line positions while removing fenced examples and HTML comments."""
    text = re.sub(
        r"<!--[\s\S]*?-->",
        lambda match: "\n" * match.group().count("\n"),
        text,
    )
    result: list[str] = []
    fence = ""
    width = 0
    for line in text.splitlines():
        opening = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
        if fence:
            if opening and opening[1][0] == fence and len(opening[1]) >= width:
                if not opening[2].strip():
                    fence = ""
            result.append("")
        elif opening:
            fence, width = opening[1][0], len(opening[1])
            result.append("")
        else:
            result.append(line)
    return result


def without_code(text: str) -> str:
    return re.sub(r"(`+)(.*?)\1", "", text)


def inline_links(text: str) -> list[tuple[int, int, str]]:
    """Return ordinary inline links, including angle and balanced targets."""
    links: list[tuple[int, int, str]] = []
    for match in re.finditer(r"!?\[[^]\n]*\]\(\s*", text):
        start = match.end()
        if start >= len(text):
            continue
        if text[start] == "<":
            end = text.find(">", start + 1)
            if end < 0:
                continue
            target = text[start + 1 : end]
            close = text.find(")", end + 1)
        else:
            chars: list[str] = []
            depth = 1
            index = start
            while index < len(text):
                char = text[index]
                if char == "\\" and index + 1 < len(text):
                    chars.append(text[index + 1])
                    index += 2
                    continue
                if char.isspace():
                    break
                if char == "(":
                    depth += 1
                elif char == ")":
                    depth -= 1
                    if depth == 0:
                        break
                chars.append(char)
                index += 1
            target = "".join(chars)
            close = text.find(")", index)
        if close >= 0:
            links.append((match.start(), close + 1, target))
    return links


def plain_heading(text: str) -> str:
    for start, end, _ in reversed(inline_links(text)):
        label = re.match(r"!?\[([^]]*)\]", text[start:end])
        if label:
            text = text[:start] + label[1] + text[end:]
    return unescape(re.sub(r"<[^>]*>", "", text)).replace("`", "")


def headings_and_anchors(lines: list[str]) -> tuple[list[Heading], set[str]]:
    headings: list[Heading] = []
    anchors: set[str] = set()
    for index, line in enumerate(lines):
        atx = re.match(r"^ {0,3}(#{1,6})\s+(.+?)\s*#*\s*$", line)
        if atx:
            headings.append(Heading(len(atx[1]), atx[2], index + 1))
        elif index and re.fullmatch(r" {0,3}(=+|-+)\s*", line):
            previous = lines[index - 1].strip()
            if previous and not re.match(r"^(?:[-*+] |\d+\. |\||#|>)", previous):
                headings.append(Heading(1 if "=" in line else 2, previous, index))
        anchors.update(re.findall(r'<(?:a|h[1-6])\b[^>]*\bid=["\']([^"\']+)', line))
    for heading in headings:
        title = plain_heading(heading.title).lower()
        slug = re.sub(r"[^\w\-\s]", "", title)
        slug = re.sub(r"\s", "-", slug)
        candidate = slug
        suffix = 0
        while candidate in anchors:
            suffix += 1
            candidate = f"{slug}-{suffix}"
        anchors.add(candidate)
    return headings, anchors


def read_document(path: Path) -> Document:
    text = path.read_text(encoding="utf-8-sig")
    lines = visible_lines(text)
    headings, anchors = headings_and_anchors(lines)
    return Document(path, text, lines, headings, anchors)


def project_documents(root: Path) -> list[Path]:
    paths = {
        root / name for name in ("README.md", "TODO.md") if (root / name).is_file()
    }
    for directory in ("docs", "reports", "research_notes"):
        if (root / directory).is_dir():
            paths.update((root / directory).rglob("*.md"))
    return sorted(paths, key=lambda path: path.relative_to(root).as_posix().casefold())


def validate(root: Path) -> Result:
    root = root.resolve()
    result = Result()
    cache: dict[Path, Document] = {}

    def issue(path: Path, line: int, message: str) -> None:
        try:
            label = path.relative_to(root).as_posix()
        except ValueError:
            label = str(path)
        result.issues.append(Issue(label, line, message))

    def document(path: Path) -> Document | None:
        path = path.resolve()
        if path not in cache:
            try:
                cache[path] = read_document(path)
            except (OSError, UnicodeError) as error:
                issue(path, 1, f"cannot read document: {type(error).__name__}")
                return None
        return cache[path]

    def check_link(doc: Document, number: int, target: str) -> None:
        parsed = urlsplit(unescape(target))
        if parsed.scheme or parsed.netloc:
            return
        relative = unquote(parsed.path)
        path = (doc.path.parent / relative).resolve() if relative else doc.path
        if relative.startswith("/"):
            path = (root / relative.lstrip("/")).resolve()
        if not path.exists():
            issue(doc.path, number, f"missing local link target: {target}")
        elif parsed.fragment and path.suffix.lower() == ".md" and path.is_file():
            linked = document(path)
            if linked and unquote(parsed.fragment) not in linked.anchors:
                issue(doc.path, number, f"missing heading fragment: {target}")

    docs = [doc for path in project_documents(root) if (doc := document(path))]
    result.documents = len(docs)
    for doc in docs:
        for number, line in enumerate(doc.visible, 1):
            clean = without_code(line)
            for _, _, target in inline_links(clean):
                check_link(doc, number, target)
            definition = DEFINITION.match(clean)
            if definition:
                target = definition[2].strip("<>")
                if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_-]*", target):
                    check_link(doc, number, target)
        if doc.path.name.upper() == "CHANGELOG.MD":
            continue
        registries = [h for h in doc.headings if h.title == "(Z) Context-Citations"]
        indexes = [h for h in doc.headings if re.match(r"\(Y\)\s", h.title)]
        if len(registries) != 1:
            issue(
                doc.path, 1, "expected exactly one final (Z) Context-Citations registry"
            )
            continue
        registry = registries[0]
        if any(
            h.line > registry.line and h.level <= registry.level for h in doc.headings
        ):
            issue(
                doc.path,
                registry.line,
                "context registry must be the final major section",
            )
        if len(indexes) != 1 or indexes[0].line >= registry.line:
            issue(doc.path, 1, "expected one (Y) usage index before the registry")
        definitions: dict[str, int] = {}
        references: set[str] = set()
        index_references: set[str] = set()
        for number, line in enumerate(doc.visible, 1):
            clean = without_code(line)
            definition = DEFINITION.match(clean)
            if definition:
                label = definition[1].casefold()
                if number <= registry.line:
                    issue(
                        doc.path,
                        number,
                        "reference definition outside the final registry",
                    )
                if label in definitions:
                    issue(
                        doc.path,
                        number,
                        f"duplicate reference definition: {definition[1]}",
                    )
                definitions[label] = number
                if re.fullmatch(r"[a-z]+00", label):
                    issue(doc.path, number, f"active zero placeholder: {definition[1]}")
                continue
            if number >= registry.line:
                continue
            for start, end, _ in reversed(inline_links(clean)):
                clean = clean[:start] + clean[end:]
            clean = re.sub(r"^\s*[-*+] \[[ xX]\]", "", clean)
            clean = re.sub(r"\[[^]\n]+\]\[([^]\n]+)\]", r"[\1]", clean)
            for match in MARKER.finditer(clean):
                label = match[1].casefold()
                references.add(label)
                if indexes and number > indexes[0].line:
                    index_references.add(label)
                if re.fullmatch(r"[a-z]+00", label):
                    issue(doc.path, number, f"active zero placeholder: {match[1]}")
        for label in sorted(references - definitions.keys()):
            issue(doc.path, 1, f"unresolved pseudo-citation: {label}")
        for label in sorted(definitions.keys() - references):
            issue(doc.path, definitions[label], f"unused reference definition: {label}")
        if len(indexes) == 1 and indexes[0].line < registry.line:
            missing_index = sorted(definitions.keys() - index_references)
            if missing_index:
                issue(
                    doc.path,
                    indexes[0].line,
                    "references missing from usage index: " + ", ".join(missing_index),
                )

    plan_path = root / "docs/global_plan.md"
    plan = document(plan_path)
    phases: dict[str, int] = {}
    if plan:
        for heading in plan.headings:
            match = re.fullmatch(r"(P[1-9]\d*):\s+(.+)", heading.title)
            if heading.level == 2 and match:
                if match[1] in phases:
                    issue(plan_path, heading.line, f"duplicate phase: {match[1]}")
                phases[match[1]] = len(phases)
        if not phases:
            issue(plan_path, 1, "no phase headings found; expected ## P1: Title")
    result.phases = len(phases)
    requirements_path = root / "docs/requirements.md"
    requirements_doc = document(requirements_path)
    requirements: set[str] = set()
    if requirements_doc:
        requirements = {
            match[1]
            for line in requirements_doc.visible
            if (match := re.match(r"^\[(REQ\d+)\]:", line))
        }
        if not requirements:
            issue(requirements_path, 1, "no REQ definitions found")
    result.requirements = len(requirements)

    tasks: dict[str, Task] = {}
    covered: set[str] = set()
    for doc in docs:
        if doc.path.parent != root / "docs/todos":
            continue
        for index, heading in enumerate(doc.headings):
            if heading.level != 3:
                continue
            if not TASK_HEADING.fullmatch(heading.title):
                if heading.title.startswith("ST-"):
                    issue(
                        doc.path,
                        heading.line,
                        "malformed task heading; expected ### ST-001: Title",
                    )
                continue
            identifier = heading.title.split(":", 1)[0]
            stop = len(doc.visible)
            for later in doc.headings[index + 1 :]:
                if later.level <= 3:
                    stop = later.line - 1
                    break
            values: dict[str, str] = {}
            current = ""
            for number in range(heading.line, stop):
                line = doc.visible[number]
                match = FIELD.match(line)
                if match:
                    current = match[1]
                    if current in values:
                        issue(
                            doc.path,
                            number + 1,
                            f"{identifier}: duplicate field {current}",
                        )
                    values[current] = match[2].strip()
                elif current and line.startswith("  "):
                    values[current] += " " + line.strip()
            task = Task(identifier, doc.path, heading.line, values)
            if identifier in tasks:
                issue(doc.path, heading.line, f"duplicate task ID: {identifier}")
                continue
            tasks[identifier] = task
            for required in sorted(REQUIRED_FIELDS):
                if not values.get(required, "").strip():
                    issue(
                        doc.path,
                        heading.line,
                        f"{identifier}: missing field {required}",
                    )
            status = values.get("Status", "")
            if status not in STATUSES:
                issue(
                    doc.path, heading.line, f"{identifier}: unknown status {status!r}"
                )
            if values.get("Phase") not in phases:
                issue(
                    doc.path,
                    heading.line,
                    f"{identifier}: unknown phase {values.get('Phase')!r}",
                )
            refs = [item.strip() for item in values.get("Requirements", "").split(",")]
            for ref in refs:
                if ref not in requirements:
                    issue(
                        doc.path,
                        heading.line,
                        f"{identifier}: unknown requirement {ref!r}",
                    )
                else:
                    covered.add(ref)
            raw_dependencies = values.get("Depends on", "")
            if raw_dependencies and raw_dependencies != "none":
                task.dependencies = [
                    item.strip() for item in raw_dependencies.split(",")
                ]
            evidence = values.get("Evidence", "").strip()
            if status == "done" and (len(evidence) < 12 or PENDING.match(evidence)):
                issue(
                    doc.path,
                    heading.line,
                    f"{identifier}: done requires non-pending evidence detail",
                )
    result.tasks = len(tasks)
    if not tasks:
        issue(root / "docs/todos", 1, "no task cards found")
    for requirement in sorted(requirements - covered):
        issue(requirements_path, 1, f"requirement has no task coverage: {requirement}")

    for task in tasks.values():
        for dependency in task.dependencies:
            if dependency == task.identifier:
                issue(task.path, task.line, f"{task.identifier}: self dependency")
            elif dependency not in tasks:
                issue(
                    task.path,
                    task.line,
                    f"{task.identifier}: unknown dependency {dependency}",
                )
            else:
                upstream = tasks[dependency]
                if task.fields.get("Status") in {"ready", "in_progress"}:
                    if upstream.fields.get("Status") != "done":
                        issue(
                            task.path,
                            task.line,
                            f"{task.identifier}: dependency {dependency} is not done",
                        )
                phase = task.fields.get("Phase")
                before = upstream.fields.get("Phase")
                if (
                    phase in phases
                    and before in phases
                    and phases[before] > phases[phase]
                ):
                    issue(
                        task.path,
                        task.line,
                        f"{task.identifier}: dependency {dependency} belongs to a later phase",
                    )
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(identifier: str) -> None:
        if identifier in visiting:
            task = tasks[identifier]
            issue(task.path, task.line, f"dependency cycle includes {identifier}")
            return
        if identifier in visited:
            return
        visiting.add(identifier)
        for dependency in tasks[identifier].dependencies:
            if dependency in tasks:
                visit(dependency)
        visiting.remove(identifier)
        visited.add(identifier)

    for identifier in sorted(tasks):
        visit(identifier)
    queue_path = root / "TODO.md"
    queue = document(queue_path)
    if queue:
        next_tasks = [
            (number, match[1])
            for number, line in enumerate(queue.visible, 1)
            if (match := re.fullmatch(r"(?:- )?Next task:\s*(ST-\d{3,})\s*", line))
        ]
        if len(next_tasks) != 1:
            issue(queue_path, 1, "expected exactly one Next task: ST-001 queue field")
        else:
            number, identifier = next_tasks[0]
            if identifier not in tasks:
                issue(queue_path, number, f"next task does not exist: {identifier}")
            elif tasks[identifier].fields.get("Status") not in {"ready", "in_progress"}:
                issue(
                    queue_path,
                    number,
                    f"next task is not ready or in_progress: {identifier}",
                )
    result.issues = sorted(set(result.issues))
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="repository root; defaults to this script's parent repository",
    )
    args = parser.parse_args(argv)
    if not args.root.is_dir():
        parser.error(f"repository root does not exist: {args.root}")
    result = validate(args.root)
    for item in result.issues:
        print(f"{item.path}:{item.line}: {item.message}")
    state = "FAIL" if result.issues else "PASS"
    print(
        f"{state}: {result.documents} Markdown files, {result.tasks} task cards, "
        f"{result.phases} phases, {result.requirements} requirements; "
        f"{len(result.issues)} issues."
    )
    print(
        "Excluded: .agents, .user_notes; CHANGELOG pseudo-citations. External URLs not fetched."
    )
    print(
        "Checks establish planning integrity only; run markdownlint and runtime/evidence checks separately."
    )
    return 1 if result.issues else 0


if __name__ == "__main__":
    sys.exit(main())
