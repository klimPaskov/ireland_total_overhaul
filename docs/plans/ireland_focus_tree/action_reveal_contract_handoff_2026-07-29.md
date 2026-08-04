# Ireland action reveal-contract handoff — 2026-07-29

## Outcome

The action-level pre-reveal finding is implemented for the exact `140` Ireland actions. Every action has exactly one reusable reveal contract inside its `visible` block. The `54` missions are unchanged and have no reveal-contract calls.

The action layer is complete without fallback or placeholder logic. Parent integration wired all thirteen category headers to the matching category reveal contracts, closing the category-to-action reachability gap described below. The later approved M2 ruling changes mission ownership and mode merging only; it does not change this action-reveal contract or the 13/140/54 inventory.

## Authority and references

Implementation was checked against:

- `AGENTS.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `docs/plans/ireland_focus_tree/source_of_truth_map.md`
- `docs/specs/ireland_focus_tree/maps/ireland_focus_tree_decision_and_mission_map.md`
- the canonical lifecycle/concealment material linked by the Ireland source-of-truth map
- the offline Decision Modding, Triggers, Effects, Data Structures, Localisation, Scopes, Modifiers, On Actions, Event Modding, Idea Modding, and AI Modding wiki pages
- vanilla `documentation/triggers_documentation.md`, `documentation/script_concept_documentation.md`, and decision precedents

The vanilla trigger documentation specifies `date > <date>` and does not document script-constant support for the date operand. The canonical fixed entry dates therefore remain literal `1939.9.1` and `1945.1.1`. Numeric reveal tuning is held in shared Ireland script constants.

## Changed files

- `common/decisions/ireland_decisions.txt`
  - Added one reveal-trigger call to each of the `140` action `visible` blocks.
  - Did not change action availability, costs, dynamic costs, command-power limits, material admission/charges, mission launches, AI weights, caps, reservations, refunds, cleanup, or route locks.
- `common/scripted_triggers/ireland_triggers.txt`
  - Added `13` category reveal contracts and `123` action-stage reveal contracts.
  - Uses authored opening, recovery, route, incident, dated, occupation-stage, and concealed-authority entry conditions.
- `common/script_constants/ireland_constants.txt`
  - Added `reveal_dail_majority_threshold`, `reveal_church_dependency_threshold`, `reveal_neutrality_recovery_threshold`, `reveal_foreign_exposure_threshold`, and `reveal_failed_order_exposure_threshold`.
- `docs/plans/ireland_focus_tree/action_reveal_contract_handoff_2026-07-29.md`
  - This handoff.

No localisation file was edited. The reveal helpers add no player-facing key, so there is no missing localisation key to transfer.

## Helper/action coverage

| Category ID | Actions | Unique action helpers | Reveal contract |
| --- | ---: | ---: | --- |
| `ireland_settlement_government` | 10 | 8 | opening, confidence/majority pressure, formation, crisis, legal review, programme, six-month review, recovery |
| `ireland_elections` | 10 | 6 | election calendar/campaign, count, formation, portfolios, charter, by-election |
| `ireland_organised_society` | 10 | 9 | public consultation, Church dependency, education/health, labour, rural/agrarian, vocational, minority, service dispute |
| `ireland_cultural_archival` | 10 | 7 | serious public lane, provincial work, site/evidence, panic, concealed transition, failed-restoration recovery |
| `ireland_radical_underground` | 10 | 10 | distinct IRA, Congress, O'Duffy, Ailtirí, and recovery gates; mission ownership is governed by the later M2 ruling |
| `ireland_provision` | 16 | 13 | component scarcity, project sequence, emergency law, shipping sequence, occupation/postwar housing, western portfolio |
| `ireland_readiness` | 14 | 14 | command, equipment, procurement, reserve, security, defence, mobility, coastwatch, harbour, patrol, liaison, agent case, plan compromise, demobilisation |
| `ireland_neutrality_incidents` | 10 | 10 | September 1939/incident entry plus airspace, internment, shipping, weather, access, censorship, border, and integrity recovery |
| `ireland_foreign` | 10 | 10 | partner-specific channels, Plan W, diaspora, German proof, safeguards, and failed-sponsor termination |
| `ireland_northern` | 10 | 10 | contact, delegations, British negotiation, plebiscite, federal, unitary, labour, wartime unity, coercion, lawful deferral |
| `ireland_occupation_integration` | 10 | 6 | occupation entry, security, rights, services, guarantees, stage-five/core review |
| `ireland_regional_external` | 10 | 10 | Celtic, Atlantic, defence, liberation, protectorate, crown, fivefold, Otherworld compact, failed-order dissolution, contribution |
| `ireland_postwar` | 10 | 10 | Emergency review, supply unwind, veterans, merchant fleet, reconstruction, republic, Commonwealth, UN, aid programme, conclusion |
| **Total** | **140** | **123** | **one helper call per action** |

## Non-live validation

- Parsed `140` action blocks: `140/140` contain exactly one `ireland_reveal_* = yes` call, and that call is inside the action's `visible` block.
- Parsed `54` mission blocks: `0/54` contain a reveal-contract call.
- Parsed category inventory: `13` categories with action counts `10/10/10/10/10/16/14/10/10/10/10/10/10`.
- Parsed helper inventory: `13` category helpers and `123` action helpers; every action helper has exactly one category-helper parent.
- Verified every country flag referenced by the new helper section has a literal `set_country_flag` or `set_timed_country_flag` producer. Trigger-shaped authorities are called as scripted triggers rather than tested as flags.
- Verified all `14` variables read by the new helpers have an existing writer; established campaign variables use the existing Ireland initialization effect, while `foreign_exposure` has existing bounded writers.
- Verified the five new `constant:ireland.*` references resolve uniquely in the shared constants file.
- Diff-shape review found exactly `140` added lines in the decisions file and no removed or altered mission/action logic. This preserves the canonical `H/P/A` availability boundaries, costs, AI, capacity, mission result ladders, refunds, and cleanup.
- Concealment spot checks:
  - `ireland_action_convene_a_hidden_evidence_council` uses only `ireland_reveal_culture_concealed`.
  - Ailtirí cell and party-state actions retain distinct writer-backed cell/public-launch route gates.
  - Otherworld compact work requires `ireland_compact_obligation_authority`.
  - later occupation work is stage-gated and cannot appear when the occupation tray first opens.
  - later regional and postwar actions require their authored route, mission-result, programme, legal, or conclusion conditions.

Live HOI4 testing was excluded by instruction.

## Parent category-header integration

The worker pass excluded `common/decisions/categories/ireland_categories.txt`. Parent review replaced each category header's duplicated or unwritten phase aliases with the corresponding `ireland_reveal_category_*` helper:

- all 13 headers retain `original_tag = IRE`;
- all 13 use exactly one matching category helper;
- duplicated route-archive and phase conditions were removed from the headers;
- the category and every action now share one writer-validated reveal contract;
- Organised Society, elections, occupation, regional work, and postwar review can no longer remain hidden because of the stale aliases.

End-to-end static category/action reachability is therefore closed at source level.

This reveal pass did not change mission declarations. The later approved M2
ruling resolves the mission-capacity question by assigning ordinals 006 and
009 to the physically nested Radical/Underground mission families while
preserving the exact 54-family inventory. See
`docs/plans/ireland_focus_tree/authority_rulings_m2_a2_c3_2026-08-01.md` and
`docs/plans/ireland_focus_tree/audits/ireland_m2_category_ownership_audit_2026-08-01.md`.
