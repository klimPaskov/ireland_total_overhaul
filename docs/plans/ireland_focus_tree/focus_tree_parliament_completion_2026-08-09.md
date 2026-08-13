# Focus tree and Parliament completion report

Date: 2026-08-12

Feature slug: `ireland_focus_tree`

Status: historical implementation inventory. Current focus geometry, reveal,
reward, Parliament cost, interaction, and asset evidence is superseded by
`focus_parliament_reward_density_completion_2026-08-13.md` and
`source_of_truth_map.md`. Numerical and presentation claims below describe the
2026-08-12 snapshot and must not be used as current completion evidence.

## Outcome

The Ireland national tree is a single 150-focus directed acyclic graph arranged
behind three opening trunks. It has one root, 150 visible connectors, and named
navigation shortcuts for government and politics, national development, and
defence and security. Culture, diplomacy, Northern policy, and the Naval
Service reveal later as support families rather than competing opening trunks.

The Parliament surface is a 510 by 248 interactive scripted GUI visible after
Ireland initialization. It contains two enlarged live chamber diagrams and four
functional human controls. Equivalent native decisions are AI-only; both paths
use the same eligibility gates, tuning constants, and record helpers.

No fallback tree, substitute mechanic, placeholder reward, duplicate seat
model, or non-functional GUI control remains.

## Focus architecture and reveal rules

The opening camera anchors on `ireland_state_still_defined`. Its three readable
campaign-level choices are:

1. government, constitutional politics, and gated political alternatives;
2. national development, industry, and National Provision;
3. defence, security, army, and air Readiness.

Three named focus shortcuts jump directly to those anchors. The continuous
palette remains at `x = 50, y = 2400`, below the 17 authored rows.

Culture, diplomacy and neutrality, Northern settlement, and the Naval Service
use `allow_branch` at their ordinary roots, matching their existing gameplay
gates, so they appear only when their prerequisites make them actionable.
Three late constitutional alternatives—Norton, Clann na Talmhan, and the
vocational constitution—are likewise concealed until their full selection
conditions are met. Eight crisis, radical, or evidence-gated families retain
their authored reveal rules: IRA, Congress, O'Duffy, clerical failure, Ailtirí,
High Kingship, Five
Provinces, and Otherworld. The source therefore contains fifteen presentation
gates in total while showing no more than three campaign trunks at the start.

The visible graph follows real semantic dependencies. The Lemass route visibly
passes through Dáil Nomination, the Otherworld dominion route visibly consumes
Containment Protocol, Naval Staff remains in the Naval Service lane, and
distant cross-system requirements remain explicit availability gates where a
connector would obscure the subject lanes.

## Reward depth

The Provision, Readiness, defence, neutrality, and diplomatic lanes use bounded
script-constant reward steps rather than generic political-power bundles.
Thirty-seven focus rewards have precise player-facing tooltips. The revised
contracts include:

- visible Food, Energy, Transport, and Maritime Provision gains;
- visible Command, Equipment, Mobilisation, Supply, Warning, Maritime
  Protection, and Intelligence gains;
- domain-appropriate Army, Navy, and Air experience;
- visible Neutrality Integrity, Social Consent, Dáil Mandate, Cabinet
  Cohesion, Administrative Reach, and Intervention Mandate changes;
- named diplomatic-channel and route transitions;
- the existing physical Marine Service ships, facilities, convoy, intelligence,
  and production projects.

Generic political-power padding was removed from Marine Service reconstruction,
the Atlantic Convoy Office, and the regional maritime pact. The reward constants
are centralized under the `ireland` script-constant category. All surviving
focus titles, descriptions, shortcut labels, and custom reward tooltips resolve.

The final graph has 150 unique IDs, 150 unique coordinates, no unresolved
prerequisites, no parent-below-child connectors, and complete AI-plan coverage.
The Lemass AI plan now includes Dáil Nomination before its capstone.

## Parliament GUI and interaction contract

`ireland_parliament_decision_ui_window` contains:

- a 510x248 dossier background;
- two balanced 247-pixel chamber cards;
- 21-frame Dáil and Seanad diagrams enlarged to 126x70 each;
- live support, majority, and chamber-composition text;
- four 204x32 actions in a two-column, two-row grid;
- a separate four-state status column beside every action.

The four human controls are `Convene Dáil`, `Win Seanad Support`, `Confidence
Pact`, and `Pass Joint Budget`. Each has a real scripted-GUI click effect, a
canonical enabled trigger, a centralized political-power cost, a one-time
completion flag, and an immediate Parliament refresh. Labels are natively
centered by their buttons. Status icons occupy their own columns and therefore
neither overlap nor intercept the click regions.

Each action uses one four-frame seal driven by the canonical current and
availability triggers: slate for a future locked step, amber for the current
step without enough Political Power, cream-gold for the current available
action, and green for a secured result. Red is reserved for an actual failure
or crisis rather than ordinary unfinished business.

The chamber summary and four programme steps are visible as soon as
`ireland_initialized` is present. The opening Dáil action is immediately usable
when Ireland controls Dublin and can pay 15 Political Power. Its shared
executor opens the National Settlement focus, which advances the Seanad stage;
the Constitutional Draft and Government Formation advance the later stages.
Native decisions and scripted-GUI buttons call the same idempotent executors,
so neither surface can bypass a gate or double-charge an action.

All costs and outcome increments live in
`common/script_constants/ireland_constants.txt`. The four record helpers remain
the single owners of seat and political-ledger mutations and are documented in
`docs/ireland_dynamic_effects.md`.

The decision parser's `ai_hint_pp_cost` field does not accept `constant:`
tokens. Its four AI budget hints therefore use file-local `@` macros with the
same 15/25/25/35 values; the executable costs, gates, and GUI labels remain
owned by the shared script-constant contract.

## Validation evidence

Final focus inspection revision `b1c47582375c4bad` reports:

- 150 focuses and exactly three opening roots/trunks;
- 150 connectors;
- 0 crossings;
- 0 connector-through-node intersections;
- 0 long connectors;
- maximum horizontal span 7 and maximum vertical span 2;
- 0 same-row spacing defects; and
- authored bounds x `-20..21`, retaining a 41-column span that is half the previous width.

Artifact:
`hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/38eaf03718c2057898eaab76ca811b380b412a07dc8d61190231e212dc1e09bc/905da3cd351731b79e9f6725233efad61df2e9a31bee5a3988fe0975750c2720/focus-inspect.b1c47582375c4bad.json`

Structural render:
`hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/92d07d264a68b616d43ed374a60c688281c0e9abe57baa9fc0125d0859954c12/676be3973e1ff0ed8c9b9e274a097cd3b95d3db4b09a69484f84e236d64ef64a/ireland_focus_tree.focus.html`

Final Parliament inspection revision `3afccc6805fec771` reports no overlap,
off-centre label, clipping, missing sprite, missing texture, missing font, or
spacing diagnostic. The four unresolved-value notices are the offline
scenario's placeholders for live country seat variables. The cost checker does
not follow a scripted-GUI click into its guarded shared executor and therefore
reports four cost mismatches. Each executor owns the matching political-power
delta, and the same cost constant drives its availability gate and visible
label.

Inspection artifact:
`hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/73c95f48e5bd3e7e39d3de317b1b255b9c2ee9a74b2380dd1934e7398c1791e8/7cf73984dfd95fa45447ca63b1248cdae9cc36d203f1a0a6fe7caa16df305bff/gui-inspect.3afccc6805fec771.json`

Render artifact:
`hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/9a4d05d71d3da947f271917a80ff70f41efc3023cd952119c17f9b6c6aa5c53d/841b57e1febfe485571063de136297b80331197fa9264c057e9e6b2df73c18be/ireland_parliament_decision_ui_window-full.svg`

Static cross-surface checks confirm 150/150 focus title and description
coverage, three shortcut labels, 150/150 reward tooltips, 32 direct material
focuses, 24 capability focuses, 59 decision/mission-unlock focuses, and all Parliament GUI
localisation references, zero duplicate English keys, no dotted maritime
constant references, and no undefined script-constant references in the
touched focus, Parliament, decision, trigger, or AI surfaces.

## Files and systems changed

- National focus graph, semantic coordinates, visible dependencies, navigation
  shortcuts, AI plan ordering, and bounded rewards.
- Parliament decision category, human GUI effects, shared native decisions,
  canonical action triggers, shared executors, record effects, constants,
  English localisation, and dynamic-effect documentation.
- Parliament background, enlarged chamber strips, action-button texture,
  four-frame action-state seal, GFX registrations, processed PNGs, manifest,
  and wiring handoff.
- Focus, Parliament, and completion audit handoffs under
  `docs/plans/ireland_focus_tree/`.

## Simplifications, omissions, and blockers

None in the requested Ireland focus-tree and Parliament surfaces. Cross-lane
availability gates are deliberate gameplay dependencies rather than hidden
substitutes: they preserve the required completed focus while avoiding a long,
misleading connector across unrelated subject lanes.
