# Recommendation approach (pilot)

Moviemental's first recommendation experience is a transparent, rule-based discovery aid. It is not a diagnostic tool, a treatment recommendation system, or a validated clinical recommender.

## Signals currently used

- User-entered theme terms are matched against character names, work titles, experience tags, moods, coping patterns, representation notes, and content warnings.
- A selected goal (feel understood, understand an experience, explore coping, or study representation) adds a lightweight relevance signal.
- Existing editorial recommendation records contribute rationale text when a character is part of a curated example.
- Users may exclude records whose documented content warnings mention suicide, substance use, violence, or abuse.
- A rough intensity hint is available only where existing curated recommendation records provide one. "Unknown" means the catalogue has not yet assessed intensity, not that the work is safe or mild.

## Current limitations

- The pilot catalogue has only 25 character records and five curated recommendation mappings. Ranking is intentionally simple and should not be described as personalized clinical matching.
- Content warnings are incomplete and are not guarantees. The user should be able to inspect the profile before deciding to watch or read.
- Search uses text matching, so synonyms, idioms, cultural nuance, and non-English queries will often be missed.
- The site does not infer a diagnosis from a viewer's answer. It does not store their answers or send them to a server.
- A story may resonate with someone without accurately representing their life. A story may also be harmful or unhelpful for a particular viewer even if the theme appears relevant.

## Next improvements

1. Add reviewed evidence and scene/episode/chapter citations for each entry.
2. Build a controlled vocabulary with synonyms, multilingual terms, and region-specific language.
3. Review intensity and content warnings with transparent criteria and, where possible, lived-experience reviewers.
4. Add feedback options such as "this matched", "not for me", and "warning missing" without collecting sensitive personal stories by default.
5. Evaluate retrieval quality with diverse test prompts and a human-reviewed benchmark before describing the recommendations as effective.

## Editorial principle

Recommend a story as a possible companion for reflection, not as a prescription. Explain why it was suggested, identify uncertainty, surface content notes, and preserve the user's choice.
