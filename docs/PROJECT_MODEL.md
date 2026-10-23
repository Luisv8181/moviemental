# Registry Data Model

Moviemental connects media works, character portrayals, psychological experiences, journeys, sources, recommendations, and reviews.

## Core entities
- **Work:** one film, series, episode, game, book, or other media item.
- **Character:** a character portrayal linked to a work.
- **Journey:** change over time; journeys may be nonlinear, unresolved, cyclical, or ambiguous.
- **Tag:** a controlled concept such as grief, isolation, avoidance, belonging, or a diagnosis.
- **Source:** evidence for a factual claim or interpretation.
- **Recommendation:** a transparent match between an audience goal and a work.

## Evidence status
- `explicit_in_work`: stated in the work.
- `creator_confirmed`: supported by an attributable creator or official source.
- `source_supported_interpretation`: supported by cited scholarship or criticism.
- `experiential_only`: describes an experience without asserting a diagnosis.
- `contested`: credible interpretations disagree.
- `unknown`: not adequately assessed.

Evidence status applies to individual claims, not the whole character. Never infer a diagnosis from one behavior, mood, plot event, or stereotype. Prefer observable, nonjudgmental descriptions when evidence is insufficient.

## Review status
`draft`, `needs_sources`, `in_review`, `reviewed`, `contested`, `archived`.

Use stable lowercase hyphenated IDs. Track source provenance and uncertainty. Avoid false clinical precision.