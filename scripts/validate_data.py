#!/usr/bin/env python3
"""Validate Moviemental JSON records, schemas, IDs, and cross-record references."""
from __future__ import annotations

import json
import sys
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schemas"
DATA_DIR = ROOT / "data"

COLLECTIONS = {
    "works": (DATA_DIR / "works", SCHEMA_DIR / "work.schema.json"),
    "characters": (DATA_DIR / "characters", SCHEMA_DIR / "character.schema.json"),
    "journeys": (DATA_DIR / "journeys", SCHEMA_DIR / "journey.schema.json"),
    "sources": (DATA_DIR / "sources", SCHEMA_DIR / "source.schema.json"),
    "recommendations": (DATA_DIR / "recommendations", SCHEMA_DIR / "recommendation.schema.json"),
}

def load_json(path: Path, errors: list[str]):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{path.relative_to(ROOT)}: cannot read valid JSON ({exc})")
        return None

def main() -> int:
    errors: list[str] = []
    records: dict[str, dict[str, dict]] = {}
    ids_seen: dict[str, str] = {}

    schemas = {}
    for kind, (_, schema_path) in COLLECTIONS.items():
        schema = load_json(schema_path, errors)
        if schema is not None:
            try:
                Draft202012Validator.check_schema(schema)
                schemas[kind] = Draft202012Validator(schema)
            except Exception as exc:
                errors.append(f"{schema_path.relative_to(ROOT)}: invalid schema ({exc})")

    for kind, (directory, _) in COLLECTIONS.items():
        records[kind] = {}
        if not directory.exists():
            continue
        for path in sorted(directory.glob("*.json")):
            record = load_json(path, errors)
            if not isinstance(record, dict):
                if record is not None:
                    errors.append(f"{path.relative_to(ROOT)}: record must be a JSON object")
                continue
            if kind in schemas:
                for issue in schemas[kind].iter_errors(record):
                    location = ".".join(str(part) for part in issue.absolute_path) or "<root>"
                    errors.append(f"{path.relative_to(ROOT)}:{location}: {issue.message}")
            record_id = record.get("id")
            if not isinstance(record_id, str) or not record_id:
                errors.append(f"{path.relative_to(ROOT)}: missing non-empty id")
                continue
            if record_id in ids_seen:
                errors.append(f"{path.relative_to(ROOT)}: duplicate ID '{record_id}' also used in {ids_seen[record_id]}")
            else:
                ids_seen[record_id] = str(path.relative_to(ROOT))
            records[kind][record_id] = record

    def check_refs(owner_kind: str, owner_id: str, field: str, target_kind: str):
        record = records.get(owner_kind, {}).get(owner_id, {})
        for ref in record.get(field, []) or []:
            if ref not in records.get(target_kind, {}):
                errors.append(f"{owner_kind}/{owner_id}: {field} references missing {target_kind} ID '{ref}'")

    for character_id, character in records.get("characters", {}).items():
        work_id = character.get("work_id")
        if work_id not in records.get("works", {}):
            errors.append(f"characters/{character_id}: work_id references missing work '{work_id}'")
        check_refs("characters", character_id, "journey_ids", "journeys")
        check_refs("characters", character_id, "source_ids", "sources")
        for field in ("diagnoses", "psychological_experiences"):
            for claim in character.get(field, []) or []:
                for source_id in claim.get("source_ids", []) or []:
                    if source_id not in records.get("sources", {}):
                        errors.append(f"characters/{character_id}: {field} claim references missing source '{source_id}'")

    for journey_id, journey in records.get("journeys", {}).items():
        check_refs("journeys", journey_id, "character_ids", "characters")
        check_refs("journeys", journey_id, "work_ids", "works")
        check_refs("journeys", journey_id, "source_ids", "sources")
        for stage in journey.get("stages", []) or []:
            for source_id in stage.get("source_ids", []) or []:
                if source_id not in records.get("sources", {}):
                    errors.append(f"journeys/{journey_id}: stage references missing source '{source_id}'")

    for work_id in records.get("works", {}):
        check_refs("works", work_id, "source_ids", "sources")

    for recommendation_id, recommendation in records.get("recommendations", {}).items():
        check_refs("recommendations", recommendation_id, "work_ids", "works")
        check_refs("recommendations", recommendation_id, "journey_ids", "journeys")
        check_refs("recommendations", recommendation_id, "source_ids", "sources")

    if errors:
        print(f"Moviemental validation failed with {len(errors)} issue(s):")
        for error in errors:
            print(f" - {error}")
        return 1

    counts = ", ".join(f"{kind}={len(items)}" for kind, items in records.items())
    print(f"Moviemental validation passed. {counts}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
