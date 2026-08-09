# Focus tree and Parliament completion report

Date: 2026-08-09

Feature slug: `ireland_focus_tree`

## Outcome

The Ireland national tree is a single 150-focus directed acyclic graph with one
root and 158 visible connectors. The generated expansion layer and universal
reward profiles are retired. The Parliament scripted GUI is a compact,
read-only projection of the native parliamentary decisions inside the actual
510 by 198 decision-category host.

No fallback tree, substitute mechanic, placeholder reward, duplicated seat
model, or alternative GUI action path was used.

## Focus consolidation and route preservation

Seven late wrapper focuses were folded into the decision-bearing focus that
already owned their state transition:

| Retired wrapper | Surviving focus |
| --- | --- |
| `ireland_domestic_industry_review` | `ireland_rural_price_board` |
| `ireland_port_and_coast_audit` | `ireland_command_audit` |
| `ireland_northern_contacts` | `ireland_national_settlement` |
| `ireland_territorial_reserve` | `ireland_readiness_baseline` |
| `ireland_govern_through_dail` | `ireland_de_valera_stewardship` |
| `ireland_reconciliation_mandate` | `ireland_de_valera_reconciliation` |
| `ireland_agrarian_support_bloc` | `ireland_clann_founding` |

The survivor writes every still-consumed compatibility flag. Prerequisites,
availability gates, history, AI queues, descriptions, and route locks were
updated to the survivor IDs. The High Kingship capstone is the explicit
survivor for the former fivefold-obligation, Otherworld-convergence, and final
convergence-order sequence. It closes the compatibility, conclusion, profile,
and verification flags in the same completion effect.

The final graph has no duplicate coordinates, unresolved prerequisites, or
cycles. Its 37 structural leaves were checked individually. They are route
capstones, intentional policy endpoints, or focuses consumed by named
availability gates, flags, events, ledgers, achievements, or conclusion
effects; none is an unconsumed dead end. Provision and Northern convergence use
state gates for distant required projects instead of adding crossing visual
connectors. This changes presentation only: the same completed focuses remain
required.

## Reward contracts

`common/scripted_effects/ireland_focus_rewards.txt` and
`common/script_constants/ireland_focus_reward_constants.txt` were removed.
There are no remaining universal focus-reward calls or generated
`*_completion_reward_tt` keys.

Every surviving focus now pays through at least one named contract:

- a route commitment, mandate, institutional transition, or conclusion review;
- a decision, mission, project, diplomatic channel, or evidence gate;
- a provision, readiness, Northern, foreign, cultural, or achievement ledger;
- a bespoke physical project, such as the Marine Service sequence.

The Marine Service retains its authored ships, facilities, experience, and
ledger effects because those effects are the represented project rather than a
generic reward bundle.

## Parliament GUI

`ireland_parliament_decision_ui_window` fits the fixed 510 by 198 host. The
panel contains:

- live Dáil and Seanad chamber summaries;
- four equal 125-pixel columns for Dáil authority, Seanad panels, confidence,
  and budget;
- one frame-driven red/green state icon for each power.

`ireland_update_parliament` initializes each power frame to 1 (pending) and
sets it to 2 (secured) from the matching completion flag. All summary and state
icons pass clicks through. The four native, one-time decisions remain the only
cost, trigger, effect, and AI owners. Route archival hides the scripted header,
preventing a stale panel after its actions are removed.

The panel reuses vanilla `GFX_checkbox_small_red_green`; no new visual asset or
fallback sprite was required.

## AI, localisation, and lifecycle alignment

- All AI-plan focus IDs resolve to the current 150-focus roster.
- The historical queue proceeds directly through the constitutional-draft
  survivor; the obsolete convergence plan was retired.
- All 150 focus titles and descriptions resolve, with no duplicate English
  keys.
- Parliament GUI and scripted-localisation references resolve. Chamber
  tooltips use live seat and majority values, and the power-state tooltip
  explains red pending / green secured.
- English localisation remains UTF-8 with BOM.
- The 1939 history bookmark points to the surviving rural-price-board focus.

## Validation evidence

The final `hoi4.focus_inspect` revision reports:

- 150 focuses and one root;
- 158 connectors;
- 0 connector crossings;
- 0 node intersections;
- 0 long connectors;
- 0 same-row spacing defects;
- 0 Ireland-local diagnostics.

Artifact:
`hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/fb32d403fdd542f6a9c2d9ec5171b2ef55d356a942e80f4fe762537d4618c9ef/2e05926efa5a18bbf5a979b0200a4e76acb0033538ace469ba0eea5f09d776e3/focus-inspect.55cadd1bd50ffb1a.json`

The final structural focus render passed. The high-fidelity raster produced the
Ireland tree PNG and resolved every Ireland focus icon. Its reported failures
are nine decoder errors for vanilla continuous-focus DDS files and one missing
vanilla continuous-focus description; no Ireland focus or asset is implicated.

The final Parliament GUI inspection has no non-information diagnostics and no
visible overlap. Its render covers 1280 by 720 and 1920 by 1080 across normal,
hover, selected, locked, disabled, warning, active, completed, empty/full,
minimum/maximum, long-text, and missing-localisation states. The render reports
zero overlap or source-graph errors.

Artifacts:

- `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/4a5d6071bec06248e31ec5c0aa7c4db0e9f007dfc5bb3176a8200a4e1a277d76/d94ce9305a7862043d0a3113c869d06be2a7237865dafce5b07a4ce6a562226e/gui-inspect.f3eae66cbc9cad24.json`
- `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/c6272ab42f0735977c8ac748263d9372e299949720ae186c26af9bcea3e37555/43319d58a8ea78c7f77cbe47eb67e19b5c65b221a8678661704156e783cc59ef/ireland_parliament_decision_ui_window-validation.json`

## Files and systems changed

- National focus source, route layout, rewards, and convergence compatibility.
- Ireland AI focus plans and 1939 completed-focus history.
- Parliament recompute effect, scripted-GUI properties/visibility, interface
  layout, scripted localisation, and English localisation.
- Generic focus-reward helper and constant files removed.
- Reward-contract and source-of-truth documentation reconciled; specialist
  focus, GUI, and localisation handoffs retained under `docs/plans/`.

## Simplifications, omissions, and blockers

None. Distant project requirements represented as availability gates are the
authoritative dependency design, not a fallback: they preserve the gameplay
requirement while preventing misleading cross-tree connector geometry.
