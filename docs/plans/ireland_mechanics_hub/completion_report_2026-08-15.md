# Ireland Cabinet Briefing and focus-presentation completion report

Date: 2026-08-15
Feature slug: `ireland_mechanics_hub`
Status: audited complete

## Outcome

The rejected six-tab National Situation Ledger has been replaced by a compact Cabinet Briefing in the decision view and a matching informational inlay in the focus view. The surface presents four ordinary strategic conditions:

- Government;
- National Supply;
- Defence;
- National Question.

Only National Supply and Defence expose numbers, each as one canonical aggregate out of 100. Government and the National Question use short qualitative states. There are no tabs, row selectors, internal record lists, diagnostic questions, manual refresh controls, overlaid status seals, or duplicated mechanic values.

The decision-view briefing has one optional `Advance Programme` button. It is visible and clickable only when the next canonical Parliament step is currently legal, and delegates to the guarded Dáil, Seanad, confidence, or budget executor. The focus inlay is informational only, so it cannot show a grey or dead action.

## Natural gameplay contract

- The briefing reads existing authoritative variables and flags; it does not create a new progression layer.
- The four card tooltips explain the practical policy consequence and direct the player to the existing decision category that owns detailed action.
- The one contextual action cannot bypass Political Power costs, stage order, settlement gates, or canonical executor checks.
- When no action is legal, the button is absent rather than grey.
- Route archival leaves a readable historical summary and exposes no dead controls.
- AI continues to use native focuses, decisions, missions, and shared executors; it never clicks the GUI.

## Presentation cleanup

The full panel and inlay both use a 460 by 248 paper surface, four distinct category emblems, one line of state text per card, and one short cabinet assessment. Redundant ready/warning/critical/locked badge overlays were removed. The focus inlay remains at `x = -600, y = 10` in the empty upper corridor and contains no interactive button.

The exceptionally long focus-effect disclosure was also removed. `ireland_refresh_exceptional_route_state` is now a public hidden wrapper around `ireland_refresh_exceptional_route_state_internal`, so internal idea replacement, clamp, counter, and cosmetic synchronization no longer floods the player tooltip. Every focus retains its authored concise reward tooltip.

## Focus-tree correction

The foreign-policy, Northern, Five Provinces, and Otherworld bands were reflowed into compact local trees. Previously detached available-only conclusions now have visible prerequisites that duplicate their existing availability requirements. The Five Provinces and Otherworld capstones use one visible OR prerequisite block over their real terminal outcomes instead of a misleading long connector from an early setup focus.

Current focus inspection revision `638d0ab4e98afd31` reports:

- 256 focuses and 262 connectors;
- exactly three true opening roots;
- all 28 authored `allow_branch` blocks visible with `always = yes`;
- zero connector crossings;
- zero connectors through unrelated focuses;
- zero long connectors;
- zero cramped same-row pairs, with minimum spacing two columns;
- zero isolated-focus diagnostics.

Strict Army, Navy, and Air experience filter parity is exact. Territorial and Northern-reclamation focuses use `FOCUS_FILTER_ANNEXATION`, including the Northern ledger, Northern policy sequence, national-question dossier, five reunification methods and resolutions, Atlantic expansion choices, enforcement, and postwar settlement sequence.

## Supplied error cleanup

The supplied Ireland-owned error signatures were checked against current source. The invalid `is_at_war` trigger, malformed dynamic Fianna cost tokens, malformed postwar factory-use constant token, invalid `localisation_key` spelling, nonreciprocal focus exclusions, and malformed building-slot form are absent. The three `KOM_democratic` flags are valid uncompressed 32-bit true-colour TGA files at the required sizes. The supplied IRQ, GER, and CHL lines are base-game sources outside this Ireland mod and were not overridden.

## Files and systems

- Source design: `docs/specs/ireland_mechanics_hub/`
- Accepted correction: `docs/plans/ireland_mechanics_hub/improvement_loop/natural_cabinet_briefing_correction_2026-08-15.md`
- Maintainer/player guide: `docs/ireland_national_situation_ledger.md`
- Decision category: `common/decisions/categories/ireland_categories.txt`
- Scripted GUI: `common/scripted_guis/ireland_scripted_guis.txt`
- Focus inlay declaration: `common/focus_inlay_windows/ireland_national_situation_inlay.txt`
- Triggers/effects: `common/scripted_triggers/ireland_mechanics_hub.txt` and `common/scripted_effects/ireland_mechanics_hub.txt`
- Dynamic text: `common/scripted_localisation/ireland_localisation.txt`
- Layouts: `interface/ireland_national_situation.gui` and `interface/ireland_national_situation_inlay.gui`
- Focus source: `common/national_focus/ireland_focus_tree.txt`
- Hidden exceptional refresh: `common/scripted_effects/ireland_exceptional_routes.txt`
- English text: `localisation/english/ireland_l_english.yml`

## Meaningful validation evidence

- Focus inspect: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/0f9c6eaa50630511890205c6c21e52729f3fca2c7012ef274bf738ac7f9d407a/892766070ec309c1746fb02a3ec04ced7066e9645c94de1d62e2cca582f80d0b/focus-inspect.638d0ab4e98afd31f5f4b3604991d1daae276ba639385e9a2c1748f6c74eb6a8.json`
- Focus render: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/a76f351b1892d1d1293ac79059fa3e26381ba9299f7986c6295a5f4c42b368a4/90a6fdc9c807747674e514f4a780d5cc04e5a1c94568afc99fab5174a00aead8/ireland_focus_tree.focus.svg`
- Decision-view inspect: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/2c802d972eb3b2d371c4ebc6141432ce6baea63f649506c5a329472def08c699/bd96e3ee2fe9ecf384c71ec726adccbb6c07cfa7747908cf2e4648444782a37f/gui-inspect.2811d298d429cf40.json`
- Decision-view render: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/8191898455a6580379351eb74ab6999851c49454071e522e1d228231b3900239/69076433219f9710888abf50fe4af574c6848ba23abc2adb86293b48f81f9878/ireland_national_situation_window-full.svg`
- Focus-inlay inspect: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/24e9c8adfd2ec18f449dec242db108b9e3aa01523dc6e597f5d4675c1718620d/64d84bf365dcb643b065dc276ed0b263b4405090f4965912d8c871ae2a0772cc/gui-inspect.c01f45039e081dc5.json`
- Focus-inlay render: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/c46930f95b8ecef27c8ae312dd6177b6b08aac971604c091b64bba0306001dd6/7686524cae7aef80303b4287a5efcca87e4aa6de80588ac9cb0a170c1d13125c/ireland_national_situation_inlay_window-full.svg`

Both GUI source graphs link without blockers and report no visible-overlap defects. The offline renderer cannot measure `context_aware_text`, execute `defined_text`, or execute engine text-sprite/button-state code; those source bindings and localisation branches are audited directly.

## Simplifications, omissions, and blockers

No fallback art, duplicate mechanic, accepted gap, omission, or Cabinet Briefing simplification remains. Independent closure is recorded in:

- `docs/plans/ireland_focus_tree/subagent_handoffs/final_focus_layout_filter_audit_2026-08-15.md`;
- `docs/plans/ireland_mechanics_hub/subagent_handoffs/final_compact_localisation_audit_2026-08-15.md`;
- `docs/plans/ireland_mechanics_hub/subagent_handoffs/final_compact_feature_completion_audit_2026-08-15.md`;
- `docs/plans/ireland_country_package/subagent_handoffs/supplied_error_cleanup_2026-08-15.md`.
