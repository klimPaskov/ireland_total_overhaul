# Ireland country-package documentation cleanup handoff

Date: 2026-08-14  
Feature slug: `ireland_country_package`  
Owner: `hoi4_documentation_curator`  
Status: reconciled through `89ff719`; parent review and commit required. No gameplay, asset,
localisation, spreadsheet, or thumbnail file was edited by this pass.

## Source-of-truth map

| Surface | Current authority | Evidence boundary | Disposition |
| --- | --- | --- | --- |
| Country-package design | `docs/specs/ireland_country_package/index.md` and its linked spec pages | Accepted specification plus implementation through `89ff719` | Current source of truth |
| Implementation reconciliation | `docs/specs/ireland_country_package/implementation_matrix.md` | 218 focuses, 222 connectors, P0/P1/P2 gameplay and accepted family-lane reflow | Current ledger; parent completion audit remains |
| Focus-tree status | `docs/plans/ireland_focus_tree/project_status.md` and `source_of_truth_map.md` | 2026-08-14 status block; older snapshots retained below historical headings | Current status plus historical provenance |
| Active feature summary | `docs/ireland_political_industrial_and_territorial_expansion.md` | 218/222, five families, seven concerns + two MIOs, P1 paths, Parliament, report cadence | Current package-facing summary |
| Runtime systems context | `docs/ireland_systems.md` | Current package status at top; broad historical inventory explicitly retained as context | Context, not completion authority |
| Event cadence | `docs/ireland_event_programme.md` | Monthly skip-after-dispatch, 120-day foreign broker, direct family reports | Current cadence summary |
| Country-package source audit | `docs/plans/ireland_country_package/subagent_handoffs/final_country_package_audit_2026-08-14.md` | Read-only source audit at `89ff719`; static pass with the same one nonblocking clerical detour | Concurrent evidence; not a live-save sign-off |
| Gameplay plans | `docs/plans/ireland_country_package/*.md` | Each root plan has an implementation disposition | Working evidence; no plan overrides specs |
| Improvement loop | `docs/plans/ireland_country_package/improvement_loop/ireland_country_package_post_tranche_addendum_2026-08-14.md` | Promoted P0/P1/P2 contracts and accepted family-lane presentation | Provenance and disposition record |
| Decision lifecycle | `docs/plans/ireland_country_package/subagent_handoffs/decision_audit_fixes_handoff_2026-08-14.md` | Exact terminal/cancellation behavior after `1984ff0` | Current lifecycle handoff |
| Family layout | `docs/plans/ireland_country_package/subagent_handoffs/ireland_country_package_family_lane_reflow_completion_2026-08-14.md` | `89ff719`; 218 focuses, 222 connectors, x `-26..21`, y `0..22`, zero structural diagnostics, one retained nonblocking clerical detour | Accepted coordinate-only reflow; parent completion audit remains |
| Layout history | `ireland_country_package_p0_family_band_layout_handoff_2026-08-14.md` and `ireland_country_package_p0_family_band_layout_final_handoff_2026-08-14.md` | Failed gateway-only trial plus reversible pre-reflow coordinate table | Superseded/retained evidence; do not use as current contract |
| Asset registration | Feature manifests under `docs/assets/ireland_*` and parent-wiring handoffs under the country-package handoff directory | Parent `.gfx`/event consumers read read-only around the registered surfaces | Wired for the listed packages; layout is separately accepted |

## Current implementation ledger

- The focus source is 218 focuses, 222 connectors, and three opening trunks.
  The accepted `89ff719` reflow places the five family roots in ordered lanes
  at row 18 with descendants in rows 19–22, bounds x `-26..21`, y `0..22`.
  Crossings, intersections, long connectors, duplicate coordinates, visible
  overlaps, and same-row spacing defects are zero. The authored
  clerical-failure two-column detour is retained as a nonblocking warning;
  straightening it would cross the adjacent Congress corridor.
- Five public families each have one 180-day settlement and one 120-day
  recovery. The five exact settlement/recovery pairs are recorded in the
  lifecycle specification and the decision audit-fix handoff.
- P1 territorial recovery is implemented for democratic plebiscite relaunch,
  Congress workers' border campaign, fascist withdrawal, restoration
  Provincial Assent reconvening, and the existing Belfast compact reopening.
- Seven selectable concerns and two MIOs expose nine 35-day factory-reserving
  contracts with distinct outputs.
- The Parliament enabled-state repair is implemented: green/brass enabled,
  engine-darkened unavailable, guarded executors shared with native decisions.
- Ordinary reports use the monthly paced dispatcher; foreign reactions use a
  120-day admission cooldown; family reports dispatch directly and use five
  distinct 210x176 report-art consumers.
- The exact decision lifecycle is terminal on natural expiry and cleanup-only on
  cancellation. Selection reserves inputs and sets `_in_progress`; selection
  does not create a durable result.

## Plan and handoff disposition table

| Document or package | Disposition | Current interpretation |
| --- | --- | --- |
| `implementation_tranche_a_national_question_territorial_2026-08-14.md` | Implemented; family-lane layout accepted at `89ff719` | National Question chain, territorial source contracts, and final layout evidence are current; parent audit remains |
| `implementation_tranche_c_industrial_contract_inputs_2026-08-14.md` | Implemented | Nine contracts, 35-day reservations, and distinct outputs are current |
| `implementation_tranche_d_northern_outcome_gates_2026-08-14.md` | Implemented | P1 outcomes and Belfast recovery are current |
| `p0_atlantic_and_p2_payoff_implementation_2026-08-14.md` | Implemented; layout accepted at `89ff719` | P2 payoff contract is current; parent audit remains |
| `p0_family_postwar_conclusion_implementation_2026-08-14.md` | Implemented; layout accepted at `89ff719` | Five settlements, five recoveries, reports, archive lifecycle, AI, and final layout evidence are current |
| `parser_and_parliament_button_fix_2026-08-14.md` | Implemented in `070fbb5`; lifecycle follow-up in `1984ff0` | Bounded Parliament/parser repair is closed; not a whole-package completion claim |
| `improvement_loop/ireland_country_package_post_tranche_addendum_2026-08-14.md` | Accepted and promoted | P0/P1/P2 findings and family-lane presentation are implemented; parent audit remains |
| `ireland_country_package_p0_conclusion_architecture_handoff_2026-08-14.md` | Implemented handoff | Helper and report architecture is current; parent report wiring is closed |
| `ireland_country_package_p0_ai_priority_handoff_2026-08-14.md` | Implemented handoff | Family/recovery AI priority is current; live AI scenarios remain parent validation |
| `ireland_p1_territorial_recovery_handoff_2026-08-14.md` | Implemented handoff | P1 recovery and cleanup source evidence is current; live engine timing remains a risk |
| `decision_audit_fixes_handoff_2026-08-14.md` | Current replacement handoff | Exact timed-project terminal and cancellation lifecycle after `1984ff0` |
| `final_decision_mission_audit_2026-08-14.md` | Superseded, retained | Six pre-fix issues are historical evidence, not current blockers |
| `baseline_completion_gap_audit_2026-08-14.md` | Superseded, retained | Baseline 215-focus/P0/P1 gaps are historical |
| `current_implementation_map_2026-08-14.md` | Superseded, retained | Pre-integration missing-event/icon findings are historical |
| `ireland_country_package_p0_family_postwar_decisions_handoff_2026-08-14.md` | Superseded for current lifecycle | Initial terminal/evaluator/AI concerns were closed by later parent work and `1984ff0` |
| `ireland_country_package_improvement_loop_handoff_2026-08-14.md` | Historical design handoff | Its accepted contracts and final family-lane evidence are superseded by current specs and `89ff719`; pending wording is retained history |
| `ireland_p0_family_conclusion_report_art_2026-08-14.md` | Complete and wired | Five report sprites are registered and consumed by `.1`–`.5` |
| `wales_cornwall_report_art_2026-08-14.md` | Complete and wired | Seven territorial report sprites are registered; `.25`–`.27` are event-led no-picture records |
| `ireland_country_package_family_lane_reflow_completion_2026-08-14.md` | Accepted at `89ff719` | Five ordered family lanes; zero structural diagnostics; one retained nonblocking clerical detour |
| `ireland_country_package_p0_family_band_layout_handoff_2026-08-14.md` | Superseded, retained | Clean baseline and bounded gateway-only trial failure remain audit evidence |
| `ireland_country_package_p0_family_band_layout_final_handoff_2026-08-14.md` | Superseded, retained | Reversible pre-reflow coordinate table; not the current layout contract |

## Contradiction list

### Resolved in this cleanup

1. Old focus-tree records reported 150, 211, or 215 focuses. Active status and
   country-package records now use 218 focuses and 222 connectors; old counts
   remain only under historical notices or historical sections.
2. The old feature summary described Parliament controls as grey and contracts
   as Political-Power selections. It now records green/brass enabled state,
   engine-darkened unavailable state, and nine factory-reserving contracts.
3. Earlier P0/P1 plans and audits described missing conclusion reports,
   Wales/Cornwall events, recoveries, or unregistered National Question icons.
   Current manifests and handoffs record those surfaces as wired; the old maps
   are explicitly superseded rather than deleted.
4. Earlier decision audits described launch-time outcomes, missing cancellation
   cleanup, and stale cooldown handling. The active lifecycle handoff and specs
   now use the `1984ff0` terminal model.
5. Earlier feature docs described one broad postwar settlement mission. Current
   docs record five 180-day family settlements and five 120-day recoveries with
   direct report art and archive-only success options.
6. Earlier cleanup records left the family-lane geometry unresolved. The
   accepted `89ff719` handoff now establishes five ordered parallel lanes,
   zero structural diagnostics, and the retained nonblocking clerical detour;
   the earlier one-row/two-row interpretation conflict is historical.

### Still open

1. Static documentation does not replace parent-owned live engine/scenario
   evidence for timed decision ordering, AI recovery choice, event cadence, or
   Parliament state transitions.
2. Broad historical focus-tree/system docs still contain old inventories in
   retained sections. Their current blocks now point to the country-package
   authority, but they should not be mistaken for a unified whole-repository
   completion report.

## Duplicate, superseded, and retained documents

- Superseded focus completion inventories: `focus_parliament_event_completion_2026-08-13.md`, `focus_parliament_reward_density_completion_2026-08-13.md`, and `political_industrial_territorial_expansion_completion_2026-08-13.md`. Notices were added; evidence was not deleted.
- Already historical focus records left unchanged: `focus_tree_parliament_completion_2026-08-09.md`, `part_7_validation_report.md`, and older dated audit/handoff records under `docs/plans/ireland_focus_tree/`.
- Superseded country-package audits: `baseline_completion_gap_audit_2026-08-14.md`, `current_implementation_map_2026-08-14.md`, and `final_decision_mission_audit_2026-08-14.md`.
- Current layout evidence: `ireland_country_package_family_lane_reflow_completion_2026-08-14.md` at `89ff719`.
- Concurrent source-level audit: `final_country_package_audit_2026-08-14.md` at
  `89ff719`; it is evidence, not a live-save sign-off.
- Superseded layout records retained for audit/rollback: the gateway-only trial handoff and the pre-reflow coordinate-table handoff.
- Retained asset provenance with current runtime status: National Question, P0 family reports, P0 settlement/recovery icons, alternate-order icon, and territorial diplomacy manifests/handoffs.
- No files were deleted or merged destructively. Historical bodies remain available for audit traceability.

## Stale prompt or instruction list

- `docs/specs/ireland_country_package/prompts/goal_prompt.md` and
  `implementation_prompt.md` remain current design prompts: they contain no
  obsolete focus counts or “do this again” instructions. They correctly direct
  the final audit and prohibit fallbacks.
- The former P0 icon handoff under
  `docs/plans/ireland_country_package/improvement_loop/` was stale because it
  called exact registered sprites “PROPOSED” and asked for parent wiring. It now
  records runtime closure and points to the full-ID sprite convention.
- The former Wales/Cornwall and P0 conclusion-art handoffs were stale because
  they requested parent `.gfx` insertion. They now record parent wiring closure.
- The body of `current_implementation_map_2026-08-14.md` still contains its
  original explorer instructions and baseline findings by design; its top
  disposition makes clear that those instructions must not drive new work.
- No current country-package prompt requires redoing the implemented P0/P1/P2
  mechanics or the accepted family-lane reflow. The only active work is the
  parent completion audit/live scenario evidence.

## Recommended parent decisions

1. Run the parent-owned live/scenario completion audit for timed lifecycle,
   recovery-priority AI, Parliament button states, report cadence, and asset
   consumers. Do not reopen mechanics based on superseded audits.
2. At final release, optionally add an index linking the retained historical
   focus-tree docs to this package handoff; do not delete historical evidence.

## Patch handoff

### Files changed

This curator pass changed documentation only. The exact modified-file list is
reported by the parent-facing `git diff --name-only`; grouped surfaces are:

- current country-package specs: index, implementation matrix, campaign
  architecture, economy/defence/statecraft, territorial campaign,
  systems/lifecycles, and AI/balance/assets/text;
- country-package root plans, improvement addendum, and historical country-
  package audits/handoffs listed in the disposition table;
- National Question, territorial diplomacy, P0 conclusion, settlement/recovery,
  and alternate-order asset manifests/handoffs;
- active focus-tree status/source-of-truth/planning records, historical focus
  completion notices, `docs/ireland_political_industrial_and_territorial_expansion.md`,
  `docs/ireland_systems.md`, and `docs/ireland_event_programme.md`;
- the accepted family-lane completion handoff reference, this cleanup handoff,
  and `documentation_resume_packet_2026-08-14.md`.

`thumbnail.png` and the rejected gateway-only layout handoff were left
untouched. The reversible pre-reflow coordinate-table handoff was retained and
marked superseded; the accepted family-lane completion handoff was committed at
`89ff719`.

### Dispositions changed

- Promoted/current: accepted P0/P1/P2 gameplay contracts, lifecycle fix,
  Parliament repair, report/icon runtime wiring, and current status summaries.
- Superseded/retained: baseline audits, pre-fix decision audit, explorer map,
  old focus counts, old completion reports, and old asset “proposed” language
  where it described an earlier integration state.
- Accepted: final family-lane renderer evidence at `89ff719`, including the
  nonblocking clerical detour rationale.
- Open: parent completion audit/live scenario evidence only.
- Unchanged: canonical goal and implementation prompts, broad historical docs
  whose old bodies are clearly under historical headings, and all gameplay or
  asset source files.

### Validation checks run

- Read-only source checks confirmed the current focus source contains 218 IDs,
  the active docs consistently use 218/222/3, and no active country-package
  record still presents 215 as current.
- `rg` checks reconciled proposed/unregistered terms in the touched P0/P1
  manifests and handoffs against the registered `.gfx`/event surfaces.
- Focus, decision, event, GFX, and DDS paths were inspected narrowly around the
  current IDs; five conclusion sprites, seven territorial sprites, ten
  settlement/recovery sprites, the alternate-order sprite, and three National
  Question focus sprites were matched to the documented consumers.
- Plan roots and country-package handoffs were read and assigned a disposition;
  superseded audits retain their original evidence and carry replacement links.
- No gameplay parser, renderer, live engine, AI simulation, or scenario check
  was run by this documentation-only pass. Those checks are deliberately
  parent-owned and remain an open risk rather than being implied as passed.

## Remaining risks

- The parent may want to recheck the committed focus geometry in a fresh local
  render; the accepted inspection reports zero structural diagnostics, with
  only the documented nonblocking clerical detour retained.
- Live engine timing and AI behavior are not proven by static docs alone.
- The broader Ireland focus-tree/system archive contains many historical counts;
  readers must follow the current package authority links at the top of active
  docs.

No gameplay completion claim is made by this handoff. Parent review and commit
are required.
