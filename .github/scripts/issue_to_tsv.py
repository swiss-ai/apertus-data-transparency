"""Parse a "New Dataset" GitHub issue form and append it as a row to the catalogue TSV.

The script is driven by the GitHub-rendered issue body (env var ``ISSUE_BODY``). GitHub
renders an issue form as a sequence of ``### <label>`` sections, so we parse those sections,
map each label onto the matching TSV column, validate the required fields, and — if valid —
append a single tab-separated row to ``Apertus dataset repository.tsv``.

Results are reported back to the workflow via ``GITHUB_OUTPUT`` (``ok``, ``name``, ``errors``).
"""

from __future__ import annotations

import os
import re
from pathlib import Path

TSV_PATH = Path("Apertus dataset repository.tsv")

# GitHub renders an empty optional field with this exact placeholder.
NO_RESPONSE = "_no response_"

# Columns that must be non-empty (mirrors ``validations.required`` in new_dataset.yml).
REQUIRED_COLUMNS = [
    "name",
    "tags",
    "licenses",
    "pii_removal",
    "robots_filtering",
    "version",
    "raw_dir",
    "processed_dir",
    "tokenized_dir",
    "processing_script",
    "tokenization_script",
]

CHECKBOX_RE = re.compile(r"^- \[([ xX])\]\s*(.*)$")


def parse_issue_body(body: str) -> dict[str, str]:
    """Parse a rendered issue-form body into a ``{label: value}`` mapping.

    Sections are delimited by ``### <label>`` headings. Checkbox sections are collapsed to a
    comma-separated list of the checked options; everything else is treated as free text with
    internal newlines flattened. The ``_No response_`` placeholder maps to an empty string.
    """
    sections: dict[str, list[str]] = {}
    current: str | None = None

    for line in body.splitlines():
        heading = line.strip()
        if heading.startswith("### "):
            current = heading[4:].strip().lower()
            sections[current] = []
        elif current is not None:
            sections[current].append(line)

    fields: dict[str, str] = {}
    for label, lines in sections.items():
        raw = "\n".join(lines).strip()
        if raw.lower() == NO_RESPONSE:
            fields[label] = ""
            continue

        checked = [m.group(2).strip() for m in map(CHECKBOX_RE.match, lines) if m and m.group(1) in "xX"]
        if any(CHECKBOX_RE.match(ln) for ln in lines):
            values = checked
        else:
            values = [ln.strip() for ln in raw.splitlines() if ln.strip()]

        fields[label] = ", ".join(values)

    return fields


def build_row(fields: dict[str, str], columns: list[str]) -> dict[str, str]:
    """Map parsed issue fields onto the TSV columns (labels now match column names 1:1)."""
    row = {column: "" for column in columns}
    for label, value in fields.items():
        if label not in row:
            continue
        # TSV cells cannot contain tabs or newlines.
        row[label] = value.replace("\t", " ").replace("\n", " ").strip()
    return row


def validate(row: dict[str, str], existing_names: set[str]) -> list[str]:
    """Return a list of human-readable validation errors (empty when the row is valid)."""
    errors = [f"Missing required field: `{col}`" for col in REQUIRED_COLUMNS if not row.get(col)]
    if row.get("name") and row["name"].lower() in existing_names:
        errors.append(f"A dataset named `{row['name']}` already exists in the catalogue.")
    return errors


def write_output(**values: str) -> None:
    """Append key/value pairs to ``$GITHUB_OUTPUT`` using the multiline heredoc syntax."""
    output_path = os.environ.get("GITHUB_OUTPUT")
    if not output_path:
        return
    with Path(output_path).open("a", encoding="utf-8") as handle:
        for key, value in values.items():
            handle.write(f"{key}<<__EOF__\n{value}\n__EOF__\n")


def main() -> None:
    body = os.environ.get("ISSUE_BODY", "")

    header = TSV_PATH.read_text(encoding="utf-8").splitlines()[0]
    columns = header.split("\t")

    existing_names = set()
    for line in TSV_PATH.read_text(encoding="utf-8").splitlines()[1:]:
        cell = line.split("\t", 1)[0].strip()
        if cell:
            existing_names.add(cell.lower())

    fields = parse_issue_body(body)
    row = build_row(fields, columns)
    errors = validate(row, existing_names)

    if errors:
        write_output(ok="false", name=row.get("name", ""), errors="\n".join(f"- {e}" for e in errors))
        print("Validation failed:\n" + "\n".join(errors))
        return

    content = TSV_PATH.read_text(encoding="utf-8")
    if not content.endswith("\n"):
        content += "\n"
    content += "\t".join(row[column] for column in columns) + "\n"
    TSV_PATH.write_text(content, encoding="utf-8")

    write_output(ok="true", name=row["name"], errors="")
    print(f"Appended dataset row: {row['name']}")


if __name__ == "__main__":
    main()
