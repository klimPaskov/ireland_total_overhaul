# Ireland Focus Tree Part 7 Validation Report

Feature slug: `ireland_focus_tree`

Validation status: historical planning report; its mandatory worker gate was later satisfied, while gameplay implementation and engine validation remain incomplete

Current-status note: this report describes the pre-implementation planning package and is retained as historical evidence. The accepted worker execution is recorded under `docs/plans/ireland_focus_tree/improvement_loop/`, and current implementation blockers are tracked in `docs/plans/ireland_focus_tree/audits/ireland_completion_followup_2026-07-18.md`.

Count-scope note (2026-07-22): the `active completion blockers | 1` result below is the historical planning-gate count for this report. It is not the current implementation-blocker count. Use `docs/plans/ireland_focus_tree/source_of_truth_map.md` for the reconciled status ledger and `docs/plans/ireland_focus_tree/audits/ireland_completion_followup_2026-07-18.md` for the latest implementation evidence.

# Result

| Measure | Result |
| --- | ---: |
| passed checks | 366 |
| failed checks | 0 |
| warnings | 0 |
| active completion blockers | 1 |
| canonical Markdown files | 35 |
| canonical words | 351,304 |
| canonical lines | 30,809 |
| canonical bytes | 2,402,852 |

At the time of this planning report, the blocker was the missing `hoi4_improvement_loop_planner` execution with `fork_context=false`. That execution has since completed and is recorded in the accepted execution report. This planning report does not substitute for the separate implementation-phase engine, asset, or scenario validation.

# Source processing

The final-gate input sweep decoded every available Markdown, TOML, text, JSON, and CSV source under `/mnt/data` before the repaired build was created. Generated final-gate work was excluded so the report did not count its own outputs.

| Input measure | Result |
| --- | ---: |
| processed text sources | 96 |
| decoded bytes | 3,157,304 |
| decoded lines | 42,620 |
| whitespace-delimited words | 456,232 |
| decoding errors | 0 |

The checksum-verified cumulative candidate was extracted into an isolated build directory. Its original internal checksum ledger passed before repair. The canonical semantic inventory then processed every heading, table, fixed identifier roster, source URL, route classification, failure reference, cleanup reference, AI reference, event reference, decision reference, and mission reference across the 35 canonical Markdown files.

The offline Paradox wiki snapshot and local Hearts of Iron IV installation named by `AGENTS.md` were consulted during implementation. Planning validation checks design consistency and handoff completeness; engine syntax, local precedent, asset, and runtime scenario validation remain separate implementation work.

# Structural validation

The validator confirmed:

- every required specification, map, matrix, research note, and prompt exists
- all 35 canonical files decode as UTF-8
- no backup or pre-canonical file remains in the canonical specification tree
- every canonical file is substantive
- Markdown fences are balanced
- headings are unique within each file
- Markdown tables have consistent columns outside fenced diagrams
- no canonical file contains `TODO`, `TBD`, or `FIXME`
- the prose rules banning em dashes and semicolons are satisfied
- the goal prompt remains below 4,000 characters
- canonical document references resolve, except for the intentionally absent mandatory worker report

# Fixed-count validation

The validator confirmed:

- 30 durable AI profiles with contiguous IDs and unique keys
- ten temporary AI overlays with contiguous IDs
- 12 foreign actor families and 12 response action classes
- a 14-day foreign reaction window and no more than four separate visible reactions before digest
- 32 achievements with the exact 8, 12, 8, and 4 tier split
- 60 sourced real-person portrait slots
- 14 institutional or collective portrait families
- 40 sourced historical symbol and document packages
- 18 alternate route flag sets
- five source-clearance states and eleven source tiers
- 120 event and news images with the 69 sourced and 51 generated split
- three scripted GUI surfaces and seven animations
- 30 route coverage rows and 15 standard conclusion families
- final convergence as a composite super-conclusion without changing the fixed conclusion count
- thirteen decision categories, 140 actions, and 54 mission families
- 18 historical event-chain families, 18 political crisis families, 12 foreign reaction families, the 236-event flavour floor, and the 484 player-facing event floor

# Constant and gate validation

The canonical index, mechanic map, route matrix, coding prompt, and owning specifications were checked for all accepted constants and gates, including:

- National Settlement opening `+25` and opening momentum `-1`
- Social Consent `55` and National Readiness `15`
- Dáil `153` formal and `152` routine
- National Provision components `55`, `25`, `40`, and `30`, displayed as `38`
- Readiness components `25`, `8`, `20`, `12`, `5`, `5`, and `30`, displayed as `15`
- Neutrality Integrity `72`
- Northern opening `U5 N40 L30 B10 S45 I10`
- three persistent route-spirit families
- mission caps `8`, `10`, and conditional `12`
- command power ceiling `60`
- Northern cores only after integration stage `5` and final review
- the complete Part 4 Dillon material, parliamentary, sovereignty, Northern, and constitutional gate
- the canonical `P/A` classification for AI-29 Otherworld containment

# Final-gate repairs

The final-gate audit found seven issues. Six were integrated:

1. removed nonpackaged plan dependencies from the mandatory worker prompt
2. normalised AI-29 from `A/P` to `P/A`
3. regenerated canonical metrics from one measured source set
4. added the root README to the declared archive inventory
5. corrected the archive name and entry count
6. replaced stale direct plan copies with the checksum-verified and repaired build

The seventh issue was the unavailable mandatory worker execution at the time of this report. It is superseded by the later execution record; current implementation blockers are listed in the follow-up audit.

# Improvement review and disposition

The parent review recorded 12 findings. Eleven were integrated into canonical sources. One was queued to implementation because the required local engine references are unavailable. The final-gate audit recorded seven further findings, with six integrated and one blocked.

The required custom improvement-loop report now exists in the later execution-report path. The planning package remains historical and cannot be used to claim gameplay completion.

# Archive validation

The repaired release-candidate archive contains 47 entries:

- 35 canonical Markdown sources
- 10 supporting evidence files
- one root README
- one internal `PACKAGE_CONTENTS.sha256` ledger

The archive passed compressed-data testing. Every listed file was extracted and matched its recorded SHA-256 value. No backup, temporary, checkpoint, continuation, or prior archive file is included.

# Completion judgment

The planning content and implementation handoff are canonically reconciled and structurally valid. The project remains incomplete under its own rules because source clearance, engine-reference checks, and required runtime scenarios remain open. The archive retains the `canonical_candidate` label as planning evidence and must not be treated as a final gameplay package.
