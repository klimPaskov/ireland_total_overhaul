# Ireland implementation recheck — 2026-07-22

Feature slug: `ireland_focus_tree`

This is a current-worktree static recheck after the runtime-art placement correction and the decision/mission lifecycle patch. It is evidence for implementation state, not a gameplay completion claim. HOI4 was not launched, and no fresh engine or scenario validation was possible while the offline MCP transport was closed.

## Current structural inventory

- Focus source: 216 focus blocks in `common/national_focus/slopx_ireland_focus_tree.txt`.
- Decisions and missions: 13 categories, 140 action decisions, and 54 mission families.
- Mission presentation: 54 named map-objective tooltips and 54 timeout-escalation descriptions are wired to the mission surfaces.
- Events: 249 main event nodes and 236 flavour nodes. The historical, political-crisis, and foreign-reaction registries remain H01–H18, P01–P18, and FR01–FR12; the foreign-reaction registry includes the reaction digest in addition to the 30 reaction nodes.
- AI and achievements: 30 durable AI profiles, 10 temporary overlays, and 32 achievements.
- Focus-selection layer: 31 Ireland national-focus plans, including a dedicated serious-cultural stewardship plan; all plan focus references and focus-factor references resolve to authored focus IDs.
- Source manifest: 169 rows: 39 complete, 28 needing user review, and 102 blocked. Clearance is still an external gate.

## Runtime art placement

- Final runtime DDS files are under the standard mod `gfx/` roots, including `gfx/interface/`, `gfx/event_pictures/ireland/`, `gfx/leaders/ireland/`, and `gfx/achievements/`.
- `assets/ireland_focus_tree/` is staging-only for source masters, processed previews, manifests, contact sheets, review material, and fallback evidence. It is not a runtime texture root.
- The current interface registrations use `gfx/...` texture paths. The only `assets/ireland_focus_tree` matches in the two Ireland route/secondary `.gfx` files are explanatory comments; no runtime `texturefile` uses the staging path.
- All 216 authored focus icons now have paired `_shine` registrations in `interface/slopx_ireland_focus_shine.gfx`; the 216 masks resolve to `gfx/interface/goals/slopx_ireland/`, and the standard shine surface is copied to `gfx/interface/goals/shine_overlay.dds`.
- The runtime event-picture root currently contains 78 DDS files: 51 generated alternate/news images and 26 complete source-manifest outputs plus the historical-chain alias image. Four stale blocked candidates were moved into the staging-only review directory and are not registered.
- The 51 generated event/news manifest rows and all 67 complete or review-gated source rows with final paths have existing DDS files whose SHA-256 values match their manifests. Blocked source rows have no final path.

## Gameplay invariants checked in source

- The opening constants and initial ledgers remain centralized in `common/script_constants/slopx_ireland_constants.txt` and the Ireland initializer: National Settlement `+25` with momentum `-1`, Social Consent `55`, Dáil `153`/`152`, Provision `55/25/40/30` displayed as `38`, Readiness `25/8/20/12/5/5/30` displayed as `15`, Neutrality Integrity `72`, and Northern `U5 N40 L30 B10 S45 I10`.
- Action costs use the native `cost` field for all 140 actions, with named-ledger political-power/command-power scarcity surcharges and burden ledgers applied in completion effects; no action mixes native and custom cost models. Physical stockpile/manpower costs remain on major provision, readiness, defence, transport, and merchant actions. The command-power ceiling remains `60`.
- Foreign partner validity is centralized for GBR, USA, GER, and ITA. Daily runtime synchronization clears channels for missing or capitulated partners, records actor-specific invalidation plus foreign-access failure, and route cleanup clears every open foreign channel.
- The Northern sequence remains separate: claims, control, occupation, settlement, integration, and final review are distinct helpers/ledgers. The only Ireland runtime `add_core_of = ROOT` is inside the final core-review helper, whose trigger requires integration stage `5` and the final review proofs.
- `slopx_ireland_enforce_hpa_boundary` remains the shared route-profile boundary helper; route identity is not implemented as a generic ideology skin.
- Hidden High Kingship, Five Provinces, and Otherworld dispatches require their respective evidence/convention/rare-condition flags in both source triggers and the daily dispatcher.

## Offline fixes in this recheck

- Removed the incompatible custom-cost pair from all 140 actions while retaining native PP costs and named-ledger surcharge deductions; the AI now receives the real base PP cost signal.
- Added centralized non-capitulation partner triggers to foreign actions, missions, and map objectives, with daily invalidation and route-archive cleanup.
- Wrapped every mission objective in a localized `custom_trigger_tooltip` and made escalation explicit in every mission description.
- Replaced the undefined focus-filter token with vanilla's `FOCUS_FILTER_INTERNATIONAL_TRADE`, added mutually exclusive personal/corporate O'Duffy capstones, repaired stale AI focus IDs and intermediate route ordering, and differentiated the affected route localisation.
- Reconciled the clerical, High Kingship, Five Provinces, and Otherworld crisis dispatches and regional decision/category gates to the current route flags; the clerical crisis no longer depends on the concealed-absurd route state, while the three concealed crisis families require their own permission, evidence, convention, and rare-condition flags in both dispatch and event source.

## Static validation after the patch

- The action/mission contract scan found `140/140` native-cost action blocks with no custom-cost tokens, `54/54` mission blocks with timeout/cancel/complete contracts, and `54/54` localized objective wrappers.
- The foreign scan found zero raw GBR/USA/GER/ITA existence checks outside the four centralized partner triggers, zero foreign mission validity gaps, and one daily channel-sync helper.
- Runtime interface scanning found `1095` `texturefile` references, `432` animation masks, and `432` shine-overlay references; all 806 unique texture paths resolve under the mod or vanilla runtime surface, with `0` non-comment staging-path references. The virtual vanilla `gfx/FX/buttonstate.lua` effect token remains a standard `effectFile` reference, not a missing texture.
- Focus registration scanning found `216/216` regular focus definitions and `216/216` paired shine definitions, with `0` missing focus masks and `0` malformed animation-scale blocks.
- Manifest hashing found `67` sourced final DDS files and `51` generated event/news DDS files checked, with zero missing files, zero mismatches, and zero blocked rows with final paths.
- Manifest path auditing found all `67` populated `final_dds_path` entries under the mod's standard `gfx/` roots, with zero final-DDS paths under the temporary `assets/` tree and zero missing runtime files.
- The touched Clausewitz source scan found balanced braces and no unsupported comparison operators. These are static checks only and do not replace engine parsing.

## Remaining blockers

1. The 28 review-gated and 102 blocked source-manifest rows require clearance decisions or user-supplied permissions; generated likenesses cannot substitute for these rows.
2. The fresh focus inspection after the final coordinate adjustment, local engine-reference checks, and all required fresh-save route, failure/recovery, Northern, hidden-route, AI, GUI, and achievement scenarios remain not-run.
3. Runtime GUI interactions, event parsing/firing, AI choices, mission timers, and live asset loading remain unproven without the local engine/MCP validation path.
4. Optional audio remains queued and is not silently invented or treated as complete.

No completion claim is made while these gates remain open.
