# Cabinet Briefing scripted-system handoff

> Parent closure: the focus-inlay button was subsequently removed because the focus-inlay API can disable but not conditionally hide it. The decision-category briefing retains the single guarded Parliament action; the inlay is intentionally informational.

Date: 2026-08-15
Owner: `hoi4_scripted_system_architect`
Scope: helper and binding changes for the accepted four-indicator Cabinet Briefing

## Result

The active National Situation scripted GUI is now a compact, presentation-only
surface with four strategic status cards:

| Card | Authoritative source | Public status predicates |
| --- | --- | --- |
| Government | constitutional settlement and parliamentary programme | `ireland_briefing_government_{ready,warning,critical,locked}` |
| National Supply | Provision aggregate and canonical bottleneck predicates | `ireland_briefing_supply_{ready,warning,critical,locked}` |
| Defence Readiness | Readiness aggregate and canonical bottleneck predicates | `ireland_briefing_defence_{ready,warning,critical,locked}` |
| National Question | authored Northern reveal and settlement ledger state | `ireland_briefing_northern_{ready,warning,critical,locked}` |

The only Cabinet Briefing action is `ireland_briefing_context_action`. It is
available only when `ireland_next_state_action_available` finds the next
canonical Parliament programme step and the route is open. Dispatch order is
Dáil, Seanad, confidence, then joint budget. Each destination executor repeats
its own guard and owns its normal costs/effects.

## Files changed

- `common/scripted_guis/ireland_scripted_guis.txt` — replaced the active
  `ireland_national_situation_scripted_gui` bindings with the four status families
  and one guarded context action. AI remains disabled.
- `common/scripted_triggers/ireland_mechanics_hub.txt` — defines the four card
  contracts, shared status bands, open/archive gate, and next-Parliament action
  availability. Existing aggregate variables, reveal predicates, flags, and
  thresholds remain authoritative.
- `common/scripted_effects/ireland_mechanics_hub.txt` — retains the public
  `ireland_execute_next_state_action` adapter and limits it to canonical guarded
  Parliament executors; refresh, row-selection, and review adapters were removed.
- `common/focus_inlay_windows/ireland_national_situation_inlay.txt` — exposes
  `ireland_focus_briefing_{government,supply,defence,northern}_status` scripted
  images and `ireland_focus_briefing_context_action`. National Question has an
  explicit locked fallback matching the parent interface's always-present card.

No interface, localisation, decision, focus-tree, asset, or thumbnail file was
changed by this handoff.

## Helper map

| Helper | Scope and inputs | Output | Side effects and call sites |
| --- | --- | --- | --- |
| `ireland_mechanics_hub_open` | Country scope; initialized original-tag Ireland, not `ireland_route_archived` | active/open predicate | Used by `ireland_next_state_action_available`; does not mutate state |
| `ireland_mechanics_hub_{state,provision,readiness,northern}_*` | Country scope; existing settlement, aggregate, reveal, focus, flag, and threshold state | family visibility and ready/warning/critical/locked predicates | Read by public `ireland_briefing_*` wrappers and scripted localisation; no new variables |
| `ireland_briefing_{government,supply,defence,northern}_*` | Country scope; one card's canonical family predicates | exact status element contracts expected by the parent GUI | Read-only status bindings in the dashboard and focus inlay |
| `ireland_next_state_action_available` | Country scope; open gate plus canonical Parliament availability triggers | whether any next programme step exists | Read-only availability gate |
| `ireland_briefing_context_action_available` | Country scope; delegates to `ireland_next_state_action_available` | dashboard/inlay button availability | Read-only gate; archive-safe |
| `ireland_execute_next_state_action` | Country scope; guarded context action | executes at most one next Parliament step | Dispatches only `ireland_execute_parliament_{dail,seanad,confidence,budget}_action`; bumps `ireland_conditions_gui_dirty` after a successful dispatch path |

The focus inlay calls the same adapter as the dashboard. No inlay action calls
the Northern review request; Northern review remains in its dedicated ledger.

## Constants and tuning

No new tuning constants were added. The status bands reuse the existing global
`ireland` constants, including settlement stages, Provision/Readiness GUI
thresholds, Northern readiness thresholds, evidence/culture compatibility
thresholds, and existing foreign compatibility thresholds. The underlying
aggregate display variables (`ireland_provision_display` and
`ireland_readiness_display`) and all component variables remain untouched.

## Event targets and cleanup

No event target, global event target, timed flag, or new persistent variable was
introduced. The archive lifecycle is represented by the existing
`ireland_route_archived` flag through `ireland_mechanics_hub_open`; no cleanup
helper is required. Existing Northern/Evidence ledger request flags remain
owned and consumed by their dedicated ledger paths.

## Migration from the rejected ledger bindings

The active Cabinet Briefing block no longer exposes tab clicks, row clicks,
selection overlays, refresh, weakest-component selectors, or diagnostic review
dispatch. The retired refresh/selection/review effects were removed from the
feature-owned scripted-effect file. Compatibility-only status/selection
predicates remain in the trigger file because the concurrent old scripted
localisation definitions still parse references to them; they have no active
Cabinet Briefing GUI or inlay binding and can be deleted after the parent
localisation cleanup removes those definitions.

## Validation

- Scoped static contract check passed for all four owned files: every parent
  dashboard status/button name is present, every inlay scripted image/button
  name is present, all four canonical Parliament executors are called, and no
  old active refresh/selection/review identifiers or nonexistent context-label
  trigger remain in the active scripted GUI block.
- `git diff --check` passed for the owned files.
- Read-only `hoi4.gui_inspect` parsed the parent dashboard and inlay source graphs
  without blocking diagnostics. Dashboard artifact/revision:
  `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/48d28156397bc0149528e3d0c24b6477e72f9a704a8121e0ba8ead4841e15e49/a10a6c7513078013a3645905779fd81179bcafe2f610fe0c67df3855a3a0a618/gui-inspect.2ec3189185cde949.json`.
  Inlay artifact/revision:
  `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/6117395065b42b8e6a95abf73b41b4e7b08593f4624f93370e75e6664c191470/673c7f4c87e5680b1e27b1bf7f459f6fbdef890ea39e6d521b4876d39a456cdb/gui-inspect.bd66a5524d78e275.json`.
- Read-only `hoi4.gui_render` completed the dashboard at 1920x1080 and
  2560x1440 with normal/locked/warning/disabled states. Render artifact:
  `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/826457c712e0b205ee60ba9032b670c015149e0010ef398ad6da3ef0d9526235/70cb5451f94fb3ee2141d41cb586d9c0cf93e3250832e0921707d05e4bfe7c1d/ireland_national_situation_window-full.svg`.
- Read-only `hoi4.gui_render` completed the inlay request; the linked artifact
  was produced but the response was wire-truncated. The source graph remains
  complete in the inspect artifact above.

## Risks and parent follow-up

- The offline renderer cannot execute `context_aware_text` or `buttonstate.lua`,
  and generic scenarios report intentional co-located status sprites plus
  unresolved/zero-size dynamic text. This is tooling fidelity evidence, not a
  claim that live value-driven state transitions were proven.
- The parent interface keeps one static locked sprite as the inlay's scripted
  image fallback; the Northern image now explicitly selects that locked sprite
  until the authored reveal. No permanent Foreign or Culture inlay was added.
- The current concurrent scripted-localisation file still contains old ledger
  defined-text branches. Compatibility predicates are intentionally retained
  until that parent-owned cleanup lands; they are not active GUI bindings.
- No live in-game execution or AI click validation was run. AI remains disabled
  for the Cabinet Briefing GUI and inlay; native decisions remain the AI surface.

## Simplifications and omissions

No gameplay simplification or new fallback mechanic was introduced. The
accepted latest integration instruction chooses only the next guarded Parliament
programme action for the shared button; Northern review is intentionally left in
the dedicated Northern ledger. The underlying ledgers, values, thresholds,
decision costs, route flags, and AI behavior were not changed.
