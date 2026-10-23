# Moviemental Character Analyst

A specialized character-analysis agent for the Moviemental registry:
five analytical lenses, one evidence discipline, schema-valid output.

## What it is

The analyst produces draft Moviemental character records — evidence-graded,
scene-anchored, and honest about uncertainty — plus a readable analysis
essay. Every output stays `review_status: "draft"`: the agent drafts, the
clinician (Luis) reviews. It upgrades thin pilot records (like the current
`experiential_only` placeholders) into source-supported analyses.

## The five lenses

1. **The Clinician** — after Jonathan Decker, LMFT (Cinema Therapy) and
   Dr. Kirk Honda (Psychology in Seattle). Structured formulation with an
   explicit information boundary; hypotheses, never diagnosis-by-fiat.
2. **The Close Reader** — after Nerdwriter, Like Stories of Old, Just
   Write. Patterns, not plot: every claim anchored in at least two moments.
3. **The Thematician** — what argument does the work make through this
   character? One falsifiable sentence.
4. **The Functionalist** — after Campbell/Vogler, Dramatica, The Take.
   Archetypes as roles, not boxes.
5. **The Ethicist** — Moviemental's own frame: stigma, agency, cultural
   context; invitations, not treatment.

Full methodology in `METHODOLOGY.md`. Inspired by these analysts, not
affiliated with them.

## Files

- `METHODOLOGY.md` — the lenses, evidence discipline, protocol, sources.
- `SYSTEM_PROMPT.md` — the runnable agent prompt (any capable LLM, or
  paste to an assistant).
- `run.py` — builds the analysis prompt for a character; validates draft
  JSON against the Moviemental character schema plus analyst invariants
  (must stay `draft`; evidence text must be substantive).
- `demo/` — worked example: BoJack Horseman. The enriched record
  (`character-bojack-horseman.enriched.json`) validates against the live
  schema; the essay (`bojack-horseman-analysis.md`) shows the five lenses.

## Usage

```bash
# Build the prompt for a character
python run.py --character "Ted Lasso" --work "Ted Lasso" \
  --work-id work-ted-lasso --medium television_series \
  --material "Seasons 1-3" --out-prompt /tmp/ted.prompt.md

# Validate a produced draft record
python run.py --validate draft.json --schema /path/to/character.schema.json
```

## Design notes

- Output is schema-valid by construction: the runner's validator enforces
  the Moviemental character schema plus `review_status: "draft"`.
- The diagnoses array stays empty unless the work states it or creators
  confirm it. The essay carries hypotheses; the record carries evidence.
- No em dashes in essay output (house style).
