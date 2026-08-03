# Ireland country package audit — 2026-07-18

Status: **blocked for package completion; parent implementation handoff**.

Historical snapshot note (reconciled 2026-07-22): the package-wiring gaps in this audit are not the current status for route activation, spirits, cosmetic identity, or focus-icon registration. Current structural evidence is in `common/scripted_effects/slopx_ireland_runtime.txt`, `common/countries/slopx_ireland_cosmetic.txt`, and `interface/slopx_ireland_icons.gfx`. Source clearance and live route/scenario validation remain partial or blocked; use `docs/plans/ireland_focus_tree/source_of_truth_map.md` and `docs/plans/ireland_focus_tree/audits/ireland_completion_followup_2026-07-18.md`.

This is an audit-only handoff. No gameplay, asset, localisation, or existing documentation file was patched by this audit. The worktree contained substantial unrelated Ireland implementation and asset changes before the audit; those changes were preserved.

## Scope and sources

The audit covered the `IRE` country package and the `NIR`/state `119` boundary, including history, opening values, map ownership and cores, route characters, country leaders, ideas, focus loading, decisions/events, AI, assets, localisation, and inherited military setup.

Canonical design and reconciliation sources read:

- `docs/specs/ireland_focus_tree/ireland_focus_tree_index.md`
- `docs/specs/ireland_focus_tree/ireland_focus_tree_spec_part_1_research_and_architecture.md`
- `docs/specs/ireland_focus_tree/ireland_focus_tree_spec_part_2_constitutional_politics.md`
- `docs/specs/ireland_focus_tree/ireland_focus_tree_spec_part_3_radical_and_hidden_routes.md`
- `docs/specs/ireland_focus_tree/ireland_focus_tree_spec_part_4_statecraft_and_war.md`
- `docs/specs/ireland_focus_tree/ireland_focus_tree_spec_part_5_decisions_events_and_lifecycles.md`
- `docs/specs/ireland_focus_tree/ireland_focus_tree_spec_part_6_ai_assets_achievements_and_text.md`
- `docs/specs/ireland_focus_tree/maps/ireland_focus_tree_canonical_reconciliation_map.md`
- `docs/specs/ireland_focus_tree/maps/ireland_focus_tree_cross_surface_reconciliation_map.md`
- `docs/specs/ireland_focus_tree/matrices/ireland_focus_tree_route_coverage_matrix.md`
- `docs/specs/ireland_focus_tree/matrices/ireland_focus_tree_ai_strategy_matrix.md`
- `docs/specs/ireland_focus_tree/matrices/ireland_focus_tree_asset_ledger.md`
- `docs/specs/ireland_focus_tree/matrices/ireland_focus_tree_lifecycle_matrix.md`

Required offline Paradox Wiki pages were consulted for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, AI modding, country creation, national focuses, state/map modding, graphical assets, portraits, and cosmetic tags. Vanilla documentation was also consulted, including `documentation/effects_documentation.md`, `documentation/triggers_documentation.md`, and `documentation/script_concept_documentation.md`, with vanilla Ireland files used as the baseline.

## Executive result

The opening package is mostly coherent and the Northern Ireland opening boundary is safe:

- `IRE` starts in capital state `113`, with vanilla Ireland home-state cores only.
- State `119` is `ENG`-owned and has only `ENG` and `NIR` historical cores in the mod override.
- Ireland does not start with state `119`, an Ireland core on state `119`, or an actual map claim before the dedicated claim focus.
- `slopx_ireland_northern_settlement_ledger` grants only an Ireland claim to state `119`.
- Focus loading is natively assigned to `IRE`, and all 216 focus icon references are registered with existing DDS files.
- The three starting spirit slots and the documented opening values are initialized through one idempotent country-scoped effect.

The package is not completion-ready. The material blockers are runtime wiring, not the opening map:

1. Fifteen route country-leader characters are declared but never recruited, activated, transitioned to, or retired.
2. The three starting idea families have 60 route/failure variants, but no route lifecycle swaps or removes any variant; all 63 idea picture names are also absent from live GFX registration.
3. The Northern core-review trigger exists, but no caller grants an Ireland core. The final-review focus only sets flags. Two prerequisite flags (`slopx_ireland_dillon_mandate_complete` and `slopx_ireland_northern_regional_review_ready`) have no setters.
4. Route flags and AI profiles do not produce corresponding party, ideology, popularity, country-leader, cosmetic-tag, or country-name changes. The mod has no Ireland-specific `common/countries`, `common/parties`, `common/cosmetic_tags`, or route identity surface.
5. The AI registry has the canonical 30 durable profiles and 10 overlays, but only two generic AI national-focus plans, both with empty `focus_factors`; route-specific focus selection is therefore not proven.
6. Only the 216 focus and 153 decision sprites are live. Eleven personal route portraits, four institutional route portraits, 63 spirit sprites, and the other planned asset classes have no live registration/final package.

These gaps require coordinated focus, event, character, idea, AI, identity, and asset work. They are not safe one-line country-history fixes, so they are handed to the parent rather than patched here.

## Country-package coverage checklist

| Surface | Status | Evidence and scope |
|---|---|---|
| Tag registration | Partial/pass for base game | `IRE` and `NIR` are vanilla-registered in `common/country_tags/00_countries.txt`; no mod-side tag override is needed for the base country. |
| Country definition | Partial | Vanilla `common/countries/Ireland.txt` and `Northern Ireland.txt` supply graphics/culture/colors. Route identities have no mod-side country/cosmetic definition. |
| History/opening | Pass with vanilla dependencies | `history/countries/IRE - Ireland.txt` sets the opening history and calls `slopx_ireland_initialize_campaign`. |
| State 119 | Pass at game start | `history/states/119-Northern Ireland.txt` leaves `owner = ENG` and cores `ENG`/`NIR`; no `IRE` core or opening transfer. |
| Claim/core progression | Blocked | The claim focus is claim-only, but the documented final core grant is absent; see `slopx_ireland_can_northern_core_review`. |
| Route characters/leaders | Blocked | 15 custom route characters exist in `common/characters/slopx_ireland_route_characters.txt`, but no lifecycle caller exists. |
| Ideas/spirits | Partial/blocked | Three opening ideas are initialized correctly; 60 variants are declared but never transitioned, and all 63 pictures lack live GFX entries. |
| Politics/parties/identity | Blocked | Only initial/1939 history politics are set. Route runtime has no party, country-leader, ideology, cosmetic-tag, country-name, or popularity transition. |
| Focus loading | Pass | `slopx_ireland_focus_tree` uses `country = { factor = 0 modifier = { add = 100 tag = IRE } }`; the tree is not default-loaded for other tags. |
| Focus route completion | Blocked | Many route gates are flags, but required setters and leader/idea/identity effects are not wired; Northern final review does not grant a core. |
| Decisions/events | Partial | The state-119 ledgers and review events exist, but the core-review action/event chain stops at flags, variables, and reactions. |
| AI | Partial/blocked | 30 profiles and 10 overlays exist; focus plans are only historical/reactive generic lists with empty `focus_factors`. |
| Localisation | Partial/pass for current visible content | Ireland focus/idea keys are present and the file has UTF-8 BOM. Route identity, party, cosmetic-tag, and route-leader localisation surfaces are not wired. |
| Assets | Blocked | 369 focus/decision sprites are live; route portraits, idea sprites, and other planned classes are absent or not registered. |
| Military/technology/industry/supply | Pass as inherited baseline | Ireland uses vanilla `IRE_1936`/`IRE_1939` OOBs and the vanilla home states; no package-local free army/industry/territory was found. |

## Exact opening values

### Country history

`history/countries/IRE - Ireland.txt` currently opens with:

- `capital = 113`.
- `oob = "IRE_1936"`.
- `set_research_slots = 3`.
- Technologies: `infantry_weapons = 1`, `infantry_weapons1 = 1`, `tech_trucks = 1`, `fuel_silos = 1`, and `basic_train = 1`.
- `set_convoys = 10`.
- 21 vanilla Ireland characters recruited, beginning with `IRE_Éamon_de_valera`; this is the correct vanilla de Valera token, not a mojibake ID.
- `set_politics`: `ruling_party = democratic`, `last_election = "1933.1.24"`, `election_frequency = 48`, and `elections_allowed = yes`.
- `set_popularities`: `democratic = 98`, `fascism = 1`, `communism = 1`.
- `slopx_ireland_initialize_campaign = yes`.

The later `1939.1.1` block adds `1198` political power and `100` command power, completes the listed generic focuses, switches to `IRE_1939`, and applies the later vanilla technology/politics block. It is not part of the 1936 opening state but should remain consistent with the route lifecycle when that lifecycle is wired.

### Campaign variables and flags

`common/script_constants/slopx_ireland_constants.txt` and `common/scripted_effects/slopx_ireland_effects.txt:12-121` agree on the following opening values:

| System | Opening values |
|---|---|
| National Settlement | value `25`; momentum `-1`; stage `5`; pending stage/days `0`; BOP value `0.25`; range `-100..100`; route clamp `-60..60` |
| External/social | Social Consent `55`; Neutrality Integrity `72`; British leverage `45`; Vatican `25`; American `5`; German `5` |
| National Provision | food `55`; energy `25`; transport `40`; maritime `30`; derived display `38` |
| National Readiness | command `25`; equipment `8`; mobilisation `20`; supply `12`; warning `5`; maritime protection `5`; intelligence `30`; derived display `15` |
| Northern ledger | Unionist `5`; Nationalist `40`; Labour `30`; British `10`; Security `45`; Integration capacity `10`; integration stage `0` |
| Dáil | formal seats `153`; routine votes `152`; majority `77`; Fianna Fáil `77` formal / `76` routine; Fine Gael `59`; Labour `8`; other `9` |
| Mission/action | normal mission cap `8`; emergency/war cap `10`; emergency-occupation cap `12`; command-power action cap `60`; burden input `1`; cost input `0` |
| Foreign reaction | reaction window `0` days at opening; visible count `0`; reaction score `0` |
| Spirit slots | all three slot state variables `0`; exactly three opening ideas are added |
| Northern map ledgers | claim ledger `1`; control, occupation, settlement, and integration ledgers `0`; claim ledger active/open flags set; later ledger-active flags clear |
| Profile | `slopx_ireland_profile_historical_de_valera` and `slopx_ireland_initialized` set |

The initialization effect is guarded by `slopx_ireland_initialized`, and is invoked by country history, `on_startup` for `IRE`, and the opening focus path. That is a good idempotency pattern; parent work should preserve the guard rather than duplicate setup.

### State 119 and no-free-territory proof

`history/states/119-Northern Ireland.txt:6-26` currently has:

- `owner = ENG`.
- Victory points `3379 = 5` and `385 = 1`.
- Existing buildings/resources retained from the state definition.
- `add_core_of = ENG` and `add_core_of = NIR` only.
- No `controller = IRE`, `owner = IRE`, `add_core_of = IRE`, `set_state_owner`, `transfer_state`, annexation, release, puppet, or province transfer effect.

The state override intentionally differs from vanilla by removing vanilla's opening `IRE` core. The other Ireland home states remain vanilla-owned/cored by `IRE` in states `113`, `134`, and `135`. The current package therefore passes the opening claims/cores separation requirement.

`common/national_focus/slopx_ireland_focus_tree.txt:2834-2856` (`slopx_ireland_northern_settlement_ledger`) uses only `add_claim_by = ROOT` in state `119`; it does not transfer the state or add a core. This is the correct claim step.

The progression is incomplete, however. `common/scripted_triggers/slopx_ireland_triggers.txt:130-136` defines `slopx_ireland_can_northern_core_review` as the stage/final-review gate, but that trigger has no caller. `slopx_ireland_northern_regional_review` at `common/national_focus/slopx_ireland_focus_tree.txt:2992-3016` sets `slopx_ireland_northern_final_review_passed` and review flags only. `events/slopx_ireland_events.txt` final/core-review events and `common/decisions/slopx_ireland_decisions.txt:25363` likewise stop at variables, flags, missions, and foreign reactions. No mod source contains an Ireland `add_core` effect. The parent must design one idempotent final-review effect with explicit state-119 control/occupation/integration checks and cleanup; do not solve this by giving an opening core.

## Route characters, leaders, politics, and identity

### Declared characters

`common/characters/slopx_ireland_route_characters.txt` declares 15 country-leader roles with `id = -1`, expiry `1965.1.1.1`, and the following route IDs:

- Personal: `slopx_ireland_w_t_cosgrave`, `slopx_ireland_richard_mulcahy`, `slopx_ireland_john_costello`, `slopx_ireland_james_dillon`, `slopx_ireland_sean_lemass`, `slopx_ireland_daniel_morrissey`, `slopx_ireland_joseph_blowick`, `slopx_ireland_frank_ryan`, `slopx_ireland_peadar_odonnell`, `slopx_ireland_gearoid_o_cuinneagain`, and `slopx_ireland_father_edward_cahill`.
- Institutional: `slopx_ireland_ira_army_council` (`The Army Council`), `slopx_ireland_high_king` (`The High King`), `slopx_ireland_five_provinces_steward` (`The Steward of the Five Provinces`), and `slopx_ireland_compact_steward` (`The Compact Steward`). Institutional names correctly avoid personal random-name pools.

The starting `IRE_Éamon_de_valera` role is correctly supplied by vanilla `common/characters/IRE.txt` and recruited by `history/countries/IRE - Ireland.txt:20`. The custom route IDs occur only in the declaration file (apart from incidental flag/focus text matches): no `recruit_character`, `add_country_leader_role`, `create_country_leader`, `set_politics`, `retire_country_leader`, or equivalent route transition call references them. The custom portrait refs are consequently both lifecycle-dead and asset-unresolved.

This is a blocking package defect. The parent needs a route transition contract covering country-leader creation/recruitment, ruling-party/ideology state, outgoing-leader retirement, re-entry prevention, route defeat/cleanup, and save-safe idempotency. The vanilla effects documentation supports `recruit_character`, `add_country_leader_role`, `create_country_leader`, and retirement effects; use those documented APIs and the lifecycle matrix rather than only setting route flags.

### Politics and country identity

Search of mod `common`, `events`, and `history` surfaces found only the opening and 1939 `set_politics`/`set_popularities` in `history/countries/IRE - Ireland.txt`. There is no mod-side `common/parties`, `common/cosmetic_tags`, country definition, `set_party_name`, `change_tag`, `set_cosmetic_tag`, `set_country_name`, or route ruling-party transition. All route AI/flags therefore leave the visible country identity and political state as base Ireland. This is not a base-tag loading error, but it is a blocker against the route-character, route-party, and cosmetic-name requirements in the canonical specs.

## Ideas and spirits

`common/ideas/slopx_ireland_spirits.txt` declares exactly 63 country ideas, all restricted with `allowed = { original_tag = IRE }`:

- Opening family members: `slopx_ireland_spirit_governing_order`, `slopx_ireland_spirit_organised_society`, and `slopx_ireland_spirit_security_external_position`.
- 60 additional route/failure variants across the same three persistent family slots.

`slopx_ireland_initialize_campaign` adds exactly the three opening ideas. This matches the canonical three-family rule and does not create a fourth starting spirit for National Settlement.

No `swap_ideas`, `remove_ideas`, or route/failure `add_ideas` call exists anywhere in the mod beyond the opening three additions. The 60 variant declarations are inert, so route locks cannot produce the documented persistent-spirit lifecycle. This requires coordinated route transition effects, not a safe local idea-file edit.

All 63 idea `picture` values use custom `GFX_slopx_ireland_spirit_*` names, but `interface/slopx_ireland_icons.gfx` registers only focus and decision sprites. No final spirit DDS package is present in `assets/ireland_focus_tree/icons`; the source-atlas/asset manifests mark spirits as incomplete. Do not substitute generic vanilla icons without parent approval because the asset instructions require explicit fallback discussion and the current package has no approved fallback.

## Focus loading and route wiring

`common/national_focus/slopx_ireland_focus_tree.txt` is `slopx_ireland_focus_tree`, `default = no`, and applies only to `IRE` through the tag modifier. It contains 216 focus nodes and 216 unique icon references. The live GFX file registers all focus refs, and all corresponding DDS paths exist. This part is a pass.

The focus tree is not a complete country package merely because it loads. Current route wiring has concrete dead gates:

- `common/national_focus/slopx_ireland_focus_tree.txt:1616` checks `slopx_ireland_dillon_mandate_complete`, but no setter exists in the mod.
- `common/national_focus/slopx_ireland_focus_tree.txt:3008` checks `slopx_ireland_northern_regional_review_ready`, but no setter exists.
- `:3014` sets `slopx_ireland_northern_final_review_passed`, but no subsequent map-core effect consumes the final-review state.
- The core-review trigger `slopx_ireland_can_northern_core_review` is defined but unused.

The older `docs/plans/ireland_focus_tree/audits/focus_tree_audit_2026-07-18.md` is stale for the current live icon and AI-plan surfaces: it predates the 369 registered focus/decision sprites and the two current AI plans. Its findings about unresolved focus icons and absent AI plans should not be copied forward; the missing lifecycle/gate/core findings remain relevant.

## Decisions and events

The current decision/event package contains the Northern ledger, review, mission, and reaction surfaces and consistently references state `119`; this is useful integration coverage. It does not mutate ownership/controller/core state. In particular:

- `common/decisions/slopx_ireland_decisions.txt:25363` (`slopx_ireland_action_conduct_the_core_eligibility_review`) activates the review mission but does not add a core.
- `events/slopx_ireland_events.txt` contains the final-review/core-eligibility event family around events `292-295`; the effects set memory/acceptance/defer flags, ledger values, and foreign reactions only.
- `common/scripted_triggers/slopx_ireland_triggers.txt:130-136` is the intended final eligibility gate, but no effect path invokes it to produce map state.

The parent should reconcile the decision, mission, event, focus, and scripted-effect paths before adding a core. The final review must be one idempotent, explicitly gated map mutation, not a new unconditional event option.

## AI and playability

`common/ai_strategy/slopx_ireland_ai_strategy.txt` contains the canonical 30 durable profile registry and 10 overlay registry, all restricted to `original_tag = IRE` with route/profile abort behavior. The profiles include historical de Valera, constitutional, interventionist, radical, clerical, high-king, five-provinces, otherworld, and convergence identities; the registry itself is broad enough for the spec.

`common/ai_strategy_plans/IRE_slopx_ireland_strategy_plans.txt` has only:

- `IRE_slopx_historical` (`:6`), with a generic opening `ai_national_focuses` list and an empty `focus_factors` block at `:87`.
- `IRE_slopx_route_reactive` (`:91`), with a shared reactive list and an empty `focus_factors` block at `:161`.

The focus tree has no `ai_will_do` weighting. Therefore the 30 profile registry is not enough to prove the canonical AI matrix: profile-specific route ordering, route lock behavior, Northern review behavior, and capstone selection are not represented in focus selection. This can leave AI Ireland on shared material/Northern focuses without committing to its profile route, or make route branches unreliable. Add profile/overlay-aware focus plans or focus weights only after the route and leader lifecycle contract is settled.

The inherited military baseline is coherent but small: vanilla `IRE_1936` supplies one nine-infantry division, one Army High Command unit at province `11293`, `start_experience_factor = 0.2`, `start_equipment_factor = 0.3`, and one `infantry_equipment_1` production line with one requested factory, `progress = 0.75`, and `efficiency = 100`. The mod history adds three research slots and ten convoys but does not add free divisions, equipment, fuel, shipping, or industry. This passes the no-free-start requirement; playability balance remains dependent on the missing route/idea/AI lifecycles.

## Assets and localisation

### Live asset coverage

`interface/slopx_ireland_icons.gfx` currently registers 369 sprite definitions with existing texture paths:

- 216 focus icons (`GFX_focus_slopx_ireland_*`).
- 13 decision-category icons.
- 140 decision-action icons.

The current asset package therefore covers the visible focus/decision surface. The asset manifests under `docs/plans/ireland_focus_tree/assets/` mark missions, spirits, overlays, laws, mechanic icons, achievements, GUI, and animations incomplete or blocked.

The following character/portrait refs in `common/characters/slopx_ireland_route_characters.txt` are not registered by any live mod GFX file:

- `GFX_slopx_ireland_portrait_w_t_cosgrave`
- `GFX_slopx_ireland_portrait_richard_mulcahy`
- `GFX_slopx_ireland_portrait_john_costello`
- `GFX_slopx_ireland_portrait_james_dillon`
- `GFX_slopx_ireland_portrait_sean_lemass`
- `GFX_slopx_ireland_portrait_daniel_morrissey`
- `GFX_slopx_ireland_portrait_joseph_blowick`
- `GFX_slopx_ireland_portrait_frank_ryan`
- `GFX_slopx_ireland_portrait_peadar_odonnell`
- `GFX_slopx_ireland_portrait_gearoid_o_cuinneagain`
- `GFX_slopx_ireland_portrait_father_edward_cahill`

The institutional refs are also unregistered: `GFX_slopx_ireland_symbol_army_council`, `GFX_slopx_ireland_symbol_high_kingship`, `GFX_slopx_ireland_symbol_five_provinces`, and `GFX_slopx_ireland_symbol_otherworld_compact`. The sourced asset package has a de Valera portrait and a small set of cleared symbols, but it does not satisfy these route refs. Real-person portraits need sourced/cleared handling; generated fictional/institutional art must retain the institutional naming rule.

### Localisation

`localisation/english/slopx_ireland_l_english.yml` has a UTF-8 BOM and contains the current 216 focus title/description keys and 63 idea keys/descriptions. Raw UTF-8 names such as `Seán Lemass` and `Gearóid Ó Cuinneagáin` decode correctly. Literal `name =` values in the character file are therefore not a character-localisation defect by themselves.

The missing surface is route identity: there are no mod-side party names, cosmetic tags, country names/adjectives, or route leader localisation keys tied to an actual transition. Once leaders/parties are wired, localisation must be added in the same change. Do not “fix” this by replacing proper UTF-8 names with ASCII or console-mojibake strings.

## Required parent work and safe sequencing

1. Define and implement the route identity/leader lifecycle: recruit or attach each route character, update party/ideology/popularity/country identity as specified, retire outgoing leaders, and make every transition idempotent.
2. Add approved, cleared portrait/symbol assets and register every route `GFX_` ref. Register spirit sprites before wiring idea lifecycle.
3. Implement the three persistent spirit-family transitions and failure/return cleanup, preserving exactly three active family slots.
4. Add the missing Dillon and Northern regional-review setters, then reconcile the final-review event/decision/focus path.
5. Implement a single gated, idempotent Northern core effect called only after stage `5`, final review, control/occupation/integration requirements, and any canonical foreign/reaction restrictions are satisfied. Keep the opening state `119` owner/core separation unchanged.
6. Add profile/overlay-aware AI focus priorities and test historical AI opening, route commitment, Northern review, and route conclusion behavior.
7. Run focus and map inspectors again after runtime wiring, then perform a fresh parse/new-game scenario validation for leader, ideas, party identity, state `119`, claim, and core timing.

## Validation evidence and skipped checks

Completed read-only checks:

- Cross-referenced the canonical specs, lifecycle/route/AI/asset matrices, offline wiki pages, vanilla documentation, and vanilla Ireland history/country/character/OOB files.
- Counted the current focus/asset surfaces: 216 focus nodes, 216 focus icons, 153 decision sprites, and 369 live GFX sprite definitions.
- Traced all mod `add_core`, `add_claim_by`, state-transfer, owner/controller, annexation, release, and puppet references. The only Ireland map mutation is the claim in `slopx_ireland_northern_settlement_ledger`; the only state-119 cores are `ENG` and `NIR` in the state history override.
- Traced route character IDs and leader lifecycle effects; no custom route character has a runtime recruiter/transition/retirement caller.
- Traced idea add/swap/remove calls; only the three opening ideas are added.
- Verified the localisation BOM and current focus/idea key coverage.

The read-only HOI4 focus/map inspector attempt was terminated after it exceeded the bounded wait without returning diagnostics. No MCP write was attempted. Source inspection and vanilla documentation supplied the evidence above; post-wiring MCP inspection remains required.

## Simplifications, omissions, and blockers

- No gameplay patch was made because the remaining defects cross country history, characters, parties, focuses, decisions/events, ideas, AI, map effects, assets, and localisation. A narrow patch would either leave the package misleadingly incomplete or create an unapproved fallback.
- No fallback portraits, spirit icons, party identities, or core grant were invented.
- The opening map/history setup, exact opening variables, base focus loading, current focus/decision icon coverage, and inherited military baseline are the completed/usable portions.
- Completion remains blocked by the lifecycle, identity, AI focus-selection, core-progression, and unresolved asset surfaces listed above.
