# Moviemental

**A psychological media atlas for characters, experiences, and life journeys.**

Moviemental connects media characters to psychological experiences, evidence-supported diagnoses, emotional states, coping patterns, relationships, and journeys over time. It helps people discover stories that may resonate with them, supports education and discussion, and makes portrayals of mental health easier to study.

## Core principles

- **People are more than diagnoses.** Capture personality, relationships, agency, context, and change.
- **Evidence before inference.** Distinguish what a work explicitly states from interpretation.
- **Experience is not diagnosis.** A mood or behavior alone does not establish a disorder.
- **Journeys are not always linear.** Recovery, relapse, acceptance, ambiguity, and unresolved endings all belong.
- **Recommendations are invitations, not treatment.** Never promise that a work will heal or help every viewer.
- **Respect copyright.** Store original metadata and analysis; do not reproduce scripts, substantial dialogue, or copyrighted datasets.

## Registry dimensions

1. **Works:** films, television, animation, anime, games, books, comics, and other media.
2. **Characters:** individual portrayals linked to works.
3. **Experiences:** moods, behaviors, stressors, relationships, and coping patterns.
4. **Diagnoses:** only when explicitly stated or supported by clearly documented interpretation.
5. **Journeys:** changes over time, including turning points, support, barriers, and outcomes.
6. **Recommendations:** transparent matches between viewer goals and stories.
7. **Representation:** stigma, nuance, agency, cultural context, and portrayal limitations.

## Repository structure

- `data/works/` — media records
- `data/characters/` — character records
- `data/journeys/` — journey records
- `data/recommendations/` — recommendation mappings
- `data/taxonomies/` — controlled vocabularies
- `data/sources/` — source records
- `schemas/` — JSON Schemas
- `scripts/validate_data.py` — schema and cross-reference validation
- `agents/character-analyst/` — five-lens character analysis agent (methodology, system prompt, runner, demo)
- `.github/workflows/validate-data.yml` — automated GitHub Actions check
- `docs/` — methodology, ethics, and roadmap

## Validate the registry

Requires Python 3.12+ and the `jsonschema` package.

```bash
python -m pip install jsonschema
python scripts/validate_data.py
```

The validator checks JSON syntax, schema conformance, globally unique IDs, and references between works, characters, journeys, sources, and recommendations. GitHub Actions runs the same checks on pushes and pull requests.

## First milestone: Moviemental 0.1

The validation foundation and a 25-character cross-media pilot are in place. The site now includes transparent coverage metrics, review-status counts, a guided story recommender, and a written recommendation methodology. The catalogue remains a pilot: source placeholders and broad narrative interpretations still require editorial review.

See [the roadmap](docs/ROADMAP.md), [the project model](docs/PROJECT_MODEL.md), [the evidence policy](docs/EVIDENCE_POLICY.md), and [the ethics and safety policy](docs/ETHICS_AND_SAFETY.md).

## Website prototype

An interactive static-site prototype is now in the repository root. It includes live search over the JSON registry, media-type filtering, topic shortcuts, character detail panels, journey exploration, a recognition-first experience discovery section, a guided theme-based recommendation flow, live registry coverage metrics, and an expansion area for Hispanic and Dominican media. See [the website preview guide](docs/WEBSITE.md) and [the recommendation approach](docs/RECOMMENDATION_APPROACH.md).

The data validation workflow has passed on the current pilot dataset. GitHub Pages deployment is configured as a workflow, but the repository's Pages site is not yet enabled; the deployment job will not publish until Pages is configured in repository settings. The repository remains private.

The catalogue is still a research pilot. Most character interpretations and content warnings need editorial source review; draft entries must not be presented as clinically reviewed.

## Disclaimer

Moviemental is an educational and media-discovery project, not a diagnostic tool, treatment service, crisis service, or substitute for professional care. Media portrayals are constructed narratives and do not represent everyone's experience.