# Ireland non-live scenario trace

Date: 2026-07-29  
Feature: `ireland_focus_tree`  
Namespace: `slopx`

## Boundary and method

The user excluded launching Hearts of Iron IV, fresh-save testing, and live
playthroughs from the completion gate. This audit therefore traces the 22
required coding-prompt scenario families through authored triggers, effects,
events, decisions, missions, focus gates, AI selection, achievement history,
and cleanup. It does not claim observed in-game timing or presentation.

The trace used the current Ireland focus tree, decisions, events, scripted
effects and triggers, script constants, AI strategies and plans, achievements,
country package, localisation, and the dated subsystem audit records.

## 2026-08-01 authority update

The owner-approved M2 ruling resolves the Radical/Underground capacity wording
issue by merging the election and parish-audit modes into their base missions
and using the two freed ordinals for the new radical mission families. The
owner-approved A2 ruling accepts the static hidden treatment for A-22, A-27,
and A-28, so the presentation question noted in scenario 21 is closed without
introducing an unsupported trigger-valued visibility key. Live testing remains
excluded by explicit user direction; this is a source trace, not a running
engine result.

## Scenario matrix

| # | Required scenario | Static trace and result |
| ---: | --- | --- |
| 1 | Historical de Valera from 1936 through postwar emergency expiry | `slopx_ireland_profile_historical_de_valera`, the shared 1936–1938 opening, the de Valera stewardship/reconciliation/emergency focuses and plans, and `postwar_emergency_expiry` form one reachable historical chain. Route conclusion and expiry cleanup are authored. Source trace complete. |
| 2 | Failed and successful 1937 Constitution outcomes | The constitutional event history records separate passed and rejected outcomes; `slopx_ireland_update_achievement_trackers` writes the positive and rejection records separately, and A-01 excludes rejection. Source trace complete. |
| 3 | Hung Dáil and lawful coalition formation | The government-formation focus opens the settlement and election decisions. Confidence-and-supply, alternative Taoiseach, presidential dissolution, coalition negotiations, cabinet portfolios, and coalition-charter actions preserve the formal/routine vote ledgers and distinct resolution records. Source trace complete. |
| 4 | Early Lemass succession and blocked succession | `slopx_ireland_lemass_developmental` has its own availability, cabinet, party-mandate and Dáil-mandate proofs; peaceful succession is recorded only through its accepted route. The historical de Valera plan does not force Lemass. Source trace complete. |
| 5 | Cosgrave, Mulcahy, Costello, Dillon, Norton, and Clann routes | Each named route has a distinct gateway, route flag, spirit progression, capstone, AI profile and focus plan. Dillon alone calls `slopx_ireland_can_dillon`; its full material, parliamentary, sovereignty, Northern and safeguard gate remains canonical. Source trace complete. |
| 6 | National Provision dual bottleneck and component collapse | `slopx_ireland_has_provision_severe_bottleneck` and `slopx_ireland_has_provision_dual_bottleneck` read the separate food, energy, transport and maritime components. The refresh effect records and clears the matching states; conclusion gates reject unresolved bottlenecks. Source trace complete. |
| 7 | Readiness mobilisation without equipment and with full supply | Mobilisation, equipment, command, supply, warning, maritime protection and intelligence remain separate readiness components. Missions and Dillon/readiness gates test the named components rather than the displayed average alone, so mobilisation cannot substitute for equipment or supply. Source trace complete. |
| 8 | Six coastwatch sectors and 83-post historical representation | The Coastwatch action/mission lifecycle uses six named sector histories, seven per-sector component ledgers, a bounded 83-post allocation total, full/partial/failure/escalation outcomes and cleanup. The Coastwatch achievement requires all six operational histories and rejects abandonment. Source trace complete. |
| 9 | Strict neutrality, discreet cooperation, severe incidents, sponsor pressure, and direct attack | Strict/armed neutrality focuses, partner-depth ledgers, airspace, shipping, rescue, internment, intelligence, weather, trade, access, censorship and law actions feed the active incident dispatcher. Severe incidents and direct attack have dedicated gates; sponsor exposure and public legitimacy remain separate. Source trace complete. |
| 10 | Every Dillon gate failure plus valid war entry and demobilisation | `slopx_ireland_can_dillon` centralises mandate, Readiness, Social Consent, Dáil majority, British Leverage, Provision and every named component, reserve, contribution and treaty safeguard. AI cannot select the route without this trigger. War entry and postwar demobilisation use separate records and cleanup. Source trace complete. |
| 11 | Northern negotiation, federation, unitary settlement, lawful deferment, coercive war, occupation, integration stage 5, and final review | The settlement-ledger focus adds only Ireland's legal claim to state 119. Control and occupation are derived from actual state conditions; negotiated, federal, unitary, deferment and coercive histories remain distinct. Integration stage 5 plus final-review proof is required before the sole Ireland core effect can run. Source trace complete. |
| 12 | IRA civil and GHQ outcomes | Civil authority and Army Council/GHQ have separate route flags, focus lanes, spirit outcomes, AI profiles, failures, transitions and capstones. Their route conclusions do not collapse into one ideology skin. Source trace complete. |
| 13 | Congress plural and vanguard outcomes | Plural and vanguard paths have separate gateways, profiles, focus plans, spirit outcomes and conclusions, with route transition and failure records retained. Source trace complete. |
| 14 | O'Duffy failure, succession, corporate order, and restoration | Personal-command and corporate lanes, the dated death/succession handling, failure cleanup, corporate order and constitutional restoration bridge are separately represented in events, route flags, AI and capstones. Source trace complete. |
| 15 | Clerical, producer, and emergency restoration outcomes | Clerical guardianship, producer-state politics and emergency constitutional restoration have separate gates, office/route records, spirit states, failures and conclusions. No political victory directly grants material assets or an office. Source trace complete. |
| 16 | Ailtirí dates, exposure, sponsor collapse, and conclusion | Public access and AI commitment retain explicit 1942 date gates; exposure and German sponsor state are separate requirements. Sponsor collapse activates its overlay and recovery path before the Ailtirí conclusion can be reviewed. Source trace complete. |
| 17 | Serious culture with no hidden reveal | `slopx_ireland_serious_culture_active` opens the historical cultural and archival lane. Hidden permission still requires independent evidence and route-specific proofs; ordinary scholarship does not reveal the concealed routes by itself. Source trace complete. |
| 18 | False lead, constitutional High King, sacral High King, federal provinces, pentarchy, compact, dominion, containment, and convergence | False-lead cleanup and the lawful-household, sacral-crown, captured-crown, Five Provinces, pentarchy, compact, Otherworld dominion/containment and convergence branches use distinct durable flags, focus paths, failures and conclusions. H, P and A permission boundaries remain explicit. Source trace complete. |
| 19 | Historical AI zero hidden commitment | The historical base profile selects the historical focus plan. Concealed Ailtirí and cultural routes require their explicit permission/date/evidence gates, and historical-AI checks suppress premature hidden decisions. Source trace complete. |
| 20 | Sponsor defeat, invalid delivery, debt, exposure, and recovery | Sponsor agreement, delivery validity, debt, exposure, defeat and collapse are separate variables/flags. `slopx_ireland_failed_sponsor_agreement_valid`, the sponsor-collapse overlay, foreign-reaction events and recovery helpers prevent a dead sponsor from remaining a free material channel. Source trace complete. |
| 21 | All 32 achievements, including every disqualifier | All 32 definitions, history writers, negative gates, localisation pairs and three DDS states exist. Positive and disqualifier source paths have been audited. The approved A2 contract accepts static `hidden = yes` for A-22, A-27 and A-28 with their reveal conditions retained in `happened`; no unsupported trigger-valued visibility key is claimed. Source trace complete under the approved static-hidden contract. |
| 22 | Route change, leader death, election defeat, coalition collapse, war entry, demobilisation, occupation end, cultural false lead, compact breach, and conclusion cleanup | `slopx_ireland_cleanup_route_state` and the subsystem cleanup helpers are called from route replacement and failure events. Mission reservations, temporary offices, overlays, event targets, occupation/integration transients, cultural evidence states, compact breach states and postwar obligations each have explicit release/clear paths while durable history is retained. Source trace complete. |

## Result

All twenty-two scenario families have complete non-live source traces under the
current authority rulings. The historical-source clearance queue remains an
independent source-package gate; it is not hidden by this scenario audit.

No live test, fresh save, playthrough, or log claim is made.
