# Ireland implementation recheck - 2026-07-23

Feature slug: `ireland_focus_tree`

This is a current-worktree static recheck. It is not a gameplay completion claim. HOI4 was not launched, as requested, and live MCP/engine/scenario validation remains open.

## Changes verified in this recheck

- The goal-icon package was independently regenerated with built-in image generation. It was not extracted, recoloured, resized from, or otherwise reprocessed from the rejected v3/v4 packages.
- All 216 fresh source PNGs from fourteen generated 4x4 atlases, with the final atlas contributing eight cells, 216 processed 100x88 transparent PNGs, and 216 final DDS files are present. The runtime DDS files are promoted to the standard `gfx/interface/goals/slopx_ireland/` path.
- The fresh package QA reports 216 unique processed hashes, transparent corners, non-empty centered silhouettes, 216 readable DDS files at 100x88, and runtime hashes matching the staged package. The accepted contact sheet is `assets/ireland_focus_tree/icons/regenerated_goal_icons_hoi4_focus_emblems_fresh_2026-07-26_v2/contact_sheets/goal_icons_complete_contact_sheet.png`; the per-item manifest is `assets/ireland_focus_tree/icons/regenerated_goal_icons_hoi4_focus_emblems_fresh_2026-07-26_v2/manifest.md`.
- The seven independent animation packages were cross-checked at their intended frame counts: source and processed frame PNGs, PNG sheets, static PNG fallbacks, GIF previews, and contact sheets remain in temporary `assets/` staging, while all fourteen runtime DDS files (seven static fallbacks and seven frame sheets) exist under `gfx/interface/animated/slopx_ireland/` and are registered by `interface/slopx_ireland_animation_assets.gfx`. Live playback remains an engine gate.
- National Provision was separated from the Radical category. The decisions source now has all thirteen canonical top-level categories rather than twelve wrappers with a misplaced Provision block.
- AI score bands are now wired in the 194 action/mission AI blocks: 76 critical objectives use the `70` band; the remaining 118 candidates use the `35` normal and `15` maintenance predicates. All 140 actions also use shared `-8 * Action Burden` penalty constants.
- The centralized AI candidate ledger now maps live cause, repair, and dependency pressure across all thirteen categories, maps the thirty durable profiles to the six canonical stances, and applies the exact normal/crisis willingness floors `25/5`, `15/0`, `10/-10`, `5/-15`, `20/0`, and `0/-25`. All 194 authored AI blocks inherit the no-prioritized-pressure gate; live queue selection remains unrun.
- The foreign-reaction ledger now prepares separate actor-validity and actor-score state from the six positive inputs plus saturation and inability reductions; it admits only capability-valid chained RC nodes, retains observation-tier actors separately, and records expected actor/class counts instead of a fixed thirty-node total.
- The foreign resolver now keeps severe nodes (including mobilisation, sponsor collapse, occupation threat, and postwar admission) outside the digest and leaves the 14-day window active until those nodes are visible and resolved. Ordinary eligible nodes alone are closed into the actor-specific digest, and event triggers/dispatcher entries require their prepared availability flags.
- The foreign lifecycle cross-check now verifies 17 chained child gates use the preceding node's resolved flag, all 30 response events write a per-window resolved flag after either response, and open/cleanup clears the full 30-flag resolution set. Event 425 (postwar admission) is severe, is absent from ordinary/digest closure, and no longer carries an ordinary visible-cap dispatcher gate.
- FR05 sponsor collapse has a separate valid-but-not-counted collapse channel and score path, allowing the collapse reaction to resolve when the ordinary German actor is no longer valid without fabricating a normal actor.
- High Kingship and Five Provinces public openers no longer require hidden permission. Five Provinces' impossible branch remains behind the A boundary and now has dedicated evidence events 217 and 219: Stone of Divisions review, then standards/sites review, with disqualification and cleanup flags.
- The seven invalid Ireland AI research targets were replaced with documented vanilla technology IDs, and the thirty focus IDs previously absent from a focus-selection plan now occur in both the historical and reactive queues with route-safe weights.
- The dated Lemass peaceful-succession achievement flag now has a pre-1943 writer in the Lemass opener. The three staged hidden achievements remain statically hidden because the local achievement contract documents only static `hidden = yes`; no unsupported dynamic-visibility key was introduced.
- The clerical conclusion gate now accepts a completed guardianship focus directly as well as the producer constitution. The completion reward records separate clerical-guardianship and producer-state conclusion flags while retaining the shared conclusion-review hook.
- All 26 complete sourced event/news sprite slots are now referenced exactly once by live main or flavour event blocks. The integration flavour event retains its generated Northern-bridge picture so the source-backed censorship sprite is not double-consumed.

## Current structural inventory

- Focus source: 216 authored focus blocks and 216 runtime goal DDS files.
- Decisions and missions: 13 categories, 140 actions, and 54 mission families.
- Events: 251 main event nodes and 236 flavour nodes (487 country events in total, including the digest and the dedicated Five Provinces evidence gates).
- AI and achievements: 30 durable profiles, 10 temporary overlays, 31 focus-selection plans, and 32 achievements.
- Localisation: 3,500 unique Ireland keys in the current localisation audit; all touched localisation files remain UTF-8 BOM encoded.
- Native PP costs remain on all 140 actions. Named-ledger surcharges and dynamic cost previews remain wired; the maximum command-power cost remains below 60.
- A current decision audit records 37 of 140 actions with explicit equipment, manpower, fuel, or convoy inputs, including the newly wired standardisation, plebiscite-security, policing, labour-settlement, and merchant-vessel commitments. The remaining actions still need canonical cost-map review for leverage, tied units, civilian-factory, train, or other non-stockpile burdens; the structural action count is not being used to claim economic completeness.
- Seven named projects now reserve native civilian-factory capacity for their actual work periods: Protected Workshops (1 for 180 days), Named Rail Corridor (1 for 150 days), Strategic Depot (1 for 120 days), Western Regional Portfolio (1 for 240 days), Infantry Standardisation (1 for 120 days), Rifles and Support Equipment (2 for 180 days), and National Reconstruction (3 for 365 days). The decision source contains twelve total factory reservations, including the five previously audited projects, with matching availability gates, timed modifiers, and player-facing requirement text.
- All twenty physical-input mission cancellation paths now call the shared capped refund helper. Each cancellation returns no more than the authored 70-percent floor of recoverable committed inputs, with per-action anti-duplication flags and cleanup-safe state reset; consumed work, losses, and damage are not restored.
- The operational cost rows now include the mapped fuel/train burdens for Command District Exercise (250 Fuel), Essential Cargo Reroute (2 Trains and 200 Fuel), Motorised Strategic Route (300 Fuel), and the Coercive Northern Campaign plan (5 Trains and 500 Fuel), with matching availability gates, charges, localisation, and cancellation refunds.
- Mission caps remain 8 normal, 10 during Emergency or war, and conditional 12 during simultaneous national emergency and Northern occupation.

## Invariants and route boundaries

- Opening values remain National Settlement `+25` with momentum `-1`, Social Consent `55`, Dail `153` formal / `152` routine, Provision `55/25/40/30` displayed as `38`, Readiness `25/8/20/12/5/5/30` displayed as `15`, Neutrality Integrity `72`, and Northern `U5 N40 L30 B10 S45 I10`.
- Northern claims, control, occupation, settlement, integration, and cores remain separate. The only Northern core effect is in the final review helper and is gated by integration stage 5 and the final review proof set. No focus grants a Northern core or free territory.
- The strict neutrality prerequisite was repaired so the armed-neutrality focus is no longer an unconditional extra branch.
- The convergence capstone now records both its convergence profile and the canonical absurd-route state.
- The convergence and hidden-route synchronization keeps the public High Kingship/Five Provinces proofs separate from the hidden Otherworld permission and game-rule proof.
- The three scripted GUI surfaces received offline fixes for sealed-evidence disclosure, Northern selection/review ownership, label-state reachability, dirty invalidation, and decorative icon placement/transparency. Live click and rendering behavior is not proven.

## Asset clearance state

The source manifest still contains 169 rows: 39 complete, 28 needing user review, and 102 blocked.

- Portraits: 9 complete, 28 review, 23 blocked.
- Symbol/document packages: 4 complete, 36 blocked.
- Sourced event/news rows: 26 complete and 43 blocked.
- The 26 complete sourced event/news rows are registered under the standard `gfx/event_pictures/ireland/` tree and each has one live event consumer; the 43 blocked rows remain unresolved.
- Current runtime inventory is 52 Ireland leader DDS files, 78 Ireland event-picture DDS files, 216 focus DDS files, and 96 achievement variant DDS files. These inventories do not close the source-clearance gate or prove the exact 60-portrait / 120-event-image allocation.
- Five C4-complete historical route portraits are registered but remain unused pending a deliberate source/route activation decision; they do not count as the missing 60-portrait package.

Generated likenesses and invented historical source substitutes were not used to close the blocked or review-gated rows.

## Static validation

- Touched Clausewitz files have balanced braces and quotes; the unsupported `<=` / `>=` operators were not found.
- The decision parser reports 13 top-level categories, 194 action/mission blocks, 140 requirement wrappers, and 140 dynamic-cost text hooks.
- The fresh goal-icon verifier reports a complete 216-row regenerated package with no reuse or visual contamination findings.
- The animation package audit reports 7/7 packages complete, with 54 total source frames and 54 processed frames matching the manifest, all staging review outputs present, and 14/14 runtime DDS references resolving under the standard `gfx` tree.
- The foreign-reaction static cross-check maps all 30 response IDs to one prepared availability writer, one event trigger, and one dispatcher gate; the digest popup no longer writes all twelve actor flags unconditionally.
- The sourced event-picture cross-check reports 26 registered complete slots, 26 unique live references, and no duplicate live source assignment.
- The foreign-window lifecycle cross-check maps two per-window response writers (accept/refuse) for all 30 response events and full 30-flag clears on open and cleanup; the resolver reads no persistent response flag, so earlier windows cannot replay into later ledgers while follow-up history remains durable.
- The main event source contains 251 balanced country-event blocks; the separate flavour source contains 236 balanced country-event blocks, each with player-facing ledger, mission, route, relationship, or persistent-memory consequences.
- Focus, event, achievement, localisation, GUI-link, texture-path, mission-contract, and AI-count checks remain structurally useful but are not engine parsing.

## Offline MCP reference evidence

- The bounded Ireland focus inspection resolved 216 focus nodes and 194 connectors with zero Ireland-local crossings, through-node intersections, or long connectors. The authored SVG render completed, and the raster review completed at a reduced review scale after the full-size raster exceeded the tool's fixed 16,384-pixel ceiling. The tool still reports fourteen unrelated vanilla global diagnostics; they are not Ireland-local failures.
- Read-only inspection of `slopx_ireland_conditions_panel_window`, `slopx_ireland_northern_settlement_ledger_window`, and `slopx_ireland_concealed_evidence_ledger_window` completed for the `ireland_audit` scenario. All three windows report complete source models, and render requests completed at 1920x1080 and 1280x720 across normal, warning, locked, and long-text states.
- The GUI inspector reports 73 shared source-graph collision diagnostics because the 140 named decision actions intentionally reuse 70 action textures. It also reports the mutually exclusive animation/fallback and status-overlay placements as visible overlaps. These are recorded as tool diagnostics for live review, not silently removed by duplicating the controlled-reuse texture budget.

## Remaining blockers

1. The 28 review-gated and 102 blocked source-manifest rows still require clearance decisions or user-supplied permissions.
2. The exact runtime source-package budget is not closed while the clearance rows and portrait/event inventories remain unresolved.
3. The decision/mission economy still needs action-specific material layers for the remaining canonical fuel, train, truck, convoy, aircraft, ship, leverage, and tied-unit cases; the seven named factory reservations above are wired, but the generic PP/CP scarcity layer is not a complete substitute for the remaining map rows.
4. Main event and action prose remains too templated in places for the final distinct-route text gate, even though the flavour namespace has substantive coverage.
5. Staged achievement visibility has no documented supported dynamic engine contract; A-22/A-27/A-28 remain statically hidden with their reveal flags tracked in `happened` until an engine-supported visibility solution is established.
6. Fresh engine-reference checks, live event firing, decision and mission timers, AI queue behavior, GUI interaction, asset loading, focus rendering, and the required fresh-save route/failure/recovery/Northern/hidden-route/AI/achievement scenarios remain not-run.
7. Live profile transitions, queue ordering, and expected-utility behavior remain unrun even though the candidate ledger and six threshold pairs now have source evidence.
8. Optional audio remains queued and is not silently invented or treated as complete.

No completion claim is made while these gates remain open.
