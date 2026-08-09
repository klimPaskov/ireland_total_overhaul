# Parliament GUI visual audit — 2026-08-09

## Scope and baseline

Read-only audit of the Parliament decision-category header. No gameplay, GUI,
GFX, localisation, or asset source was edited by this audit.

The requested `ff5b4a8` object is not reachable in the local repository. The
pre-redesign baseline was instead recovered from `HEAD` before concurrent
redesign work touched the worktree:

- GUI blob: `1c487d627d37a69a88c2b53f64a631fa22531cab`
- GFX blob: `eb5652c21e372f54985fa21a9c531ef855b3d9b1`
- Baseline GUI source: `interface/ireland_parliament_scripted_gui.gui`

The proposal below is for that baseline. Concurrent modifications to the GUI,
GFX, localisation, and the generated panel asset appeared after baseline
capture; they are not reverted or claimed as this audit's work.

## Evidence consulted

- `interface/ireland_parliament_scripted_gui.gui` baseline: a 198 px header
  with two right-aligned chamber sprites and a separate four-checkbox row.
- `common/scripted_guis/ireland_scripted_guis.txt`:
  `ireland_parliament_decision_ui` only maps the two chamber frame variables
  and four institutional-state frame variables. It contains no `effects` and
  no GUI button path.
- `common/scripted_effects/ireland_parliament.txt`:
  `ireland_update_parliament` maintains 21-frame Dáil/Seanad support sprites
  and the four two-frame institutional states; it dirties the GUI only when a
  displayed ledger changes.
- `common/decisions/categories/ireland_categories.txt` and
  `common/decisions/ireland_decisions.txt`: native decisions are the sole
  owners of cost, availability, AI, and completion:
  `ireland_action_convene_the_dail`,
  `ireland_action_negotiate_seanad_support`,
  `ireland_action_secure_a_confidence_compact`, and
  `ireland_action_pass_a_joint_budget`.
- Vanilla references:
  `interface/usa_congress_scripted_gui.gui` establishes the compact,
  decision-category chamber-summary pattern; its scripted GUI drives only
  sprite frames. `interface/AST_cabinet_trust_scripted_gui.gui` establishes a
  visual institutional-state strip with distinct state visuals and tooltips.
- Offline Paradox wiki pages for Interface Modding and Scripted GUI Modding:
  layering is source order, `iconType` supports property-driven frames, and
  `decision_category` GUI is embedded in the category description host.
  The broader required data, trigger, effect, scope, localisation, decision,
  modifier, idea, AI, event, and on-action pages were also consulted.

### GUI MCP evidence

`hoi4.gui_inspect` was called for workspace
`mod_ireland_total_overhaul_aaca88216c92`, first with the Parliament window
and then without a selector. `hoi4.gui_render` was also called for
`ireland_parliament_decision_ui_window` at 1920x1080 and 1366x768 with normal,
locked, active, completed, and long-text scenarios. All three usable MCP
requests failed before inspection/render with `Transport closed`; therefore
there is no MCP artifact URI or fidelity score. The findings are source- and
asset-backed rather than a substitute visual render.

The concurrently supplied [510x198 panel PNG](../../../assets/ireland_parliament_panel/processed_png/parliament_summary_background_510x198.png)
was inspected directly. It has a light parchment upper field and dark green
lower band, which is suitable for the hierarchy below but creates a hard
contrast requirement: white `hoi_*` text is not acceptable on the parchment.

## Issues, sorted by severity

### Critical — the baseline has no readable hierarchy

The baseline uses the whole left side as a single text ledger and puts both
support sprites at the far right. Dáil data is at y=0–60 and Seanad data at
y=61–121, with no left/right chamber distinction. It reads as two stacked
debug rows, not as a bicameral institution. There is no panel identity, card
structure, or visual separation between chamber support and the legislative
sequence.

### Critical — the four institutional states are four unrelated checkboxes

The baseline labels sit at y=148 and the status boxes at y=165. Even though
their x-centres are evenly spaced, no rail or grouped stage surface explains
the intended order: Dáil sitting -> Seanad support -> confidence compact ->
joint budget. The player must infer that four isolated red/green checkboxes
are a programme sequence.

### High — no fixed 510 px art contract or contrast plan

The baseline window uses `width = 100%` while the host is only documented as
510 px. This prevents pixel-authored panel art from being a reliable design
surface. The newly supplied 510x198 parchment/leather panel makes the problem
more visible: default white `hoi_18mbs`/`hoi_16mbs` text will lose contrast in
the light upper field. Use a dark font such as `vic_18_black` for the title and
chamber text; retain white `hoi_16mbs` only in the dark lower progress band.

### Medium — chamber support is technically dynamic but visually secondary

The 21-frame Dáil and Seanad sprites are correct gameplay indicators, but the
baseline treats them as edge decoration. Their numeric majority value and
composition are not spatially associated with their own chamber illustration.
The two frames should be the visual centre of two equal chamber areas, with
the number immediately below each frame.

### Medium — composition abbreviations need one explicit legend

`FF`, `FG`, `Lab`, and `Oth` are compact enough for the surface, but
`ireland_parliament_dail_composition_tt` currently describes the aggregate
without expanding those abbreviations. Keep the compact row, but make its
tooltip name Fianna Fáil, Fine Gael, Labour, and Others.

### Low — current generic state tooltip is not step-specific

The checkbox tooltip only says that red is pending and green is secured. The
individual label tooltips already provide the action meaning, so retain them;
do not add click handlers to the state marks.

## Exact 510x198 hierarchy proposal

This is deliberately a summary above the native rows, not a second control
surface. It uses the supplied 510x198 background as a decorative base and
keeps all interactive gameplay in the four native decisions.

| Layer / element | Exact bounds or position | Presentation and responsibility |
| --- | --- | --- |
| Root | `0,0,510,198` | Set the container to a literal `width = 510`, `height = 198`; this matches the decision-category host and panel art. |
| Decorative background | `0,0,510,198` | `GFX_ireland_parliament_summary_background`, `alwaystransparent = yes`. The upper parchment is chamber information; the lower green band is the institutional sequence. |
| Identity band | `x=0, y=1, w=510, h=20` | Centred static title, e.g. `ireland_parliament_title`. Use a dark 18 px font. This identifies the surface before the player reads numbers. |
| Dáil chamber field | `x=4, y=23, w=247, h=105` | Left half of the upper field. Header at `4,23`, frame at `80,39` (the 94x50 vanilla 21-frame sprite), support at `4,91`, composition at `4,110`. Centre-align all four elements. |
| Seanad chamber field | `x=259, y=23, w=247, h=105` | Right half, mirrored to the Dáil. Header at `259,23`, frame at `337,39` with `scale = 0.7` (the 132x73 source becomes approximately 92x51), support at `259,91`, composition at `259,110`. Centre-align all four elements. |
| Sequence heading | `x=0, y=130, w=510, h=16` | Centred white text on the dark band: `ireland_parliament_powers_header`. It names the lower area as a sequence rather than a spare status row. |
| Sequence rail | `x=45, y=148, w=420, h=30` | A passive row/rail behind the four state markers. It must be art only and never a button. The supplied background already provides the broad band; a thin shared-row sprite is sufficient if a visible rail is wanted. |
| Four state markers | top-lefts `(49,148)`, `(176,148)`, `(303,148)`, `(430,148)` | Preserve the existing `GFX_checkbox_small_red_green` marker ids and property mappings. Its 62x31 two-frame DDS gives four 31x31 markers, perfectly centred beneath the 125 px label columns. Frame 1 is pending and frame 2 is secured. |
| Four state labels | `(2,180,125,16)`, `(129,180,125,16)`, `(256,180,125,16)`, `(383,180,125,16)` | White, centred text in chronological order: Dáil sitting, Seanad support, Confidence compact, Joint budget. Keep each existing action-specific tooltip on its label. |
| Native decision rows | begin below `y=198` | The first visible native decision remains the only route to changing state. No GUI element may occupy this vertical range. |

Rendering order must be: background, title and chamber headers, chamber
support frames, chamber numeric/composition text, rail, markers, then lower
labels. This makes the data read as identity -> two live chambers -> one
four-step governmental programme.

## State and interaction contract

- Preserve `dail_icon` and `seanad_icon` exactly. Their `frame` properties
  already use `ireland_dail_icon_frame` and `ireland_seanad_icon_frame`, which
  are calculated from live support ratios and clamped to the 1–21 frame range.
- Preserve the four existing marker identifiers and their properties:
  `ireland_parliament_power_dail_state`,
  `ireland_parliament_power_seanad_state`,
  `ireland_parliament_power_confidence_state`, and
  `ireland_parliament_power_budget_state`.
- Preserve `context_type = decision_category`, `dirty =
  ireland_parliament_gui_dirty`, current `visible`, and
  `visible_when_empty = yes`. The category is intended to show from campaign
  initialization, including the short pre-focus interval before
  `ireland_settlement_open` exposes the first native decision.
- Do not add `buttonType`, scripted-GUI `effects`, GUI costs, GUI availability,
  or GUI AI weights. Decorative icons stay `alwaystransparent = yes`; text
  remains a tooltip target only. This preserves native decisions as the sole
  click owners.

## Are scripting or property changes needed?

No gameplay scripting, trigger, event, decision, AI, or property changes are
needed for this hierarchy. Existing properties supply both dynamic chamber
frames and all four institutional states; `ireland_update_parliament` already
initializes and refreshes them.

Implementation only needs:

1. the GUI layout and its literal 510x198 root;
2. the existing/static background sprite registration if the panel art is
   accepted;
3. a title localisation key and the expanded Dáil-abbreviation tooltip;
4. font selection that keeps upper parchment text dark and lower-band text
   light.

Do not rename the six property-bound element ids unless the matching
`properties` entries are changed in the same patch. No new property entry is
required for the title, background, or passive rail.

## Decision category lifecycle notes

`ireland_settlement_government` is allowed for original IRE, visible through
`ireland_parliament_open`, and intentionally `visible_when_empty = yes`.
`ireland_parliament_open` requires initialization and closes on
`ireland_route_archived`. The four native opening decisions are one-time,
sequentially revealed, remove themselves when the route is archived, and
advance the retained `ireland_parliament_stage` from 1 through 5. The GUI
correctly becomes an all-secured historical summary after the joint budget;
do not hide it merely because all four opening steps are complete.

## Mission quality notes

No Parliament GUI-owned timed mission exists. The audited surface represents
four native opening decisions, not missions; therefore owner/category/region/
duration/success/failure/duplicate-risk fields are not applicable here. The
nearby settlement missions remain native decision-category content and are
not duplicated by the GUI.

## Cost and requirement clarity notes

The opening actions retain their native political-power costs (15, 25, 25,
and 35) and custom requirement tooltips. The read-only header should not echo
or spend those costs: the currently visible native action directly below the
summary is the authoritative cost and availability surface. This avoids a
second, potentially stale cost display.

## AI validity and route-lock notes

The GUI has no click effects, so it introduces no AI action, target, or
route-lock risk. Native decisions retain their IRE, archive, settlement,
stage, Dáil/Seanad-majority, PP, and Leinster checks. Keeping the header
visible does not expose an invalid action; the underlying decision visibility
and availability checks remain authoritative.

## Localisation and tooltip gaps

- Add the static title only if the redesign uses the identity band:
  `ireland_parliament_title`.
- Expand the Dáil bloc abbreviations in
  `ireland_parliament_dail_composition_tt`.
- Keep `ireland_parliament_dail_status_tt`,
  `ireland_parliament_seanad_status_tt`, the two composition tooltips, and the
  four individual state-label tooltips. They already describe current values
  and the four institutional actions without exposing raw triggers.

## Cleanup and exploit-risk notes

No GUI-owned flags, variables, targets, costs, missions, or effects exist, so
the surface introduces no cleanup or farming loop. Route archival hides both
the category/window and opening decisions. Retaining this read-only contract
is the primary exploit safeguard.

## Recommended implementation files and identifiers

| File | Change | Identifiers |
| --- | --- | --- |
| `interface/ireland_parliament_scripted_gui.gui` | Replace the baseline stacked header with the exact hierarchy above. | `ireland_parliament_decision_ui_window`, `dail_icon`, `seanad_icon`, four existing state ids. |
| `interface/ireland_gui_assets.gfx` | Register only the accepted static 510x198 backdrop. | `GFX_ireland_parliament_summary_background` |
| `gfx/interface/ireland/gui/parliament/parliament_summary_background.dds` | Use the accepted decorative backdrop if it passes contrast review. | `parliament_summary_background` |
| `localisation/english/ireland_l_english.yml` | Add title and expand the composition tooltip; preserve UTF-8 BOM. | `ireland_parliament_title`, `ireland_parliament_dail_composition_tt` |

`common/scripted_guis/ireland_scripted_guis.txt`,
`common/scripted_effects/ireland_parliament.txt`, the decision category, and
the four native decisions require no change for the proposed visual hierarchy.

## Validation and remaining uncertainty

Meaningful validation performed: source-level geometry was checked against the
actual asset dimensions. The Dáil source is 1974x50 / 21 frames = 94x50; the
Seanad source is 2772x73 / 21 frames = 132x73; the four-state sprite is 62x31
/ 2 frames = 31x31; and the proposed panel asset is exactly 510x198. All
proposed positions fit inside the container without covering the decision
rows.

Meaningful validation skipped: deterministic GUI render/click-region review
could not run because the installed HOI4 MCP transport closed. Resolution,
long-localisation, hover, and live in-game fidelity therefore remain to be
reviewed once that service is available. In particular, verify dark text on
the parchment, white text on the lower leather band, and no overflow from
localized chamber names.

No simplification or fallback was introduced by this audit.
