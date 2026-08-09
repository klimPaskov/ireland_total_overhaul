# Focus tree and Parliament completion report

Date: 2026-08-09

Feature slug: `ireland_focus_tree`

## Outcome

The Ireland national tree is a single 150-focus directed acyclic graph with one
root and 159 visible connectors. The generated expansion layer and universal
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
cycles. Its 36 structural leaves were checked individually. They are route
capstones, intentional policy endpoints, or focuses consumed by named
availability gates, flags, events, ledgers, achievements, or conclusion
effects; none is an unconsumed dead end. Provision and Northern convergence use
state gates for distant required projects instead of adding crossing visual
connectors. This changes presentation only: the same completed focuses remain
required.

## Semantic layout and progressive reveal

The opening camera anchors on `ireland_state_still_defined`. The authored tree
now reads left to right as political crisis and constitutional government,
Northern policy, culture and society, industry and National Provision,
diplomacy and neutrality, army/air/coastal readiness, and the far-right Marine
Service. The naval lane no longer sits inside the political or industrial
centre.

The continuous-focus palette is explicitly anchored at `x = 50, y = 2400`,
below the final authored row. It remains close to the opening camera's central
axis but no longer covers a political, cultural, industrial, diplomatic, or
defence lane.

All ordinary subject families are visible from the opening screen. Exactly
eight crisis, radical, or evidence-gated roots retain `allow_branch`: IRA,
Congress, O'Duffy, clerical failure, Ailtirí, High Kingship, Five Provinces,
and Otherworld. Their inherited descendants appear only when the existing
gate and Ireland-scoped layout refresh succeed.

Narrow prerequisite corrections make the visible connectors describe their
real subject dependencies. In particular, defence and readiness fan from the
shared defence gateway; readiness still requires Command Audit through its
availability gate. Transport now visibly feeds stockpiles and the maritime
reserve, while recovery no longer appears to depend on an optional naval pact.

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

- a generated 1930s dossier background with a parchment chamber field and a
  dark legislative-progress band;
- one Houses of the Oireachtas title and two equal-width Dáil/Seanad chamber
  cards;
- identically sized live support arcs, centered majority figures, and compact
  composition summaries for both chambers;
- one horizontal four-step track for Dáil authority, Seanad support,
  confidence, and budget, with a frame-driven red/green state for each step.

`ireland_update_parliament` initializes each power frame to 1 (pending) and
sets it to 2 (secured) from the matching completion flag. All summary and state
icons pass clicks through. The four native, one-time decisions remain the only
cost, trigger, effect, and AI owners. Route archival hides the scripted header,
preventing a stale panel after its actions are removed.

The Parliament summary is visible as soon as Ireland initialization completes.
Its four native actions remain gated by `ireland_settlement_open`, so early
visibility does not bypass their political prerequisites.

The panel reuses vanilla `GFX_checkbox_small_red_green` and the existing live
chamber-strip state system. Its decorative background is registered as
`GFX_ireland_parliament_summary_background`; source, processed preview, DDS,
prompt, manifest, and wiring handoff are retained under
`docs/assets/ireland_parliament_panel/`. A 21-frame 90x50 Seanad derivative is
processed frame by frame from the existing project strip so both chambers have
the same 50px visual height without fractional GUI scaling. No fallback sprite
was used.

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
- Every maritime ledger delta reads the registered
  `constant:ireland_maritime.ledger_standard_delta`; the invalid dotted
  category form is absent.

## Validation evidence

The final `hoi4.focus_inspect` revision reports:

- 150 focuses and one root;
- 159 connectors;
- 0 connector crossings;
- 0 node intersections;
- 0 long connectors;
- 0 same-row spacing defects;
- 0 Ireland-local diagnostics.

Artifact:
`hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/3ca1558a3b879ffd558d5fdad951f222f71d92ff473ec325a545a6bc6082a758/65bd0cb5262b5ea5c9d64c933bc8b35f7bb06aacf657efbe5a70d84e56027e43/focus-inspect.e3a6dbf54659fc69.json`

The final structural focus render passed. The high-fidelity raster produced the
Ireland tree PNG and resolved every Ireland focus icon. Its reported failures
are nine decoder errors for vanilla continuous-focus DDS files and one missing
vanilla continuous-focus description; no Ireland focus or asset is implicated.

Render artifacts:

- `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/4b998600688da0effb679e604db8f8d965e0cb41d5e11a1a4c7a8ed20ac3092b/e48be564d21e5abd3608f0c555836b021301734fa9dcaa48154468f3bb2c7805/ireland_focus_tree.focus.html`
- `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/e6121bda644e36b632f3336ea192adea60293f8f3deef53d8c2b365ee041c9bf/cb92306c73ff07c1e684074d6d9bd6197d598d2051c01e352cc9dea8c5b81f2a/ireland_focus_tree.focus.png`

The final Parliament GUI inspection passes its source graph and has no visible
overlap, clipping, text overflow, missing sprite, missing texture, or missing
font. Its render covers 1366 by 768 and 1920 by 1080 across normal,
hover, selected, locked, disabled, warning, active, completed, empty/full,
minimum/maximum, long-text, and missing-localisation states. The render reports
zero overlap or source-graph errors. Its four unresolved-value notices are the
offline renderer's expected placeholders for country-scoped live seat and
majority variables; every referenced variable is initialized by the Parliament
system and is deliberately shown as live data.

Artifacts:

- `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/6bdb582d039d626eb1538f5134af2cad513e3fc7a20995b42c47be0ad133d05b/86a43d18fcb572b90870b2317d90352488a8b1091bec94d3c5be5af900d83582/gui-inspect.5f725bd58271c2f7.json`
- `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/e68361e5c99358adaf0fc2698ade6a7d8e2893f7c622c102cfa57d19226afaf8/9f7b286b3a46c9bad5c5e9b148908948f152a10ded9fcaa7d3535778a917f5ee/ireland_parliament_decision_ui_window-validation.json`
- `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/ef220ede0f0c3bc4e6486c3cdc26b9d1a7ddbd193797659a1de117b97afc986e/49120d0bfac15f29da690caa190867e5d2e9ffe859e3277a9444ebda2c2ae1c2/ireland_parliament_decision_ui_window-state-matrix.png`

## Files and systems changed

- National focus source, route layout, rewards, and convergence compatibility.
- Ireland AI focus plans and 1939 completed-focus history.
- Parliament recompute effect, scripted-GUI properties/visibility, interface
  layout, scripted localisation, and English localisation.
- Parliament presentation assets: generated 510x198 dossier background,
  frame-preserving compact Seanad strip, runtime DDS files, sprite
  registrations, prompt, manifest, processed previews, and wiring handoff.
- Generic focus-reward helper and constant files removed.
- Reward-contract and source-of-truth documentation reconciled; specialist
  focus, GUI, and localisation handoffs retained under `docs/plans/`.

## Simplifications, omissions, and blockers

None. Distant project requirements represented as availability gates are the
authoritative dependency design, not a fallback: they preserve the gameplay
requirement while preventing misleading cross-tree connector geometry.
