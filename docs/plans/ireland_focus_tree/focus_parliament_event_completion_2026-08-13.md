# Ireland Focus, Parliament, and Event Programme Completion - 2026-08-13

> Historical snapshot notice: this report predates the current country-package
> integration and is superseded for counts, lifecycle contracts, and completion
> status by `docs/specs/ireland_country_package/index.md`,
> `docs/specs/ireland_country_package/implementation_matrix.md`, and the
> 2026-08-14 documentation-curator handoff. Its 150-focus inventory and
> earlier presentation evidence are retained as provenance only. At the time
> of this snapshot, final family-band evidence was unavailable; that historical
> state is superseded by the accepted `89ff719` family-lane handoff.

## Outcome

This implementation closes the current focus-tree layout and reward pass,
Parliament presentation and interaction pass, and report-event clarity and
cadence pass as one coherent player-facing package.

## National focus tree

- The tree contains 150 focuses, 150 connectors, and exactly three opening
  trunks: government and politics, national development, and defence and
  security.
- Coordinates occupy x `-26..21` and y `0..16`. Politics and industry use
  straighter vertical cores, while their shortcut cameras target
  `ireland_government_formation` and `ireland_development_authority`. Defence
  targets `ireland_maritime_protection`.
- Focus inspection revision `c449f5b90475357b` reports no crossing,
  connector-through-node, long-connector, or spacing defect. The only
  Ireland-local layout advisory is a two-column detour inside the concealed
  clerical-failure family; placing it directly under its parent creates a
  collision in the visible constitutional lane.
- All 150 focuses retain focus-specific reward tooltips. The direct reward
  union covers material deliveries, construction, fuel, equipment, research,
  doctrine, experience, claims, and named decision or mission unlocks. Political
  and institutional rewards name the actual gameplay surface they open instead
  of presenting implementation flags as rewards.
- Search filters match direct effects. Army, navy, and air experience filters
  match 11, 9, and 4 direct experience rewards respectively. All 23 research
  filters match a research or doctrine bonus. No manpower filter remains on a
  focus without a direct manpower, unit, or order-of-battle effect.

Focus inspection artifact:
`hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/ab0589809014e4ae6dcc4b3c9b3ef2acca67a058be59d7c35c99bc957dab2f69/08f2395c5aa9c69e9ec5b1fc6fc10ec336936e1a4f30d3e3bfe385620fa3dd21/focus-inspect.c449f5b90475357b.json`

Focus render artifact:
`hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/8d43b121a5ebaf13fa1ffc3bcacf102e010fdf9409b48a287bbc509d1fe91dec/ce7830f770cebc83495a50920d0ad090fd69f1ffbfe56da6ba0f7fcf4429b733/ireland_focus_tree.focus.html`

## Parliament

- The 510 by 248 panel keeps the chamber diagrams above a two-by-two action
  grid. The title, programme heading, chamber totals, party values, majority,
  opposition, costs, and Other-seat values use readable colour roles.
- The four stages use distinct Dáil document, Seanad harp, confidence book, and
  budget globe emblems, each with locked, unaffordable, current, and completed
  frames.
- Convening the Dáil is a free opening action after initialization and Irish
  ownership of Dublin. The National Settlement, Constitutional Draft, and
  Government Formation focuses then expose Seanad support, confidence, and
  joint-budget decisions in sequence at 25, 25, and 35 Political Power.
- GUI clicks and native decisions call the same guarded, idempotent executors.
  The panel therefore cannot disagree with decision availability or charge a
  different cost.

The final Parliament inspection and render evidence is recorded in
`docs/plans/ireland_focus_tree/subagent_handoffs/parliament_final_audit_2026-08-13.md`.

## Event programme

- The four Ireland event sources contain 495 top-level events and 998 unique
  choices. Every event has a picture; all 121 used picture sprites resolve to a
  registered GFX definition and an existing texture.
- Every choice calls a unique, nonempty `.effects` tooltip. Numeric choices
  calculate and print the exact signed post-clamp changes that will be applied.
  Fixed resource contributions name exact costs; state-only choices name their
  durable policy, route, review, or evidence outcome; timed reviews state their
  durations.
- Descriptions identify the actor, immediate situation, and country stakes.
  Choice wording no longer requires the player to infer effects from flags or
  vague ledger language.
- Ordinary reports run through `on_monthly_IRE`, present at most one eligible
  report, and skip the next monthly pulse after a successful dispatch. This
  bounds ordinary programme reports at six per year. Milestone events remain
  immediate.
- A source may open one 14-day foreign-reaction window after the 120-day global
  cooldown. The broker presents at most one unresolved actor response and, when
  necessary, one aggregate digest. Seen actor reports are durable and are not
  reset into replay loops.

The event cadence and tooltip contract is documented in
`docs/ireland_event_programme.md`.

## Assets

The Parliament pass adds four project-owned four-frame DDS strips under
`gfx/interface/ireland/gui/parliament/`, with source PNGs, processed PNGs,
manifest, contact sheet, and GFX handoff under
`docs/assets/ireland_parliament_panel/`. Existing sourced and generated event
art remains wired through the stable Ireland report and news sprite families.

## Meaningful validation

- Focus MCP revision `c449f5b90475357b`: 150 focuses, 150 connectors, no
  crossing, intersection, long-connector, or spacing defect.
- Focus filter/direct-effect parity: no false-positive or missing Army, Navy,
  Air, Research, or Manpower tag.
- Parliament audit: initial and later-stage controls resolve with distinct state
  art, shared executors, sequential native decisions, and no overlap or clipped
  click region.
- Event source audit: 495 pictures present, 121/121 picture sprites and textures
  resolve, 998/998 options have matching effect tooltips, and all 975 numeric
  option outcomes use event-precomputed exact applied deltas.
- Event MCP revision `f88d81d48a749e47`: no blocking event diagnostic in the
  large-workspace scan. The adapter defers workspace-wide helper projections;
  the Ireland-specific source audits above cover the exact option, image, and
  cadence contracts.

Event inspection artifact:
`hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/755f086be5e3f22ad68d72599da15704ac872abfdc2022938323e2a415e230be/c15b14931d98bd9f2f43aeb7126142563fd1e5cf2fc6120c39f5118d981096ab/event-lint-f88d81d48a74.json`

## Simplifications, omissions, and blockers

None. No fallback art, placeholder image, duplicate Parliament executor,
direction-only numeric event effect, extra opening focus trunk, generic reward
bundle, or replaying daily event queue remains in the completed package.
