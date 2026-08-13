# Parliament GUI and Starting Decision Audit - 2026-08-13

## Scope and result

Read-only audit of the Parliament scripted-GUI surface and the `ireland_settlement_government` decision category following the reported opening-screen state: the lower panel showed `Legislative powers` and four seals, but no action buttons or labels; the category offered no human-visible decision at campaign start.

No gameplay, GUI, localisation, asset, or scripted files were changed. This handoff is the sole subagent file written for the audit.

The source renders all four controls when `ireland_settlement_open` is true, so the checked-in source does **not** reproduce a state in which the powers panel and its four seals are visible but the controls are hidden. There is nevertheless a small, source-backed hardening change that removes the only redundant element-level visibility path and preserves all interaction semantics.

## Evidence reviewed

### Project files

- `interface/ireland_parliament_scripted_gui.gui`
- `interface/ireland_gui_assets.gfx`
- `common/scripted_guis/ireland_scripted_guis.txt`
- `common/scripted_triggers/ireland_parliament.txt`
- `common/scripted_effects/ireland_parliament.txt`
- `common/decisions/categories/ireland_categories.txt`
- `common/decisions/ireland_decisions.txt`
- `common/script_constants/ireland_constants.txt`
- `common/scripted_effects/ireland_effects.txt`
- `common/national_focus/ireland_focus_tree.txt`
- `localisation/english/ireland_l_english.yml`
- `docs/assets/ireland_parliament_panel/manifest.md`
- Prior handoffs, especially `docs/plans/ireland_focus_tree/subagent_handoffs/parliament_start_visibility_2026-08-09.md` and `parliament_interaction_audit_2026-08-11.md`.

### Required implementation references

Reviewed the offline Paradox wiki pages required by `AGENTS.md`, including Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Interface modding, and Scripted GUI modding.

The relevant scripted-GUI rule is that an element is visible by default unless its `<element>_visible` scripted trigger says otherwise; `_click_enabled` controls interaction separately. Decision Modding documents `visible_when_empty = yes` and decision-category scripted GUIs as valid informational surfaces.

Reviewed vanilla `common/scripted_guis/_documentation.md`, `common/scripted_guis/USA_congress_scripted_gui.txt`, `interface/usa_congress_scripted_gui.gui`, `interface/ast_right_vs_left_campaign_scripted_gui.gui`, its GFX precedent, and the relevant font definitions in `interface/core.gfx`. Vanilla confirms the decision-category GUI context and the `buttonType`/`quadTextureSprite`/`buttonFont`/`buttonText` pattern. `hoi_16mbs` is white; `vic_18_black` is black.

### Fresh GUI-tool evidence

Fresh inspection and render used source revision:

`616f0bf6bd9b1670997fede0f3586a113ce2cc29249e23d9077cc819f3f12fd3`

- Baseline inspect artifact: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/d7a08f03dad020f34e05e02cc67466c01720dc150f389596bbb58b6bc1067ef3/449bed115400a6a2d96e5ff183fad70a363fc94c00911338384f3be3c26ebb8f/gui-inspect.616f0bf6bd9b1670.json`
- Baseline render artifact: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/9655905f9f00c89ce2fa542fb9399cd12fd1b21b1f5e3c0f6b9e07c8fc011f6f/ceac67f64cc1c2ebdbaf7145a977b561e4b7646ee92f5b4c7c5148e967bd4e1d/ireland_parliament_decision_ui_window-full.svg`
- Valid-open settlement inspect artifact: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/14aae8232e83a031df08262f7e75166bf05340ce1aa83f27913a6b8d3060bfcd/29180d807e591ba6ce4f58cdead192522e2ec45bd588d02d0e713a16e3c281db/gui-inspect.616f0bf6bd9b1670.json`
- Valid-open settlement render artifact: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/c14d6bd313647d74edc37d72ad78ae35475040714ed830be007a0b7059e1f5c5/1d4ed5588db0bfc0f7351091f5a222538cca82ed62e6605eb920f443c94ccdec/ireland_parliament_decision_ui_window-full.svg`

The valid-open scenario sets `IRE`, `ireland_initialized`, `ireland_settlement_open`, stage one, and the action-state variables. Its render includes all four 204×32 controls and their white labels; inspect reports no button/seal overlap. The four `GUI_COST_MISMATCH` findings are checker false positives: the tool does not follow a GUI click to the existing shared executor which applies the actual political-power debit. No direct cost should be added merely to silence those findings.

The render approximation does not execute `buttonstate.lua` and reports a small font-glyph approximation gap. Those are render-tool fidelity limitations, not evidence of a missing in-game texture, sprite, or label.

## Issue list, sorted by severity

### High — redundant button visibility can suppress the only human action surface

**Files/identifiers:** `common/scripted_guis/ireland_scripted_guis.txt`; `ireland_parliament_powers_panel_visible`, `ireland_parliament_{dail,seanad,confidence,budget}_button_visible`.

The lower container and all four button visibility triggers each test the identical condition:

```txt
has_country_flag = ireland_settlement_open
```

The seals are ordinary GUI icons nested in the same container; their geometry is separate from the buttons (seals at x 10/262; controls at x 44/296). The screenshot cannot arise from these checked-in conditions alone because, if the lower container is visible, the four button conditions also pass. It can, however, arise if an element-specific visibility binding resolves differently at runtime or from an integration discrepancy outside the inspected files.

**Recommended exact fix:** remove these four lines only:

```txt
ireland_parliament_dail_button_visible = { has_country_flag = ireland_settlement_open }
ireland_parliament_seanad_button_visible = { has_country_flag = ireland_settlement_open }
ireland_parliament_confidence_button_visible = { has_country_flag = ireland_settlement_open }
ireland_parliament_budget_button_visible = { has_country_flag = ireland_settlement_open }
```

Keep `ireland_parliament_powers_panel_visible` as the single container gate and retain every `*_button_click_enabled` trigger. Because GUI elements default to visible, buttons will then appear whenever the already-visible powers panel appears, while their existing stage, completion, capital, settlement, and political-power checks still control whether they can be clicked. Do not replace `buttonType`, `quadTextureSprite`, `buttonFont`, `buttonText`, or shared click effects.

**Uncertainty:** this hardens a redundant suppression path but cannot prove the screenshot's external/runtime cause from source alone. The proposed post-patch render should be repeated with the same valid-open scenario.

### Medium — the Parliament title is black on the asset's dark top rail

**File/identifier:** `interface/ireland_parliament_scripted_gui.gui`; `@TITLE_Y`, `ireland_parliament_title`.

The panel asset has a dark wood/green title rail at its top. The title starts at `@TITLE_Y = 1` and uses `vic_18_black`, whose vanilla colour is black. This is a direct contrast problem. The chamber titles remain black on parchment and are appropriate; the lower section header already uses readable white `hoi_16mbs`.

**Recommended exact fix:** change the title surface only:

```txt
@TITLE_Y = 0
...
font = "hoi_16mbs"
...
maxHeight = 16
```

Retain centre alignment and `maxWidth = @PARLIAMENT_WIDTH`. This seats the title in the dark rail and uses the established white Parliament-panel font without adding a sprite or localisation key. Re-render at 1920 and 2560 after the edit; do not change the parchment chamber headers.

### Low — no human-visible native decision exists before the National Settlement focus

**Files/identifiers:** `common/decisions/ireland_decisions.txt`; `ireland_action_convene_the_dail`; `common/scripted_triggers/ireland_parliament.txt`; `ireland_parliament_dail_action_available`; `common/national_focus/ireland_focus_tree.txt`; `ireland_national_settlement`.

This is intentional in the current implementation, not a missing executor: the category is visible from `ireland_initialized` via `ireland_parliament_open`, has `visible_when_empty = yes`, and all four native decisions have `is_ai = yes`. The focus `ireland_national_settlement` sets `ireland_settlement_open`; only then is the GUI panel and its human controls intended to appear. Initialisation happens in 1936 history and sets the Parliament variables, but not `ireland_settlement_open`.

If the new requirement is that the category must present an actionable-looking human decision at campaign start, use a **single blocked Dáil preview**, not a second active action after the focus. This preserves route semantics and shared execution:

```txt
ireland_action_convene_the_dail = {
	visible = {
		original_tag = IRE
		NOT = { has_country_flag = ireland_route_archived }
		ireland_parliament_stage_one = yes
		NOT = { has_country_flag = ireland_parliament_dail_session_complete }
		OR = {
			is_ai = yes
			NOT = { has_country_flag = ireland_settlement_open }
		}
	}
	# leave available, cost, complete_effect, remove_trigger, and ai_will_do unchanged
}
```

For a human player, this makes the Dáil decision visible only before the focus opens the GUI. Its unchanged availability continues to require `ireland_settlement_open`, Dublin ownership, the stage, completion state, and the existing political-power gate. Its unchanged `complete_effect` calls `ireland_execute_parliament_dail_action`, so no executor is duplicated and no route is bypassed. Once the focus opens the GUI, the native preview disappears and the existing GUI control is the sole human action surface. AI retains its existing sequential native decisions.

Update the existing unavailable-tooltip text in `localisation/english/ireland_l_english.yml` to say that the National Settlement focus must first open the programme; preserve UTF-8 BOM. This is clarity-only and should not expose implementation terminology.

If a visible-but-blocked preview is not acceptable, no valid human starting action can be added without changing the National Settlement route gate. In that case, the empty informational category is the correct current behaviour and this item should be rejected rather than weakening `ireland_parliament_dail_action_available`.

## Decision-category lifecycle

| Phase | Category | Human action surface | Route guard / cleanup |
|---|---|---|---|
| 1936 initialisation | `ireland_settlement_government` visible because `ireland_parliament_open` requires `IRE`, `ireland_initialized`, and no archive. `visible_when_empty = yes`. | None for humans under current design; proposed Dáil preview would be visible but unavailable. | `ireland_initialize_campaign` creates variables/stage/dirty state. |
| After `ireland_national_settlement` | Same category; scripted GUI lower panel appears on `ireland_settlement_open`. | Four GUI buttons, each routed to its shared executor. | Availability enforces stage, completion, settlement, Dublin, and PP. |
| Completion | Seals advance from `ireland_update_parliament`; stage becomes five once all four flags are present. | Finished controls disable; no repeat action. | Per-action completion flags and `fire_only_once` prevent replay. |
| Archive / route change | Category/gui hide or decisions remove. | No stale controls should remain. | `ireland_route_archived` hides GUI and removes native decisions. |

## Mission quality notes

No mission or timed decision is present in this surface. The immediate Parliament actions are owned by `IRE`, under `ireland_settlement_government`, and Dáil availability additionally requires Dublin (`state = 113`). They have no duration, partial-success branch, or failure branch because each is an immediate, guarded state-transition action. There is no duplicate/repeat risk: every action has both a completion flag and `fire_only_once`; the shared executor repeats the canonical availability test before applying effects.

## Cost and requirement clarity

The Parliament actions use central constants and one shared execution path:

| Action | Displayed cost / gate | Shared executor |
|---|---:|---|
| Convene Dáil | 15 PP / >14 PP | `ireland_execute_parliament_dail_action` |
| Win Seanad Support | 25 PP / >24 PP | `ireland_execute_parliament_seanad_action` |
| Confidence Pact | 25 PP / >24 PP | `ireland_execute_parliament_confidence_action` |
| Pass Joint Budget | 35 PP / >34 PP | `ireland_execute_parliament_budget_action` |

The distinct costs and sequential requirements are clear, dynamic, and not a flat PP store: outcomes also move Parliament variables, support, mandate, cohesion, stability, and administrative reach. The native `custom_cost_trigger = { always = yes }` is display-only; availability is correctly enforced by the canonical scripted trigger and again inside the executor. Retain that pattern.

## AI validity and route locks

GUI AI is disabled. Native AI decisions have descending base weights (10/9/8/7) and the same stage/settlement/PP guards as the human GUI path. They have no country targets, borders, war goals, or formable dependencies, so there are no invalid-target or unsafe-route issues in scope. `ireland_route_archived` is the correct permanent route lock and has a matching decision-removal and GUI-visibility path.

## Localisation and tooltip gaps

All current title, section label, action labels, action tooltips, native decisions, and custom availability/cost keys are present. No sprite-localisation gap was found. The only recommended localisation edit accompanies the optional starting Dáil preview: state the focus prerequisite in the unavailable tooltip so an initial human player knows why the decision cannot yet be taken.

## Cleanup and exploit risk

No free-unit, equipment, core, war-goal, or political-power exploit loop is present. A completed action cannot be replayed through either button or native decision because the executor, availability trigger, completion flag, and `fire_only_once` align. Do not add direct button costs or direct effects; doing so would risk cost duplication or bypass the canonical executor.

## Recommended implementation order

1. In `common/scripted_guis/ireland_scripted_guis.txt`, remove only the four redundant per-button `*_visible` bindings described above.
2. In `interface/ireland_parliament_scripted_gui.gui`, apply the title-rail font/position adjustment only.
3. If the parent accepts a starting human preview, make the single `ireland_action_convene_the_dail` visibility change and its tooltip clarification. Do not make later Parliament decisions human-visible and do not relax `ireland_parliament_dail_action_available`.
4. Re-run GUI inspect/render under an open-settlement scenario at 1920 and 2560. Check one live available Dáil state, a locked Dáil state, and the initial pre-focus preview state. Verify that only the shared executor subtracts PP and advances flags.

## Required handoff fields

- **Changed files:** only this audit handoff: `docs/plans/ireland_focus_tree/subagent_handoffs/parliament_start_audit_2026-08-13.md`.
- **Changed IDs:** none; read-only audit.
- **Before/after behaviour:** no source behaviour changed. Proposed behaviour is described above.
- **Meaningful validation:** fresh `hoi4.gui_inspect` and `hoi4.gui_render` artifacts demonstrate source-control rendering in a valid open-settlement scenario and identify no button/seal geometry conflict.
- **Skipped validation:** no live game execution or source patch validation because this task is explicitly read-only; screenshot's runtime condition cannot be conclusively recreated from inspected source.
- **Remaining issue:** identify why the reported client can display a powers container/seals while the source-equivalent controls are absent, if it persists after the redundancy removal. Do not solve this by duplicating action effects or loosening the route gate.
- **Skills used:** `hoi4-decisions-missions`, `hoi4-focus-trees`, and `hoi4-subagents`.

## Final implementation verification — 2026-08-13

### Verdict

**PASS — no functional blocker found.** The implemented Parliament surface satisfies the requested presentation and route-safety conditions. This follow-up remained read-only; the handoff is the only file updated.

### Confirmed implementation contract

- **Title and readability:** `@TITLE_Y = 4`, `hoi_16mbs`, and `maxHeight = 16` are present on `ireland_parliament_title`. The title is consequently white on the panel's dark top rail. The dark-on-parchment chamber headings remain unchanged, so the font change does not reduce their contrast.
- **Programme visibility from initialisation:** `ireland_parliament_powers_panel_visible` now uses `ireland_parliament_open = yes`; there are no `ireland_parliament_{dail,seanad,confidence,budget}_button_visible` bindings. The GUI default-visible rule therefore presents all four controls as soon as `ireland_initialized` makes Parliament open. The buttons can be disabled, but cannot independently disappear while their parent panel remains visible.
- **Readable labels and values:** each control keeps its `hoi_16mbs` button font and its localised white name plus yellow political-power amount: 15, 25, 25, and 35 PP. All four button labels, tooltips, the title, and the section label resolve in `localisation/english/ireland_l_english.yml`; their referenced background, button, state-seal, and chamber sprites are present in `interface/ireland_gui_assets.gfx`.
- **Canonical interaction path:** each `*_button_click` still calls exactly one `ireland_execute_parliament_*_action`. Each executor repeats the canonical availability trigger, applies exactly one central PP delta, and invokes its existing record helper. The four `*_button_click_enabled` trigger bindings remain intact. No direct GUI cost or duplicate effect was added.
- **Initial human decision:** `ireland_action_convene_the_dail` is visible for a human only before `ireland_settlement_open`; it remains unavailable until the unchanged canonical Dáil trigger accepts the settlement flag, Dublin, stage, completion state, and PP gate. Its localisation names `The National Settlement` as the prerequisite.
- **No duplicate human path after settlement:** once `ireland_settlement_open` is true, the human branch of that native decision is false and the GUI is the only human action surface. AI retains the Dáil native decision after settlement and the later AI-only native sequence.
- **AI/cost/cleanup safety:** native AI weights remain 10/9/8/7 and all four executors retain their original 15/25/25/35 PP constant deltas. Completion flags, `fire_only_once`, route archival checks, and the executor-side availability checks still prevent repeat, free, or bypassed actions.

### Visual and source validation

Fresh GUI-tool runs used source revision:

`ee8ef78b282d3f6c2f59c9f1fb4cf3c128381815c86d7d8c3d7cc2523755d94d`

| Scenario | Inspect artifact | Render artifact | Result |
|---|---|---|---|
| Human initialisation: `ireland_initialized`, no settlement flag | `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/a781c9a4bf758c43d8d6300971575e1c84549d270088f50d894f60597da112c2/6c794e73fa7fc481edda68da87b3e0a09ce48951e3ac3474f40c8a15cc7a4a7e/gui-inspect.ee8ef78b282d3f6c.json` | `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/49f64718de0767a65aaee19d5bd5427c9f2bfb86604b030f81a0c6d72c74a019/3ee6ad2743e260969cfde1846aa43d88a9bbda6718fc957295bb64c06c5f65ef/ireland_parliament_decision_ui_window-full.svg` | GUI source graph parses; all controls render in the initial disabled/locked presentation; no visible overlap diagnostic at 1920×1080 or 2560×1440. |
| Human settlement open: `ireland_initialized`, `ireland_settlement_open`, stage one | `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/dc3978a6530e0a4a9722d01bc30f4691b91a8edf559e11f27f8cde18b64191b0/85061ae5745240c76d878f3e73d474c4fd9036873ef9ddefef4284021f8783e9/gui-inspect.ee8ef78b282d3f6c.json` | `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/34343ea9d715e42f983781e744df86638986ec7c036dd907b9673de44de843ba/54420338081dc7dcbef8f9d4af3ca31dd4cbd9f238bee4b36668f2b6b35465e8/ireland_parliament_decision_ui_window-full.svg` | Same source-graph and no-overlap result; button/seal placement fits the 100px lower panel (two 32px rows at y 20 and y 60). |

The inspector's four `GUI_COST_MISMATCH` reports are retained as a known tool limitation, not an implementation defect: it does not trace from the GUI click wrapper into `ireland_execute_parliament_*_action`, where each PP debit is present. Adding direct costs to the GUI wrapper would create the very duplicate/free-path risk under review and must not be done.

The renderer also labels `textSpriteType` controls with `buttonstate.lua` as partially modelled because it cannot execute the engine's button-state shader. The controls' DDS, GFX definition, font, and localisation keys all resolve; this is not a missing-sprite or missing-localisation finding.

## Stable lifecycle re-audit - 2026-08-13

### Verdict

**Functional PASS; completion BLOCKED on four player-facing localisation defects.** The Dáil-first lifecycle, executor ownership, costs, focus gates, and GUI layout are coherent. No duplicate/free action path, missing GFX/localisation key, route bypass, or overlap was found. The remaining blocker is that three later action tooltips omit their new focus requirements and the National Settlement reward describes a stage transition already made by the Dáil action.

This section supersedes the preceding lifecycle finding, which describes the pre-stable Dáil preview design.

### Confirmed lifecycle

| Step | Canonical availability | Transition | Surface |
|---|---|---|---|
| Dáil | Parliament open, stage one, not completed, Dublin, and more than 14 PP; deliberately no settlement flag gate. | Shared Dáil executor takes 15 PP and its record helper sets `ireland_parliament_dail_session_complete` plus `ireland_settlement_open`, then recomputes stage two. | Native Dáil decision is visible to humans and AI from initialisation; GUI calls the same executor. |
| National Settlement | Custom focus requirement checks Dáil completion. | Completes the distinct focus milestone required by Seanad; does not duplicate `ireland_settlement_open`. | Focus route. |
| Seanad | Settlement flag, completed National Settlement, stage two, seat condition, Dublin, and more than 24 PP. | Shared executor takes 25 PP and advances stage three. | Human GUI; AI-native base 9. |
| Confidence | Settlement flag, completed Constitutional Draft, stage three, Dublin, and more than 24 PP. | Shared executor takes 25 PP and advances stage four. | Human GUI; AI-native base 8. |
| Joint Budget | Settlement flag, completed Government Formation, stage four, chamber majorities, Dublin, and more than 34 PP. | Shared executor takes 35 PP and advances stage five. | Human GUI; AI-native base 7. |

`ireland_constitutional_draft` is downstream of the National Settlement route and `ireland_government_formation` follows the Election Mandate and Constitutional Draft. No unreachable focus/action cycle was found. Ireland history initialises Parliament at stage one; no explicit history PP grant was found, so executable-at-initialisation correctly remains subject to the stated PP and Dublin requirements.

### Source and layout verification

- The category and lower panel use `ireland_parliament_open`; all four buttons default visible because there are no per-button `*_visible` bindings. The four `*_button_click_enabled` triggers remain the only interaction gate.
- Each GUI click and native decision routes into exactly one `ireland_execute_parliament_*_action`, which repeats canonical availability, uses the same central 15/25/25/35 PP constants, and records a completion flag. `fire_only_once` and archive removal remain in place. Dáil is available from two surfaces but has only one guarded effect path.
- The title is y=4 in white `hoi_16mbs`. Each button uses the white label/yellow PP-value localisation. Its 204px control begins at x=44/296, while the state seal occupies x=10/262; two 32px rows at y=20 and 60 fit the 100px lower panel with no collision.
- GFX definitions resolve for the background, action-state sheet, chamber sprites, and button sprite. All referenced GUI title/header/label/tooltip/cost keys exist.

### Fresh GUI evidence

Final shared revision: `2cae4f1fc2b90dd97ddf1728c9f4a22dab89f768dbc9add770c84da84f207e5f`.

| Scenario | Inspect artifact | Render artifact | Result |
|---|---|---|---|
| Initial human, stage one, no settlement flag | `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/c4756f8fc6e5b1b7d1e5fd776d7dac5d01a468e91bd10902925d9dbf97ebac98/1b6c32c17142478712513008d7b5376ff4f03c93db65389d9e10ecfc13bfacc3/gui-inspect.2cae4f1fc2b90dd9.json` | `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/34343ea9d715e42f983781e744df86638986ec7c036dd907b9673de44de843ba/fe47978e5a336946c73021097a76f3559ee69b1ca52f04d4b84c630dada34156/ireland_parliament_decision_ui_window-full.svg` | All controls present; no visible-overlap finding at 1920x1080 or 2560x1440. |
| Post-Dáil, settlement flag/stage two, before National Settlement | `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/28df455665fba609767d761e9307d98653451cbcc65f659a683f7adc5c3a70c2/0686dad1f693e28da9bc8d2ac2583b40a49d3f227eaf9d9e9b06f7cce1ce3eb8/gui-inspect.2cae4f1fc2b90dd9.json` | `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/eeaaa384480b14505c918f5c8a4e6261176bc544ef3fafbf783830bc536f8c39/74dd01ea5718bbeb60930a7e1406396cea1c600a2e8d28cb2733d89733630961/ireland_parliament_decision_ui_window-full.svg` | Complete/locked states fit; source keeps Seanad unavailable until National Settlement is complete. |

The render-scenario schema does not model owned states, so source availability was separately verified for Dublin and PP. The tool's `GUI_COST_MISMATCH` warning is a false positive: it does not traverse GUI wrappers into the shared executors containing the PP debit. Do not add a direct button cost. `buttonstate.lua` is likewise a renderer-fidelity limitation, not a missing asset.

### Exact actionable defects

1. **Medium — Seanad focus gate absent from player text.** Add `The National Settlement` to `ireland_parliament_seanad_button_tt` and `ireland_action_negotiate_seanad_support_requirements_tt`.
2. **Medium — Confidence focus gate absent from player text.** Add `Constitutional Draft` to `ireland_parliament_confidence_button_tt` and `ireland_action_secure_a_confidence_compact_requirements_tt`.
3. **Medium — Budget focus gate absent from player text.** Add `Government Formation` to `ireland_parliament_budget_button_tt` and `ireland_action_pass_a_joint_budget_requirements_tt`.
4. **Medium — National Settlement reward timing is inaccurate.** Change `ireland_national_settlement_reward_tt` from “Advances the legislative programme to Seanad Support” to wording that it authorises/unlocks Seanad Support; stage two has already been set by the Dáil record helper.

### Non-blocking source-comment cleanup

`interface/ireland_parliament_scripted_gui.gui` should say that the native Dáil decision is executable for both humans and AI at campaign start, while later native Parliament decisions remain AI-only. This is documentation-only and does not affect gameplay.

## Tooltip and comment closure - 2026-08-13

### Final verdict

**COMPLETE — no remaining Parliament lifecycle, tooltip, GUI-localisation, or native-decision-comment blocker.**

The seven requested text surfaces now match the stable canonical triggers:

- Seanad GUI and native requirement text name **The National Settlement**.
- Confidence GUI and native requirement text name **Constitutional Draft**.
- Joint Budget GUI and native requirement text name **Government Formation**.
- `ireland_national_settlement_reward_tt` correctly says it authorises Seanad Support rather than advancing the parliamentary stage.
- The Parliament GUI comment now correctly describes the shared guarded executors instead of calling all native decisions AI-only.

The focus names exactly match the three `has_completed_focus` checks in `ireland_parliament_seanad_action_current`, `ireland_parliament_confidence_action_current`, and `ireland_parliament_joint_budget_action_current`. Dáil remains the initial action and is unchanged by this wording-only closure.

Fresh `hoi4.gui_inspect` evidence on source revision `3c745c24803c88b87b786e7617147b38b9adafb16bd286d131e4d9a3075e301e` resolved the current GUI graph and localisation links without a visible-overlap diagnostic:

`hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/8f2a77e73ad5b4f86a29cfb777f073b4a18285a6e044510d0e0f45532b3f1b41/cdd9274f15def241f0ce61eb8011691d3052cbfb7216ca5375e621da14a1d82b/gui-inspect.3c745c24803c88b8.json`

No full render was repeated because this closure changes only localisation strings and a source comment; the current-layout render evidence remains recorded above. The inspect tool still emits its known inability to trace GUI wrappers into shared PP executors and its `buttonstate.lua` approximation warning; neither represents an implementation defect.
