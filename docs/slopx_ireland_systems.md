# Ireland Total Overhaul runtime systems

Feature slug: `ireland_focus_tree`; namespace: `slopx`.

This document describes the implemented Ireland runtime contract and its remaining integration surfaces. The canonical specifications under `docs/specs/ireland_focus_tree/` remain authoritative for exact route names, counts, thresholds, dates, and source classifications.

## Current status and evidence boundary

Reconciled 2026-08-02: this document records the intended/current runtime contract and structural source evidence; it does not claim gameplay completion. Use `docs/plans/ireland_focus_tree/source_of_truth_map.md` for the normalized `implemented` / `partial` / `blocked` / `queued` / `not-run` status ledger and `docs/plans/ireland_focus_tree/project_status.md` for the latest tranche evidence.

The current worktree contains structural evidence for the focus, event, decision/mission, AI, GUI, scripted-localisation, route-identity, spirit, and achievement surfaces described below. The source-clearance gate remains blocked: the authoritative manifest records 15 blocked portraits, 8 blocked symbol/document packages, and 15 blocked sourced event/news slots; there are no remaining `needs_user_review` rows. Five cleared FRUS packages now feed the four H04 emergency-news nodes and the F15 neutral-markings node. Live engine parsing, fresh-1936 and route scenarios, AI simulations, GUI interaction, achievement playthroughs, and final global-diagnostic review remain not-run or unresolved. No fallback or substitute asset is implied by this status.

## Opening state

`slopx_ireland_initialize_campaign` creates a sovereign Ireland campaign with National Settlement `+25`, Settlement Momentum `-1`, Social Consent `55`, Neutrality Integrity `72`, British/Vatican/American/German leverage `45/25/5/5`, formal Dáil seats `153`, routine votes `152`, Fianna Fáil `77/76`, Fine Gael `59`, Labour `8`, and other seats `9`.

National Provision stores Food/Energy/Transport/Maritime as `55/25/40/30`; the derived display is `(55+25+40+30+2)/4 = 38`. National Readiness stores Command/Equipment/Mobilisation/Supply/Warning/Maritime Protection/Intelligence as `25/8/20/12/5/5/30`; the derived display is `105/7 = 15`. The Northern ledger begins at Unionist `5`, Nationalist `40`, Labour `30`, British `10`, Security `45`, Integration `10`, with integration stage `0` and claim-only state.

Only three persistent route-spirit families are installed: Governing Order, Organised Society, and Security and External Position. Route stages and contributors are stored in the shared variables and flags; no fourth persistent spirit is created by a route.

Nonhistorical AI selects one constitutional base profile once at campaign
initialisation with the canonical weights `55/12/8/5/7/2/8/3` for de Valera,
Lemass, Cosgrave, Mulcahy, Costello, Dillon, Norton, and constitutional
vocationalism. Historical mode and human-controlled campaigns use the de
Valera base. The selection changes profile priorities without committing a
route or granting a focus reward; the authored route gate still records the
actual political choice.

Concealed `A` commitments are opt-in through the `slopx_ireland_hidden_content`
game rule. Its effective permission is the conjunction of the enabled rule,
the cultural evidence permission, and the existing public, regional, unusual-
campaign, and disqualifier checks. Disabling the rule clears effective hidden
permission and prevents the High Kingship, Five Provinces, and Otherworld
branch gates from opening while leaving serious culture and its evidence
history intact.

## Shared runtime helpers

The owning files are:

- `common/script_constants/slopx_ireland_constants.txt`
- `common/scripted_triggers/slopx_ireland_triggers.txt`
- `common/scripted_effects/slopx_ireland_effects.txt`
- `common/scripted_effects/slopx_ireland_runtime.txt`
- `common/on_actions/slopx_ireland_on_actions.txt`

The initialization effect is idempotent. Monthly Settlement movement uses momentum multiplied by `2`, clamped to `-10..10`; stage movement requires a seven-day confirmation and returns only after the five-point margin. A committed route clamps Settlement to `-60..60` and opens a 180-day review. BOP presentation mirrors the authoritative Settlement variable through the native `slopx_ireland_national_settlement` balance of power.

The Dillon trigger is the sole shared intervention gate. It requires mandate `90`, Readiness `45`, Social Consent `60`, a Dáil majority, British leverage below `60`, the complete sovereignty/home-reserve/contribution/safeguard set, Northern policy or lawful deferment, no constitutional crisis, Provision `50` with every component at least `30`, Maritime Access and Transport `40`, Equipment/Command/Supply `40`, and the protected reserve. No focus, decision, event, or conclusion may bypass it.

Northern claims, control, occupation, settlement, integration, and cores are separate state surfaces. The opening state override removes the vanilla Irish core from state `119`; a future Irish core is legal only after integration stage `5` and a passed final regional review. No focus grants an Irish Northern core.

## Dynamic helper contract

All helpers are country-scoped unless an explicit target is documented.

| Helper | Inputs | Outputs and side effects |
| --- | --- | --- |
| `slopx_ireland_initialize_campaign` | none; called for IRE at startup | Writes all opening variables, activates exactly three spirit slots, installs the opening spirits, sets the claim-only Northern state, selects the historical or weighted constitutional AI base, initializes the native BOP, and recomputes derived values. Idempotent. |
| `slopx_ireland_recompute_provision` | four Provision component variables | Writes display value and bottleneck flags. Severe/dual/zero-component flags are mutually maintained; it grants no free equipment or factories. |
| `slopx_ireland_recompute_readiness` | seven Readiness component variables | Writes display value and equipment/supply/warning/maritime bottleneck flags. Readiness is not a passive political-power store. |
| `slopx_ireland_commit_route` | `slopx_ireland_route_commitment_input` | Clamps Settlement, stores route commitment, clears old momentum contributors, opens the 180-day review, and resets pending stage state. Route-specific leaders/laws/offices remain the caller's responsibility. |
| `slopx_ireland_begin_conclusion_review` | none | Starts the 180-day conclusion review once the caller has checked route-specific conclusion requirements. It does not grant recognition, territory, industry, units, fuel, shipping, or alignment. |
| `slopx_ireland_finalize_route_conclusion` | due conclusion review, one authored route capstone, live ledgers and route history | Resolves full, partial, blocked, or failed conclusion state; records named blocked surfaces; closes foreign/neutrality transient chains; archives the route with zero active objectives; preserves route, damage, law, office, leverage, obligation, and disqualifier history. It grants no territory, core, industry, equipment, unit, fuel, shipping, administration, alignment, office, or recognition. |
| `slopx_ireland_record_mission_result` | active mission flag and result `1` full / `2` partial / `3` failure / `4` cancelled / `5` escalated | Records the result, decrements active mission count, cleans mission target state, and refreshes capacity. |
| `slopx_ireland_rebuild_mission_counters` | active mission flags | Rebuilds the active count, thirteen named category counters, category capacity flags, and the reserved critical-slot flag from the 54 named mission families. Provision, Readiness, and Neutrality incident caps widen only under their named emergency conditions; constitutional, provision, invasion, neutrality-incident, Northern, occupation, and route-review mission families can consume the reserved slot when their live need flag is set, while routine launches stop at the reservation threshold and keep their own deadlines and cleanup. |
| `slopx_ireland_sync_route_profile` | weighted base selection, committed route, and hidden-route gates | Selects one durable AI route profile, maps an uncommitted nonhistorical base to the plausible profile lane, and keeps the H/P/A profile boundary explicit. |
| `slopx_ireland_sync_route_gate_flags` | Clann and vocational prerequisite flags plus their dynamic stakeholder ledgers | Maintains the Agrarian Support Bloc gate at Agrarian Cohesion `50` and the vocational mandate gate at Social Consent `50` and Minority Confidence `35`; it does not create seats or party membership. |
| `slopx_ireland_sync_law_registry` | seventeen staged law variables and their dated route/action/crisis flags | Maintains Constitutional Government, Emergency Authority, Censorship, Rationing, Tillage, Mobilisation, Internment, Public Order, Occupation, Education, Religion, Language, Economic Control, Trade and Shipping, Foreign Access, Northern Settlement, and Guarantee ladders. Each family exposes active, public-entry, review-due, abuse, and exit state; no law is represented as a passive spirit. |
| `slopx_ireland_sync_office_registry` | route leaders, constitutional transitions, Northern stage, and command ledgers | Separates President, Taoiseach, Tánaiste, party leader, parliamentary leader, cabinet, Chief of Staff, security chief, movement leader, armed-wing commander, council chair, provincial chair, High King/Regent, Compact Steward, and Transitional Administrator. Vacancy flags feed the leadership/office overlay and preserve former-office history in route flags. |
| `slopx_ireland_refresh_route_spirits` | committed route and contributor flags | Removes stale route variants, then installs exactly one evolving variant in each of the three persistent spirit families. |
| `slopx_ireland_activate_route_leader` | committed route | Retires the previous active route leader, recruits/promotes the attested or authored route character, and records the transition once. |
| `slopx_ireland_sync_route_identity` | committed route and completed constitutional subroute | Applies the registered route cosmetic tag and clears the prior route identity before a transition is shown. |
| `slopx_ireland_sync_northern_ledger` | state 119 control plus Northern policy flags | Advances control, occupation, settlement, integration, and final-review ledgers independently; it never creates a claim, transfers a state, or grants a core by itself. |
| `slopx_ireland_sync_northern_final_review_proofs` | current state-119 control, law stages, Northern consent ledgers, named mission/action records, and review thresholds | Rebuilds the separate representation, policing, courts, finance, services, transport, rights, resistance, guarantees, withdrawal, demobilisation, sustained-security, and emergency-law proof flags. Stage five requires every proof plus 180 days at Security Stability `70`; it never changes ownership, control, claims, or cores. |
| `slopx_ireland_apply_northern_core_review` | strict final review trigger | Adds the Irish core to state 119 only after actual control, stage-five integration, settlement services, final review, and the separate core review all pass. |
| `slopx_ireland_update_achievement_trackers` | witnessed route, ledger, mission, and war history | Converts live minima/maxima and route conclusions into achievement progress without granting gameplay rewards. |
| `slopx_ireland_update_achievement_history` | named route transitions, law failures, offices, evidence, obligations, foreign reactions, Northern reviews, and ratification records | Persists all 32 achievement-history flags, including irreversible disqualifiers and the 365-day confidence-and-supply expiry; it never grants territorial, material, diplomatic, or political rewards. |
| `slopx_ireland_sync_operational_state` | Provision/Readiness components, emergency route flags, war state, Security Loyalty, and incident sources | Derives live emergency, command-collapse, mobilisation, security-collapse, and incident-family flags. Recovery clears only live failure state; durable achievement history is recorded separately. |
| `slopx_ireland_sync_cultural_evidence` | Cultural Capacity, named H/P work, full mission records, Northern contacts, public knowledge, obligations, and disqualifier history | Recomputes the four public culture components, concealed evidence counters, public-lane flags, and independent-evidence reveal state without granting route or material rewards. |
| `slopx_ireland_sync_plebiscite_state` | Campaign-open and passed/rejected/recovered result flags | Synchronizes generic and Northern plebiscite-open state and closes both after a recorded result. |
| `slopx_ireland_sync_gui_requests` | Conditions, Northern, and evidence request flags plus row selections from the three scripted GUIs | Consumes each request once, refreshes the owning authoritative projections, records the last-reviewed row, and advances the corresponding GUI dirty counter. |
| `slopx_ireland_sync_ai_priority_flags` | Durable route profiles and temporary AI overlays | Rebuilds thirteen category-priority flags consumed by the 140 action and 54 mission AI weights, then refreshes the domain, shared utility, and candidate-ledger layers. |
| `slopx_ireland_sync_ai_candidate_ledger` | profile stance, category priorities, live bottlenecks, failures, deadlines, and reserved dependencies | Rebuilds the thirteen cause/repair/dependency candidate ledgers and applies the exact six normal/crisis willingness floors. It changes AI ranking only; it never opens content or grants a gameplay resource. |
| `slopx_ireland_sync_neutrality_incident_family` | generic active incident plus numbered source flag | Maps the active source to exactly one of nine neutrality families and clears stale subtype state after cleanup. |
| `slopx_ireland_open_event_gateways` | initialized, open route, and foreign-window state | Opens the event programme and schedules a foreign-reaction digest after the visible reaction window closes. |
| `slopx_ireland_dispatch_event_programme` | source triggers copied into the gateway | Scans the authored event families with a persisted cursor, fires at most one event per day, preserves source/date/route/hidden gates, and closes on route cleanup. |
| `slopx_ireland_open_foreign_reaction_window` | none | Opens a 14-day reaction window, clears visible-count state, and prepares the reaction digest. The event/action caller owns actor-specific effects. |
| `slopx_ireland_cleanup_route_state` | none | Removes temporary route-review contributors, all active/terminal mission objective flags, pending review state, and route event targets. It is idempotent and preserves route history, offices, laws, party identities, damage, leverage, obligations, and disqualifiers. |
| `slopx_ireland_sync_national_settlement_bop` | authoritative Settlement variable | Converts `-100..100` to the native `-1..1` BOP range through a meta effect. The variable remains authoritative. |

Two narrower admission contracts keep the named cultural and maritime work physical. `slopx_ireland_historic_site_admission_valid` requires full control of state 135, a live serious-culture/archive lane, regional participation, Social Consent `35`, one rights-bearing local constituency, 250 manpower, 5 Trucks, and 10 Support Equipment maintenance kits; the historic-site action calls it again before writing its Cultural Capacity result. `slopx_ireland_marine_patrol_craft_coverage_valid` requires the action-specific coastal patrol-craft commitment bound to the charged 3-Convoy allocation. The Neutral Approaches map objective rechecks that flag alongside the port, industrial, naval, shipping, warning/rescue, and readiness proofs, and cancellation, timeout, success, failure, escalation, and route cleanup all release it. The flag is an authored coverage abstraction, not a merchant-stockpile shortcut, spawned unit, or free ship.

## Decisions and missions

The decision surface owns exactly thirteen categories, 140 named actions, and 54 mission families. Action costs are derived from burden and component state; Command Power never exceeds `60`. Missions use the canonical normal/emergency/occupation capacity caps `8/10/12`, named regional objectives, deadlines, full and partial success, failure/escalation outcomes, AI weights, and cancellation cleanup. The named region registry and Coastwatch six-sector grouping live in the decision/mission implementation and its handoff documentation.

The four paired logistics safeguards use side-effect-free physical contracts shared by action admission, AI material tests, mission availability, live result evaluation, and cleanup-facing map objectives. The Dublin-to-Cork rail pair requires full control of states `113` and `135`, endpoint infrastructure, 5 Trains, 250 manpower, 200 Fuel, one factory reserved for 180 days, and returns at most 3 Trains, 175 manpower, and 140 Fuel on cancellation; its full/partial Transport Serviceability bands are `50/35`. The essential-cargo pair requires the state-135 receiving-port platform, industrial complex, live merchant route, Dublin-to-Cork railway, and a naval-base capacity tier keyed to the two named maritime missions; it charges 5 Convoys, 2 Trains, and 200 Fuel and returns at most 3 Convoys, 1 Train, and 140 Fuel. The command exercise requires the state-113 arms/infrastructure platform, Supply Readiness `20`, one division to launch and two for full success, with full/partial Command and Supply bands `50/35` and `35/20`; it charges 50 Infantry Equipment and 250 Fuel. Belfast contracts require state-119 industrial/infrastructure control, Labour Cooperation `30` to launch and `45` for full success, Industrial Capacity `40/55` for partial/full success, 2 factories reserved for 300 days, and the existing 100 Support Equipment, 50 Trucks, and 250 Fuel charge. No pair mutates divisions or grants free factories, equipment, fuel, shipping, territory, cores, or political power.

The direct historic-site action keeps the same H/P boundary: its local-support gate is a live regional institution plus one rights-bearing constituency, while its maintenance obligation is a concrete 10 Support Equipment charge. It is not satisfied by the later stewardship result. The patrol pair keeps craft, shipping, repair, warning/rescue, and mission state separate: the Convoy charge binds a named craft-coverage flag, and the mission objective refuses to resolve if that commitment is missing.

Northern progression keeps claim, control, occupation, settlement, integration, and core review as separate ledgers. The settlement focus opens the ledger and issues only the state-119 claim. Runtime alone can establish settlement stage five and integration stage five after current proof surfaces pass; the regional-review focus records that the formal review has started. Only the idempotent core-review effect can add the core, and it rechecks current control, consent, law, resistance, guarantee, withdrawal, demobilisation, and review-proof state.

## Neutrality and statecraft

Neutrality Integrity is changed by active airspace, shipping, rescue, internment, intelligence, weather, trade, access, censorship, law, incident, and public-legitimacy choices. Foreign reactions are grouped by the twelve canonical actor families and twelve response classes. Only four reaction results are visible during a 14-day window; subsequent results are consolidated into a digest. Political success never bypasses material gates or grants free strategic assets.

## H/P/A boundary

Historical material and institutions remain `H`. Grounded divergence remains `P`. Concealed culture can expose `P` possibilities, but the `A` boundary requires independently verified impossible evidence, public capacity, obligation discipline, and the canonical reveal. AI, localisation, achievements, assets, and cleanup use the same gates. Serious culture remains useful even when no concealed route is found.

## Asset and UI wiring checklist

Final runtime visual files are owned under the standard mod `gfx/` roots and are registered from `interface/slopx_ireland_icons.gfx`, `interface/slopx_ireland_secondary_assets.gfx`, `interface/slopx_ireland_gui_assets.gfx`, `interface/slopx_ireland_event_art.gfx`, `interface/slopx_ireland_route_assets.gfx`, `interface/slopx_ireland_bop_assets.gfx`, and `interface/slopx_ireland_animation_assets.gfx`. `assets/ireland_focus_tree/` is temporary source, processing, manifest, review, and fallback-evidence space only. The implementation exposes only the historical base flag and the 18 registered alternate route identities; no unverified All-Island flag is used as a shortcut. The implementation must keep these stable families aligned:

- 60 sourced real-person portrait slots: `GFX_slopx_ireland_portrait_<roster_id>`.
- 40 sourced historical symbol/document slots: `GFX_slopx_ireland_symbol_<package_id>`.
- one historical base flag set and 18 alternate route flag sets in `gfx/flags/` with medium/small variants; the route tags are `IRE_SLOPX_ARMY_COUNCIL`, `IRE_SLOPX_CIVIL_REPUBLICAN`, `IRE_SLOPX_WORKERS_PARTY`, `IRE_SLOPX_WORKERS_SMALLHOLDERS`, `IRE_SLOPX_CORPORATE_ESTATE`, `IRE_SLOPX_ODUFFY_PERSONAL`, `IRE_SLOPX_CATHOLIC_GUARDIANS`, `IRE_SLOPX_GAELIC_CORPORATE`, `IRE_SLOPX_CHRISTIAN_NATIONAL`, `IRE_SLOPX_REGIONAL_AIS_EIRGHE`, `IRE_SLOPX_AIS_EIRGHE`, `IRE_SLOPX_HIGH_KING_SACRAL`, `IRE_SLOPX_HIGH_KING_CONSTITUTIONAL`, `IRE_SLOPX_PENTARCHY`, `IRE_SLOPX_FIVEFOLD_FEDERATION`, `IRE_SLOPX_OTHERWORLD_DOMINION`, `IRE_SLOPX_COMPACT_TWO_IRELANDS`, and `IRE_SLOPX_CONVERGENCE_ORDER`. Their cosmetic-tag definitions live in `common/countries/slopx_ireland_cosmetic.txt`; route transitions call `set_cosmetic_tag` only after a route identity is authored, and cleanup calls `drop_cosmetic_tag`.
- at least 216 distinct focus icons, one per implemented focus; 13 category icons; 70 action icons; 54 mission icons.
- 63 persistent-spirit icons across the three evolving families; 27 temporary-state icons; 51 law icons; 45 mechanic icons. The ordinal DDS packages are mapped in source order to the exact spirit and mission IDs, seventeen law ladders, and the mechanic/overlay registries.
- 32 achievement concepts with locked/unlocked/hidden states (96 files), registered against the exact 32 achievement IDs in source order.
- 120 event/news images split into 69 sourced and 51 generated entries.
- exactly three GUI surfaces: National Conditions Panel, Northern Settlement Ledger, and Concealed Evidence Ledger.
- exactly seven frame-based animations with independent frames and static fallbacks; no animated portrait is permitted.
- up to three optional audio briefs, each with provenance and licence notes.

The event gateway currently has all 485 authored calls wired, with a one-event-per-day guard and cursor advancement. The generated icon registration covers all 216 focus, 13 category, 54 mission, 63 spirit, 27 temporary-overlay, 51 law, 45 mechanic, and 96 achievement-state DDS files. The 140 named action sprites resolve to exactly 70 allocated action textures through cross-category controlled reuse; no visible category repeats an icon. The three GUI surfaces have static backgrounds, rows, status states, review controls, and route/evidence-driven animation/fallback decorations. The seven independent animation packages are registered with their exact frame counts, rates, looping modes, and static fallbacks. The source package and real-person portrait wires remain separate completion gates; this document is not a completion claim until every manifest and engine check is closed.

## Future extensions

Future work should deepen regional service delivery, postwar reconstruction, and the six Coastwatch sectors without adding a fourth persistent spirit or a new GUI surface. Additional research should improve C1/C2 source clearances through authoritative archives, never through generated likenesses or silently substituted historical images. Any new dynamic helper must be documented in `docs/slopx_dynamic_effects.md` before use.
