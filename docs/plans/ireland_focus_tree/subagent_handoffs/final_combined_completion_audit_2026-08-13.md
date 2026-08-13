# Final combined completion audit — 2026-08-13

Feature slug: `ireland_focus_tree`

Mode: final read-only audit of the frozen 215-focus source. This handoff is the
only file changed by the completion auditor.

## Verdict

**Complete at the requested static-source, asset, localisation, AI,
documentation, and offline MCP inspection/render boundary.** No focus,
Parliament, event, territorial, advisor, concern, MIO, localisation, AI, asset,
or documentation blocker remains.

The single disclosed source residual is the concealed
`ireland_clerical_failure_bridge -> ireland_clerical_guardianship` connector:
it moves two columns over one row but is not long, crossing, intersecting, or
too close to another node. It is a nonblocking authored detour, not a fallback.

## Completion by surface

| Surface | Status | Evidence |
| --- | --- | --- |
| Focus structure, rewards, filters, AI, localisation, icons | complete | 215 unique focuses; final focus revision `d8b63828f71934c3`; source/GFX/localisation/AI crosswalk |
| Parliament presentation and lifecycle | complete | GUI/scripted-GUI/triggers/executors/native decisions; fresh GUI inspection revision `7f3852e55f472fa8` |
| Territorial diplomacy, settlement, images, cadence | complete | 16 triggered-only territorial events; 31 options/tooltips; decisions, triggers, effects, constants, art manifests |
| Full event inventory and clarity | complete | 511 event IDs, 1,029 options and 1,029 matching effect tooltips across five Ireland event files |
| Advisors, concerns, contracts, and MIOs | complete | 45 advisor roles; seven concerns; two MIOs; nine independent one-use contracts |
| Active documentation | complete | source-of-truth map, implementation document, completion report, canonical spec, and promoted addendum agree with frozen source |

## Focus tree

The source has 215 focuses and 222 connectors, bounds x `-42..21` and y
`0..17`, and exactly three opening roots/trunks. Its three shortcuts point into
the centres of politics (`ireland_government_formation`), industry
(`ireland_development_authority`), and defence
(`ireland_maritime_protection`). The 27 later branch roots use `allow_branch`
and remain hidden until their authored family, route, cabinet, territorial, or
postwar reveal condition is true.

The final specialist focus inspection, revision `d8b63828f71934c3`, reports
215/215 graph reachability, 222 connectors, zero crossings, zero
connector-through-node intersections, zero long connectors, zero same-row
spacing defects, and no unresolved prerequisite, mutual-exclusion, or AI-plan
focus reference. The sole Ireland advisory is the disclosed clerical detour;
the other warning is the unrelated vanilla
`continuous_restrict_freedom_desc` localisation warning.

Final focus evidence:

- inspect: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/b08b004fd287b5d1761161ebe673917f0f9bfb0a5e9685c200577e3fb46bdd9a/40d6dbe67ef52ef9e7b5923279b804889b737f840f2dd776af2ed4e017e7badb/focus-inspect.d8b63828f71934c3.json`;
- HTML: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/1054e0beb854a0ee79130b1bc81f6e7416c5f62f4317710c9941c25ede95d79f/06506e11742ba603663a9433030209f56b4456c0c7061bdf2fcf47e9b577eec1/ireland_focus_tree.focus.html`;
- SVG: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/d896988a8486cdcb3b6403090c891004943443fc4cd9758e5d041467d933b0ba/0fe4f222844beb03a8bf2cb327a8d28baf9a59d2fa9791fdbfcfbe34f3809fe1/ireland_focus_tree.focus.svg`.

Every focus has a completion reward, custom reward tooltip, title,
description, registered icon, existing texture, shine registration, and AI
plan reference. The final sprite cleanup leaves each of the 27 public-family
static sprites defined once in `interface/ireland_icons.gfx` and their 27 shine
sprites once in `interface/ireland_public_family_focus_icons.gfx`; no duplicate
or missing focus sprite remains.

The strict reward/filter source crosswalk is exact for the correction's
effect-valued filters:

| Filter | Tagged / direct grants | Mismatches |
| --- | ---: | ---: |
| Army XP | 14 / 14 | 0 |
| Navy XP | 11 / 11 | 0 |
| Air XP | 4 / 4 | 0 |
| Research/doctrine | 28 / 28 | 0 |
| Manpower/unit grants | 0 / 0 | 0 |

Industry, international-trade, balance-of-power, political-character,
stability, annexation, and historical tags describe the direct named
institution, unlock, state instrument, or political outcome of their focus;
none is used to disguise an XP grant or an unrelated branch label.

The five public families meet the canonical depth/domain contract and retain
their family lock separately from later profile commitment. Their cabinets,
economy/company interaction, security, foreign posture, Northern policy,
reconstruction/recovery, and endpoints are reachable. The territorial and
postwar branches remain progressively revealed rather than opening a fourth
trunk.

## Parliament

The 510x248 panel keeps the title on the upper parchment rail, above the two
chamber cards. The Dáil composition uses distinct support/opposition/other
colours and a compact Other label; values and labels remain legible. The four
actions have distinct four-frame emblem assets and separate click regions.

The canonical shared-executor sequence is intact:

1. Convene Dáil is current at stage 1 and free when initialized Ireland owns
   Dublin.
2. Seanad support follows Dáil plus National Settlement and costs 25 PP.
3. Confidence follows Seanad plus Constitutional Draft and costs 25 PP.
4. Joint budget follows confidence plus Government Formation and costs 35 PP.

GUI clicks and human-visible native decisions use the same current/available
triggers and idempotent executors. Completion flags advance the stage, so later
decisions appear sequentially and no parallel human path duplicates an action.
The requirement tooltips enumerate the same stage, focus, completion, Dublin,
majority, and affordability gates as the click trigger.

Fresh GUI inspection revision `7f3852e55f472fa879051f4761cff29c1f53e8027af28326fc67fe98780bc948`
parses and links the source graph and reports no `GUI_VISIBLE_OVERLAP`:
`hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/60c27e84db15a57e795ee9a0af9e2147bf0dfe5f1c50c7542ee5829faaa0b106/d538d4bb2edfd9b5352a062b874248e9bbc3f035d4eee1ecf3714d387c746778/gui-inspect.7f3852e55f472fa8.json`.
The 1920x1080/2560x1440 state render is
`hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/164ff927e976510637fb105951264d0a5fb67b5f66108e4a1535f200e6018666/fe63dd5827ca981477333c5dcb0eb7d0c450695f42d84197cf16a7f2d4a4491d/ireland_parliament_decision_ui_window-full.svg`.
The analyzer's three apparent paid-action cost mismatches are bounded false
positives: it does not follow the click wrapper into the 25/25/35 PP executors.
It also only partially renders `buttonstate.lua`; direct source review supplies
the lifecycle evidence.

## Events, territorial policy, cadence, and images

The five event files contain 511 unique event IDs: the prior 495-event
programme plus 16 target-country territorial events. They contain 1,029
options, and every option has its matching exact-effect
`custom_effect_tooltip`; event title, description, option, and tooltip
localisation references resolve. The earlier programme retains its exact
post-clamp numeric previews and fixed contribution costs. The 31 territorial
options name the exact acceptance, counteroffer, refusal, claim, cooldown,
settlement, or cleanup result.

All 511 events have a picture. Their 126 unique picture sprites resolve to
registered, existing DDS assets. The 16 territorial events use five distinct
210x176 report images with source/processed/runtime manifests; none is a
placeholder or missing-image fallback.

The territorial file defines four response chains covering Ulster ultimatum,
Belfast compact, Highlands demand, and Ulster enforcement. Every event is
`is_triggered_only`. Recipient acceptance/counter/refusal returns to a named
requester result event; terminal paths set the 180-day reopening cooldown and
run cleanup. Issued, delivered, offered, active, and cooldown records prevent
replay. Saved requester, controller, and state targets are cleared
deterministically.

Coercive admission and completion recheck peace, route authority, readiness,
Dublin, Dáil majority, reserves, command power, exact target controller,
faction relation, relative strength, and required naval reach. Historical AI
does not use coercive territorial decisions. No external state gains an
automatic core.

Postwar resolution is per holding and per SCO/WLS subject relationship. Local
rights, protectorate/release, and Highlands integration-review outcomes write
separate records. The Atlantic settlement mission cannot finish while a
retained relevant relationship is unresolved, reserves shared mission
capacity, and releases active/capacity/temporary state on completion,
cancellation, timeout, route cleanup, or total loss of scope.

Fresh narrow territorial event lint revision
`586c951a24d6c13a1a134ba8c6ade7bda7a298fe591605b2643a4c474bec9b6c`
reports no blocking diagnostic:
`hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/6fe8aba5b99b326d8d066b9db559b714351ef653238548fcfd1af89cea5d8d58/63a30880328db6a07a18375db5a3b08541b1b895509f1e5df4a8aa0b694469d9/event-lint-586c951a24d6.json`.
Workspace-scale helper/lifecycle projection was deferred by the tool, so the
target, cooldown, replay, settlement, and cleanup conclusions above come from
the narrower direct source crosswalk.

The pre-existing cadence correction remains intact: ordinary dispatch is one
monthly pulse with a one-pulse cooldown; foreign windows admit at most one
actor report, optionally schedule one aggregate digest, enforce the 120-day
reopening cooldown, preserve durable seen records, and leave every chained
reaction reachable after its predecessor. The territorial events add no daily
or ordinary-dispatch path.

## Advisors, concerns, contracts, and MIOs

All 45 advisor blocks resolve through idea tokens, localisation, registered
GFX, existing approved advisor-card DDS files, pool flags, and route/date/
office lifecycle triggers. The five cabinet focuses expose the intended pools;
the constitutional service pool remains reachable across democratic profiles.

The capability matrix is seven industrial concerns plus two real MIOs, not
nine concerns. All nine focuses set distinct unlock flags and expose nine
independent, one-use 25-PP/35-day contracts. Player-facing steel localisation
is “Irish Steel”; the legacy internal token does not expose “Steel Holdings.”
Irish Shipping uses the March 1941 or national-emergency gate.

Ford Cork includes vanilla's motorised/mechanised organization and supplies a
local-assembly trait. Harland and Wolff includes the task-force ship
organization and supplies yard/refit traits. Both are restricted to
original-tag Ireland, are visible/available only after their focus flags, have
valid parent/position trait wiring, focus visibility/size effects, AI weights,
localisation, icons, and existing textures. Harland and Wolff remains behind
the lawful state-119 settlement gate.

## Accepted plans and disposition

The political/territorial improvement addendum is marked accepted,
implemented, and promoted into the canonical specification. Its five-family
depth, cabinets, seven-concern/two-MIO matrix, target-country diplomacy,
naval-access proof, per-holding settlement, art, localisation, AI, and cleanup
contracts are present. The exploratory 210–225 band was reconciled to 215
manually reviewed focuses without omitting a promised role. No unresolved
improvement-loop addendum remains, so another planner pass is not recommended.

The earlier 188-focus completion audit is now explicitly headed superseded and
historical. Its six findings were rechecked here and are closed by current
source.

## Documentation closure

The three documentation discrepancies found during the first frozen pass are
closed:

1. `docs/plans/ireland_focus_tree/source_of_truth_map.md` records x `-42..21`
   and 64 occupied coordinate columns.
2. `docs/plans/ireland_focus_tree/political_industrial_territorial_expansion_completion_2026-08-13.md`
   records seven concerns plus two MIOs, 65 added focuses, and no remaining
   feature blocker or simplification.
3. `docs/ireland_political_industrial_and_territorial_expansion.md` no longer
   lists the implemented negotiated foreign-response chains as future work and
   its validation contract distinguishes seven concern ideas from two MIOs.

The historical 188-focus audit remains explicitly superseded. The canonical
specification and implemented/promoted improvement addendum agree with the
current 215-focus source.

## Simplifications, omissions, blockers, and next actions

Simplifications, omissions, and blockers: **none**.

The requested combined feature is repository-complete at the static-source,
asset, localisation, AI, documentation, and offline MCP inspection/render
boundary. The one concealed clerical detour and bounded MCP renderer limits are
disclosed nonblocking validation residuals. No fallback implementation was
used, and no new `hoi4_improvement_loop_planner` pass is warranted.
