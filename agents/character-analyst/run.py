#!/usr/bin/env python3
"""Moviemental Character Analyst — runner.

Builds the analysis prompt for a character (prints it, or saves it), and
validates a produced draft record against the Moviemental character schema.

Usage:
  python run.py --character "BoJack Horseman" --work "BoJack Horseman" \\
      --work-id work-bojack-horseman --medium "television_series" \\
      --material "Seasons 1-6; key episodes: S3E11, S4E2, S6E15" \\
      --out-prompt /tmp/bojack.prompt.md

  python run.py --validate draft.json --schema /path/to/character.schema.json
"""
import argparse, json, os, sys

BASE = os.path.dirname(os.path.abspath(__file__))

def load_system_prompt():
    with open(os.path.join(BASE, "SYSTEM_PROMPT.md")) as f:
        return f.read()

def build_prompt(character, work, work_id, medium, material, extra=""):
    sp = load_system_prompt()
    brief = f"""## Assignment

Character: {character}
Work: {work} (work_id: {work_id})
Medium: {medium}
Material consulted: {material}
{f'Additional notes: {extra}' if extra else ''}

Follow the protocol in order: Intake, five lens passes, Synthesis (both
artifacts), Self-audit. Output the draft character record JSON first in a
```json block, then the analysis essay in a ```markdown block.
"""
    return sp + "\n\n" + brief

def validate(record_path, schema_path):
    try:
        import jsonschema
    except ImportError:
        print("jsonschema not installed; pip install jsonschema", file=sys.stderr)
        return False
    with open(schema_path) as f:
        schema = json.load(f)
    with open(record_path) as f:
        record = json.load(f)
    jsonschema.validate(record, schema)
    # analyst-specific invariants
    assert record["review_status"] == "draft", "agent output must stay draft"
    for claim in record.get("psychological_experiences", []) + record.get("diagnoses", []):
        assert claim["evidence_status"] in (
            "explicit_in_work", "creator_confirmed",
            "source_supported_interpretation", "experiential_only",
            "contested", "unknown"), f"bad grade: {claim['evidence_status']}"
        assert len(claim.get("evidence", "")) > 40, \
            f"evidence text too thin for tag {claim['tag']!r}"
    print(f"OK: {record_path} validates "
          f"({len(record.get('psychological_experiences', []))} experiences, "
          f"{len(record.get('diagnoses', []))} diagnoses)")
    return True

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--character"); ap.add_argument("--work")
    ap.add_argument("--work-id"); ap.add_argument("--medium", default="television_series")
    ap.add_argument("--material", default="")
    ap.add_argument("--extra", default="")
    ap.add_argument("--out-prompt")
    ap.add_argument("--validate"); ap.add_argument("--schema")
    a = ap.parse_args()
    if a.validate:
        if not a.schema:
            print("--schema required with --validate", file=sys.stderr); sys.exit(2)
        sys.exit(0 if validate(a.validate, a.schema) else 1)
    for req in ("character", "work", "work_id"):
        if not getattr(a, req):
            print(f"--{req.replace('_','-')} required", file=sys.stderr); sys.exit(2)
    prompt = build_prompt(a.character, a.work, a.work_id, a.medium, a.material, a.extra)
    if a.out_prompt:
        with open(a.out_prompt, "w") as f:
            f.write(prompt)
        print(f"wrote {a.out_prompt} ({len(prompt)} chars)")
    else:
        print(prompt)

if __name__ == "__main__":
    main()
