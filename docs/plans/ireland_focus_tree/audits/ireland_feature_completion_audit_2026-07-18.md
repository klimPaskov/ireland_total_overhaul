# Ireland overhaul feature-completion audit — 2026-07-18

Audit role: `hoi4_feature_completion_auditor`  
Feature slug: `ireland_focus_tree`  
Disposition: **incomplete and blocked; final decisions remain with the main agent**  
Edit boundary: documentation report only; no gameplay, localisation, interface, or asset file was edited.

Supersession note (reconciled 2026-07-22): this audit predates the ordered flavour-chain repair, the 30-plan/194-priority AI repair, the semantic achievement-asset wiring, the processed P-02 Lemass source, the runtime mission counters/reservations, the GUI request consumers, and the route-identity wiring. Its findings are retained as the audit snapshot; the current disposition is in `docs/plans/ireland_focus_tree/audits/ireland_completion_followup_2026-07-18.md` and the normalized ledger is `docs/plans/ireland_focus_tree/source_of_truth_map.md`. Source clearance and all live engine/scenario validation remain unresolved.

## Scope and source precedence

This audit compares the current workspace against:

- `AGENTS.md`;
- the canonical package rooted at `docs/specs/ireland_focus_tree/`, especially `ireland_focus_tree_index.md`, Parts 1–6, the coding prompt, specialised prompts, matrices, maps, and research notes;
- the current Ireland implementation under `common/`, `events/`, `history/`, `interface/`, `localisation/`, `gfx/`, and `assets/ireland_focus_tree/`;
- `docs/plans/ireland_focus_tree/` plans, improvement-loop addenda and dispositions, manifests, clearance records, handoffs, status files, and earlier audits;
- the required offline wiki pages and relevant local vanilla documentation and precedents named by `AGENTS.md`.

The canonical fixed budget is recorded at `docs/specs/ireland_focus_tree/ireland_focus_tree_index.md:108-121`. It includes 13 categories, 140 actions, 54 mission families, at least 484 player-facing events including at least 236 flavour events, exactly 30 durable AI profiles plus 10 overlays, 32 achievements, 60 real-person portraits, 14 institutional/collective portraits, 40 source packages, one historical base flag plus 18 alternate sets, 120 event images split 69 sourced/51 generated, exactly three scripted GUIs, and exactly seven animations.

Current asset repair addendum (2026-07-22): the historical base-flag gap cited by this historical audit has been repaired with the S-01 source-derived `IRE.tga` normal/medium/small set, and the five C4 portrait registrations plus 22 C3 review registrations are recorded in the current source manifest/GFX handoff. The source-clearance and live-engine gates remain open; the older findings below are retained as historical audit evidence.

Older audits and handoffs are useful historical evidence but are not automatically current. In particular, the current source has since added Dillon and Northern setters, lawful Northern core review, route character/party/identity effects, 40 AI strategy blocks, 22 focus plans, 18 alternate flag families, and scripted Northern localisation. This report does not repeat older missing-file claims where the present source contradicts them.

## Completion status by surface

| Surface | Status | Current evidence | Blocking or unproven remainder |
|---|---|---|---|
| Canonical source and plans | Partial | The source-of-truth package and mandatory improvement-loop report exist. | Status/validation files still say the worker report and local references are unavailable; ILR-01–ILR-09 remain broadly queued without current per-finding closure. |
| Shared runtime and route lifecycle | Partial, structurally improved | Initialisation, route character activation/retirement, party politics, spirits, identities, Dillon gating, Northern review, and cleanup helpers exist in `common/scripted_effects/ireland_runtime.txt`. | No live scenario proof for route changes, deaths, election defeat, coalition collapse, sponsor defeat, occupation end, postwar cleanup, or conclusion failure/partial paths. |
| Focus tree | Structurally present; runtime unproven | Current inspection resolves 216 nodes and 216 titles, with no Ireland-tree diagnostics or connector crossings. | No in-engine prerequisite, bypass, mutual-exclusion, search-filter, AI-route, or route-coverage playthrough. The rendered layout spans 455 columns, so navigation/readability remains an in-game risk. |
| Decisions and missions | **Blocked by semantic simplification** | Current source contains 13 categories, 140 action cost blocks, and 54 mission timeouts; all 194 action/mission entries have `ai_will_do`. | Per-category caps and the reserved critical-slot contract are not implemented as specified; AI weights do not consume durable profiles/overlays; no objective/partial/failure/cancellation/exploit scenario audit. |
| Events | **Blocked by chain semantics and validation** | 249 main events plus 236 flavour events = 485; runtime has 485 matching dispatch calls. | Follow-up flags are write-only, the dispatch cursor is write-only, and family nodes are independently eligible rather than outcome-linked chains. No bounded Ireland event-tool pass or live trigger/scope/follow-up test exists. |
| Country package, leaders, parties, identity, Northern state | **Blocked by runtime assets/localisation; lifecycle unproven** | Current runtime applies route leaders, parties, spirits and 18 cosmetic tags. Northern core grant is gated through the review helper rather than opening history. | Eleven referenced route portrait sprites are undefined; all 18 cosmetic tags lack country-name localisation; no live state/control/occupation/integration/core audit. |
| AI | Partial | `common/ai_strategy/ireland_ai_strategy.txt` has 40 top-level blocks, including 10 overlays; runtime synchronises overlay flags. | Only 22 focus plans exist for 30 durable profiles, several profiles are collapsed into route-family plans, and decision/mission AI has no profile or overlay references. Required queue, hidden-route, sponsor-collapse, Northern, war, recovery, and conclusion simulations are absent. |
| Achievements | **Blocked by engine icon placement and hidden-state contract** | `common/achievements/ireland_achievements.txt` has 32 definitions and durable tracking helpers exist. | No Ireland files exist under engine path `gfx/achievements/`; the 96 staged files use ordinal names elsewhere. Seven canonically hidden/reveal-gated achievements have no `hidden = yes` or equivalent hidden presentation. No all-32/disqualifier test exists. |
| Sourced and generated assets | **Blocked by clearance and wiring** | Fixed icon families, generated event art, GUI art, seven animation registrations, and 18 alternate flag sets are present; all 793 Ireland `texturefile` paths currently declared in `.gfx` resolve. | 59/60 real portraits, 37/40 source packages, and 68/69 sourced event/news slots remain unavailable; five cleared/review assets are not wired. The 14 collective portraits and historical base flag have no completed canonical-to-runtime disposition. |
| Scripted GUI and animation | Partial | Exactly three scripted GUIs and seven `frameAnimatedSpriteType` registrations exist. Northern model/region/failure scripted localisation is wired through `context_aware_text`. Northern review runs sync, core review and achievement tracking. | Row-selection variables are write-only; conditions-review and evidence-inspection request flags have no gameplay consumer. No current live-value, resolution, click-region, reveal, or fallback test exists. |
| Localisation and researched text/audio | Partial | Broad Ireland localisation and scripted Northern text exist. | All 18 cosmetic identities are unlocalised. The selected constitutional quote, *The Celtic Twilight* allusion, and Dúchas evidence backup in the text handoff are not found in shipped localisation. Audio remains optional and unselected, so it is an open optional package rather than a gameplay blocker. |
| Validation and completion evidence | **Blocked** | Current static counts, path resolution, source-clearance audit, and focus inspection provide useful bounded evidence. | The mandatory task-specific parser/error, in-engine, AI, GUI, achievement, event-chain, asset-clearance, and 22-scenario validation set at `ireland_focus_tree_coding_prompt.md:297-341` has not been demonstrated. |

## Current verified implementation and corrected stale claims

The following current-source facts should be retained when planning repairs:

- Dillon and Northern gates are no longer simply absent. Dillon state is set in `common/scripted_effects/ireland_runtime.txt:1686` and consumed by the focus gate at `common/national_focus/ireland_focus_tree.txt:1631`. Northern settlement state and core review appear at `common/scripted_effects/ireland_runtime.txt:1791-1814`, with the focus gate at `common/national_focus/ireland_focus_tree.txt:2983`.
- Route character, party, spirit and cosmetic identity transitions are implemented across `common/scripted_effects/ireland_runtime.txt:1052-1590`.
- Mission occupancy is rebuilt from 54 active mission flags at `common/scripted_effects/ireland_runtime.txt:5-276`; this is real lifecycle work even though category-cap semantics remain wrong.
- The AI strategy registry currently has 40 top-level blocks and 10 of them are overlays. The focus-plan layer currently has 22 top-level `IRE_ireland_*` plans at `common/ai_strategy_plans/IRE_ireland_strategy_plans.txt:6-659`.
- The icon families currently contain 216 focus, 13 category, 140 decision-action, 54 mission, 63 spirit, 27 temporary-overlay, 51 law, 45 mechanic-ledger, and 96 achievement DDS files. There are 18 alternate flags in each of `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`.
- `interface/ireland_northern_ledger.gui:110-146` calls `[GetIrelandNorthernModel]`, `[GetIrelandNorthernRegion]`, and `[GetIrelandNorthernFailureState]`; these functions exist in `common/scripted_localisation/ireland_localisation.txt:6-79`. The dynamic Northern projection is therefore wired, contrary to older static-text concerns.

These facts establish substantial implementation volume. They do not prove canonical behavior or release readiness.

## Missing or simplified requirements

### 1. Per-category caps and critical mission slots are reduced to the global cap

The canonical prompt fixes different category caps at `docs/specs/ireland_focus_tree/prompts/ireland_focus_tree_decision_mission_prompt.md:11-27`: five opening categories cap at 2, Provision and Readiness change from 3 to 4 in their emergencies, Neutrality changes from 2 to 3 during an incident, Northern/occupation/postwar cap at 3, and the remaining categories cap at 2. Critical component, invasion, constitutional, occupation, and route-review objectives must reserve slots.

Current `ireland_update_mission_capacity` rebuilds the global active count, but every category `_at_capacity` flag at `common/scripted_effects/ireland_runtime.txt:284-369` compares the same `ireland_active_mission_count` against the same global `ireland_mission_capacity`. No category-specific active counts or cap variables were found. `ireland_critical_slot_reserved` is set only when the global queue is already full at `:280-281`; it does not pre-reserve a slot, pause or replace a lower-priority routine objective, or distinguish the required critical classes.

Impact: the fixed category-cap table, critical queue behavior, simultaneous-emergency behavior, and AI queue contract are not implemented. This is a gameplay blocker, not a balance-polish issue.

### 2. Event volume is present, but the canonical chains are not causally linked

The canonical event contract requires named multi-node sequences and outcome ranges, for example the separate 1937 drafting/campaign/plebiscite/election/commencement nodes at `ireland_focus_tree_spec_part_5_decisions_events_and_lifecycles.md:493-534`. The current files do meet the numeric floor: 249 main and 236 flavour definitions, with 485 runtime calls and no count shortfall.

Semantic evidence does not show real follow-up chains:

- all 249 main events and all 236 flavour events write a `ireland_followup_*` flag;
- no `has_country_flag` or `clr_country_flag` reader for those follow-up flags was found in either Ireland event file or the runtime dispatcher;
- `ireland_event_dispatch_cursor` is assigned 485 times but never checked;
- the H01 nodes at `events/ireland_events.txt:7-343` use substantially independent date/profile/gateway triggers. The following node does not require the prior node's closed flag or branch result;
- the dispatcher at `common/scripted_effects/ireland_runtime.txt:2287-2344` obtains seriality from a monolithic first-eligible scan and `ireland_event_dispatch_taken`, not from family state or outcome linkage.

Impact: ordering can be driven by file order and date eligibility, while a previous choice does not demonstrably select, block, or alter the next required node. Count compliance therefore masks a chain simplification. The 18 historical, 18 crisis, 12 foreign-reaction, conclusion, and cleanup families require semantic inspection and scenario repair rather than another event-count pass.

### 3. AI registry count exists, but action/mission and profile parity do not

The 40 strategy-block count satisfies the declared 30+10 roster at a registry level. Runtime overlay activation/exit flags are also present. However:

- `common/ai_strategy_plans/IRE_ireland_strategy_plans.txt` has 22 plans, not one plan per durable profile. IRA, Congress, O'Duffy, clerical/producer, High King, Five Provinces and Otherworld variants are collapsed into route-family plans (`:451-659`);
- `common/decisions/ireland_decisions.txt` contains `ai_will_do` for all 140 actions and 54 missions, but contains zero `ireland_profile_*` and zero `ireland_overlay_*` references;
- representative action AI is a static base plus a blocked-state zero, e.g. `common/decisions/ireland_decisions.txt:160-166`, rather than the AI matrix's primary/support domains, deadlines, feasibility, burden, dependency, consent, exposure, repetition, region collision, emergency pre-emption, and reserved-slot behavior.

Impact: focus-selection scaffolding exists, but canonical decision/mission priority equivalence is not demonstrated. Hidden-route prohibitions, sponsor collapse, invalid delivery, Northern models, war entry/demobilisation, and recovery-profile moves remain untested.

### 4. Achievement icon delivery does not follow the engine custom-achievement contract

The current 32 definitions and tracker flags are substantial. Static reference checks found every achievement's durable flags/variables represented in runtime tracking surfaces. The visual delivery is nevertheless blocked:

- the offline `paradox_wiki/Achievement modding - Hearts of Iron 4 Wiki.md:84-90` states that custom achievements require three exact-ID images under `gfx/achievements/` and do not require an interface `spriteType`;
- the workspace has zero Ireland files under `gfx/achievements/`;
- 96 files instead exist at `assets/ireland_focus_tree/icons/final_dds/achievements/` as `achievement_ireland_001.dds`, `_grey`, `_not_eligible`, etc.;
- they are registered as ordinary sprites beginning at `interface/ireland_secondary_assets.gfx:244`, while the achievement ID is semantic, e.g. `ireland_constitution_with_confidence` at `common/achievements/ireland_achievements.txt:20`.

The hidden contract is also missing. The matrix says hidden achievements start invisible at `docs/specs/ireland_focus_tree/matrices/ireland_focus_tree_achievement_matrix.md:16`, with A-22, A-27 and A-28 reveal-gated and A-29–A-32 hidden at `:53-63`. Current achievement source has six reveal-flag references but zero `hidden = yes` declarations, and all names/descriptions are exposed in `localisation/english/ireland_l_english.yml:3007-3028`.

Impact: the 96 staged icons do not prove that the engine will load them for custom achievements, and seven hidden/reveal-gated entries do not meet the presentation contract. All 32 triggers and disqualifiers remain unvalidated in game.

### 5. Real portraits and sourced event/news art remain release blockers

The audit's historical clearance snapshot recorded the following at audit time. These values are retained for audit provenance, but are superseded for current status by `docs/plans/ireland_focus_tree/assets/source_manifest.json` and `docs/plans/ireland_focus_tree/assets/clearance_audit.md`:

- `docs/plans/ireland_focus_tree/assets/clearance_audit.md:11-13` records 1/60 portraits complete, 2/40 symbol/document packages complete plus one review-pending, and 1/69 sourced event/news slots complete;
- `:29` records 164 C1 leads, one C2 package, one C3 package, and three C4 entries;
- `:57-60` states that 59 portraits and 68 sourced event/news slots lack exact object-level clearance;
- `docs/plans/ireland_focus_tree/assets/source_research_report.md:72` independently records 59 portrait, 37 source-package, and 68 sourced event/news blockers.

Runtime evidence makes this more than a documentation-only gap:

- `common/characters/ireland_route_characters.txt:9-119` references 11 `GFX_ireland_portrait_*` sprites; none is defined in any current `.gfx` file;
- only five sourced final DDS files exist under `assets/ireland_focus_tree/sourced/final_dds/`, and no filename reference to them was found in current gameplay/interface source;
- the Ireland event files expose exactly 51 unique `picture` sprites, matching the generated allocation. No second 69-image sourced allocation is wired, so the canonical 120-image split is not delivered.

The canonical 14 institutional/collective portraits at `ireland_focus_tree_asset_ledger.md:23` also lack a 14-entry canonical-to-runtime manifest. Four institutional characters currently use route emblems at `common/characters/ireland_route_characters.txt:130-163`; this may be an intended reuse, but the handoffs do not disposition the full 14-item requirement.

Impact: route leaders can resolve to missing portraits, and the historically anchored visual programme is mostly unavailable. No generated likeness or generic substitution is allowed under the canonical asset rules.

### 6. Cosmetic identities have flags but no country-name localisation

The runtime applies 18 tags from `IRE_IRELAND_ARMY_COUNCIL` through `IRE_IRELAND_CONVERGENCE_ORDER` at `common/scripted_effects/ireland_runtime.txt:1485-1587`, and all 18 flag families exist at normal/medium/small sizes. No localisation entry beginning with any of those 18 cosmetic-tag IDs was found under `localisation/`.

Impact: route transformations risk raw/fallback country naming even where the correct flag appears. This blocks a complete country-package handoff.

The historical base flag is also unresolved. There is no feature-owned `IRE.tga` at any of the three runtime flag sizes. The source manifest's S-01 record is conditional, while runtime currently falls through to the vanilla base flag. The main agent must explicitly accept and document controlled vanilla reuse or deliver the canonical sourced historical base set; it cannot remain an undisclosed fallback.

### 7. GUI projection is present, but several interactions are write-only

The three GUI surfaces and seven animations meet the fixed structural count, and all current Ireland `.gfx` texture paths resolve. Northern dynamic text is correctly wired, and its review action performs real work at `common/scripted_guis/ireland_scripted_guis.txt:180-185`.

The remaining interaction gap is narrower:

- `ireland_conditions_selected_row` is written 15 times at `common/scripted_guis/ireland_scripted_guis.txt:18-74` and read nowhere;
- `ireland_northern_selected_row` is written six times at `:173-178` and read nowhere;
- `ireland_evidence_selected_row` is written five times at `:260-264` and read nowhere;
- `ireland_conditions_review_requested` is only set/cleared at `:78-82`;
- `ireland_concealed_evidence_inspection_requested` is only set/cleared at `:265-266`.

The visible conditions and evidence button copy promises to open a scheduled review/current evidence record at `localisation/english/ireland_l_english.yml:3148-3149` and `:3184-3185`, but no handoff consumes those request flags. If row clicks are intentionally decorative selection state, that simplification is not documented; if they are intended to alter detail projection, that behavior is missing.

### 8. Asset-budget and researched-text dispositions drift from the canonical ledger

The canonical asset ledger fixes 70 decision-action icons with controlled reuse at `docs/specs/ireland_focus_tree/matrices/ireland_focus_tree_asset_ledger.md:29`. At this audit's snapshot date, delivery contained 140 decision-action DDS files and all 140 had distinct SHA-256 digests; that was an undisposed source-of-truth deviation at the time. Supersession (2026-07-22): the current package allocates 70 action DDS rows, maps all 140 named action aliases to those rows, prevents within-category duplicates, and retains the 70 superseded rows outside the runtime package under `docs/plans/ireland_focus_tree/assets/retired_icon_candidates/decision_actions/`. See `docs/plans/ireland_focus_tree/assets/icon_package_audit_2026-07-22.md` for the current static evidence.

The selected research handoff is also not integrated. `docs/plans/ireland_focus_tree/text_research/ireland_focus_tree_text_research.md:27-55` selects a constitutional Article 1 fragment, *The Celtic Twilight* allusion, and a Dúchas Fairymount evidence line, and `:300` recommends their use. None of those selected strings or identifying phrases was found in current Ireland localisation/events. This is a presentation/source handoff omission. Optional audio remains explicitly non-blocking because the handoff at `:296` makes no selection and says no route or achievement depends on audio.

### 9. Action-cost tuning is dynamic in places but remains heavily duplicated

The decisions do apply scarcity-sensitive political/command surcharges, so they are not a purely fixed political-power store. However, `common/decisions/ireland_decisions.txt` repeats 140 numeric `cost` fields plus per-action burden, scope, political-cost, command-cost, threshold, cooldown and timeout values. The file-level four `@` scarcity constants do not centralise the broader tuning table, and repeated action logic is not routed through one documented dynamic helper.

Impact: this falls short of `AGENTS.md`'s centralised dynamic tuning and reusable-helper standard and makes canonical balance review difficult. Treat it as a maintainability and balance-confidence gap after the queue semantics are repaired, not as proof that all costs are static.

## Accepted plans and current disposition

The mandatory improvement-loop report exists at `docs/plans/ireland_focus_tree/improvement_loop/ireland_focus_tree_improvement_loop_execution_report.md`. It recommends stopping broad design expansion and proceeding through bounded implementation (`:7-15`, `:174-176`). Its implementation observations at `:41-49` describe an earlier empty-runtime baseline and are stale as inventory facts, but the accepted integration contracts remain relevant.

| Accepted addendum | Current disposition | Evidence |
|---|---|---|
| IL-A01 canonical runtime contract | Partial | Shared runtime/constants/helpers exist, but category queues, event chain state, tuning centralisation, and engine validation remain open. |
| IL-A02 shared opening | Structurally implemented; acceptance unproven | Opening values and shared focus/runtime surfaces exist. No fresh-1936 vertical scenario proves a meaningful policy loop before route completion (`execution_report.md:66-72`). |
| IL-A03 route/lifecycle/conclusion | Partial | Route characters, parties, spirits and identities are present. Conclusion partial/failure, GUI request handoffs, event-chain causality and cleanup scenarios remain unproven. |
| IL-A04 Northern/neutrality separation | Structurally improved; acceptance unproven | Dillon and post-integration core checks now exist. Northern, occupation, neutrality, war-entry and demobilisation scenarios are absent. |
| IL-A05 AI/asset/researched-text parity | **Blocked** | Strategy registry exists, but decision/mission AI parity, real portraits, sourced event art, achievement delivery, cosmetic localisation and selected researched text remain open. |
| IL-A06 completion evidence | **Unmet** | The required route, country, decision/mission, AI, localisation, asset, achievement, event, GUI and feature-completion evidence set has not been completed. |

`docs/plans/ireland_focus_tree/improvement_loop/ireland_focus_tree_finding_disposition.md:26-34` still queues ILR-01 through ILR-09. Several inventory descriptions there are stale because implementation has advanced, but the queue has not been reconciled to current source. The main agent should update each row to implemented, partial, blocked, rejected with reason, or still queued with reason. The addenda preserve the canonical design rather than changing it, so this audit finds no accepted design change that must first be promoted into `docs/specs/`; the open work is implementation and evidence closure.

Tracking is internally inconsistent:

- `docs/plans/ireland_focus_tree/project_status.md:21,98,116,135` and `part_7_validation_report.md:36,104,125` still say the offline references and mandatory worker report are unavailable;
- `ireland_focus_tree_finding_disposition.md:49` records FG-007 integrated and the worker returned with `fork_context=false`;
- earlier country/focus/decision/GUI/localisation audits contain findings that later source edits partially repaired, but no single current implementation handoff supersedes their stale assertions.

This documentation drift makes completion claims unsafe even where code has advanced.

## Meaningful validation performed and unresolved limits

### Performed

- Current static inventory confirmed 216 focuses, 13 categories, 140 actions, 54 missions, 485 event definitions/calls including 236 flavour events, 40 AI strategy blocks including 10 overlays, 22 focus plans, 32 achievements, three GUIs, seven animation registrations, and the fixed generated icon/flag families listed above.
- Current `.gfx` path audit found 793 Ireland `texturefile` paths and zero missing target files. This does not cover character portrait tokens or the engine's special custom-achievement path convention.
- Current focus inspection resolved 216 nodes/titles with zero Ireland-tree diagnostics and zero connector crossings. Artifacts:
  - inspect JSON: `hoi4-agent://workspace/mod_ireland_total_overhaul_65a6b5f140a7/artifact/da27942a67a47a10c6fe38122f14169877c0f3ab97e8a23ffadd8dd14ed0237c/70ffc339d5b6524c5cb85093714319035e29c8cf63279a74b0107f25b8fc3d19/focus-inspect.f974169d29650ecf.json`
  - structural HTML: `hoi4-agent://workspace/mod_ireland_total_overhaul_65a6b5f140a7/artifact/768329bf8387374219ef17763b7abc30afb996ac46e93b2fff2dc9e61f92eb25/75e3930e50b9821ae29f3f58905d5d8be1c71dd1a65e3b69f741b9c5d5b45b54/ireland_focus_tree.focus.html`
  - structural SVG: `hoi4-agent://workspace/mod_ireland_total_overhaul_65a6b5f140a7/artifact/b099643b4cee04ad2bf4313b93d88696989a5411828c21647e7775f92e15a25d/64b7430971496af2da4f0bddddaeb2c964ff4c7b3dad8057abb5a90938542885/ireland_focus_tree.focus.svg`
  - structural JSON: `hoi4-agent://workspace/mod_ireland_total_overhaul_65a6b5f140a7/artifact/b89095243a440850eb802dd751661d7fa9b7ba70f0449919055612a07188c1f1/ed7b96480ec41868ef6f54466b0ea09b999108120b2551238ed23e436aa11213/ireland_focus_tree.focus.json`
  - source map: `hoi4-agent://workspace/mod_ireland_total_overhaul_65a6b5f140a7/artifact/1db85fe1af172b07626e097eb32a68e65bf5422f3c37f5aff579aff2fd0f6cc6/432fbe3810e84e08743126d0eca0e757fa811dcd5cf5390a02d2524646294c5f/ireland_focus_tree.focus.source-map.json`
- The focus render's aggregate validation flag was false because the workspace scan also reported 14 unrelated vanilla continuous-focus sprite references. Those global diagnostics are not attributed to the Ireland tree; the Ireland-specific tree returned zero diagnostics.
- Source release confidence is bounded by the explicit manifest/clearance audit rather than inferred from file presence.

### Missing or inconclusive

- No current parser/error-log or in-engine load result was provided for the Ireland package.
- No historical/nonhistorical playthrough or any of the 22 required validation scenario classes at `ireland_focus_tree_coding_prompt.md:318-341` was demonstrated.
- No AI simulation covers all durable profiles, overlays, reserved slots, hidden permission, sponsor collapse, Northern choices, war, recovery or conclusions.
- No live scripted-GUI render with current game values, click-region exercise, hidden reveal, or resolution matrix was demonstrated.
- No all-32 achievement run validates eligibility, progress, hidden presentation, icon loading, durable disqualifiers or completion.
- No scenario audit proves event trigger ordering, option scopes, follow-up causality, picture selection, foreign-reaction digest limits, or conclusion cleanup.
- A current event inspection attempt could not be bounded to the Ireland namespaces and scanned the wider workspace. It returned partial/global unresolved diagnostics and is **not** an Ireland validation pass: `hoi4-agent://workspace/mod_ireland_total_overhaul_65a6b5f140a7/artifact/02702fc321d11a9497c0b14266de212df806b89052ca4de586efbed1d7872929/e9c26ffad7a774fe3f93325028608f60db992197cf410004c8dee8680e7b7a56/event-scan-f974169d2965.json`.
- No release-clearance closure exists for the blocked portrait/source/event-art records.

## Remaining blockers

Release/completion blockers, in priority order:

1. Implement and validate real per-category mission caps plus reserved/pre-emptive critical-slot behavior.
2. Replace write-only event follow-up state with outcome-linked family chains and validate historical, crisis, foreign, conclusion and cleanup sequences.
3. Give decision/mission AI profile- and overlay-aware priorities, reconcile 22 focus plans to the 30-profile matrix, and run the required AI scenarios.
4. Install custom achievement icons under `gfx/achievements/` with exact achievement-ID filenames, implement the hidden/reveal contract, and test all 32 entries/disqualifiers.
5. Resolve 11 undefined runtime portrait sprites and the wider 59-portrait clearance gate; clear and wire the 69 sourced event/news allocation and the remaining source packages without generated likenesses or undocumented substitutes.
6. Add localisation for all 18 cosmetic identities and disposition the historical base flag as controlled reuse or a sourced feature asset.
7. Complete or explicitly reduce the GUI interaction contract: consume row selection/review/inspection state or document and obtain approval for the simplification.
8. Reconcile the 14 collective portraits, 70-versus-140 decision icon budget, selected researched text, and stale plan/handoff/status records.
9. Run the task-specific parser, focus, decision/mission, event, country, AI, GUI, achievement, asset and 22-scenario validation matrix; record failures and repairs rather than converting static count checks into completion proof.

## Recommended next actions for the main agent

1. Treat mission-queue semantics and event-chain causality as the first gameplay repair tranche; both are hidden by otherwise correct fixed counts.
2. In the next AI tranche, preserve the existing 40-block registry but add canonical profile/overlay-aware action and mission scoring and explicitly disposition each collapsed focus plan.
3. Route achievement and portrait work through the asset owner before any completion claim. Achievement path/name repair and the 11 undefined portrait sprites are direct runtime-facing blockers; source clearance remains a content-release blocker.
4. Wire cosmetic localisation and GUI request/selection behavior, then run country-package, localisation and GUI audits against the repaired source.
5. Execute the canonical validation scenarios and update `ireland_focus_tree_finding_disposition.md`, `project_status.md`, `part_7_validation_report.md`, asset handoffs, and any superseded audit notes with exact current dispositions.

### Improvement-loop planner recommendation

Do **not** spawn `hoi4_improvement_loop_planner` again for this feature now. The existing execution report already supplies IL-A01–IL-A06, explicitly stops broad expansion, and ILR-01–ILR-09 remain unresolved in the disposition ledger. The feature's principal gaps are implementation, source clearance, wiring and validation—not lack of canonical depth. Reconsider a new planner pass only after the current addenda are implemented, promoted, queued with a current reason, or rejected, and only if a surviving audit then shows a depth gap not covered by the existing canonical package.

## Final audit judgment

The Ireland overhaul has substantial structural implementation and meets many fixed numeric inventories, but it must **not** be treated as complete. Mission-cap semantics, event-chain causality, AI action parity, achievement delivery/hidden behavior, portraits and sourced event art, cosmetic localisation, GUI handoffs, and task-specific runtime validation remain unresolved. The main agent owns whether to repair, queue, reject, or formally amend each finding; this audit makes no gameplay edits and no completion claim.
