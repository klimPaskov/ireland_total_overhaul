# Continuous-focus position audit — 2026-08-09

## Scope and verdict

Read-only audit of the `ireland_focus_tree` continuous-focus anchor. No
gameplay, focus, interface, GFX, or localisation source was edited by this
audit. The only requested output is this handoff.

**Verdict: retain `continuous_focus_position = { x = 50 y = 2400 }`.** It is a
convenient and unobtrusive placement below the authored tree, and it does not
change the tree's focus coordinates, connector layout, or initial camera
position. The anchor is materially below the deepest focus row while matching
the normal vanilla x/y range for large trees.

## Source baseline

- `common/national_focus/ireland_focus_tree.txt:23` keeps
  `initial_show_position = { focus = ireland_state_still_defined }`.
- `common/national_focus/ireland_focus_tree.txt:26` sets
  `continuous_focus_position = { x = 50 y = 2400 }`.
- MCP inspection reports one national tree with 150 focuses, 14 generic
  continuous focuses, bounds `x=-24..38`, `y=0..16`, and one continuous
  palette. The deepest authored row is therefore row 16 of a 17-row tree.
- The worktree already contains concurrent changes from the parent and other
  agents. This audit did not revert or claim those changes.

## Evidence consulted

Repository and guidance:

- `AGENTS.md`.
- `.agents/skills/hoi4-focus-trees/SKILL.md`, especially the layout rule that
  continuous focuses must be placed somewhere convenient and the requirement
  to use MCP layout/render evidence for complex audits.
- The required offline wiki pages, including
  `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md` and the
  core data/trigger/effect/modifier/localisation/scope/on-action/event/
  decision/idea/AI pages. The national-focus page documents that
  `continuous_focus_position` is the **top-left corner in pixels**, with a
  default of `x=50 y=1000`, and that `initial_show_position` independently
  controls the first camera position.
- Vanilla documentation inventory under
  `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation`.
  There is no separate vanilla national-focus layout manual; the available
  documentation was checked for focus-tree tooling and engine behavior.

Vanilla source precedents for the same property include:

| Vanilla file | `continuous_focus_position` |
| --- | --- |
| `common/national_focus/argentina.txt` | `{ x = 200 y = 2300 }` |
| `common/national_focus/afghanistan.txt` | `{ x = 0 y = 2500 }` |
| `common/national_focus/austria.txt` | `{ x = 50 y = 2500 }` |
| `common/national_focus/chile.txt` | `{ x = 50 y = 2500 }` |
| `common/national_focus/spain.txt` | `{ x = 50 y = 2500 }` |
| `common/national_focus/sweden.txt` | `{ x = 50 y = 2500 }` |
| `common/national_focus/germany.txt` | `{ x = 500 y = 1300 }` |

The generic continuous palette itself remains at the vanilla default
`position = { x = 50 y = 1000 }` in
`common/continuous_focus/generic.txt`; the country-tree property is the
per-tree override.

## Geometry and unobtrusiveness

The offline wiki gives the focus-grid scale as 96 pixels per x unit and 130
pixels per y unit. The national MCP layout reports row 16 as the deepest
focus row, so its top anchor is approximately `16 * 130 = 2080` pixels. The
national render reports a `11216 x 2092` focus canvas before the raster's
review padding. The continuous palette render reports 14 entries and a
`1174 x 608` palette surface.

With the authored palette top-left at `(50, 2400)`:

- the palette begins roughly 308 pixels below the national render's reported
  bottom (`2400 - 2092`), or roughly 228 pixels below the raster output's
  reviewed bottom (`2400 - 2172` with the requested padding);
- the palette therefore does not occupy the row-16 focus area and cannot
  cover the last focus row or its prerequisite connectors;
- `x=50` is the same left anchor used by the generic palette and many vanilla
  country trees. Since the palette is below all focuses, this x value has no
  branch-overlap consequence;
- the palette's full rendered surface reaches approximately y=3008, which is
  a deliberate scrollable lower section rather than an overlap with the
  17-row authored tree.

This is a modest gap (about 1.7–2.5 focus-row heights depending on whether
review padding is counted), not a detached second tree. A lower value such as
`y=2250` could reduce scrolling, but would provide less separation from the
row-16 node and is not required by the current layout evidence.

## Camera and layout interaction

The property is a palette anchor, not a focus-node coordinate transform. MCP
national inspection keeps the same layout hash and reports:

- `crossingCount = 0`
- `nodeIntersectionCount = 0`
- `longConnectorCount = 0`
- `tooCloseSameRowPairCount = 0`
- `maximumHorizontalSpan = 8`
- `maximumVerticalSpan = 3`
- `diagnosticCount = 0`

The initial camera remains explicitly anchored to
`ireland_state_still_defined` at source line 23. Adding or retaining the
continuous palette position therefore does not move the first-open camera or
reflow the national focus nodes. Players will need to scroll downward to
reach the palette, which is expected for a menu intentionally placed below a
tall tree.

## MCP artifacts and validation

Workspace: `mod_ireland_total_overhaul_aaca88216c92`.

- National inspect (150-focus layout and diagnostics):
  [focus-inspect.e3a6dbf54659fc69.json](hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/3ca1558a3b879ffd558d5fdad951f222f71d92ff473ec325a545a6bc6082a758/65bd0cb5262b5ea5c9d64c933bc8b35f7bb06aacf657efbe5a70d84e56027e43/focus-inspect.e3a6dbf54659fc69.json)
- National structural render:
  [ireland_focus_tree.focus.html](hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/4b998600688da0effb679e604db8f8d965e0cb41d5e11a1a4c7a8ed20ac3092b/e48be564d21e5abd3608f0c555836b021301734fa9dcaa48154468f3bb2c7805/ireland_focus_tree.focus.html),
  [ireland_focus_tree.focus.svg](hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/5d0ac457bf131d40da0b1b10f063c7ad85504291b41a4352e2b1b2f492294361/6303fcb3a522f86bfccc414ccdf97e8c9033499ba038c6384203000dcb25ad5a/ireland_focus_tree.focus.svg),
  [ireland_focus_tree.focus.json](hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/d1b0d3a720839074c2ecd4599b20d410965e152d3091b699693f6e278d60e528/7df5d14986043465f5e8b7fb9054ad848df5a3d91bf54f9c7bc3a26bafd67125/ireland_focus_tree.focus.json)
- National high-fidelity raster:
  [ireland_focus_tree.focus.png](hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/e6121bda644e36b632f3336ea192adea60293f8f3deef53d8c2b365ee041c9bf/cb92306c73ff07c1e684074d6d9bd6197d598d2051c01e352cc9dea8c5b81f2a/ireland_focus_tree.focus.png)
- Continuous-palette inspect:
  [focus-inspect.e3a6dbf54659fc69.json](hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/30021c1d2e5fb2536ce0f1c7733608f43ed0bd389ca4b70ab93ce5ce692e9230/1b296f722bc65ffa6dab76227e06337aae5071f5a93e640ceb6837e2759c2786/focus-inspect.e3a6dbf54659fc69.json)
- Continuous-palette render:
  [generic_focus.continuous.html](hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/2ff10035e0c8488f63919ab7869be931b84258ee0d978933c500134456017f1f/d2606240088dde0fbca12235fc301fccf4b19d4afb5ffc7e4396b053626fd342/generic_focus.continuous.html),
  [generic_focus.continuous.svg](hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/668c9418c73fb424f12331f79dac66875ef038cfc39de57cc708a7f929a2a499/a609abc3c38ad0915b08099697bbc3f526a14f92b7c8a797cbe424efdde2b6a6/generic_focus.continuous.svg)
- Continuous-palette raster:
  [generic_focus.continuous.png](hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/11368ed83b4f42ff02f9f5620770fb51b08791212d6877d315cf736df7dda1f0/36632c3daaaf3f78b2a7f2f680dca09afd14aaa3071740d7b3806b7d448386d6/generic_focus.continuous.png)

The national structural inspection and continuous-palette inspection passed
their layout checks. The palette render reported only the pre-existing
vanilla `continuous_restrict_freedom_desc` localisation warning. The
high-fidelity raster additionally surfaced nine vanilla continuous-focus DDS
pixel-data truncation diagnostics for the game-supplied icons; these are
asset-validation issues outside this placement audit and do not implicate the
Ireland anchor or national-tree geometry.

Meaningful validation skipped: an in-game 16:9/ultrawide camera interaction
test was not available through the offline MCP artifacts. The source and
render evidence establish the anchor's relative placement and camera
independence, but the parent should still eyeball the palette after loading
the tree at the project's target UI scales. No source patch or fallback was
introduced.

## Parent handoff

No implementation action is required for this issue. Keep the current
`x=50, y=2400` anchor unless live review shows a project-specific scroll
preference; if that happens, test a small y-only adjustment while preserving
the independent `initial_show_position` focus anchor. Do not move the
continuous palette back to the generic default (`y=1000`), which would place
it in the middle of the authored branch lanes.
