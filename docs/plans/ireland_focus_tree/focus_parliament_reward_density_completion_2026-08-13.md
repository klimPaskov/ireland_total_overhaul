# Focus Density, Reward, and Parliament Completion - 2026-08-13

## Outcome

This tranche corrects the three reported surfaces together:

- the national tree keeps exactly three opening trunks while reducing its
  horizontal span from 82 columns to 41;
- all 150 focuses expose a focus-specific completion outcome, and the material
  lanes add real equipment, construction, industrial, fuel, and research deliveries; and
- the Parliament surface shows its four programme controls from initialization,
  provides a usable starting Dáil action, and uses
  stronger text hierarchy and colour.

## Focus layout

The source retains 150 focuses, 150 connectors, and the three opening roots
`ireland_state_still_defined`, `ireland_economic_war_review`, and
`ireland_defence_estimates`. Authored coordinates now occupy x `-20..21` and y
`0..16`. Culture, diplomacy, Northern policy, naval work, constitutional
alternatives, and exceptional routes remain progressively revealed rather than
becoming extra opening trunks.

Focus inspection revision `b1c47582375c4bad` reports zero connector crossings,
zero connector-through-node intersections, zero long connectors, zero same-row
spacing defects, a maximum horizontal connector span of seven, and a maximum
vertical span of two.

Inspect artifact:
`hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/38eaf03718c2057898eaab76ca811b380b412a07dc8d61190231e212dc1e09bc/905da3cd351731b79e9f6725233efad61df2e9a31bee5a3988fe0975750c2720/focus-inspect.b1c47582375c4bad.json`

Render artifact:
`hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/92d07d264a68b616d43ed374a60c688281c0e9abe57baa9fc0125d0859954c12/676be3973e1ff0ed8c9b9e274a097cd3b95d3db4b09a69484f84e236d64ef64a/ireland_focus_tree.focus.html`

## Reward contract

Every focus calls its own `ireland_<focus>_reward_tt` key. All 150 keys resolve
and describe the actual player-facing outcome: a named category, action,
mission, route commitment, institutional transition, physical project, or
conclusion review. No completion is presented as an unexplained flag or
recompute helper.

The direct reward union now covers 46 focuses: 32 have material, construction,
or fuel effects; 24 have research, doctrine, agency, or event capabilities;
one records Ireland's legal claim to Northern Ireland without granting a core
or control;
and 59 focus IDs expose named decision or mission unlocks. These classes
overlap where a project both delivers capacity and opens playable work.

- development and defence trunks provide bounded factories, infrastructure,
  fuel, radar, anti-air defence, rifles, support equipment, trucks, trains, and
  convoys;
- capability focuses provide one-use 50% industry, support, electronics,
  artillery, naval, and doctrine bonuses rather than more factories; and
- cultural, constitutional, foreign, Northern, and exceptional focuses expose
  60 native unlock tooltips for 58 existing decisions and missions.

The amounts are bounded file-local constants. Political, cultural, foreign,
Northern, and exceptional routes do not receive arbitrary factories: their
tooltips name the existing decisions, missions, institutional profiles, and
reviews that their completion flags actually unlock.

## Parliament behaviour

The `510x248` Parliament panel keeps its two `247x126` chamber cards and four
`204x32` programme buttons. The title is moved from y `1` to y `4` and changed
from black to the white `hoi_16mbs` font. Chamber parties, support values,
majorities, opposition, costs, and the programme header use distinct colour
roles.

The lower programme panel is now visible whenever the Parliament surface is
open. The four redundant per-button visibility triggers were removed, so the
panel can no longer show only seals while hiding its controls. Each control
remains locked by its canonical `*_action_available` trigger and still calls
the guarded shared executor; no cost or effect is duplicated.

The first Dáil action is available from initialization for 15 Political Power
through both the category and the scripted GUI. Both call the same guarded,
idempotent executor. Convening the Dáil records the first sitting and opens the
National Settlement focus; that focus advances the programme to Seanad support.
The Constitutional Draft and Government Formation focuses gate the confidence
compact and joint budget stages respectively.

GUI inspection artifact:
`hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/73c95f48e5bd3e7e39d3de317b1b255b9c2ee9a74b2380dd1934e7398c1791e8/7cf73984dfd95fa45447ca63b1248cdae9cc36d203f1a0a6fe7caa16df305bff/gui-inspect.3afccc6805fec771.json`

GUI render artifact:
`hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/9a4d05d71d3da947f271917a80ff70f41efc3023cd952119c17f9b6c6aa5c53d/841b57e1febfe485571063de136297b80331197fa9264c057e9e6b2df73c18be/ireland_parliament_decision_ui_window-full.svg`

The GUI analyzer's four cost notices are a known static-analysis limitation: it
does not follow the click effect into the shared executor. The executor owns the
15/25/25/35 Political Power debits and repeats the same availability test used
by the buttons and AI decisions.

## Files and systems changed

- `common/national_focus/ireland_focus_tree.txt`
- `common/decisions/categories/ireland_categories.txt`
- `common/decisions/ireland_decisions.txt`
- `common/scripted_effects/ireland_parliament.txt`
- `common/scripted_guis/ireland_scripted_guis.txt`
- `common/scripted_triggers/ireland_parliament.txt`
- `interface/ireland_parliament_scripted_gui.gui`
- `localisation/english/ireland_l_english.yml`
- focus reward and canonical feature documentation under `docs/`

No new visual asset was required. The existing Parliament background, chamber
sprites, four-state seals, and button texture remain the final art package.

## Simplifications, omissions, and blockers

None. No fallback, placeholder, duplicate executor, generic reward bundle,
additional opening trunk, free Northern territory/core, or silent route bypass
was introduced.
