# National Situation Ledger focus inlay audit

Date: 2026-08-15
Scope: focus-tree inlay declaration, inlay window definition, inlay GUI, localisation, and inlay assets
Mode: read-only audit; no gameplay, focus, layout, GUI, asset, or thumbnail source was patched; no commit created

## Executive result

The inlay is structurally wired and its requested coordinates are clear of all 256 focus anchors. The current focus source differs from `HEAD` only by the seven-line `inlay_window` declaration at `common/national_focus/ireland_focus_tree.txt:51-57`; focus blocks, prerequisites, completion rewards, focus icons, connectors, and AI weights were not changed by this feature.

The remaining closure risk is evidence, not an identified source collision: the focus MCP renderer/rasterizer does not composite `focus_inlay_windows` into the focus-tree raster. The exact coordinate scan proves anchor clearance, but a combined focus-tree + inlay raster or equivalent game-view capture is still required to prove decoded icon/connector bounding-box clearance and initial-camera usability. The standalone GUI renderer also has no value-driven Ireland scenario fixture; its complete 14-state matrix renders six dynamic values unresolved.

## Files and identifiers audited

| Surface | Evidence |
| --- | --- |
| Focus declaration | `common/national_focus/ireland_focus_tree.txt:51-57`; `id = ireland_national_situation_inlay`, `position = { x = -600 y = 10 }` |
| Inlay definition | `common/focus_inlay_windows/ireland_national_situation_inlay.txt:2-58`; `internal = yes`, original-tag/init visibility, six scripted images, two scripted buttons |
| Inlay GUI | `interface/ireland_national_situation_inlay.gui:4-29`; 460x248 container, six status/value pairs, two action buttons |
| GFX registration | `interface/ireland_gui_assets.gfx:5,10-13,63-65`; background, four shared status sprites, and shared action button |
| Dynamic inlay localisation | `common/scripted_localisation/ireland_localisation.txt:960-982`; Northern and Culture public-state phrases |
| English labels/tooltips | `localisation/english/ireland_l_english.yml:6204-6242`; labels, status text, purpose tooltips, refresh and Parliament action text |
| Asset documentation | `docs/assets/ireland_mechanics_hub/manifest.md:15-19`, `gfx_handoff.md:3-11` |
| Behaviour contracts | `common/scripted_triggers/ireland_mechanics_hub.txt:9-51,335-451,564-599`; visibility/status/open-state and canonical action gates |

The concurrent worktree still has `thumbnail.png` modified. This audit did not read/write it beyond observing its status and did not alter it.

## Route coverage table

The focus inlay is an information/action projection. It introduces no focus route, branch, prerequisite, reward, connector, or AI plan.

| Inlay family | Current implementation | Route/content result |
| --- | --- | --- |
| Settlement / State | `ireland_focus_inlay_state_status` selects ready/warning/critical/locked through the existing `ireland_mechanics_hub_state_*` triggers; `ireland_focus_inlay_state` and its tooltip expose settlement purpose. | Present; points to the existing National Settlement and Parliament systems; no route change. |
| Provision | `ireland_focus_inlay_provision_status` mirrors `ireland_mechanics_hub_provision_*`; value and tooltip use the existing derived Provision display. | Present; no capacity grant, focus reward, or new bottleneck. |
| Readiness | `ireland_focus_inlay_readiness_status` mirrors `ireland_mechanics_hub_readiness_*`; tooltip describes the seven operational components and existing gate. | Present; no military reward or threshold change. |
| Foreign / Neutrality | The compact contract deliberately labels this family `Neutrality`; `ireland_focus_inlay_neutrality_status` mirrors the existing neutrality triggers and tooltip names foreign access, incident credibility, and security conclusions. | Present as the specified compact Foreign summary; no leverage, agreement, or diplomatic route change. |
| National Question / Northern | `ireland_focus_inlay_northern_status` uses the existing six-factor status triggers. `GetIrelandMechanicsHubInlayNorthern` returns locked, failure, critical, ready, warning, or stage phrases without exposing a concealed row. | Present; no Northern reveal, settlement, occupation, or integration gate is bypassed. Full-ledger row helpers retain exact progressive predicates at `ireland_mechanics_hub.txt:335-413`. |
| Culture / Evidence | `ireland_focus_inlay_culture_status` uses existing Culture triggers. `GetIrelandMechanicsHubInlayCulture` distinguishes public capacity, sealed evidence, revealed credible evidence, and public disqualifier states. | Present; concealed evidence is not exposed by the inlay; no Evidence review or cultural reward is duplicated. |
| Actions | Refresh button is available only through `ireland_mechanics_hub_open`; State action is available only through `ireland_next_state_action_available` and calls the canonical Parliament executor. | Present; no-op archive controls are closed; no cost, reward, progress, or hidden reveal is added. |

## Exact corridor proof

The accepted addendum defines the focus-tree scale as 96 horizontal pixels per focus `x` unit and 130 vertical pixels per focus `y` unit. The inlay declaration is `x = -600`, `y = 10`, and the GUI container is `width = 460`, `height = 248`, giving the half-open footprint `x[-600,-140), y[10,258)`.

Read-only parser results over the current focus source:

| Check | Result |
| --- | ---: |
| Resolved focus anchors scanned | 256 |
| Anchors inside `x[-600,-140), y[10,258)` | 0 |
| Focus rows reaching the corridor horizontally near the top | Cultural lane `ireland_cultural_survey = (-768,0)` and `ireland_archival_record = (-768,130)`; economic lane `ireland_economic_war_review = (0,0)` and `ireland_rural_price_board = (0,130)` |
| First row-2 anchors | `ireland_serious_cultural_stewardship = (-768,260)` and `ireland_provision_baseline = (0,260)`; both are outside horizontally and row 2 starts 2 px below the inlay footprint |
| Horizontal edge clearance to nearest top/row-1 lanes | 168 px from the left edge to `x=-768`; 140 px from the right edge to `x=0` |

The scan includes all 256 focus coordinates, not only the visible opening focuses. The inlay does not cover the initial focus target (`ireland_state_still_defined` at `(-1152,0)`) or the documented cultural/economic lanes. The current focus inspect additionally reports no connector crossings, node intersections, long connectors, or excessive connector spans.

This is an anchor/corridor proof. The focus MCP raster output is a focus-only image and does not draw the separate inlay window. Therefore `nodeIntersectionCount = 0` must not be interpreted as a combined inlay/node bounding-box proof; parent closure still needs one combined focus-view artifact or an equivalent manually overlaid review.

## No focus gameplay/reward/connector changes

The only current source diff in `common/national_focus/ireland_focus_tree.txt` is:

```text
inlay_window = {
    id = ireland_national_situation_inlay
    position = { x = -600 y = 10 }
}
```

Current versus `HEAD` source counts are identical: 256 focus blocks, 222 prerequisite blocks, and 256 completion-reward blocks. No focus identifier was added, removed, renamed, or edited by this feature. No focus icon, `available`, `allow_branch`, `bypass`, `mutually_exclusive`, `prerequisite`, `completion_reward`, `ai_will_do`, shortcut, or connector declaration is in the diff. No focus filter or route lock was changed.

The current inspect layout hash is `dee813d687f55041d88e9456d9ce5d57ee2d5971763bf373b11bf55102b00c92`, matching the pre-inlay tree baseline recorded in `docs/plans/ireland_mechanics_hub/subagent_handoffs/improvement_loop_handoff_2026-08-15.md`. It reports 256 focuses and 234 connectors, with 0 crossings, 0 node intersections, 0 long connectors, and 0 too-close connectors. The inlay declaration is outside focus blocks and cannot alter these gameplay structures.

## Icon and asset coverage

| Asset role | Source registration / consumer | Audit result |
| --- | --- | --- |
| Inlay panel background | `GFX_ireland_mechanics_hub_inlay_background` → `gfx/interface/ireland/gui/conditions/focus_inlay_background.dds`; consumed at GUI line 10 | Wired. Final DDS is 460x248 RGBA, opaque alpha as intended for the static panel. Source/processed PNGs and manifest are present under `docs/assets/ireland_mechanics_hub/`. |
| Ready, warning, critical, locked statuses | `GFX_ireland_gui_status_ready/warning/critical/locked` → `gfx/interface/ireland/gui/shared/status_*.dds`; six scripted-image groups at inlay lines 11-47 | Wired. Each shared status DDS is 32x32 RGBA. The `locked` fallback is last in each scripted image group. |
| Refresh and Parliament action button | `GFX_ireland_gui_parliament_step_button` → `gfx/interface/ireland/gui/parliament/parliament_step_button.dds`; GUI lines 28-29 | Wired. Existing 204x32 button asset is reused; no new gameplay or icon family. |
| Dynamic Northern/Culture text | `GetIrelandMechanicsHubInlayNorthern` and `GetIrelandMechanicsHubInlayCulture`; GUI lines 25-26 | Wired to public-state localisation; no hidden Northern/Evidence value is required by the source. |
| Full-ledger selected markers | `GFX_ireland_mechanics_hub_tab_selected`, `GFX_ireland_mechanics_hub_row_selected` | Present for the separate decision GUI; not used by the focus inlay and not a missing inlay asset. |

No inlay missing-sprite or missing-DDS diagnostic was produced by the GUI graph/render checks. The offline renderer reports partial appearance for both button text sprites because it does not execute vanilla `gfx/FX/buttonstate.lua`; this is an offline representation limit, not a missing source registration.

## Localisation and reward mismatch list

No inlay localisation key is missing in the current English surface. The GUI labels and tooltips resolve to `ireland_l_english.yml:6204-6242`; the two scripted public-state localisers resolve to keys at `ireland_localisation.txt:960-982`. Refresh wording is bounded to displayed/public report recomputation and explicitly says it grants no value, reward, or progress (`ireland_l_english.yml:6206`). Archived wording explains that values remain readable while refresh is unavailable (`:6207`).

No focus reward mismatch exists because no focus reward was changed and the inlay has no reward block. The two buttons call existing helpers only; their tooltips identify canonical Parliament/ledger behaviour rather than presenting a duplicated reward.

The generic GUI render does report six unresolved dynamic expressions (`ireland_national_settlement`, `ireland_provision_display`, `ireland_readiness_display`, `ireland_neutrality_integrity`, `GetIrelandMechanicsHubInlayNorthern`, and `GetIrelandMechanicsHubInlayCulture`). These are unresolved because the supplied `ireland_focus_inlay_operational` scenario has no state variables/flags, not because the localisation keys are absent. A value-driven scenario fixture is still needed.

## AI behavior gaps

None identified for this feature. The focus inlay is `internal = yes` and has no AI click surface in the vanilla inlay schema. The specification explicitly keeps the inlay and dashboard human-facing; native focus plans, decisions, missions, and canonical executors remain the AI surface. No AI weight, focus filter, route-aware strategy, or AI reward path was added or changed.

## Focus MCP metrics and artifacts

All focus tools used the current Ireland tree with horizontal spacing 96, vertical spacing 130, review scale 1, and padding 60 where applicable. Workspace: `mod_ireland_total_overhaul_aaca88216c92`.

### `hoi4.focus_inspect`

- `focusCount = 256`, `continuousFocusCount = 14`.
- Bounds `x=-44..31`, `y=0..26` (76 columns, 27 rows).
- `connectorCount = 234`.
- `crossingCount = 0`, `nodeIntersectionCount = 0`, `longConnectorCount = 0`.
- Total/max horizontal span `212/4`; vertical span `245/4`; Manhattan span `457/8`.
- Layout hash: `dee813d687f55041d88e9456d9ce5d57ee2d5971763bf373b11bf55102b00c92`.
- Validation passed for blocking diagnostics. The 251 diagnostics are authored same-row spacing warnings in the existing tree, not inlay collisions; no source change was made to them.

Artifact: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/db2e555ce4ac7a9d3ef1657ddf8bf4068c1de3b8ec40deed3fd3574c9be7b082/ca8a40ea0ab34f2e00920a6b3a0a5cb132b028a6c9e8adf830f5d7955f30baa5/focus-inspect.90beeec44304c287.json`

### `hoi4.focus_render`

- Output 7464x3576 at the requested 96x130 layout scale; layout hash unchanged.
- Validation passed with no blocking diagnostics.
- Eight isolated-focus warnings and the missing vanilla `continuous_restrict_freedom_desc` localisation were reported; all are unrelated to the inlay and pre-existing focus-tree/vanilla content warnings.

Artifacts: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/7f0827cca38af456c79438034077703e5eeeaae3e12d1c212f6891f31ebfc46f/c669106786a2b209f3c32cfc3044679ac4d6671f7a754c57159496df85c2811c/ireland_focus_tree.focus.html` and `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/b1c23339e67d9cfe388cefa04b147b08bda4a239489c8acde9541604ca06bb9/aeea37dd00cbb458fc8c78ac9cffbd7b72bef42a9a46faa970f90d6db6d6df83/ireland_focus_tree.focus.svg`

### `hoi4.focus_raster`

- Output 7464x3576 with the same layout hash and focus metrics.
- PNG output was produced, but validation was false because nine vanilla continuous-focus DDS textures contain truncated pixel data: `continuous_naval_production`, `continuous_air_production`, `continuous_non_factory_construct`, `continuous_reduce_training_time`, `continuous_suppression`, `continuous_repair`, `continuous_tech_share`, `continuous_boost_freedom`, and `continuous_restrict_freedom`.
- The raster also repeats the eight unrelated isolated-focus warnings and the missing vanilla continuous-focus localisation warning.
- This raster does not include the separate inlay window, so it cannot close the combined placement proof by itself.

Artifact: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/518a6da67aebefe95174c2f4861ebe2c0e45054f81191cfdaf81eb8bb7a9c1f5/3b0544b990f655d8792ed6e616e955695ff7e93dffe7d42da32d0f7d7efa7d65/ireland_focus_tree.focus.png`

## GUI inspect/render evidence

`hoi4.gui_inspect` parsed the inlay source graph with no visible-overlap diagnostic. It reported 17 inspected elements, 45600 nodes, 103026 edges, 23392 elements, 17771 sprites, 200 fonts, and 21 scripted GUIs. Artifact: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/16cbc2c0b1bc0a26d28ab6f7707252315b752b8f32751b8ad7b3ee4b549bcd06/d8720859e1481a3c66899ade2181b51b54a8f5b236fb6041c8df4ffa972e64aa/gui-inspect.7f7b1126f87a3ebc.json`.

The complete `hoi4.gui_render` matrix used `ireland_focus_inlay_operational`, both 1920x1080 and 2560x1440 resolutions, and all 14 named states: normal, hover, selected, locked, disabled, warning, active, completed, empty-list, full-list, minimum-value, maximum-value, long-text, and missing-localisation. It produced 27 artifacts, including full, cropped, annotated, click-region, source-map, state-matrix, resolution-scale, and comparison outputs. Source graph and visible-overlap checks passed; the overall validation remains false only because the generic scenario leaves the six dynamic values unresolved and the offline renderer approximates/ignores some engine-only presentation.

Useful artifacts from the complete matrix:

- Full inlay PNG: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/b6394b6362f80e2f836199247362f46576893c2167a1d7ae59a3c6c5849c76d9/ee7fb311a61fa93be1f102a387735d9cd84cd99ccf9248d548165fbfe400050d/ireland_national_situation_inlay_window-full.png`
- State matrix PNG: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/677026bebecae394852f2821ca204abbd237e7e63491831ceb196081422e1ce2/8ed5f791fe445e714afedbc30cd34731e367a1cb2129cdbf43b30bd5d7130dc0/ireland_national_situation_inlay_window-state-matrix.png`
- Resolution-scale PNG: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/791c72a1f4a83d8de57caf893371cd25d419276f392026aa32260689f958c97e/153949d91f887ce4bdf5964ed83afffb7c6dd0e108b7111183e2b4de24027165/ireland_national_situation_inlay_window-resolution-scale.png`
- Validation JSON: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/1c60d3ba98e1e9971d6bc50801311c1c63eec2ffd74b7820d0a2f25f6d27b54a/759c4f4668316846ab778987cb6baf7ecaec872aac10799fad17c80973bf63f4/ireland_national_situation_inlay_window-validation.json`

## Missing/simplified content and remaining route risks

No requested gameplay or route content is missing from this inlay scope. No fallback art, placeholder reward, duplicate executor, new currency, new mechanic family, or AI shortcut was introduced.

The following evidence limits remain:

1. The focus inspect/render/raster pipeline cannot show the inlay composited with all focus nodes, connectors, shortcuts, and the initial camera. The anchor scan is exact, but combined visual placement remains unclosed.
2. The GUI source graph is valid, but no runnable value/flag scenario manifest was present. The complete state matrix therefore tests element/state coverage rather than proving mutually exclusive status outputs, archived disabled controls, Northern partial/midroute reveal, or sealed/revealed Evidence behaviour with live values.
3. Focus raster validation is blocked by the nine unrelated vanilla continuous-focus DDS truncation diagnostics listed above. This is not an Ireland inlay asset failure.
4. Focus inspect retains existing same-row spacing diagnostics and focus render retains isolated-focus/vanilla continuous-localisation warnings. They are outside this inlay-only audit and were not “fixed” by moving gameplay nodes.

## High-priority follow-up

1. Generate or manually overlay a combined full-tree focus view at the accepted `(-600,10)` placement, including connectors, shortcuts, initial camera, and decoded focus icons; retain the exact 256-anchor scan as supporting evidence.
2. Add/use value-driven scenario fixtures for the named corrective-addendum cases (opening locked, Provision/Readiness bottleneck, Foreign imbalance, Northern partial and midroute, Evidence sealed/revealed, archived, long text, operational/archived inlay) and rerender both target resolutions. Confirm one mutually exclusive status sprite per family and disabled archived controls.
3. Rerun raster validation in an environment with intact vanilla continuous-focus textures, or record those engine asset errors as an accepted external validation limitation.

No implementation patch or plan was written because the requested task was read-only. This file is the handoff path for parent review:
`docs/plans/ireland_mechanics_hub/subagent_handoffs/final_focus_inlay_audit_2026-08-15.md`

## Required reference surfaces consulted

Before auditing, I read `AGENTS.md`, the focus-tree, feature-assets, and subagent skills, the specified Ireland mechanics-hub documents and corrective addendum, the offline Paradox wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, events, decisions, ideas, AI, interface, scripted GUI, and national focuses, plus the relevant vanilla documentation and the vanilla focus-inlay precedent (`common/focus_inlay_windows/documentation.md` and Germany's inner-circle inlay). No web wiki source was used.
