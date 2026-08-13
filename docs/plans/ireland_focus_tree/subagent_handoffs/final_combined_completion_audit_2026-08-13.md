# Final combined completion audit — 2026-08-13

Feature slug: `ireland_focus_tree`

Audit mode: read-only gameplay/source audit. This handoff is the only file
written by the completion auditor.

## Verdict

**Complete at the requested static-source, asset, localisation, and offline
render boundary.** The final frozen source satisfies the combined focus-tree,
Parliament, event-clarity, event-art, and event-cadence correction. No requested
route, control, event, choice, image, tooltip, cooldown, AI entry path, or
documentation update remains omitted or blocked.

There is one disclosed nonblocking layout residual: the concealed
`ireland_clerical_failure_bridge -> ireland_clerical_guardianship` connector
moves two columns over one row. It is neither long nor crossing, and removing
the offset would collide with the visible constitutional lane. No fallback or
substitute implementation was used.

## Completion by surface

| Surface | Status | Final evidence |
| --- | --- | --- |
| Focus layout and navigation | complete | `common/national_focus/ireland_focus_tree.txt`; final MCP revision `c449f5b90475357b1f3730c6d3065c3d444a8e190ecddc72b87b40239e27d967` |
| Focus search filters | complete | direct reward/filter parity audit over all 150 focus blocks |
| Parliament presentation and interaction | complete | GUI, scripted-GUI, triggers, executors, native decisions, localisation, and four distinct runtime sprites |
| Event inventory and player clarity | complete | four Ireland event files, 495 top-level events, 998 choices and 998 matching effect tooltips |
| Event images | complete | 495 picture references through 121 unique registered, existing, correctly sized DDS assets |
| Ordinary and foreign event cadence | complete | monthly ordinary dispatcher with a one-pulse cooldown; one actor per foreign window, optional digest, and 120-day admission cooldown |
| Active documentation | complete | current completion reports, source-of-truth map, event programme, systems document, and focus/event maps agree with final source |

## Focus tree

The source contains 150 focuses and 150 connectors. Only the government and
politics, national development, and defence and security trunks are visible at
the opening; the other no-prerequisite families remain behind their authored
`allow_branch` reveal conditions. The three navigation shortcuts target useful
branch centres rather than roots:

- politics -> `ireland_government_formation` at `0.66`;
- industry -> `ireland_development_authority` at `0.66`;
- defence -> `ireland_maritime_protection` at `0.70`.

Final focus inspection passed with bounds x `-26..21`, y `0..16`, zero connector
crossings, zero connector-through-node intersections, zero long connectors,
zero same-row spacing defects, maximum horizontal span 6, and maximum vertical
span 2. The sole Ireland diagnostic is the disclosed concealed clerical detour.
The other warning belongs to vanilla `continuous_restrict_freedom_desc` and is
not an Ireland source defect.

Final focus evidence:

- inspect: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/ab0589809014e4ae6dcc4b3c9b3ef2acca67a058be59d7c35c99bc957dab2f69/08f2395c5aa9c69e9ec5b1fc6fc10ec336936e1a4f30d3e3bfe385620fa3dd21/focus-inspect.c449f5b90475357b.json`;
- HTML render: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/8999bc9a5cb559400cd0db93dbff70801b0c01a82ad370546f7aebb150a1d981/e669f6d02d40f161cda19cafddbfaa9360d6ef7a46d5c2e384136f9b8932b3b1/ireland_focus_tree.focus.html`;
- SVG render: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/48f72d38181f34356877accc12e866b432595198497fac9d247f870e85995e20/39ac3e982cae0a79560816c53d8a1080a2bc3bab53f9d54b374b34356de5c016/ireland_focus_tree.focus.svg`.

The direct completion-reward audit found exact tag/effect parity and no false
positive or false negative for the filters the correction made effect-strict:

| Filter | Tagged / direct grants | Mismatches |
| --- | ---: | ---: |
| Army XP | 11 / 11 | 0 |
| Navy XP | 9 / 9 | 0 |
| Air XP | 4 / 4 | 0 |
| Research/doctrine | 23 / 23 | 0 |
| Manpower/unit grants | 0 / 0 | 0 |

The earlier cultural/evidence research false positives and semantic manpower
tags are absent. Industry, trade, balance-of-power, historical, and political
tags remain only on focuses whose direct outcome belongs to those player-facing
domains; no XP tag is being used as a topical branch label.

## Parliament

The final panel is `510x248`. The title is at y `7` in `vic_18_black` on the
light parchment rail. Chamber cards begin below the title, and the two action
rows fit inside the lower programme panel. The opening-state GUI inspection
found no `GUI_VISIBLE_OVERLAP` among the 22 inspected elements. The Dáil
composition uses distinct green/blue/red/yellow roles and the compact `Oth`
label, so Other seats remain legible; support, majority, opposition, and total
values have distinct colour roles.

The four action seals are separate four-frame DDS assets and have distinct
SHA-256 hashes:

- Dáil: `57841484260DE9223065EF5553F592DDB2D2AB39DB16BA87C7FC136AC206B80A`;
- Seanad: `BF006B9DB2ADE1B0C260682E96FF7689FDBCC0DBFACBD1DB6F2E69D013284A2F`;
- confidence: `F1DD65B6BDA364E4DE0033E65D95977DF0BC12EECB67E69A0B9AB785D0901E7F`;
- budget: `9215252359BBD1084B21BE8F757387A2228F27B92FFF5BD4EFA0A96802C4D154`.

The action lifecycle is a single guarded sequence shared by GUI clicks and
human-visible native decisions:

1. Dáil is current at programme stage 1, has no Political Power gate, costs
   `0`, and is usable from initialization while Ireland owns Dublin/state 113.
2. Seanad becomes current after the Dáil record and National Settlement focus;
   it costs `25` Political Power.
3. Confidence becomes current after Seanad and Constitutional Draft; it costs
   `25` Political Power.
4. Joint budget becomes current after confidence and Government Formation; it
   costs `35` Political Power.

Each native decision is `fire_only_once`, uses the same canonical current and
available triggers as the GUI, and calls the same idempotent executor. Completion
flags advance the programme stage in order, so there is no duplicate or
overlapping human path.

Final GUI evidence:

- inspection revision `ee085bc27a15282024bf9252587b133bf6671bac5ad065136862e29a593901b3`:
  `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/df2e8921ca87c8d4245218ee9bbfea9decdbbc5901fa0f0d6db563ba88f17f04/cefc82fb5f763a1011c85daec4ce641a44a280c8df684ba788fffce0fbc06b63/gui-inspect.ee085bc27a152820.json`;
- 1920x1080 and 2560x1440/state render:
  `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/ff7841afabbb80b192d3cadd922b94d9dbb720b1e0f971248fcf61ae0cc26345/ab25f799c46dc944ae268e9a866b87ea2f9766bb8138f69ec6f94d989bfe25b8/ireland_parliament_decision_ui_window-full.svg`.

The GUI analyzer reports three apparent 25/25/35 cost mismatches because it
does not follow the click wrapper into the shared executor. Direct source review
confirms that those executors debit `parliament_seanad_pp_delta`,
`parliament_confidence_pp_delta`, and `parliament_budget_pp_delta`. It also does
not execute `buttonstate.lua` or engine text-sprite generation. These are bounded
offline-tool limitations, not implementation defects.

## Events, choices, localisation, and images

The frozen inventory is:

- `events/ireland_route_events.txt`: 256 events;
- `events/ireland_flavour_events.txt`: 236 events;
- `events/ireland_member_contribution_events.txt`: 1 event;
- `events/ireland_public_conclusion_events.txt`: 2 events;
- total: 495 unique top-level event IDs and 998 unique option keys.

Every event has a nonempty title, description, and picture reference. Every
choice has exactly one `custom_effect_tooltip`, it is the matching
`<option-key>.effects` key, and all 495 titles, 495 descriptions, 998 options,
and 998 effect keys resolve in English localisation.

The exact-effect classification is complete:

- 975 choices that change numeric values show exact signed, post-clamp applied
  deltas;
- those strings contain 1,899 preview-variable references, and every reference
  is assigned inside the same owning top-level event before the options appear;
- five member-contribution choices state their exact fixed Political Power,
  Command Power, equipment, manpower, fuel, train, truck, and convoy costs;
- the remaining 18 choices are state/flag-only outcomes and name the record,
  closure, transition, or failure they create; the 14-day observation and
  180-day conclusion-review durations are explicit.

Descriptions are 17–69 words (average 31.9) and identify the actor, immediate
problem, and stakes. Option text is 3–16 words (average 7.8) and states the
policy being adopted. The captured-crown third option now computes its three
preview deltas in event 623 itself; no preview value is inherited from another
event.

All 495 picture references resolve through 121 unique sprites: 102 report-event
sprites at `210x176` and 19 news-event sprites at `397x153`. Each referenced
sprite has exactly one definition, each texture path exists, and no referenced
DDS has a bad header or wrong dimensions. No missing-image fallback or
placeholder is part of this event set.

The final narrow event-tool refresh is supplemental because the tool deferred
workspace-wide helper/lifecycle projections in this large mod; it reports no
blocking diagnostic or skipped source:
`hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/04e22b9bdc6182d60c40f0713c9fcbb5f643479ac6ce1507bb67d57a44e82d94/b82e305b29cafc1fa491bfa865edf4c50723e5355b9a795381b48e14ef64e0df/event-scan-f88d81d48a74.json`.

## Cadence, replay, and reachability

`on_daily_IRE` performs runtime reviews and window ticking but does not call the
ordinary dispatcher. `on_monthly_IRE` is the sole ordinary programme pulse.
The dispatcher contains 457 unique ordinary event calls, each guarded by its
durable seen flag and the one-dispatch-per-pulse flag; it then sets a one-month
cooldown. Foreign events 400–430 are absent from this queue. The resulting
ordinary ceiling is six reports per year.

The foreign broker opens a 14-day window only when no window is active, the
route is open, and the 120-day timed admission flag is absent. Four days pass
before the day-10 response point. The response helper sets its one-shot
`response_dispatched` flag before entering a 30-entry random list. All 30 actor
events have an availability setter, all 30 occur exactly once in that list, and
all 30 write their durable `ireland_event_seen_400..429` record when shown.
Those seen records are never cleared when a new reaction window opens.

There are 12 actor roots and 18 chained actor nodes. Each chained availability
gate requires the predecessor's resolved flag, and the predecessor event writes
that flag in its closing block. Thus no actor report is structurally orphaned.
Unselected nodes remain unseen and eligible for later valid windows; selected
nodes cannot replay. The visible count is capped at one. If other eligible
responses remain, one digest is scheduled after the window closes; the digest
is a new aggregate of that window's pending responses, not a replay of an actor
report, and its scheduling flag prevents duplicate digests in the same window.

## Plans and documentation disposition

- `ireland_focus_tree_parliament_correction_addendum_2026-08-11.md` is
  implemented; its older seven-shortcut/opening presentation was explicitly
  superseded by the user's three-trunk correction.
- `ireland_focus_tree_concrete_reward_density_addendum_2026-08-13.md` is
  implemented and promoted into the spec/index, source-of-truth map, and current
  completion report.
- `ireland_focus_tree_layout_reveal_addendum_2026-08-09.md` is superseded by
  the correction addendum and final source layout.
- `ireland_focus_tree_parliament_improvement_addendum_2026-08-05.md` is
  superseded, implemented, and reconciled.
- `ireland_focus_tree_next_pass_addendum_2026-08-06.md` is historical planning
  for the former 211-focus worktree; the implemented 150-focus reports supersede
  its inventory and reduction work. It contains no unresolved current-scope
  implementation item.

The active documents now use `events/ireland_route_events.txt`, record 256 main
events, three opening trunks, free opening Dáil action, sequential human native
decisions, the one concealed clerical detour, 495 events/998 choices, exact
preview semantics, monthly ordinary cadence, one actor/optional digest, and the
120-day foreign admission cooldown. Older snapshots that retain historical
counts or presentation are explicitly marked superseded or historical and are
not current completion claims.

## Simplifications, omissions, blockers, and next actions

Blocking simplifications, omissions, and blockers: **none**.

Nonblocking disclosed residuals and evidence limits:

- one concealed two-column clerical connector detour remains by deliberate
  collision avoidance; there is no long connector, crossing, node intersection,
  or spacing defect;
- the offline GUI analyzer cannot follow wrapper-to-executor Political Power
  costs or render engine text/button-state effects;
- the event MCP refresh is partial at workspace scale, so exact event counts,
  tooltip ownership, art resolution, dispatcher uniqueness, replay, and chain
  reachability are established by the narrower source audits above.

No asset gap remains for the requested surfaces. Additional family-specific
archival image variety in `docs/ireland_event_programme.md` is an optional future
extension, not a missing image or current completion requirement.

Recommended next action: commit the reviewed correction. A new
`hoi4_improvement_loop_planner` pass is **not recommended**: accepted depth
addenda are implemented or superseded, and the remaining optional art-variety
idea does not justify expanding this already complete correction.
