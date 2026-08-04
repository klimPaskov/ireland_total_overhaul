# Ireland Focus Tree Static Source Validation — 2026-07-28

This record captures the current source-level checks after the Ireland focus-goal regeneration, the logistics, historic-site, patrol-craft, clearance-evidence, High Kingship branch-lifecycle, focus-AI, and focus-layout tranches. It is an audit record, not a completion claim. Live engine loading, reference comparison, source clearance, GUI behavior, AI playthroughs, and the required scenario programme remain open.

## Scope

The checked feature slug is `ireland_focus_tree`; the script namespace is `ireland`. The user requested that final goal sprites live under the mod's runtime `gfx` tree. Temporary source and audit material remains under `assets/ireland_focus_tree/` and is not referenced by runtime `.gfx` definitions.

Before source changes, the repository instructions, the required offline Paradox wiki pages, the relevant local vanilla documentation, and vanilla precedents were consulted. The source audit below is deliberately static because the user asked not to launch HOI4.

## Structural counts

| Surface | Current count | Evidence source |
| --- | ---: | --- |
| National focuses | 216 | `common/national_focus/ireland_focus_tree.txt` |
| Evolving decision categories | 13 | `common/decisions/categories/ireland_categories.txt` |
| Decision actions | 140 | `common/decisions/ireland_decisions.txt` |
| Mission families | 54 | `common/decisions/ireland_decisions.txt` |
| Historical event families | 18 | `events/ireland_events.txt` (`H01`–`H18`) |
| Political crisis families | 18 | `events/ireland_events.txt` (`P01`–`P18`) |
| Consequential flavour events | 236 | `events/ireland_flavour_events.txt` |
| Durable AI profiles | 30 | `common/ai_strategy/ireland_ai_strategy.txt` |
| Temporary AI overlays | 10 | `common/ai_strategy/ireland_ai_strategy.txt` |
| Foreign actor families | 12 | `common/scripted_effects/ireland_effects.txt` / `common/scripted_triggers/ireland_triggers.txt` |
| Foreign response classes | 12 | `common/scripted_effects/ireland_effects.txt` |
| Achievements | 32 | `common/achievements/ireland_achievements.txt` |

The event source contains 251 event IDs. Its family header accounts for the current historical, crisis, foreign-reaction, postwar, digest, and Five Provinces evidence-gate groups; the separate flavour file contains the 236 flavour-event blocks.

## Localisation coverage

The English localisation currently contains both a title and a `_desc` key for every focus ID: 432 expected keys, 0 missing. It also contains both keys for every decision action and mission ID: 388 expected keys, 0 missing.

Localisation source: `localisation/english/ireland_l_english.yml`.

This key-presence check does not prove UTF-8-with-BOM encoding, in-game rendering, readable dynamic requirements, or concealment behavior; those remain part of the engine/reference and scenario checks.

## Goal-icon runtime parity

The regenerated focus-goal package contains 216 fresh, consistent HOI4-style emblem sprites. The final DDS files are in:

`gfx/interface/goals/ireland/`

The runtime definitions are in `interface/ireland_icons.gfx` and reference 216 goal DDS files. The runtime directory contains 216 DDS files. The shine definitions in `interface/ireland_focus_shine.gfx` contain 216 focus-shine entries and 432 mask references.

The icon audit found no runtime texture path into `assets/ireland_focus_tree/`, no missing goal sprite, no bad dimension, no visible key-green matte, no opaque square corner, no edge contact, and no off-center emblem. The current regenerated contact sheet is:

`assets/ireland_focus_tree/icons/regenerated_goal_icons_vanilla_focus_emblems_fresh_2026-07-27_v4/contact_sheets/goal_icons_complete_contact_sheet.png`

The static audit cannot substitute for an in-game focus-tree render.

The bounded offline MCP focus inspection was rerun against the correct
workspace `mod_ireland_total_overhaul_65a6b5f140a7` and the current source path without
launching HOI4. It returned `FOCUS_INSPECTED` for tree
`ireland_focus_tree`: 216 focus blocks, 216 resolved titles, 197
connectors, zero Ireland-local crossings, zero node intersections, zero long
connectors, and zero Ireland-tree diagnostics. The matching render returned
`FOCUS_RENDERED`; its layout hash is
`1cfbb1f7ca61d5fe3683561dd504dd6ec82d606112dc036ea314f09e64339847` and its
render dimensions are 79504 by 5920. The MCP global validation flag remains
false because fourteen unrelated vanilla continuous-focus entries have
missing sprites or localisation. This is authored-tree reference evidence,
not a global validation pass; engine loading and live scenarios remain open.

The current AI reconciliation also records 31 focus-selection plans, 30
durable profiles, 10 temporary overlays, zero unresolved plan focus
references, and route-plan coverage for all 17 visible gateways. This remains
static source evidence; live focus selection and probability behavior are not
run.

## Static hygiene evidence

- Focus source brace delta: `0`.
- Unsupported `<=` or `>=` comparisons in the checked focus, decision, and
  event sources: `0`.
- English Ireland localisation starts with the UTF-8 BOM `EF BB BF`.
- Runtime goal DDS count: `216`.
- Focus goal texture registrations: `216`; focus-shine registrations: `216`.
- Focus title/description and action/mission key-presence sweeps: `0`
  missing keys.

The exact command outputs are reconciled in
`docs/plans/ireland_focus_tree/focus_layout_inspection_2026-07-28.md` and
`docs/plans/ireland_focus_tree/focus_ai_reconciliation_2026-07-28.md`.

## High Kingship branch lifecycle

The existing High Kingship focus/event surfaces now carry separate lawful-household, sacral-crown, and captured-crown markers. The captured-crown outcome applies source-specific consent, exposure, and settlement shocks, opens a foreign-reaction handoff, marks route failure, and is consumed by an explicit recovery bridge; the charter and capstone record branch-specific conclusion flags. AI and achievement-history gates exclude the captured-crown failure lane from the clean constitutional route. This is source-level wiring evidence only; event timing, hidden visibility, AI choice, engine parsing, and cleanup execution remain unverified.

## Boundary and cost checks

- The focus tree has no core, claim, state-owner, or transfer writer.
- The only `add_core_of` writer found in the current `common` and `events` source is the final-review runtime path at `common/scripted_effects/ireland_runtime.txt:5091–5094`, guarded by the strict integration-stage-five and final-review trigger in `common/scripted_triggers/ireland_triggers.txt:1177`.
- There are 420 direct command-power deductions in `common/decisions/ireland_decisions.txt`; the largest base action cost is 35. The current scarcity surcharge adds at most 10, giving a static upper bound of 45 and remaining below the requested maximum of 60.
- The three persistent route-spirit families are defined in `common/ideas/ireland_spirits.txt`.
- The National Settlement, Northern opening state, National Provision, Readiness, Neutrality Integrity, and related values remain implemented through the current scripted system; numeric parity alone is not treated as proof of all runtime transitions.

## Source clearance status

The current source manifest at `docs/plans/ireland_focus_tree/assets/source_manifest.json` records 169 manifest entries:

| Family | Complete (C3/C4) | Needs user review | Blocked |
| --- | ---: | ---: | ---: |
| Portraits | 10 | 28 | 22 |
| Symbols and documents | 4 | 0 | 36 |
| Event/news imagery | 26 | 0 | 43 |
| **Total** | **40** | **28** | **101** |

The five-state clearance model in the manifest remains active: C0 discovered, C1 provenance recorded, C2 restricted or review required, C3 cleared with conditions, and C4 unrestricted. No blocked historical source material was promoted into final runtime assets. The fresh generated goal-icon package is a separate generated-art package and does not clear the unresolved sourced portrait, symbol/document, or event/news entries.

## Deliberately unverified surfaces

The following are not claimed complete by this record:

- parser/load validation against the live HOI4 executable;
- local vanilla engine-reference comparisons and GUI layout rendering;
- fresh-1936, shared-opening, constitutional-route, convergence, postwar, Northern Ireland, hidden-content, AI, achievement, and cleanup scenarios;
- full per-ID audit of all 140 actions and 54 missions, including every dynamic cost, named objective, deadline, full/partial/failure/escalation branch, AI weight, and cleanup path;
- final source clearance for the 101 blocked manifest entries and user decisions for the 28 review entries;
- independent animation-frame validation and the full source-package, portrait, flag, icon, GUI, animation, and optional-audio budgets;
- live validation of the H/P/A boundary and all route-specific activation gates.

The active project status and source-of-truth documents must continue to report these as open before the overall goal can be marked complete.
