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

- live Dáil and Seanad chamber summaries;
- four equal 125-pixel columns for Dáil authority, Seanad panels, confidence,
  and budget;
- one frame-driven red/green state icon for each power.

`ireland_update_parliament` initializes each power frame to 1 (pending) and
sets it to 2 (secured) from the matching completion flag. All summary and state
icons pass clicks through. The four native, one-time decisions remain the only
cost, trigger, effect, and AI owners. Route archival hides the scripted header,
preventing a stale panel after its actions are removed.

The Parliament summary is visible as soon as Ireland initialization completes.
Its four native actions remain gated by `ireland_settlement_open`, so early
visibility does not bypass their political prerequisites.

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
`hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/d4a39796bce33bf7ea6637aead1b99aa1248bd3a340f64e1f3144a367a636e94/421bc58e6e4be5c1a2c9125922e517a6e8c84186840a2b3571cffda032443e43/focus-inspect.f3eb8148dafc7f96.json`

The final structural focus render passed. The high-fidelity raster produced the
Ireland tree PNG and resolved every Ireland focus icon. Its reported failures
are nine decoder errors for vanilla continuous-focus DDS files and one missing
vanilla continuous-focus description; no Ireland focus or asset is implicated.

Render artifacts:

- `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/67401071261e3f1648c6521d254d2b757f2028e3ccab5445a8e62cc206281e98/f79d48bf724598116eea5331a85be43bdbc0aed34e9b63c13734e2a8e900c245/ireland_focus_tree.focus.html`
- `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/7507d0e1a2562589350eb99148e691015122db8c36e83557a50a0f4243f7934b/5117e75d29ccb6d20df949b037663bf187330b8731e8a9da99b9afa1eea5bf2e/ireland_focus_tree.focus.png`

The final Parliament GUI inspection has no blocking source-graph diagnostics
and no visible overlap. Its render covers 1366 by 768 and 1920 by 1080 across normal,
hover, selected, locked, disabled, warning, active, completed, empty/full,
minimum/maximum, long-text, and missing-localisation states. The render reports
zero overlap or source-graph errors.

Artifacts:

- `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/2e7f8437b9a25f66afccfe7683fff5300f7e8b844a8fea4ddbc880f46fa375bc/f292ac6a858f48e0b16ea925647a2b6b410716a7c736bb5abb35597af2e6c31e/gui-inspect.ff5b4a8e1f20057e.json`
- `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/d857d868c9d3627f19a9b3de9f02d4def7a3dc54d538724b0f2a24495bb865ba/2e6b5fb9d3d2bd7a7be12d941292630be04a6ca499c72a0148d3c68747b533b0/ireland_parliament_decision_ui_window-validation.json`
- `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/53387608ad150283192eec6cad203649f187b16f91d61340578e4c85139f86c6/b8d73f7bc168ffe25212af211c24b07ddb928b5193c9a2025d6dc8027f42ff18/ireland_parliament_decision_ui_window-state-matrix.png`

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
