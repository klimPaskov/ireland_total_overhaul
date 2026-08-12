# Parliament interaction audit — 2026-08-11

Feature slug: `ireland_focus_tree`

Scope: read-only audit of the Ireland Parliament decision-category GUI and its
four opening actions. No gameplay, GUI, GFX, localisation, asset, focus, or
event source was edited by this audit.

## Outcome

The reported no-op is real on the surface the player is naturally trying to
use. `ireland_parliament_decision_ui` contains no `effects` block and the
window contains no `buttonType`. The four apparent parliamentary controls are
pass-through status `iconType` elements and passive text labels. They cannot
select any action.

The four native decisions beneath the embedded GUI are separately functional
in source; they are not the no-op. They own the existing costs, checks,
one-time gates, record effects, and AI weights. Their presentation is simply
at odds with a GUI that looks like an action deck. Because the requested
experience is clickable Parliament controls, the recommended resolution is a
**functional scripted-GUI / native-AI split**, not a passive-only redesign.

## Evidence

- Required repository, decision/mission, focus-tree, and subagent guidance;
  the offline Data structures, Triggers, Effects, Modifiers, Localisation,
  Scopes, On actions, Event modding, Decision modding, Idea modding, AI
  modding, Interface modding, and Scripted GUI modding references were read.
- Required vanilla documentation was read, including scripted-GUI reference
  material, trigger/effect documentation, and script-constant documentation.
  Vanilla `USA_congress`, `MTG_congress.txt`,
  `USA_congress_scripted_gui.txt`, and
  `usa_congress_scripted_gui.gui` were inspected. Vanilla Congress is a good
  precedent for live chamber frames, but it is deliberately a summary rather
  than an interactive control deck.
- Source ownership was traced through
  `common/decisions/ireland_decisions.txt`,
  `common/decisions/categories/ireland_categories.txt`,
  `common/scripted_guis/ireland_scripted_guis.txt`,
  `common/scripted_effects/ireland_parliament.txt`,
  `common/scripted_triggers/ireland_parliament.txt`,
  `common/scripted_effects/ireland_effects.txt`, the opening focuses, GUI/GFX,
  and English localisation.
- Fresh read-only MCP inspection returned `GUI_INSPECTED` for
  `ireland_parliament_decision_ui_window`, workspace
  `mod_ireland_total_overhaul_aaca88216c92`:
  [inspection graph](hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/df4734a3154800dd068551ee23e158859a8d1c355330b2173ffc0943e09de48f/c7e1a29ae676473332af0cc655f187d604c862e0b6035e1c7912dc8844dbe016/gui-inspect.5f725bd58271c2f7.json).
  It confirms a parsable source graph, but the synthetic scenario leaves the
  four live chamber texts unresolved and cannot demonstrate an effect path.
- Fresh `GUI_RENDERED` output supplied the full, cropped, annotated,
  click-region, hierarchy, layout, and fidelity artifacts. Key references are
  [annotated render](hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/09d17bb55cf6b380f27df05a2aced79bd4d2f00044ff25531ad15e245c600b3f/0101dbcd09b2d56394959ee69c97d817626d6a20810704f3d8a360662e1c290c/ireland_parliament_decision_ui_window-annotated.png),
  [click regions](hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/ab397bea75c9ee7d22299708f2386363188e92f7580125b32edba60252cc821b/58d7f2bba1d641885a79d6059e6557b224f5b85cf59473e79ee85173fbc0d42c/ireland_parliament_decision_ui_window-click-regions.png),
  and [layout evidence](hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/4dc6bd05c3cda2c308d0a79f8e5e38406b1d227ffc8b5ab074ea916db77b484e/0568edaee92c66413c1a13296d7315546683cd3826cfb94df2d7f0695bf44654/ireland_parliament_decision_ui_window-layout.json).
  The renderer does not simulate a GUI click. Its no-overlap result therefore
  does not disprove the observed inherited-clipping problem: the current
  lower controls sit exactly on nested clip boundaries with no safety margin.

## Issues, ordered by severity

### Critical — the apparent Parliament controls have no executable owner

`interface/ireland_parliament_scripted_gui.gui` contains only `iconType` and
`instantTextBoxType` affordances. In particular:

- `ireland_parliament_power_dail_state`
- `ireland_parliament_power_seanad_state`
- `ireland_parliament_power_confidence_state`
- `ireland_parliament_power_budget_state`

are passive `GFX_checkbox_small_red_green` icons. Their four corresponding
labels are passive text boxes. `common/scripted_guis/ireland_scripted_guis.txt`
provides properties, visibility triggers, and `dirty`, but no Parliament
`effects`, `*_click_enabled`, or `ai_weights` entries. A click either passes
through or performs no game action. The general tooltip says only whether red
or green means pending/secured, which reinforces the false action affordance.

### High — adding GUI effects without changing ownership would create a dual-cost path

The native actions use engine `cost` fields while their `complete_effect`s call
the `ireland_record_parliament_*` effects. Directly adding the same record
calls to GUI clicks would create two human interaction paths with different
cost presentation and no shared cost executor. Copying native effects into the
GUI is not acceptable: it risks PP divergence, inconsistent requirements, and
an eventual duplicate credit path.

### High — the lower checkpoint strip has zero clipping tolerance

The root is `510 x 198`. Its `ireland_parliament_powers_panel` is exactly
`y=133, h=65`, ending at the root bottom. The nested progress track is exactly
`y=17, h=31`; every 31-pixel checkbox is placed at local `y=0`, touching that
clip rectangle at both vertical edges. The label row starts at local `y=48`
and has `h=17`, ending exactly at its parent boundary. The final label reaches
`x=508` in a 510-pixel root. This gives the renderer no allowance for the
actual glyph/sprite bounds, inherited decision-description clipping, or UI
scale rounding. The reported icon/label intersection is consistent with this
geometry even though the source parser has no hard overlap diagnostic.

### High — chamber seats are too small for the purpose of the panel

The Dáil's 21-frame strip is only `94 x 50` per frame; the compact Seanad
strip is only `90 x 50`. They occupy a minor part of each `247 x 109` chamber
field. The chamber summaries consequently read as text cards with decorative
arcs rather than a legible parliamentary seat display.

### Medium — the summary can appear before its first action exists

`ireland_initialize_campaign` establishes the ledgers and
`ireland_parliament_open` reveals the category after `ireland_initialized`.
The first native action remains hidden until the
`ireland_national_settlement` focus writes `ireland_settlement_open`. This is
valid lifecycle behaviour, but a functional GUI must not show a misleading
disabled action grid in the interval. Hide the action grid until the focus
gate; keep the chamber summary visible.

### Medium — GUI cost and requirement clarity is absent

The native decisions correctly expose 15/25/25/35 PP and concise requirement
tooltips. The GUI labels describe outcomes only and never show a cost, the
current requirement set, a disabled reason, or a post-click outcome. This is
unacceptable once those controls become the human action surface.

### Low — historical documentation still describes this panel as intentionally passive

The existing 2026-08-09 completion and visual-audit handoffs state that
pass-through icons and native-only decisions were intentional. That decision
conflicts with the current requested interaction contract and should be marked
superseded by the implementation handoff, rather than followed as current
design.

## Visible-affordance and runtime ownership map

| Visible item | Current type and bounds | Current owner | Actual result when used |
| --- | --- | --- | --- |
| Background and Houses title | background / text, `0,0,510,198` | presentation | Decorative/informational only. |
| Dáil/Seanad chamber arcs | `iconType`, `94x50` / `90x50` | `ireland_update_parliament` frame properties | Live passive support display. |
| Chamber status/composition texts | text boxes | scripted localisation | Live passive numbers/tooltips. |
| Four red/green checkpoints | `iconType`, four `31x31` images | frame properties only | No click effect; the likely surface reported as a dead button. |
| Four checkpoint labels | text boxes, four `125x16` labels | localisation only | No click effect; an outcome tooltip but no action. |
| Native decision rows | HOI4 decision widgets below the GUI | four native decision definitions | The only current clickable path; source indicates they execute correctly. |

## Native action audit

| Action | Current availability | PP | Completion owner | AI | Runtime result |
| --- | --- | ---: | --- | --- | --- |
| `ireland_action_convene_the_dail` | Open settlement, stage 1, Dublin | 15 | `ireland_record_parliament_dail_session` | base 10 | 76→77 routine Dáil votes, then stage 2. |
| `ireland_action_negotiate_seanad_support` | Stage 2, Dublin, Seanad below majority | 25 | `ireland_record_parliament_seanad_support` | base 9 | 30→32 Seanad government seats against a 31-seat majority, then stage 3. |
| `ireland_action_secure_a_confidence_compact` | Stage 3 and Dublin | 25 | `ireland_record_parliament_confidence_compact` | base 8 | external support if absent; +2 routine votes, then stage 4. |
| `ireland_action_pass_a_joint_budget` | Stage 4, Dublin, both majorities | 35 | `ireland_record_parliament_joint_budget` | base 7 | stability, administrative reach, mandate/cohesion, terminal stage 5. |

The initialized opening is mechanically reachable: Dáil routine support starts
at 76/77 and the Seanad at 30/31. The first action establishes Dáil majority;
the second establishes Seanad majority; the third adds two more routine votes;
the fourth is then legal. Every action is `fire_only_once`, completion state
is retained deliberately for the historical display, and `ireland_route_archived`
hides the category/window/actions. No country target, dead counterpart,
external border, mission, event target, timer, or cooldown affects this chain.

## Recommended human / AI interaction contract

Adopt the functional GUI variant. Do not retain a visual action strip that is
not clickable, and do not allow humans to choose between a native row and a
GUI button for the same action.

1. Make four GUI `buttonType`s the **only human action entry points**:
   `ireland_parliament_dail_action_button`,
   `ireland_parliament_seanad_action_button`,
   `ireland_parliament_confidence_action_button`, and
   `ireland_parliament_budget_action_button`.

2. Give each a matching `effects` entry that calls one shared executor,
   respectively `ireland_execute_parliament_dail_session`,
   `ireland_execute_parliament_seanad_support`,
   `ireland_execute_parliament_confidence_compact`, and
   `ireland_execute_parliament_joint_budget`. The executor is the one place
   that checks the canonical availability trigger, deducts its PP price, calls
   the existing `ireland_record_parliament_*` effect, and therefore dirties
   the GUI. It must be idempotent against its completion flag.

3. Promote the existing four
   `ireland_parliament_*_action_available` scripted triggers to the canonical
   availability rules. Both the GUI `*_click_enabled` triggers and the native
   AI decisions must use those helpers. Keep the existing human-readable
   custom requirement tooltips around those helpers; do not expose their raw
   state/flag checks.

4. Move PP charging into the shared executor, once, and make the native
   decision route use the same executor. Preserve its `ai_hint_pp_cost` so AI
   reserves the applicable 15, 25, 25, or 35 PP before taking it. Centralise
   those four values in a Parliament script-constant table before sharing them
   across decision and scripted-GUI files; do not duplicate file-local `@`
   numbers in the GUI.

5. Restrict each of the four native decision definitions to `is_ai = yes` in
   its `visible` contract while retaining every existing route/stage condition.
   Human IRE sees only the GUI buttons. AI IRE sees and evaluates only the
   native decisions, retaining the current base 10/9/8/7 priority ladder.
   The Parliament scripted GUI has no `ai_weights` and uses
   `ai_enabled = { always = no }`; it is never an AI execution path.

6. Show all four GUI buttons only after `ireland_settlement_open`; before
   that, show the chamber summary alone. Afterward, the completed action is
   visibly secured/disabled, the one current action is enabled only when its
   canonical trigger is true, and later actions are visibly locked/disabled.
   Each button tooltip must include icon-first PP cost, short requirement
   summary, the detailed custom requirement tooltip, and its visible outcome.
   The scripted-GUI localisation forms `[!<button>_click]` and
   `[!<button>_click_enabled]` are the appropriate effect/requirement tooltip
   hooks.

7. Route archival remains the sole terminal cleanup. It hides the category,
   GUI, and native AI decisions. Completion flags and chamber variables remain
   intentionally as historical state; no target, mission, event target, or
   cooldown cleanup is needed.

This produces exactly one action owner per controller: human → GUI executor;
AI → native decision → same executor. It preserves existing rewards and
staging, has no free-click or PP-farming loop, and does not add a second
Parliament mechanic.

## Exact interaction layout

The current `510x198` art cannot support four legible action buttons and
larger chambers without reviving the clipping problem. Use a fixed `510x246`
panel and a matching, non-interactive `510x246` background. The existing
`GFX_ireland_gui_action_button` is `280x38`; with `scale = 0.85`, each action
button is an effective `238x32`.

| Element | Exact bounds/position | Notes |
| --- | --- | --- |
| Root | `0,0,510,246` | Literal pixel size; no percentage dimensions. |
| New decorative backdrop | `0,0,510,246` | One non-interactive background; preserve high-contrast parchment chamber field and dark action field. |
| Title | `0,1,510,18` | `vic_18_black`, centred. |
| Dáil card | `4,22,247,120` | Equal card; dark header/status text. |
| Dáil seat strip | local `61,19,126,67` | New 21-frame `126x67` derivative; centred, 34% wider and 34% taller than current. |
| Dáil status / composition | local `0,89,247,14` / `0,105,247,14` | Centred, `Main_14_black`; does not touch card bounds. |
| Seanad card | `259,22,247,120` | Equal card. |
| Seanad seat strip | local `61,18,126,70` | New 21-frame `126x70` derivative from the full Seanad strip; centred. |
| Seanad status / composition | local `0,89,247,14` / `0,105,247,14` | Same baseline as Dáil. |
| Programme heading | `0,144,510,16` | Centred white `hoi_16mbs` on the dark band. |
| Dáil action button | `10,164,238,32` | `buttonType`, scale `0.85`; current/completed/locked state comes from scripted triggers. |
| Seanad action button | `262,164,238,32` | Same size. |
| Confidence action button | `10,202,238,32` | Same size. |
| Budget action button | `262,202,238,32` | Same size; 12px bottom margin remains. |
| State icon slots | `(13,165)`, `(265,165)`, `(13,203)`, `(265,203)`, each `31x31` | `alwaystransparent = yes`, so the button below receives the click. Use ready/current/locked state art, not a red/green checkbox as the action surface. |
| Button labels | `(47,171,190,16)`, `(299,171,190,16)`, `(47,209,190,16)`, `(299,209,190,16)` | `hoi_16mbs`, icon-first PP label, `alwaystransparent = yes`; must never capture the button click. |

Create two large seat assets by resizing each frame independently, not by
non-integral GUI scaling:

- `gfx/interface/ireland/gui/parliament/dail_chamber_ui_large.dds` — 21 frames
  at `126x67` (full strip `2646x67`), registered as
  `GFX_ireland_parliament_dail_large_ui`.
- `gfx/interface/ireland/gui/parliament/seanad_chamber_ui_large.dds` — 21
  frames at `126x70` (full strip `2646x70`), registered as
  `GFX_ireland_parliament_seanad_large_ui`.

These are presentation derivatives of the current 21-frame sources. They do
not change the frame variables or parliamentary arithmetic.

## Decision-category lifecycle notes

- Owner/category: original `IRE` / `ireland_settlement_government`.
- Start: `ireland_initialize_campaign` initializes chamber values and stage 1;
  the read-only chamber portion appears after `ireland_initialized`.
- Focus integration: `ireland_national_settlement` sets
  `ireland_settlement_open`, at which point the four action buttons may appear.
  This is the only focus gate for the opening Parliament sequence.
- Active progression: the current one of four actions advances a retained
  stage value from 1 to 5. The grid shows completed/current/locked states
  without exposing later actions as executable.
- Terminal: `ireland_route_archived` hides all human and AI action surfaces;
  the persistent flags are correct historical records, not stale state.

## Mission quality notes

There is no Parliament GUI-owned mission. The audited actions are immediate,
one-time institutional decisions: owner `IRE`, category
`ireland_settlement_government`, regional requirement Dublin, duration none,
success the corresponding record effect, failure/partial-success none, and
duplicate risk none. They should not receive artificial timers or failure
rolls merely to make buttons look active.

## Cost and requirement clarity notes

Political Power is an appropriate price for these constitutional acts; this is
not a passive PP store. The effects establish working majorities and durable
institutional state rather than giving trivial modifiers. The equal 25-PP
middle prices are defensible because each represents a discrete upper-house or
confidence bargain.

The new human buttons must surface `£pol_power 15`, `£pol_power 25`,
`£pol_power 25`, and `£pol_power 35` inline, followed by the current action
name. Their tooltip must explain the current stage and Dublin/majority
conditions with the existing four requirement keys; the canonical trigger
renders unmet conditions red. Do not expose raw flags, variables, or state id
113.

## AI validity and route-lock notes

There are no country targets, dead tags, borders, escalation variants, or
external routes in this action family. The action stage means only the next
native AI decision is relevant at a time, so the existing 10/9/8/7 weights do
not compete within the family. Preserve the original-IRE, route-archive,
settlement, Dublin, and chamber-majority locks. GUI AI must be explicitly
disabled once native decisions become the AI-exclusive surface.

## Localisation and tooltip work required

Keep all existing chamber status, composition, and action-effect localisation.
Add controller-specific UI keys for the four button labels and tooltips, plus
completed/current/locked state wording if not supplied through scripted
localisation. The tooltip keys must bind the GUI click-effect and
click-enabled output. Update the previously generic
`ireland_parliament_power_status_tt` only if the checkbox strip is retained as
non-clickable history; otherwise remove it with the retired strip. Preserve
UTF-8 with BOM.

## Cleanup and exploit-risk notes

The current native sequence has sound one-time protection through
`fire_only_once`, stage gates, and completion flags. The GUI version must
retain that protection in its shared executors: no effect is permitted if its
completion flag already exists or its canonical availability trigger fails.
The one shared PP charge prevents free-clicks or duplicate charging. No unit,
equipment, factory, claim, core, war-goal, target, or cooldown exploit is
created by this change.

## Recommended implementation surface

| File | Required change | Identifiers |
| --- | --- | --- |
| `common/scripted_guis/ireland_scripted_guis.txt` | Add four human GUI effects, visible/click-enabled state triggers, explicit no-GUI-AI rule, and property/state bindings. | Four `ireland_parliament_*_action_button` ids. |
| `common/scripted_effects/ireland_parliament.txt` | Add four shared, idempotent human/AI executors; retain the existing record/update effects. | Four `ireland_execute_parliament_*` helpers. |
| `common/scripted_triggers/ireland_parliament.txt` | Make existing action-availability helpers authoritative and expose clear button-state helpers if needed. | `ireland_parliament_*_action_available`. |
| `common/decisions/ireland_decisions.txt` | Route the four AI-native decisions through the shared executors; hide them for human IRE; preserve AI hints/weights. | Four `ireland_action_*` IDs. |
| `common/script_constants/` | Add the central Parliament PP-cost table used by both controller paths. | Suggested `ireland_parliament` category. |
| `interface/ireland_parliament_scripted_gui.gui` | Replace passive clipped checkpoint strip with the four-button `510x246` layout. | Root window, four buttons, four status slots, `dail_icon`, `seanad_icon`. |
| `interface/ireland_gui_assets.gfx` and `gfx/interface/ireland/gui/parliament/` | Register the two large 21-frame seat derivatives and matching 510x246 background. | `GFX_ireland_parliament_dail_large_ui`, `GFX_ireland_parliament_seanad_large_ui`. |
| `localisation/english/ireland_l_english.yml` | Add button labels/tooltips and state wording; preserve current outcomes. | Four button label/tooltip key families. |
| `docs/assets/ireland_parliament_panel/` | Update the panel and derivative manifest after final assets exist. | 510x246 background and large seat strips. |

## Validation performed and limitations

- Confirmed every current visible affordance, property mapping, and four native
  decision-to-record-effect call site.
- Confirmed the full scripted stage reaches both majorities from the real
  initialized values, then ends at stage 5.
- Confirmed the source dimensions of the current assets: action plate
  `280x38`, Dáil strip `1974x50` / 21 frames, Seanad full strip `2772x73` /
  21 frames, compact Seanad `1890x50` / 21 frames, and checkbox `31x31` per
  frame.
- MCP inspection/render artifacts are listed above. They are useful layout
  evidence but not proof of live action execution; their synthetic scenario
  does not resolve the country-scoped values or invoke GUI effects.

Meaningful validation intentionally skipped: no source was changed, so there
was no rewritten GUI to render and no live-game interaction test to perform.
The implementing agent must render normal/current/completed/locked/long-text
states at 1366x768 and 1920x1080, then inspect one human click per stage,
one insufficient-PP disabled case, pre-settlement presentation, AI native
execution, and route archival.

## Remaining issues and disposition

No source patch was applied by this audit. The only blocker is implementation
of the chosen functional ownership contract and its associated large-seat /
background asset package. No passive fallback is recommended: it would retain
the exact experience the user rejected.

## Final implementation re-audit — 2026-08-12

This section supersedes the historical baseline findings above. The requested
human-interactive Parliament implementation is present and source-valid: each
of the four `buttonType` controls has a matching scripted-GUI effect and
enabled trigger; a successful click performs exactly one guarded PP debit and
then its one-time record helper. The completion flag created by that helper
makes the same control unavailable before another debit can occur. The native
decisions are `is_ai = yes`, use vanilla-style custom-cost ownership, and call
their guarded executors, so the AI pays once and does not use the GUI.

The category and chamber summary appear immediately after
`ireland_initialized`; the action grid remains gated by
`ireland_settlement_open`. Initialisation assigns all displayed chamber
ledgers, stage, frames, and dirty value before that surface can appear. The
510x248 panel, 126x70 21-frame chamber strips, 204x32 controls, and 31px-wide
checkbox frames are correctly registered. The action columns are disjoint:
the status frames occupy `x=10..41` / `262..293`, while the buttons occupy
`x=44..248` / `296..500`; the two rows are separated by 8px.

Fresh read-only MCP inspection completed at revision `c53a3711f2a901e9` and
fresh rendering covered normal, hover, selected, locked, disabled, warning,
active, completed, empty/full, min/max, long-text, and missing-localisation
states at 1366x768 and 1920x1080. Artifacts: [inspection graph](hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/8a71593031f9902b801dbec2bbfb712ae8c58778723fbe938f08017c49ecfc22/76f02dc2e5ef7ec671a4bdbfef07b2d2a2c64b3d369a6372bb403c1e97c9fe4f/gui-inspect.c53a3711f2a901e9.json) and [full render](hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/b06136b2c77825b2cfc5ee6a9fe7ff0ea0448d0889f31d872eafe7c1b53d4118/cb14e511f023eb11a9c6aa770a343494170fbe78c66d46f1c0141824a07e0263/ireland_parliament_decision_ui_window-full.svg).

### MCP cost warnings — tool limitation, not a gameplay defect

`GUI_COST_MISMATCH` is emitted once per button because the checker does not
resolve `constant:` deltas nested in guarded scripted-GUI effects. Each cited
handler directly contains the matching debit — `-15`, `-25`, `-25`, or `-35`
through `constant:ireland.parliament_*_pp_delta` — and its matching enabled
trigger requires more PP than the companion `*_pp_gate`. The label, gate, and
debit are driven by the same constants. This is therefore not a free-action or
double-charge defect. The analogous native custom-cost pattern is used in
vanilla decisions, which debit resources from `complete_effect` rather than a
normal decision `cost` field.

### Exact unresolved defects

1. **Minor UI clipping risk — both chamber composition rows exceed their parent
   by one pixel.** In `interface/ireland_parliament_scripted_gui.gui`, each
   126px-high chamber puts its composition textbox at local `y=109` with
   `maxHeight=18`, covering local `y=109..126` rather than remaining within the
   parent’s `0..125` bounds. It also sits directly against the lower powers
   panel at absolute `y=148`. Move the status row to local `y=90` and the
   composition row to local `y=108`; the two 18px rows then occupy `90..107`
   and `108..125`, leaving all text inside the chamber without changing assets,
   root size, or click regions.

2. **Low maintenance-contract drift — the GUI does not call the documented
   shared executors.** `common/scripted_effects/ireland_parliament.txt:9-10`
   says the executors are the single owner for human and AI paths, but
   `common/scripted_guis/ireland_scripted_guis.txt:40-67` duplicates the same
   guarded gate/debit/record sequence directly. Current behavior is correct
   because it shares the availability triggers, constants, and record helpers;
   the risk is future change drift and inaccurate ownership documentation. The
   completion report at
   `docs/plans/ireland_focus_tree/focus_tree_parliament_completion_2026-08-09.md:132-138`
   also records no clipping and calls the executors shared, neither of which is
   fully true after this audit. `docs/ireland_dynamic_effects.md:928-939`
   correctly describes the GUI's direct equivalent path.
   Replace each GUI `if` body with its corresponding
   `ireland_execute_parliament_*_action = yes` call, or amend the comments and
   completion report to state that the GUI intentionally owns its equivalent
   PP debit. No current player-facing no-op, duplicate payment, AI-route,
   visibility, localisation, GFX, or action-grid overlap defect remains.

## Closure verification — 2026-08-12

This section supersedes the two unresolved findings in the preceding
implementation re-audit.

### Final verdict

**Accepted — no unresolved Parliament interaction defects remain.**

- The chamber rows now occupy local `y=90..107` and `108..125` within each
  126px chamber. They no longer intersect the parent boundary or the lower
  powers panel.
- Each GUI click handler calls its corresponding guarded
  `ireland_execute_parliament_*_action`; each AI-only native decision calls the
  same executor. Every executor owns one eligibility gate, one PP debit, one
  record helper, and the completion flag that disables repeat execution.
- The category/summary initialisation, 126x70 chamber assets, 204x32 action
  rectangles, separate 31px status frames, visibility gates, and AI-only
  native path remain correct.

Fresh read-only MCP inspection reached revision `eea11ae6ef3527ea` and
confirmed a parsable linked GUI graph with no visible-overlap diagnostic.
Fresh rendering covered the normal, hover, selected, locked, disabled, warning,
active, completed, empty/full, min/max, long-text, and missing-localisation
states at 1366x768 and 1920x1080. Artifacts: [inspection graph](hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/487d4709be3babe2a7fd1ec1439908ba6067f27c6f51839fd98e5de07938ff0a/a07c5b9f80a768ae15c2490ecab00dde1471221985f6f276fcee0588b043f861/gui-inspect.eea11ae6ef3527ea.json) and [full render](hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/f1fdaad8f48923124b9c0c735449a8f2fd0126c88de014efcb747d5afb443c7e/99d9da16e7b8365f122f6dddc9d8aa4565348a2d5b5838c41100e397f4382597/ireland_parliament_decision_ui_window-full.svg).

### MCP cost diagnostics — checked limitation

The four `GUI_COST_MISMATCH` messages remain a checker limitation, not a
payment defect. The checker requires a direct debit in each GUI handler and
does not follow the handler into `ireland_execute_parliament_*_action`. Each
shared executor contains the matching guarded
`constant:ireland.parliament_*_pp_delta`; its canonical availability trigger
uses the paired PP gate, and the visible labels match the central cost table.
The human and AI paths therefore charge once, never free-execute, and cannot
drift.

## State-seal re-audit — 2026-08-12

This section supersedes the prior accepted verdict for the four-frame state
seal addition.

### Verified

The one-seal-per-action surface is structurally sound. The four 32x32-frame
states are supplied by the registered 128x32 DDS, each action owns exactly one
pass-through state icon, and the current/available triggers are correctly
factored so the executor, button enablement, and frame selection use the same
requirements. The shared executor contract and the 204x32 button/status-column
geometry remain intact. Fresh MCP inspection revision `7efa20fde6ec3fcc` has no
overlap, alignment, clipping, spacing, or missing-asset diagnostic; its render
artifact is [here](hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/965590013ce89528f81de25146a533349082c8a6d3ce50a2b0aabbe95147fb0b/cc4a820b0eaeac82442b30fededbed641b9a380fc62b5e4325d7ec795ae1cd4c/ireland_parliament_decision_ui_window-full.svg).

### Exact unresolved defect — state seals can become stale at a PP threshold

`ireland_parliament_decision_ui` declares
`dirty = ireland_parliament_gui_dirty`; per the scripted-GUI dirty contract,
that means its `properties` (including the four state frames) update only when
that variable changes. `ireland_update_parliament` now recomputes a current
action’s frame from `has_political_power`, but its dirty comparison at
`common/scripted_effects/ireland_parliament.txt:92-100,236-251` tracks neither
the four previous state-frame variables nor Political Power. A daily PP gain
that crosses, for example, the Dáil 15 PP gate changes the source frame from
amber to gold without incrementing `ireland_parliament_gui_dirty`. The button
can therefore become enabled while its seal remains amber (and conversely
after an unrelated PP loss) until a separately tracked Parliament value
changes.

Fix this in `ireland_update_parliament` by snapshotting the four
`ireland_parliament_power_*_frame` variables before their recomputation and
adding their post-recomputation `not_equals` checks to the existing dirty OR
block. That gives each availability-state transition one property refresh
without returning to per-tick GUI updates. The four `GUI_COST_MISMATCH`
messages remain the already documented executor-indirection checker limitation,
not an additional defect.

## Final state-seal closure — 2026-08-12

This section supersedes the preceding state-seal finding.

**Final verdict: complete — no unresolved Parliament interaction, state,
alignment, visibility, cost, or AI-path defect remains.**

`ireland_update_parliament` now snapshots all four prior state-frame variables,
recomputes the Parliament stage before projecting the four seals, and compares
each projected frame in its dirty-condition OR. A stage transition and a PP
threshold transition therefore both increment `ireland_parliament_gui_dirty`,
refreshing the scripted-GUI properties exactly when the current/available seal
can change. The visual one-seal contract, shared human/AI executors, canonical
gates, and anti-double-charge behavior remain intact.

No gameplay or UI source was changed by this final audit. The only MCP design
messages are the documented `GUI_COST_MISMATCH` executor-indirection limitation;
they are not runtime defects.
