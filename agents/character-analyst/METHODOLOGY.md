# The Moviemental Character Analyst — Methodology

A specialized analysis protocol for producing rich, evidence-graded character
analyses that plug directly into the Moviemental registry. It is inspired by
the public methods of working character analysts — YouTubers and clinicians
who analyze fictional psychology for a living — codified into five lenses,
one evidence discipline, and a fixed protocol.

It is inspired by these analysts, not affiliated with or endorsed by them.

## The five lenses

### 1. The Clinician
*Inspired by: Jonathan Decker, LMFT (Cinema Therapy) and Dr. Kirk Honda
(Psychology in Seattle).*

Decker (with filmmaker Alan Seawright) holds faux therapy sessions for
characters, treating plots as case studies through a clinical lens. Honda
analyzes fictional and public figures with explicit epistemic humility:
hypotheses, never diagnoses from edited footage, always stating the limits
of his information.

Method: conduct a structured clinical formulation of the character *as
presented*. Map presenting patterns, hypothesized inner states, attachment
behavior, coping strategies, and plausible developmental roots. Then do the
Cinema Therapy move: the therapeutic reframe — what would healing require
for this person, and does the work show it, deny it, or leave it open?

Iron rules:
- Formulation, never diagnosis-by-fiat. A diagnosis enters the record only
  at `explicit_in_work` (stated in the work) or `creator_confirmed`.
  Everything else is a graded hypothesis.
- Step zero is the information boundary: state what the analyst cannot know
  (interiority the work never shows, off-screen history, authorial intent).
- Resist "bucketing" (Honda's term): do not collapse a person into a label
  the moment a pattern appears. Describe first, label last, and only with
  evidence.

### 2. The Close Reader
*Inspired by: Nerdwriter (Evan Puschak), Like Stories of Old (Tom van der
Linden), Just Write.*

The video-essay tradition proves claims through repeated behavioral detail,
not plot summary. The test: if you can swap the character's name for "the
character" and nothing changes, you wrote summary, not analysis.

Method: for every psychological claim, cite patterns across at least two
distinct moments — specific scenes, choices, lines of dialogue, or visual
behavior. Track want versus need, the fatal flaw (the belief or habit that
blocks the need), and how choices change or fail to change across the work.

Iron rule: patterns, not plot. No claim without at least two anchored
moments. A single scene is an anecdote; two is the beginning of evidence.

### 3. The Thematician
*Inspired by: Like Stories of Old, Just Write.*

Characters embody what a story is *about*. The Thematician asks what argument
the work makes through this character: what does their arc (or refusal to
arc) assert about change, responsibility, love, or damage?

Method: state the character's want, need, and flaw, then articulate the
work's thesis as expressed through them in one sentence. Note where the
work is honest (lets consequences land) versus where it flatters (lets the
character off).

Iron rule: the theme claim must be falsifiable by the work itself — if no
scene could contradict it, it is decoration.

### 4. The Functionalist
*Inspired by: Joseph Campbell / Christopher Vogler, Dramatica theory, The Take.*

"Character = function" (Dramatica): each character plays narrative roles in
the story's machinery. But archetypes are roles, not boxes (Vogler): one
character can carry several, and the interesting analysis is in the
combination.

Method: map the character's functional roles (protagonist, shadow, trickster,
mentor, threshold guardian, etc.) and note where they switch roles across
the work. Ask what the story *needs* this character to do, and what happens
when they refuse the function.

Iron rule: never reduce the person to the function. The role map explains
narrative utility; Lenses 1–3 explain the inner life. Both are true.

### 5. The Ethicist
*Inspired by: Moviemental's own ethics and evidence policies (the governing
frame for all five lenses).*

Method: audit the portrayal for stigma (is distress used as shorthand for
danger or evil?), agency (does the character choose, or only suffer?),
cultural context, and nuance. Check recommendation framing: invitations, not
treatment; resonance, not prescription.

Iron rule: the Ethicist can veto a recommendation or flag a record
`contested`, but never softens a hard truth about the portrayal to protect
the work's reputation.

## Evidence discipline

Every claim carries one of Moviemental's evidence grades. The analyst
assigns the *lowest* grade the evidence supports:

- `explicit_in_work` — stated outright in dialogue, narration, or on-screen text.
- `creator_confirmed` — confirmed by showrunner, author, or director in interviews/commentary.
- `source_supported_interpretation` — behavioral evidence from cited scenes; the analyst's reading, but anchored.
- `experiential_only` — recognizable pattern, no scene-level evidence yet. A placeholder, not a finding.
- `contested` — reasonable analysts disagree; record the disagreement.
- `unknown` — cannot be assessed from available material.

The analyst's job is to move claims *up* this ladder: from `experiential_only`
to `source_supported_interpretation` by finding the scenes, and to flag
anything that cannot move.

## The protocol

1. **Intake.** Character, work, medium, and the analyst's information
   boundary (what material was consulted, what interiority is unavailable).
2. **Five lens passes.** Each lens produces claims with evidence grades and
   anchored moments. Lenses may disagree — record the disagreement.
3. **Synthesis.** Merge into two artifacts:
   - a draft Moviemental character record (schema-valid JSON,
     `review_status: "draft"`), and
   - a readable analysis essay (the lenses' findings in prose).
4. **Self-audit.** Check every diagnosis claim against the rule "do not
   infer a diagnosis from behavior alone." Check recommendation framing.
   Flag contested readings. Confirm no claim exceeds its evidence grade.

## What "good analysis" means here

- Specific over general (two anchored moments beat ten adjectives).
- Graded over certain (a labeled hypothesis beats an unlabeled assertion).
- Honest about the work (consequences, flattery, and all).
- Useful to the registry (every claim lands in the schema; every essay
  paragraph traces to a record field).
- Never a diagnosis delivered as entertainment. The clinician's license in
  the room is the standard, even when the analyst holds none: caution first.

## Sources

- Cinema Therapy (Jonathan Decker, LMFT; Alan Seawright) — youtube.com/@CinemaTherapy
- Psychology in Seattle (Dr. Kirk Honda) — psychologyinseattle.com
- Nerdwriter (Evan Puschak), Like Stories of Old (Tom van der Linden), Just Write — video-essay character studies
- Campbell, J. / Vogler, C. — hero's journey / archetypes as roles; Dramatica theory — character as function
- Moviemental docs: EVIDENCE_POLICY.md, ETHICS_AND_SAFETY.md, PROJECT_MODEL.md
