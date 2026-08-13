# Superseded expansion completion audit — 2026-08-13

Status: superseded by the later 215-focus completion pass and final combined
completion audit. The findings below describe the earlier frozen 188-focus
implementation and are retained only as historical implementation evidence.

Mode: read-only feature-completion audit. Gameplay, localisation, interface,
asset, and source-spec files were not edited. `thumbnail.png` was not touched.

## Verdict

**Incomplete at the repository's no-simplification completion standard.** The
runtime contains the requested visible breadth and several independently
complete surfaces, but six accepted-design or reachability gaps remain. The
current completion report's no-omission verdict is therefore not supported by
the frozen source.

## Completion status by surface

| Surface | Status | Frozen-source result |
| --- | --- | --- |
| Focus inventory and layout | Complete for the implemented 188-focus graph | 188 focuses, 195 connectors, five mutually exclusive family gates, zero crossings, zero connector-through-node intersections, zero long connectors, and zero same-row spacing defects. One concealed clerical detour remains nonblocking. |
| Public family route clarity and depth | **Partial / blocker** | All five family gates exist and are localised, but four families do not meet the accepted depth/coverage contract and the gates do not form the accepted post-Settlement public row. |
| Industrial companies and contracts | Complete for the compact concern implementation; **simplified against accepted plan** | Nine selectable concern ideas, nine unlock focuses, nine separate one-use contracts, and nine runtime marks exist. Ford and Harland & Wolff are concerns rather than the accepted MIO implementations; Irish Shipping lacks its planned founding gate. |
| Advisor-card asset workflow | Complete | 45 characters, 45 idea tokens, 45 matching small-portrait sprites, 45 runtime DDS cards, 45 manifest entries, and 45 source inputs. The Chaos Redux measured-template workflow produced 65x67 BGRA advisor cards; no fallback or blank card was found. |
| Advisor gameplay unlocks | **Partial / blocker** | Five cabinet focuses exist, but the constitutional pool is unreachable to several democratic profiles and its player-facing roster is incomplete. |
| Territorial policy breadth | Complete for visible inventory | Twenty decisions/missions cover Northern methods, access/support, three external claims, postwar review, local rights, protectorates, Highlands review, and the Atlantic settlement mission. No external core is granted. |
| Coercive final-tick safety | Complete | All four coercive completion limits re-run `ireland_atlantic_claim_enforcement_ready`, live controller, control/ownership, faction, and exact direct-controller `strength_ratio` checks. Changed conditions use the cancellation/refund branch. No `alliance_strength_ratio` remains. |
| Postwar launch capacity and cleanup | Complete for the single-mission implementation | `ireland_territorial_open_postwar_review` checks launch capacity and a player-facing territorial scope, cancels during preparation when capacity or all eligible relationships are lost, revalidates both at completion, sets `ireland_mission_complete_atlantic_settlement_active`, and updates capacity on start, cancellation, timeout, conclusion, and route cleanup. |
| Postwar per-holding settlement | **Partial / blocker** | One global settlement-record flag can close the whole mission after only one holding is treated. |
| Parliament availability | Complete | The four GUI buttons, native decisions, shared executors, canonical availability triggers, and live red/green checklist rows agree. Grey buttons explain stage, focus, Dublin, completion, chamber majority, and Political Power requirements exactly. |
| AI and localisation | Complete for the implemented compact systems; not proof of omitted plan depth | The 38 expansion focuses have route-reactive coverage; historical AI uses the democratic/peaceful/material line and coercive decisions are disabled for historical AI. Current identifiers resolve to localisation and GFX. |
| Documentation and accepted-plan disposition | **Blocked** | The active improvement addendum says implemented/promoted although it was not merged into `docs/specs/ireland_focus_tree/` and its acceptance ledger remains materially unmet. |

## Six blocking or simplified findings

### 1. Four public political families remain below the accepted depth contract

Evidence:

- The accepted addendum requires at least 16 substantive focuses per public
  family, at least eight selectable in one playthrough, and explicit coverage
  of governing form, economy, security, foreign posture, advisor, company,
  Northern policy, reconstruction, recovery, and capstone
  (`...political_and_territorial_expansion_addendum_2026-08-13.md`, acceptance
  criteria around lines 782-793).
- The communist core is only
  `ireland_congress_reform_bridge` (focus source line 3451),
  `ireland_organise_congress` (3491), the plural/vanguard pair (3513/3541),
  and their capstones (3573/3596).
- The fascist core is only `ireland_oduffy_network_revival` (3621),
  `ireland_oduffy_personal_command` (3666), `ireland_army_acceptance` (3698),
  `ireland_corporate_order` (3719), and two capstones (3741/3769).
- The oligarchic core is `ireland_vocational_constitution` (1360) and its
  capstone (1408). The restoration core is
  `ireland_high_king_evidence_gate` (4040), `ireland_elective_crown` (4082),
  concealed `ireland_guardian_crown` (4104),
  `ireland_crown_powers_charter` (4126), and the capstone (4170).
- Adding each family's cabinet and its few shared territorial nodes still does
  not reach 16 family-specific focuses or the required policy-domain coverage.
- The five gates exist, but their coordinates are scattered:
  democratic `(-16,4)`, communist `(-12,3)`, fascist `(-6,10)`, oligarchic
  `(-8,7)`, and restoration `(-4,4)`. This is not the accepted single legible
  post-National-Settlement gateway row.

Required acceptance fix: either implement the missing substantive family
packages and place all five public gates in the accepted, visually legible fan,
or formally narrow/reject the depth and gateway-row requirements in the
accepted design and source specs. A count reconciliation alone is not enough;
each retained family must still evidence all required policy domains.

### 2. The constitutional advisor pool is not reachable from the whole democratic family

Evidence:

- `ireland_constitutional_service_cabinet` at
  `common/national_focus/ireland_focus_tree.txt:4474` has one prerequisite
  block containing only `ireland_constitutional_stewardship` and
  `ireland_de_valera_reconciliation_capstone` (`:4480`). HOI4 treats focuses
  in one prerequisite block as alternatives, but neither alternative is on
  the Lemass, Fine Gael, Labour/Norton, or Clann profiles.
- Its completion sets
  `ireland_advisor_pool_constitutional_service_unlocked`, while the public
  advisor trigger `ireland_route_advisor_de_valera_lemass` requires that pool
  flag (`common/scripted_triggers/ireland_triggers.txt:4451-4459`). This leaves
  the pool flag unavailable to democratic profiles that the public family is
  meant to cover.
- Thekla Beere's advisor definition uses that trigger
  (`common/characters/ireland_route_characters.txt:1081-1100`), but
  `ireland_constitutional_service_cabinet_reward_tt` at
  `localisation/english/ireland_l_english.yml:5307` names Traynor, Hyde/O'Kelly,
  Aiken, and MacEntee only. Thekla Beere is omitted.
- `ireland_congress_workers_cabinet_reward_tt` (`:5310`) says the vanguard
  advisors become eligible “if the Vanguard Cell is later chosen,” although
  the cabinet itself requires a plural or vanguard capstone
  (`ireland_focus_tree.txt:4488-4497`); plural permanently excludes that later
  choice, and vanguard was already chosen.

Required acceptance fix: give the constitutional cabinet a reachable public
democratic-family prerequisite or explicit alternatives covering every
intended democratic profile, then make the reward tooltip enumerate every
advisor actually unlocked and every remaining route/date condition. Correct
the Congress timing wording to reflect the already-selected capstone.

### 3. One global postwar record can conclude several unresolved holdings

Evidence:

- The local-rights decisions for states 120/122/123, Scottish/Welsh
  protectorates, and Highlands integration all set the same country flag,
  `ireland_atlantic_state_settlement_recorded`
  (`common/decisions/ireland_expansion_decisions.txt:603,614,625,640,656,671`).
- The conclusion path accepts that one global record and can close the single
  Atlantic mission even when Ireland still controls other external states or
  retains another subject relationship. The mission is capacity-safe and
  cleanup-safe, but it is not a per-holding settlement ledger.
- Protectorate effects only release/puppet SCO or WLS and set settlement flags;
  they do not attach the accepted reconstruction obligation or autonomy
  handling.

Required acceptance fix: reserve and record settlement separately for every
controlled external state and relevant SCO/WLS subject relationship. The
conclusion must require every currently retained holding to have its own
rights, protectorate/release, or integration-review outcome. Protectorate
outcomes must also implement the accepted reconstruction/autonomy obligation,
with success, loss, timeout, and archival cleanup.

### 4. Accepted diplomatic demand/refusal phases and naval-access proof are absent

Evidence:

- `common/decisions/ireland_expansion_decisions.txt` contains no target country
  event or saved event-target response chain for the Ulster ultimatum or the
  state 120/122/123 claims. The ultimatum is a self-timed preparation followed
  by direct enforcement; external claim decisions directly add a claim and a
  180-day war goal after readiness succeeds.
- This omits the accepted consent, refusal, counter-offer/partial outcome, and
  force phases described in the addendum's territorial table (including the
  demand/refusal entries around lines 403-425 and the cleanup requirements
  around lines 607 and 834).
- `ireland_atlantic_claim_enforcement_ready` checks material reserves and
  peace, but there is no actual naval-access/reach proof for Cornwall despite
  the accepted coercive-AI and readiness criterion around line 846.

Required acceptance fix: implement the accepted target-scoped diplomatic
response chain with explicit consent/refusal/partial/force results and
deterministic event-target cleanup, and add a real naval-access/reach gate for
the Cornwall coercion path. If direct self-timed coercion is intentionally
preferred, it must be explicitly accepted as a design reduction and promoted
to the source spec.

### 5. Two planned MIOs and the Irish Shipping historical gate are simplified

Evidence:

- All nine runtime companies are ordinary industrial-concern ideas in
  `common/ideas/ireland_industrial_concerns.txt`. The accepted company table
  specifies Ford Cork as a motorised MIO and Harland & Wolff as a naval MIO
  (addendum lines 311 and 315), with project MIO definitions listed among the
  required implementation surfaces near line 759.
- `ireland_irish_shipping_registry` at
  `common/national_focus/ireland_focus_tree.txt:4650-4667` requires the
  maritime reserve and Atlantic convoy office but has no March 1941/emergency
  founding gate from the accepted research basis.
- `docs/ireland_political_industrial_and_territorial_expansion.md:25` calls
  Irish Steel “Steel Holdings,” while the runtime UI and accepted historical
  naming require Irish Steel.

Required acceptance fix: implement and wire the Ford and Harland & Wolff MIO
packages, including their intended contracts and AI selection, or explicitly
accept/promote the ordinary-concern substitution. Add the intended Irish
Shipping date/emergency trigger and align documentation to the Irish Steel
runtime name.

### 6. The accepted addendum is not actually promoted and its completion claim is stale

Evidence:

- The addendum header says “implemented and promoted” at line 7, but its own
  promotion instruction at lines 903 onward requires the architecture,
  family locks, exact focus manifest, company/advisor matrix, territorial
  state groups, AI rules, asset requirements, and acceptance criteria to be
  merged into `docs/specs/ireland_focus_tree/` before that status is used.
- Searches of the active spec tree found none of representative implementation
  identifiers such as `ireland_republican_government`,
  `ireland_define_the_national_question`,
  `ireland_company_electricity_supply_board`,
  `ireland_mission_complete_atlantic_settlement`, or
  `ireland_advisor_pool_constitutional_service_unlocked`.
- The addendum retains nearly all acceptance boxes unchecked while the active
  completion report says no route, package, or simplification is omitted.
- New public helper contracts including
  `ireland_atlantic_claim_enforcement_ready` and
  `ireland_can_launch_postwar_mission` are not documented in
  `docs/ireland_dynamic_effects.md`.

Required acceptance fix: after resolving findings 1-5, merge the finally
accepted architecture and exact contracts into `docs/specs/ireland_focus_tree/`,
update the acceptance ledger with evidence, document the new reusable trigger
contracts, and only then mark the addendum promoted and the feature complete.
If a requirement is rejected or narrowed, record that disposition explicitly
rather than silently treating it as implemented.

## Supported completed implementation

- National Settlement sets the reveal state, and the five public family gates
  use a shared family lock with pairwise mutual exclusion. The family gate no
  longer prematurely commits the downstream profile.
- Exactly nine selectable industrial concerns and nine independent, one-use
  material contracts exist; their concern/flag/contract/GFX crosswalk is
  complete for the compact implementation.
- The 45-card advisor package is complete. The current manifest hashes match
  the runtime DDS files, all cards are 65x67, and the contact sheet shows the
  expected Chaos Redux dossier frames and readable portraits. No advisor-card
  fallback was used.
- Territorial scope is limited to state 119 for the Northern settlement and
  states 120/122/123 plus SCO/WLS for the Atlantic policy. No automatic
  external core was found.
- Coercive final ticks revalidate full shared readiness and exact target
  controller strength/faction/control. Player-facing wording correctly says
  “at least” for the numeric thresholds.
- The final frozen postwar-launch patch is correct: the preparation decision
  exposes an explicit scope tooltip, cancels if all eligible holdings are lost,
  rechecks that same scope and mission capacity before start, refunds a failed
  launch, and maintains the active-capacity marker through every terminal
  hook.
- Parliament is sequential and diagnostically clear. GUI click gates, native
  decisions, and live tooltip rows derive from the same canonical triggers.

## Meaningful validation and limits

- Fresh focus inspection used workspace
  `mod_ireland_total_overhaul_aaca88216c92`, revision
  `34d40fca3ec85b8dadfbb7fd3d6416bd21e854d64136b2c40cc2618c70ba8681`:
  `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/5a3a7cfedf302acba3ec2deeabef854fe641e4634d11815f1994ceace7d4f3f4/8b503ae0108338fff495aac800864edbdf559559732f6f992603a9af2e3fef48/focus-inspect.34d40fca3ec85b8d.json`.
- Fresh rendered graph:
  `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/110af78f7dface0b16e346ad98faffb39313df24f84936193d756375e85e882a/db6410882935bd6c4f7d1eb9257ad3d81035ffdf35f2a2c514f4b61d44568be5/ireland_focus_tree.focus.html`.
- Fresh Parliament GUI inspection used revision
  `1c2498eb38b76ec55fc32e8fbb3e0a39573eaebe3930ab379d00217e49656d62`:
  `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/ee2377ee35023a43c73e06539e76fd9eda279cd73ae2a4ff28c1b8f3a6f259ac/83f29e5c7680ad5c1ddbb520dfc5e7e67f83e19422c6fe14aa95a7bf944b0a4c/gui-inspect.1c2498eb38b76ec5.json`.
  Its three cost-mismatch diagnostics are wrapper-tracing false positives: the
  source executors debit Seanad, Confidence, and Budget exactly once. The tool
  also cannot fully render Lua-driven button state in the minimal scenario.
- Advisor source/runtime/manifest counts and hashes were cross-read, and the
  current contact sheet was visually inspected. The remaining validation limit
  is that this audit did not have a live HOI4 advisor-picker screenshot.

## Accepted-plan disposition and next actions

The political/industrial/territorial improvement addendum is **partially
implemented and still unresolved**, not fully implemented/promoted. The
188-focus count reconciliation is acceptable only as a count decision; it
does not dispose of the family-depth, MIO, diplomatic-response, or per-holding
postwar requirements.

Recommended order:

1. Repair constitutional cabinet reachability and exact advisor tooltips.
2. Implement the missing public-family depth/coverage and settle the gateway
   layout contract.
3. Replace the global postwar record with per-holding settlement accounting
   and add protectorate obligations.
4. Implement or formally reject the diplomatic response chain and naval-access
   proof.
5. Implement or formally accept the MIO substitution and correct company
   historical/documentation gates.
6. Re-run focus, decision/mission, country-package, localisation, and final
   completion audits; then promote the accepted result into specs.

Do **not** request another `hoi4_improvement_loop_planner` pass. The existing
addendum already covers the unresolved depth and implementation gaps; it must
be implemented, narrowed with an explicit reason, or rejected before another
planner pass.

## Skills and references used

Applied `hoi4-feature-planning`, `hoi4-improvement-loop`, `hoi4-subagents`,
`hoi4-focus-trees`, `hoi4-decisions-missions`, `hoi4-events`, and
`hoi4-feature-assets`. The required offline wiki pages, current vanilla
documentation, vanilla Ireland character/GFX precedents, focus prerequisites,
decision availability, advisor small portraits, and industrial concern/MIO
separation were consulted. No skill was created or changed.
