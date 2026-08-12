# Focus tree and Parliament completion report

Date: 2026-08-12

Feature slug: `ireland_focus_tree`

## Outcome

The Ireland national tree is a single 150-focus directed acyclic graph arranged
into seven separated subject lanes. It has one root, 150 visible connectors,
and named navigation shortcuts for politics, culture, industry, diplomacy, the
Northern question, army/air readiness, and the far-right Naval Service.

The Parliament surface is a 510 by 248 interactive scripted GUI visible after
Ireland initialization. It contains two enlarged live chamber diagrams and four
functional human controls. Equivalent native decisions are AI-only; both paths
use the same eligibility gates, tuning constants, and record helpers.

No fallback tree, substitute mechanic, placeholder reward, duplicate seat
model, or non-functional GUI control remains.

## Focus architecture and reveal rules

The opening camera anchors on `ireland_state_still_defined`. The lanes read
left-to-right as:

1. politics, constitutional government, and gated political alternatives;
2. culture and public evidence;
3. industry and National Provision;
4. diplomacy and neutrality;
5. the Northern question;
6. army and air Readiness;
7. the Naval Service.

Seven named focus shortcuts jump directly to those anchors. The continuous
palette remains at `x = 50, y = 2400`, below the 17 authored rows.

Ordinary policy families are visible at the opening. Eight crisis, radical, or
evidence-gated families retain their authored `allow_branch` rules: IRA,
Congress, O'Duffy, clerical failure, Ailtirí, High Kingship, Five Provinces,
and Otherworld. Their descendants appear only after the relevant route or
evidence state is secured.

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

The chamber summary is visible as soon as `ireland_initialized` is present. The
four action rows appear only when the national settlement opens, so early
visibility does not bypass political prerequisites. The corresponding native
decisions are `is_ai = yes` and call idempotent shared executors; human players
therefore use the GUI while AI retains an ordinary decision path without a
double charge.

All costs and outcome increments live in
`common/script_constants/ireland_constants.txt`. The four record helpers remain
the single owners of seat and political-ledger mutations and are documented in
`docs/ireland_dynamic_effects.md`.

## Validation evidence

Final focus inspection revision `9f4f86cc5796922d` reports:

- 150 focuses and one root;
- 150 connectors;
- 0 crossings;
- 0 connector-through-node intersections;
- 0 long connectors;
- maximum horizontal span 6 and maximum vertical span 2;
- 0 same-row spacing defects;
- 0 Ireland focus diagnostics.

Artifact:
`hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/73a78f94783795326e576ef61757af1fb35871f10ca6dd9e16ae402461a2eef9/50b8461f4de0061cc8fd45ef89013c0febc85fb6124714f9883adebcc1dabca8/focus-inspect.9f4f86cc5796922d.json`

Structural render:
`hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/0f9501fc221c42155cac3ac66aa33cede2cba3e7f4bf08b07bc5a85a1aa73ea2/7b61e92441dda7b16c3c2dd4bc61d82b402bcf48d53dcb942f1430d09fac6c22/ireland_focus_tree.focus.html`

High-fidelity raster:
`hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/15cf201ce13947b67834a4a1fa6924373584cf7c2ea2a361c18a13a27b273a5a/d8f9f0d646d6fff4b03ee9043d730d4504a2c8c4876bd3cb155d53a7812da62c/ireland_focus_tree.focus.png`

The raster resolves all 150 Ireland focus icons. Its reported DDS failures are
limited to vanilla continuous-focus textures that the offline decoder cannot
read; no Ireland focus asset is implicated.

Final Parliament inspection revision `7efa20fde6ec3fcc` reports no overlap,
off-centre label, clipping, missing sprite, missing texture, missing font, or
spacing diagnostic. The four unresolved-value notices are the offline
scenario's placeholders for live country seat variables. The cost checker does
not follow a scripted-GUI click into its guarded shared executor and therefore
reports four cost mismatches. Each executor owns the matching political-power
delta, and the same cost constant drives its availability gate and visible
label.

Inspection artifact:
`hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/5c8de1b3855e70055af0ba10c9caea6919f47bc2f8c43ae2a840c3249a63e550/fb846fb7dce35268e11e732521378bca818238e0bc2974c11ace082437d5fd84/gui-inspect.7efa20fde6ec3fcc.json`

Render artifact:
`hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/965590013ce89528f81de25146a533349082c8a6d3ce50a2b0aabbe95147fb0b/2aa71812eb4b40a11d9e20ed073e264bbd4570e26616419f595feff8a54dff58/ireland_parliament_decision_ui_window-full.svg`

Static cross-surface checks confirm 150/150 focus title and description
coverage, seven shortcut labels, 37/37 reward tooltips, 21/21 Parliament GUI
localisation references, zero duplicate English keys, no dotted maritime
constant references, and no undefined script-constant references in the
touched focus, Parliament, decision, trigger, or AI surfaces.

## Files and systems changed

- National focus graph, semantic coordinates, visible dependencies, navigation
  shortcuts, AI plan ordering, and bounded rewards.
- Parliament decision category, human GUI effects, AI-only native decisions,
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
