# Ireland Country Package Final Completion Audit — 2026-08-14

> Historical audit boundary: this report records the pre-exceptional-route
> `8fe5c62` state and is superseded by the later 256-focus completion audit.
> Its incomplete verdict remains useful as implementation history, not as the
> current package status.

## Audit identity

- Audit mode: read-only feature-completion audit.
- Audited revision: `8fe5c6248a3328968bc98d97557312dda63931ae`.
- Scope: the comprehensive Ireland overhaul brief, the canonical country-package and focus-tree specifications, the accepted 2026-08-14 improvement addendum, gameplay and AI script, assets, localisation, Parliament GUI, events and cadence, characters and advisors, companies and MIOs, territorial expansion, all five political families, P0/P1/P2 work, and completion documentation.
- Gameplay files changed by this audit: none.
- Thumbnail changed by this audit: no; the pre-existing `thumbnail.png` worktree modification was preserved.

## Verdict

**INCOMPLETE.**

The current package is substantially implemented and its principal P0/P1/P2 corrections are present, but the repository does not yet meet its own completion standard. Five blockers remain:

1. Three portrait slots in the canonical source manifest remain blocked: P-26 Patrick Cogan, P-45 Mick Fitzpatrick, and P-55 Liam D. Walsh.
2. The High King, Five Provinces, and Otherworld routes remain much shallower as selectable focus architectures than the compatible detailed Part 3 route contracts require.
3. The monthly event dispatcher records a cursor without using it to resume dispatch, so later eligible events can starve; flavour event `ireland_flavour_events.500` can also fire after de Valera has been displaced.
4. Active source-of-truth and completion documents disagree about the current 218-focus/222-connector revision, asset blockers, and final completion state.
5. The named current historical, five-family, failure/recovery, hidden-route, AI blocked-recovery, and cumulative balance acceptance scenarios required by the country-package implementation matrix have neither current evidence nor an explicit current-spec waiver.

These are not cosmetic observations. They are direct failures of the asset, depth, event-cadence, documentation, and completion-proof requirements. A `COMPLETE` recommendation would therefore be inaccurate.

## Completion status by surface

| Surface | Status | Evidence and disposition |
|---|---|---|
| Focus-tree structure and layout | Complete statically | Fresh inspection found 218 focuses and 222 connectors, exactly three roots, gateways at row `y = 14` and `x = -24, -18, -12, -6, 0`, zero crossings, zero node intersections, zero long connectors, zero duplicate positions, and zero cramped same-row pairs. Four concealed-branch advisories are non-blocking. |
| Strict focus filters | Complete statically | The final filter corrections remove inappropriate industrial and annexation-pipeline filters while preserving family and diplomatic categorisation. The final focus audit and direct source review agree. |
| Direct and capability rewards | Complete for the accepted P2 tranche | The named Atlantic filler rewards were replaced with durable operation or capability handoffs; four settlement/policy cards and `Atlantic Ambition` were accepted as capability handoffs rather than inert rewards. |
| Five main political families | Complete structurally; scenario proof pending | The democratic, republican, communist, fascist, and clerical families have distinct gateways, event conclusions, AI route mappings, and report images. Current named route scenarios have not been recorded. |
| Exceptional/hidden political routes | **Incomplete — simplified** | High King has five selectable focus nodes, Five Provinces four, and Otherworld six. This does not deliver the compatible Part 3 selectable-route depth for captured/sacral crown outcomes, Irish Confederation, Crown and Five Provinces, Four Provinces and Empty Chair, Fifth Province, Rival Irelands, Tuatha sovereignty, Fianna guardianship, regional courts, exploitation, and cross-route conclusions. Some concepts exist only as flags, events, or ideas. |
| Territorial campaign | Complete statically | The northern, Welsh, Cornish, and Atlantic surfaces are connected; Welsh and Cornish response/refusal chains and P1 recovery logic are present. Audited territorial transfers, claims, and war goals target states 119, 120, 122, and 123. No early northern core-grant effect was found. |
| Timed decisions and missions | Complete statically | Fourteen audited P0/P1 timed cards have `days_remove`, `complete_effect`, `remove_effect`, `cancel_trigger`, `cancel_effect`, and launch-state flags. Durable outcomes occur through expiry removal; immediate completion only marks in-progress state. |
| Decision cooldown parser safety | Complete statically | Territorial plebiscite and diplomacy cooldown writes use parser-safe file-local macro literals. Forty-three audited simple timed-flag writes contain no unsafe variable/constant token in a duration field. |
| Parliament scripted GUI | Complete statically; runtime-state proof limited | Fresh inspection found no layout overlap or source blocker. The Dáil, Seanad, confidence, and budget controls route through shared guarded executors; the charged actions debit the defined 25/25/35 PP costs and Dáil is free. Four source-state frames and distinct button strips exist. The offline renderer does not execute `buttonstate.lua`, so live button-state transitions remain outside this evidence. |
| Events, images, and effects | Partially complete | 524 picture references resolve to 133 unique registered images; the five family conclusions use distinct present 210×176 report images. Direct focus/decision reports and the 120-day foreign broker exist. The dispatcher/cadence defects described below remain. |
| Event cadence / no daily spam | Partially complete | No unscoped world daily/weekly/monthly iteration was found. `on_daily_IRE` performs synchronisation, and its separate conclusion launch is a tightly gated one-shot. The public programme is monthly. However, the monthly ordered programme does not actually resume from its cursor and therefore cannot demonstrate intended coverage. |
| Companies, MIOs, and contracts | Complete statically | Seven industrial concerns, two MIOs, and nine one-use 35-day industrial contracts are present. Contracts require productive civilian capacity, reserve factories, and give distinct outputs. |
| Characters, leaders, and advisors | Complete structurally, **asset-incomplete** | Source contains 45 advisor blocks and 24 country-leader blocks, with localisation coverage. Three required canonical real-person portrait source slots remain blocked and have no source/processed/final/runtime consumer. |
| Achievements | Complete structurally | Thirty-two achievement definitions and their localisation/art assets are present. Static-hidden handling for A-22/A-27/A-28 follows the recorded engine-field ruling, but the current scenario matrix is unexecuted. |
| Localisation | Complete for current gameplay identifiers | The final localisation audit recorded 5,911 unique keys and coverage for focuses, decisions, events, GUI, advisors, companies, and MIOs. Seven unused defined-text helpers and four legacy Parliament tooltip copies are cleanup debt, not completion blockers. |
| Visual assets | **Incomplete** | Current gameplay sprites inspected in this audit resolve, including P0 decision icons and the five family report images. The canonical real-person portrait source package still has three blocked rows. Father Edward Cahill is a separately recorded route-extension source blocker outside the canonical 169-row/60-portrait budget. |
| AI and balance | Implemented statically; acceptance proof pending | P0 added recovery priority, historical-route non-coercion, and family-specific Atlantic mappings. The current named AI blocked-recovery and cumulative balance scenarios have not been recorded. |
| Documentation and completion tracking | **Incomplete** | Several active documents retain 218/226 or contradictory asset-blocker counts, while an older audit claims completion. The current authoritative 218/222 state is therefore not consistently represented. |

## Missing or simplified requirements

### 1. Canonical portrait-source clearance

`docs/plans/ireland_focus_tree/assets/source_manifest.json` contains 166 complete rows and three blocked canonical rows:

- P-26 — Patrick Cogan
- P-45 — Mick Fitzpatrick
- P-55 — Liam D. Walsh

Each blocked row lacks a verified source, processed portrait, final DDS, and runtime consumer. The detailed focus-tree asset contract requires 60 real portrait slots, and AGENTS.md forbids a completion claim with missing assets. These three rows are therefore hard blockers even though they do not currently cause a missing-sprite loader failure.

Father Edward Cahill is separately recorded in `docs/plans/ireland_focus_tree/source_of_truth_map.md` as a route-extension source gap. It is outside the canonical manifest budget, so it must not be silently added to the count of three, but it should be either completed or explicitly rejected/queued when the exceptional-route tranche is resolved.

### 2. Exceptional-route selectable depth

The current focus source gives High King five selectable nodes, Five Provinces four, and Otherworld six. The compatible detailed Part 3 route specification calls for materially more playable differentiation and connective conclusions, including the captured/sacral crown split, Irish Confederation, Crown and Five Provinces, Four Provinces and Empty Chair, Fifth Province, Rival Irelands, Tuatha sovereignty, Fianna guardianship, regional courts, exploitation, and cross-route conclusions.

The package contains some associated flags, events, and ideas, but those are not equivalent to the requested selectable focus architecture. This is an undisclosed simplification in the current completion claim. The accepted 2026-08-14 post-tranche addendum does not resolve this depth gap.

### 3. Event dispatcher cursor and route leakage

The public programme in `common/scripted_effects/ireland_runtime.txt` schedules 221 ordinary Ireland events plus 236 flavour events. It sets a programme cursor repeatedly, but only compares that cursor for broad range normalisation; individual entries do not use the cursor to skip already-scanned entries and resume later in the sequence. Every eligible monthly dispatch therefore begins from the start of the list.

Because a successful dispatch also applies a one-month programme cooldown, the 1937–1956 campaign window offers only about 114 ordinary dispatch opportunities from 228 monthly pulses. Later eligible entries can consequently starve even though the script records a cursor. This prevents the intended ordered, paced report programme from being proven complete.

Separately, `events/ireland_flavour_events.txt` permits `ireland_flavour_events.500` under historical, plausible, or absurd route states, while its localisation specifically describes de Valera's authority. It can therefore become stale after his displacement. The event needs a valid-leadership/route gate, alternative contextual localisation, or a documented rejection.

This audit did confirm that there is no general daily event spam: the recurring public programme is monthly, the foreign broker uses a 120-day cooldown, and the daily country-scoped hooks are synchronisation or tightly gated one-shot logic. The blocker is ordered coverage and contextual gating, not the existence of a world daily loop.

### 4. Documentation authority disagreement

The following active or completion-facing documents are stale or internally contradictory:

- `docs/specs/ireland_country_package/ai_balance_assets_and_text.md` still records revision `89ff719` and 218/226.
- `docs/ireland_systems.md` records 218/226 and, in one section, 15 blocked portraits, eight blocked symbol/document rows, and 15 blocked event/news rows, while another section records three blocked portraits.
- `docs/plans/ireland_focus_tree/project_status.md` records revision `89ff719` and 218/226.
- `docs/plans/ireland_focus_tree/source_of_truth_map.md` mixes 218/226, older 216/197 status rows, and contradictory statements describing three, four, or five remaining portrait/source blockers.
- `docs/plans/ireland_country_package/current_implementation_map_2026-08-14.md` retains the pre-correction 218/226 state.
- `docs/plans/ireland_country_package/final_country_package_audit_2026-08-14.md` claims completion at the stale 218/226 revision and does not carry the canonical portrait blockers.
- `docs/plans/ireland_country_package/documentation_cleanup_handoff_2026-08-14.md` states that active country-package documents consistently agree on 218/222, which the files above disprove.
- The accepted improvement addendum still uses gateway-row acceptance wording at y3/y4 and says there should be no linear detour, while the final accepted layout uses y14 and contains four non-blocking concealed-branch advisories. Its decision-icon handoff paths also differ from the final wired paths.

The current `docs/specs/ireland_country_package/index.md` and `implementation_matrix.md` correctly record 218 focuses and 222 connectors. Until the other active source-of-truth and completion surfaces are reconciled or explicitly marked historical/superseded, documentation completion is blocked.

### 5. Current acceptance-scenario evidence

The current `docs/specs/ireland_country_package/implementation_matrix.md` requires named historical, five-family/territorial, failure/recovery, hidden-route, AI blocked-recovery, and cumulative balance scenarios before final completion. The 2026-08-14 P0/P1/P2 handoffs repeatedly leave these checks to the parent, and no current evidence file records them.

An older source-only scenario trace covers the earlier focus-tree prompt families and records that a live HOI4 playthrough was excluded. That does not automatically discharge the newer country-package acceptance gate. This is currently an authority conflict, not proof that the gameplay necessarily fails. Completion requires one of the following explicit dispositions:

- run and record the current permitted source/static scenario matrix and probability/balance checks; or
- amend the current spec with an explicit accepted waiver defining which live/runtime scenarios remain outside scope and which static evidence substitutes for them.

## Accepted plans and disposition

| Accepted plan | Disposition |
|---|---|
| P0 territorial flow and route access | Implemented and promoted into the current country-package specs. Wales/Cornwall response and refusal handling, recovery priority, historical non-coercion, and route locks are present. Scenario proof remains open. |
| P0 Atlantic operation and family mapping | Implemented. Filler Atlantic rewards were replaced with operation/capability handoffs, and AI family mappings are present. Scenario proof remains open. |
| P1 five-family political identity and reports | Implemented. The five family gateways, conclusion reports, distinct report images, and route handoffs exist. Current five-family acceptance scenarios remain open. |
| P1 timed settlement/recovery safety | Implemented. Five 180-day settlements, five 120-day recoveries, alternate order, Congress rebuild, Provincial Assent/reconvening, and fascist withdrawal use timed expiry/cancel cleanup patterns. |
| P1 Parliament usability | Implemented statically. All four controls are wired through shared executors, with source-state sprites and guarded costs. Live Lua-driven state transitions are not demonstrated by the offline renderer. |
| P2 named payoff replacement | Implemented. Named filler rewards are replaced with direct effects or durable capability launches. |
| Final family-lane reflow and gateway row | Implemented. The final 218/222 layout, y14 gateway row, and strict-filter corrections inspect cleanly. |
| Accepted 2026-08-14 improvement addendum documentation reconciliation | Partial. Gameplay tranches were implemented, but the addendum's acceptance wording and several source-of-truth documents were not reconciled with the final layout and asset state. |
| Older detailed exceptional-route contracts | Partial/simplified. Route identity exists, but selectable focus depth remains materially below the compatible Part 3 contract. |

No accepted plan reviewed by this audit provides a documented rejection or queue reason for the exceptional-route depth, dispatcher coverage, three canonical portrait blockers, or current scenario-evidence gate.

## Meaningful validation performed

### Fresh focus inspection and render

Fresh tools inspected the current `ireland_focus_tree` source, not a prior report:

- Revision: `97013150a7474f29e4dc8fea9ebe4e163875d57faff0b3fc69b630da1fda5756`
- Result: 218 focuses, 222 connectors, bounds x -26..21/y 0..22, zero crossings/intersections/long connectors/duplicate positions/cramped same-row pairs.
- Inspect artifact: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/cef93413019260f758c5bd8c1d6cd3ba02f4105da571f2ecf98b759c39ce3e00/ff8b072165eb89950c5dcac511e230c7e1ee962b90a7b2a985ec6e815fd8eb5a/focus-inspect.97013150a7474f29.json`
- HTML render: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/965860e12e6bb0f02e554804774de46a348d16c527751f8017e2f10a59a5cab1/2e8a8de387486a83eb20d75316e51f2278833a1f30a13a38dbc5e92d6bc7fd51/ireland_focus_tree.focus.html`
- SVG render: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/596a9cb9b9c7448cfa8b8b5c6eb503ef3873ad102ae80d95f75e18bc3ec04885/e4d7e7634aea669abb04c5289ea3eefa9d4e734be8df57f621c8456eee707aa1/ireland_focus_tree.focus.svg`
- JSON render: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/cc67a5157851f77ca0a62b01b519b2ca7bb971f96baeb7a033619ffe6e4139de/d635581276b399a6b3c7a9d5409aa34462a8d261abca8efa1c875462a2f993aa/ireland_focus_tree.focus.json`

### Fresh Parliament inspection and render

The `ireland_parliament_decision_ui_window` source graph was inspected at the initialised Ireland scenario:

- Inspect artifact: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/0fb8a281d0ffeebb3124d6b8d90e55660c852a1aa62bff8b66677550e0a71f56/cf14512088aaa618b9a6d03fcdd7b5d66e0bc30b23c5026eb13c035aaaa27aa3/gui-inspect.4286b3ee6189f14d.json`
- Multi-resolution/state SVG render: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/58a718a59ee91a0950ffb49ef8cbde90d6044bea7738b999fc524274f6a446f4/49d4bbee99b2f964dd146912ec5937808365f9e13b93bb8d538e81447bbd5321/ireland_parliament_decision_ui_window-full.svg`

The inspector reported three direct cost mismatches because it does not follow wrapper calls into the shared executors. Direct source review resolved those apparent errors: the Seanad, confidence, and budget executors debit the same 25/25/35 PP values that the GUI displays. The renderer also does not execute `buttonstate.lua`; therefore the render proves geometry and source sprites, not live locked/active/completed transitions.

### Targeted source checks that affect confidence

- Verified the fourteen P0/P1 timed decision lifecycles and that durable results are written on expiry removal rather than immediate completion.
- Verified the parser-safe literal cooldown macros and the absence of unsafe nonliteral values in the simple timed-flag duration writes reviewed.
- Resolved all 524 event picture references to registered GFX names and checked the five family report DDS files as distinct 210×176 images.
- Verified that only country-scoped daily/monthly hooks participate in the audited Ireland systems and that the recurring public programme is monthly.
- Counted seven industrial concerns, two MIOs, nine one-use industrial contracts, 45 advisor blocks, 24 country-leader blocks, and 32 achievement definitions.
- Traced territorial state effects to the intended northern/Welsh/Cornish states and found no premature audited core grants.
- Compared active documentation claims against the current source manifest and final 218/222 focus result.

## Validation not present

- No current evidence records the named historical, five-family, failure/recovery, hidden-route, AI blocked-recovery, and cumulative balance acceptance scenarios.
- Offline GUI inspection cannot demonstrate Lua-driven runtime button-state transitions.
- No evidence proves that the event programme's full eligible catalogue is reachable within campaign cadence; direct source inspection instead found a cursor design that can starve later entries.
- The three blocked portrait identities have no source-clearance evidence.

## Required next actions

1. Source or explicitly remove/replace, with spec approval, P-26 Patrick Cogan, P-45 Mick Fitzpatrick, and P-55 Liam D. Walsh. Update the source manifest, final DDS/runtime wiring where retained, and asset handoff.
2. Correct the public programme so its cursor actually resumes ordered dispatch, then add a bounded reachability/cadence audit. Tighten or contextualise `ireland_flavour_events.500` so de Valera-specific copy cannot appear after his displacement.
3. Decide and implement the missing selectable depth for High King, Five Provinces, and Otherworld, or explicitly narrow the compatible detailed Part 3 contract in the canonical spec. Do not leave the current shallower form presented as full implementation.
4. Run and record the current source/static acceptance matrix and AI/balance scenarios, or promote an explicit waiver/substitute-evidence rule into the current country-package spec.
5. Reconcile the active specs, source-of-truth map, project status, system documentation, addendum acceptance wording, implementation map, and stale completion audits to the final 218/222 state and the true three-row canonical asset blocker count.
6. Repeat the final feature-completion audit only after those dispositions are in the repository.

## Improvement-loop recommendation

Use `hoi4_improvement_loop_planner` for one bounded exceptional-route expansion addendum after the current scope authority is reconciled. The feature technically exposes High King, Five Provinces, and Otherworld routes, but their selectable focus depth does not meet the intended detailed Part 3 architecture, and the accepted 2026-08-14 country-package addendum does not cover this gap. The planner should be restricted to those three routes, their cross-route conclusions, associated event/advisor/portrait dependencies, AI selection, and balance/acceptance scenarios; it should not reopen the completed five-family, territorial, Parliament, or P0/P1/P2 work.

## Simplifications, omissions, and blockers

- Simplification: exceptional-route concepts are represented more through events/flags/ideas than the requested selectable focus architecture.
- Omission: three canonical real-person portrait source packages.
- Defect: the event cursor is written but does not control per-entry resume order; later eligible events can starve.
- Defect: one de Valera-specific flavour event is not route/leadership-safe.
- Documentation gap: multiple active completion-facing files contradict the final layout and asset state.
- Validation gap: current named acceptance and balance scenarios have no recorded disposition.

No other unreported fallback or simplification was identified in the audited P0/P1/P2 surfaces. This report does not authorise a completion claim until the blockers above are resolved or explicitly rejected through the canonical design authority.
