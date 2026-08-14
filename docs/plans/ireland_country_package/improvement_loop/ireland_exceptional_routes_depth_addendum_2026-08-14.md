# Ireland Exceptional Routes Depth Addendum

Date: 2026-08-14  
Status: implementation-ready improvement addendum  
Scope: High Kingship, Five Provinces, Otherworld, and their convergence conclusions  
Classification: concealed P/A route expansion  

## Decision

The exceptional routes still need one bounded depth tranche. This is not a new
sovereignty family. It replaces the current compressed five-focus High
Kingship, four-focus Five Provinces, and six-focus Otherworld selections with
the already specified internal branches, failures, recoveries, and
convergences.

Add exactly **38 focuses**:

| Family | New focuses | Resulting selectable structure |
| --- | ---: | --- |
| High Kingship | 7 | constitutional household, captured crown, sacral crown, two captured outcomes, two sacral outcomes |
| Five Provinces | 9 | federal, Empty Chair, confederal, pentarchic, Fifth Province, and Rival Irelands conclusions |
| Otherworld | 18 | compact law, Tuatha sovereignty, Fianna guardianship, regional courts, containment, sealing, and exploitation |
| convergence | 4 | three pair conclusions and one three-family conclusion |
| **Total** | **38** | **256 total focuses from the current 218-focus source** |

The current 218 focus IDs remain. Reposition only the existing exceptional and
restoration support nodes named below. Keep exactly three roots and keep the five
public family gateways at `y = 14`. The existing 222 connectors are the baseline,
not a target count. New connectors must come only from the prerequisite graph in
this addendum.

## Promises this tranche must close

Implementation is incomplete until all of these are selectable and have their
own state, pressure, outcome, recovery, AI, text direction, and visual identity:

- a crown independent of its sponsoring party, a captive crown, a rescued crown,
  a sacral crown under geasa, and unbounded sacred rule
- a funded federal republic, a lawful Empty Chair, an Irish Confederation, a
  pentarchy, a Fifth Province, and Rival Irelands
- a balanced compact, Tuatha-associated sovereignty, a materially equipped
  Fianna service order, regional Otherworld courts, restored human sovereignty,
  a sterile sealing state, and deliberate exploitation
- Crown and Five Provinces, High King of Two Irelands, Five Courts of the
  Otherworld, and the Fivefold High Kingdom of Two Irelands

Flags, events, or ideas without a focus and decision lifecycle do not satisfy a
listed promise.

## Boundaries

Do not add:

- a fourth concealed sovereignty family
- Brehon judges or Fianna service as independent route families
- a single supernatural nation, generic fantasy species roster, magical resource
  deposits, or unexplained combat bonuses
- free divisions, free equipment, free cores, automatic territorial ownership,
  automatic annexation, or automatic war goals
- a new scripted GUI, new decision category, or a daily or monthly world scan
- a route-dependent audio requirement or a new animation package
- any thumbnail edit

The Brehon learned-order work remains a cross-route legal module. Fianna service
remains one Otherworld compact form. Every extraordinary benefit must be attached
to a finite obligation, material delivery, site condition, or political cost.

## Canonical state model

### Shared implementation rule

Create `common/script_constants/ireland_exceptional_routes.txt` for every new
threshold, delta, duration, dynamic cost tier, and AI weight. Use
`constant:ireland_exceptional_routes.<key>` wherever the field accepts a script
constant. Where a duration or other field rejects constants, copy the constant to
a normal or temporary variable first. Do not duplicate the same value across
focuses, decisions, events, and triggers.

Focus completion, decision completion, and event options call one refresh effect.
No new on-action is required. Boolean state uses flags. Scales and counts use
variables.

### High Kingship

Reuse `ireland_national_settlement` as the crown authority axis and retain its
canonical signed bands:

- constitutional conclusion: `+20` through `+50`
- sacral conclusion: `-45` through `-20`
- captive failure: above `+75`
- unbounded sacred failure: below `-75`

Add or initialise:

- `ireland_royal_legitimacy`, opening `55`
- `ireland_royal_obligation_burden`, opening `20`
- `ireland_household_reach`, opening `20`

The present route clamp of `-60` through `+60` makes both canonical failures
unreachable. High Kingship actions after commitment must clamp the Settlement to
the existing global `settlement_min` and `settlement_max`, not the narrower route
clamp. This exception applies only while a High Kingship conclusion is unresolved.

Clean constitutional readiness requires Royal Legitimacy at least `60`,
Household Reach no more than `45`, no foreign claimant sponsor, no captured-crown
flag, and a Settlement in the constitutional band. The living-land conclusion
requires Royal Legitimacy at least `65`, no overdue geis, a completed royal
circuit, Site Stewardship at least `60`, and a Settlement in the sacral band.

### Five Provinces

Add or initialise:

- `ireland_federal_cohesion`, opening `50`
- `ireland_mandate_leinster`, opening `45`
- `ireland_mandate_munster`, opening `45`
- `ireland_mandate_connacht`, opening `45`
- `ireland_mandate_ulster`, opening `0`
- `ireland_mandate_mide`, opening `35`
- `ireland_middle_balance`, opening `50`

A valid ordinary mandate is at least `55`. Federal conclusion readiness requires
Federal Cohesion at least `60`, each participating mandate at least `55`, a funded
common budget, provincial rights, and National Settlement from `-10` through
`+35`. Mide is an institutional and cultural voice, not a new map state. An
Ulster mandate is valid only through the existing lawful Northern settlement,
representative convention, cultural delegation, or negotiated special-status
flags. Ownership, a core, a claim, or occupation alone never creates it.

The Empty Chair requires Leinster, Munster, Connacht, and Mide at `55`, Federal
Cohesion at `60`, Minority Confidence at `60`, a protected Ulster seat, and no
invented Ulster mandate. Rival Irelands becomes available when Federal Cohesion
falls below `25`, two participating mandates fail, a provincial guard refuses
common command, or a provincial fiscal mission fails twice.

### Otherworld

Reuse `ireland_national_settlement` as the sovereignty axis after the verified
entry:

- Otherworld dominion: `-100` through `-76`
- Sovereignty of the Mounds: `-75` through `-46`
- balanced compact: `-15` through `+15`
- Human Stewardship: `+16` through `+45`
- containment authority: `+46` through `+75`
- sterile sealing state: `+76` through `+100`

Reuse `ireland_compact_trust` and `ireland_veil_stability`, both already opening
at `55`. Add or initialise:

- `ireland_otherworld_active_obligations`, opening `0`
- `ireland_otherworld_broken_obligations`, opening `0`
- `ireland_fian_readiness`, opening `0`
- `ireland_regional_compact_count`, opening `0`

The obligation ledger is a count plus named due flags. Every accepted bargain
must have an owner, deadline, success, partial result, failure, and cleanup.
Compact conclusions require trust and stability at least `60`, no due obligation,
and no broken-compact flag. A breach begins when Veil Stability reaches `0`, two
obligations are overdue, or deliberate extraction completes.

Fianna readiness counts delivered training, manpower, equipment, supply, command,
and one completed service objective. A focus cannot create a unit. The player
must train and deploy the formation through ordinary mechanics. A route helper
may recognise the completed template and force state, but it must not add
manpower, equipment, or divisions.

### Three-family convergence

The final conclusion requires the live values, not only completion flags:

- constitutional or elected crown and valid succession
- five valid provincial voices with a lawful Ulster rule
- balanced Otherworld compact
- `ireland_cultural_site_stewardship` at least `85`
- `ireland_cultural_regional_participation` at least `80`
- `ireland_cultural_archival_record` at least `85`
- `ireland_social_consent` at least `65`
- no captive crown, provincial warlord, fabricated evidence, exclusion state,
  foreign patron, deliberate breach, dominion, or sealing-state conclusion
- successful 180-day convergence review

The final result creates recurring succession, provincial veto, compact
obligation, site-defence, rights-review, and foreign-pressure work. It is not a
universal positive modifier.

## Exact focus layout and rewards

Focus cost `5` means 35 days and cost `10` means 70 days under the current tree
rules. No new focus is a pure flag setter. Each focus either changes a live route
value, opens a decision or mission, fires a state-defining event, transforms the
single spirit slot, or commits a conclusion.

### High Kingship reflow

Reposition and reconnect these existing nodes:

| Existing ID | Coordinate | Required prerequisite or role change |
| --- | --- | --- |
| `ireland_high_king_evidence_gate` | `(0,14)` | unchanged public-to-concealed gateway, initialise the three crown values |
| `ireland_claimants_convention` | `(0,15)` | prerequisite `ireland_high_king_evidence_gate`, fire existing convention event `ireland_events.214` |
| `ireland_elective_crown` | `(-2,16)` | prerequisite `ireland_claimants_convention`, mutually exclusive with guardian form |
| `ireland_guardian_crown` | `(2,16)` | prerequisite `ireland_claimants_convention`, mutually exclusive with elective form |
| `ireland_crown_powers_charter` | `(0,17)` | OR prerequisite elective or guardian, record powers and constitutional limits |
| `ireland_provincial_compact` | `(-2,18)` | prerequisite charter, add provincial assent and a bounded legitimacy gain |
| `ireland_brehon_law_commission` | `(2,18)` | prerequisite charter, add legal capacity and open learned-order mediation only |
| `ireland_crown_defence_council` | `(0,19)` | AND prerequisite compact and commission, define civilian command and guard limits |
| `ireland_household_council` | `(0,21)` | prerequisite defence council, constitutional conclusion choice, mutually exclusive with the captured and sacral roots below |
| `ireland_high_king_capstone` | `(0,24)` | OR prerequisite household council, rescued crown, captive throne, living land, or unbounded sacred rule |

`ireland_household_council` now completes the independent-household conclusion.
Its reward must audit appointments, reduce Household Reach, set the clean crown
conclusion, refresh the governing spirit, and open succession and petition
actions. It must not share conclusion flags with the sacral or captured paths.

Add these seven focuses:

| ID | Coordinate | Cost | Prerequisite and exclusion | Concrete reward |
| --- | --- | ---: | --- | --- |
| `ireland_crown_in_party_hands` | `(-4,21)` | 5 | `ireland_crown_defence_council`; mutually exclusive with `ireland_household_council` and `ireland_the_stone_gives_its_answer`; authoritarian sponsor or capture event | commit captured path, raise Household Reach by `20`, lower Legitimacy by `10`, add one obligation, apply the existing captive-crown governing form, fire event `441`, unlock household audit and break actions |
| `ireland_break_the_captive_crown` | `(-5,22)` | 10 | captured root plus completed break action; mutually exclusive with captive throne | record palace break or lawful abolition of sponsor control, remove the captive form, set rescued constitutional conclusion, lower Household Reach by `25`, refresh the ordinary crown form, fire event `442` |
| `ireland_the_captive_throne` | `(-3,22)` | 10 | captured root plus Settlement above `75` or failed break mission; mutually exclusive with rescue | commit failure conclusion, preserve the captive spirit and party-control penalties, set the captive cosmetic tag, close clean succession decisions, begin recurring legitimacy and opposition review |
| `ireland_the_stone_gives_its_answer` | `(4,21)` | 5 | defence council, verified impossible Lia Fáil result, no fabrication; mutually exclusive with household and captured roots | commit sacral path, shift Settlement toward sacral authority, add the first obligation, fire event `440`, use the existing crown-selection animation, unlock geis acceptance |
| `ireland_geasa_of_the_crown` | `(4,22)` | 5 | stone answer | open the obligation ledger and royal-circuit mission, add a named due geis selected by event `443`, refresh the sacral governing form, no permanent bonus before fulfilment |
| `ireland_high_kingdom_of_the_living_land` | `(3,23)` | 10 | geasa, clean sacral trigger, successful circuit; mutually exclusive with unbounded rule | commit the living-land conclusion, use the existing sacral cosmetic identity, convert only fulfilled obligations into bounded timed benefits, start continuing site and petition duties |
| `ireland_unbounded_sacred_rule` | `(5,23)` | 10 | geasa and Settlement below `-75`, or two broken geasa and refusal of penance; mutually exclusive with living land | commit failure conclusion, apply an unbounded-sacral governing replacement with law, consent, and foreign-recognition penalties, close clean convergence, open council limitation, abdication, and compact-submission recovery |

The High King capstone performs route cleanup and starts the ordinary conclusion
review. Remove its current automatic grants of every convergence flag:
`ireland_fivefold_obligation_complete`,
`ireland_fivefold_obligation_ready`,
`ireland_otherworld_convergence_complete`,
`ireland_otherworld_convergence_ready`,
`ireland_crown_province_convergence_complete`,
`ireland_convergence_components_ready`,
`ireland_convergence_order_capstone_complete`,
`ireland_convergence_order_concluded`, and
`ireland_convergence_verified`. The four convergence focuses below become the
only owners of those results.

### Five Provinces reflow

Move the existing nodes to the clear east band:

| Existing ID | Coordinate | Required role |
| --- | --- | --- |
| `ireland_five_province_mandates` | `(25,5)` | route entry and mandate initialisation |
| `ireland_federal_republic` | `(21,7)` | ordinary federal commitment root |
| `ireland_pentarchy_guardians` | `(29,7)` | absurd provincial-sovereignty root |
| `ireland_five_provinces_capstone` | `(25,11)` | OR of all six terminal conclusions |

Add these nine focuses:

| ID | Coordinate | Cost | Prerequisite and exclusion | Concrete reward |
| --- | --- | ---: | --- | --- |
| `ireland_provincial_powers_convention` | `(25,6)` | 5 | mandates | fire event `444`, open province-by-province mandate and budget actions, make rights, finance, guard, transport, and Ulster rules visible |
| `ireland_fund_the_federal_compact` | `(21,8)` | 10 | federal republic plus funded-common-compact mission success; mutually exclusive with Empty Chair | commit Federal Republic conclusion, set common-budget and common-command flags, refresh the federal spirit, open recurring equalisation and veto arbitration |
| `ireland_four_provinces_and_an_empty_chair` | `(19,9)` | 10 | federal republic, four southern voices valid, Ulster mandate absent, protected-seat mission complete; mutually exclusive with funded five-voice federation | commit valid partial conclusion, set protected-chair flag and distinct governing replacement, fire event `445`, open later lawful participation review without claim, core, or ownership |
| `ireland_council_by_provincial_mandate` | `(25,7)` | 5 | powers convention; mutually exclusive with federal republic and pentarchy guardians | commit confederal path, increase Middle Balance, open confederal council and rotating-chair actions |
| `ireland_irish_confederation` | `(25,8)` | 10 | mandate council, four or five valid voices, confederal budget and rights clauses | commit Irish Confederation conclusion, use confederation cosmetic identity and same-slot governing replacement, begin recurring contribution schedule and withdrawal arbitration |
| `ireland_five_sovereign_orders` | `(29,8)` | 5 | pentarchy guardians | give each recorded provincial voice a separate budget, guard, and veto obligation, lower Federal Cohesion, open the middle-place dispute, do not create states, subjects, or armies |
| `ireland_pentarchy_of_ireland` | `(27,9)` | 10 | five sovereign orders, five lawful voices at threshold, Middle Balance stable; mutually exclusive with Fifth Province and Rival Irelands | commit pentarchy conclusion, refresh existing pentarchy spirit and identity, open recurring unanimity and common-defence bargains |
| `ireland_the_fifth_province` | `(31,9)` | 10 | five sovereign orders, Mide mandate and Uisneach review complete, no fabricated claim; mutually exclusive with pentarchy and Rival Irelands | commit symbolic fifth-province conclusion, apply a same-slot centre-arbitration spirit, open assembly and mediation duties, never create a new state or core |
| `ireland_rival_irelands` | `(29,10)` | 10 | five sovereign orders plus failure trigger; mutually exclusive with pentarchy and Fifth Province | commit failure conclusion, apply existing rival-sovereignties penalty form and cosmetic identity, close convergence, open disarmament, renewed convention, or negotiated confederation recovery |

The capstone OR-prerequisite list is exactly:
`ireland_fund_the_federal_compact`,
`ireland_four_provinces_and_an_empty_chair`,
`ireland_irish_confederation`,
`ireland_pentarchy_of_ireland`,
`ireland_the_fifth_province`, or `ireland_rival_irelands`.

### Otherworld reflow

Move the existing nodes to a separate west band:

| Existing ID | Coordinate | Required role |
| --- | --- | --- |
| `ireland_otherworld_investigation` | `(-36,4)` | investigation entry |
| `ireland_otherworld_evidence_ledger` | `(-36,5)` | verified posture decision point |
| `ireland_compact_with_otherworld` | `(-36,6)` | negotiated contact root |
| `ireland_containment_protocol` | `(-28,6)` | containment root |
| `ireland_dominion_claim` | `(-44,10)` | exploitation terminal only, remove its current AND prerequisite on compact and containment |
| `ireland_otherworld_capstone` | `(-36,12)` | OR of compact, Tuatha, Fianna, human, sealed, or dominion terminals |

At the evidence ledger, `ireland_compact_with_otherworld`,
`ireland_containment_protocol`, and `ireland_turn_contact_into_power` are mutually
exclusive and correspond to the choices already made in `ireland_events.437`.
Rejection in event `437` routes to containment and later human restoration. It
does not erase the verified event or return the campaign to historical
classification.

Add these eighteen focuses:

| ID | Coordinate | Cost | Prerequisite and exclusion | Concrete reward |
| --- | --- | ---: | --- | --- |
| `ireland_turn_contact_into_power` | `(-44,6)` | 5 | evidence ledger and exploitation choice; mutually exclusive with compact and containment | commit exploitation, lower Trust and Veil Stability, unlock named-site extraction mission, fire event `450` |
| `ireland_compel_an_answer` | `(-44,7)` | 5 | exploitation root | spend command, political, and security capacity to open a coercive obligation; any benefit is timed until its extraction mission resolves |
| `ireland_the_state_owns_the_mounds` | `(-44,8)` | 10 | compel answer | fire event `454`, seize administrative custody only, lower Site Stewardship and Trust, open restitution counterplay, grant no state ownership or resource deposit |
| `ireland_a_breach_made_deliberately` | `(-44,9)` | 10 | state owns mounds plus failed or completed coercive extraction | fire event `455`, set deliberate-breach disqualifier, apply existing compact-breach pressure and open breach containment; prerequisite for existing dominion claim |
| `ireland_the_rights_of_local_guardians` | `(-34,7)` | 5 | compact root; mutually exclusive with Elder Claim and Hounds roots | fire a rights and custody event, raise Trust, record human-law minimums, open obligation and regional-hearing actions |
| `ireland_a_law_for_two_orders` | `(-34,8)` | 10 | local guardians, balanced compact trigger | commit Compact of Two Irelands conclusion, refresh compact spirit and identity, start recurring obligation and rights review |
| `ireland_recognise_the_elder_claim` | `(-42,7)` | 5 | compact root and verified Tuatha-associated evidence; mutually exclusive with local-guardian and Hounds roots | commit Tuatha path, shift sovereignty left, record which site court makes the claim, fire event `451` |
| `ireland_the_courts_beneath_the_hills` | `(-42,8)` | 5 | elder claim | recognise bounded standing and jurisdiction, add one site duty, keep human criminal and minority rights unconditional |
| `ireland_a_government_under_the_mounds` | `(-42,9)` | 10 | courts, sovereignty band, Trust at least `50`, no deliberate breach | commit Sovereignty of the Mounds conclusion, apply a same-slot Tuatha governing form, open submission, renegotiation, and human-law recovery, no foreign policy or army control without further obligations |
| `ireland_the_hounds_are_heard_again` | `(-38,7)` | 5 | compact root and verified Fianna-associated evidence; mutually exclusive with guardian-rights and Elder Claim roots | commit Fianna path, fire event `452`, open service charter without creating a formation |
| `ireland_muster_a_modern_fian` | `(-38,8)` | 5 | Hounds | unlock a normal player-built template and readiness ledger, begin equip-company mission, add no manpower or equipment |
| `ireland_no_host_without_equipment` | `(-38,9)` | 5 | muster and full material checks | certify only an actually deployed, equipped, supplied, trained, and commanded formation, raise Fian Readiness, open one service objective |
| `ireland_guardians_of_two_irelands` | `(-38,10)` | 10 | equipment focus plus completed service objective and no broken geis | commit Fianna guardianship conclusion, use existing guardians icon, apply a same-slot security form with continuing service and supply duties |
| `ireland_regional_otherworld_courts` | `(-30,7)` | 5 | compact root, compatible with any one compact authority lane | fire event `453`, open one regional-hearing action for each lawful voice, initialise regional compact count |
| `ireland_no_single_story_rules_them_all` | `(-30,8)` | 10 | regional courts plus at least four recorded compacts | protect separate regional actors and contradictory terms, open reconciliation mission, set Five Courts component ready only at five lawful compacts |
| `ireland_the_emergency_must_end` | `(-28,7)` | 5 | containment protocol; mutually exclusive with sealed state | open perimeter-narrowing actions and public review, lower security burden only through completed closure objectives |
| `ireland_human_sovereignty_restored` | `(-28,8)` | 10 | emergency must end, Veil Stability at least `60`, evidence archived, no permanent detention | commit human-stewardship conclusion, retain a bounded site office and witness safeguards, remove emergency penalties, never reclassify the impossible evidence as historical |
| `ireland_the_sealed_state` | `(-26,8)` | 10 | containment protocol plus Settlement above `75` or failed emergency review; mutually exclusive with emergency must end | commit failure conclusion, apply the existing containment form as a permanent same-slot penalty, close balanced convergence, open later archive release and civil-authority recovery |

The Otherworld capstone OR-prerequisite list is exactly:
`ireland_a_law_for_two_orders`,
`ireland_a_government_under_the_mounds`,
`ireland_guardians_of_two_irelands`,
`ireland_human_sovereignty_restored`,
`ireland_the_sealed_state`, or `ireland_dominion_claim`.

### Convergence band

Add these four focuses after the component capstones:

| ID | Coordinate | Cost | Prerequisite and availability | Concrete reward |
| --- | --- | ---: | --- | --- |
| `ireland_high_king_of_two_irelands` | `(-8,25)` | 10 | High King capstone AND Otherworld capstone; living-land crown, valid succession, compact or mound-court law, no captive, unbounded, dominion, or sealed state | fire event `458`, commit the crown-Otherworld conclusion, set only `ireland_otherworld_convergence_complete/ready`, use the existing Otherworld convergence icon and one bounded governing replacement |
| `ireland_crown_and_five_provinces` | `(8,25)` | 10 | High King capstone AND Five Provinces capstone; elected or powers-returned guardian crown, lawful provincial conclusion, no captive or Rival Irelands | fire event `457`, commit crown-province conclusion, set only `ireland_crown_province_convergence_complete`, use the existing crown-province icon, open succession and provincial-veto review |
| `ireland_five_courts_of_the_otherworld` | `(16,25)` | 10 | Five Provinces capstone AND Otherworld capstone; five lawful voices, five recorded regional compacts, no Rival Irelands, dominion, or sealed state | fire event `459`, commit Five Courts conclusion, set `ireland_fivefold_obligation_complete/ready`, use existing fivefold-obligation icon, open contradictory-obligation arbitration |
| `ireland_fivefold_high_kingdom_of_two_irelands` | `(4,27)` | 10 | AND prerequisite all three pair focuses and exact three-family trigger | fire event `460`, set `ireland_convergence_components_ready`, start the 180-day convergence review, use existing convergence capstone icon; only full mission success sets `ireland_convergence_order_capstone_complete`, `ireland_convergence_order_concluded`, and `ireland_convergence_verified` |

The full route is reachable in one coherent playthrough: choose an elective crown,
take the verified sacral branch while retaining its constitutional election and
law, complete a valid federal or confederal Five Provinces conclusion, complete
the balanced Otherworld compact plus the regional-courts side lane, finish the
three pair focuses, then pass the convergence review.

## Decisions and missions

Use existing categories only: `ireland_settlement_government`,
`ireland_cultural_archival`, `ireland_readiness`,
`ireland_occupation_integration`, and `ireland_regional_external`. Reuse the
existing crown association, fivefold compact, compact-obligation, five-sites,
and provincial-assent decisions. Add the following IDs.

| ID | Type and duration | Cost or objective | Full result | Partial or failure and recovery |
| --- | --- | --- | --- | --- |
| `ireland_action_audit_the_royal_household` | action | dynamic `15/20/25` PP by Household Reach | remove one captured appointment, Reach `-10`, Legitimacy `+5` | exposed obstruction adds one obligation; repeatable only while capture exists |
| `ireland_action_break_the_party_crown` | action | `25` PP, neutral security command, two clean household audits | open rescue focus and fire palace-break event | failure starts `ireland_mission_break_the_party_crown`; sponsor may retain control, never auto-purged |
| `ireland_action_accept_a_royal_geis` | action | choose one currently affordable named obligation | create due flag and a bounded conditional benefit | refusal lowers Legitimacy, breach records the exact geis and opens penance |
| `ireland_mission_complete_the_royal_circuit` | 120 days | visit four lawful provincial centres and one protected royal site, with transport and security supplied | circuit success, Legitimacy and Site Stewardship rise | four objectives gives conditional result; fewer or a lost site creates boycott or broken-obligation recovery |
| `ireland_mission_break_the_party_crown` | 120 days | keep Household Reach below `60`, Social Consent at `55`, and security neutral | rescue focus becomes available | expiry commits Captive Throne unless abolition or a new convention is chosen |
| `ireland_action_negotiate_a_provincial_budget` | action | dynamic `15/20/25` PP and one civilian-factory commitment by cohesion | raise one named mandate and record its contribution | refused budget lowers Cohesion and increments fiscal-failure count |
| `ireland_action_reserve_the_ulster_chair` | action | `20` PP, Minority Confidence `60`, no coercive northern flag | protected empty chair recorded | false representation sets exclusion and fabricated-mandate disqualifiers |
| `ireland_action_call_a_confederal_council` | action | `20` PP, four participating voices | settle one contribution or veto | absent voice lowers Cohesion but does not erase its mandate |
| `ireland_action_arbitrate_a_provincial_veto` | action | `20` PP or scaled concession | resolve one veto, adjust Middle Balance toward centre | imposed ruling raises rival-authority pressure |
| `ireland_mission_fund_the_common_compact` | 120 days | deliver common budget, transport contribution, and funded command | federal funding flag and Cohesion gain | two of three gives conditional funding; expiry records a fiscal failure and opens confederal rescue |
| `ireland_mission_keep_the_fifth_seat_open` | 180 days | preserve rights and northern contacts without invented mandate or coercion | Empty Chair remains a stable conclusion | partial result starts renewed contact; coercion invalidates the chair and opens Rival Irelands pressure |
| `ireland_mission_prevent_rival_irelands` | 120 days | restore Cohesion to `45`, settle two budgets, and return guards to common law | renewed convention, confederation, or lawful dissolution recovery | expiry commits Rival Irelands and its recurring foreign-pressure crisis |
| `ireland_action_record_an_otherworld_obligation` | action | dynamic `15/20/25` PP plus the selected policy or material commitment | add named due obligation with owner and deadline | refusal changes Trust; no benefit is granted before acceptance |
| `ireland_action_hear_a_regional_court` | action | `20` PP, valid local voice and access to its site | record one regional compact and its distinct terms | conditional compact remains local; failed hearing reduces Trust without faking national assent |
| `ireland_action_restitute_a_seized_site` | action | `25` PP, withdraw assigned security, surrender extracted benefit | repair Trust and Veil Stability, clear one seizure | partial restitution opens a monitored obligation; refusal preserves breach |
| `ireland_action_narrow_the_containment_perimeter` | action | `20` PP, civil-authority and witness safeguards | reduce containment pressure and release one site | unsafe release lowers Veil Stability; continued detention raises sealing-state pressure |
| `ireland_mission_equip_a_fian_company` | 120 days | player-trained formation, manpower, infantry and support equipment, supply, command, and training | certify service company, raise Fian Readiness | understrength completion creates cultural service corps only; expiry gives no unit and records route fraud if claimed as ready |
| `ireland_mission_keep_the_veil_at_five_sites` | 180 days | five named lawful site duties, no hostile occupation shortcut | Veil Stability and Site Stewardship rise | four sites creates a penance obligation; fewer creates a breach crisis |
| `ireland_mission_repair_the_broken_compact` | 120 days | restitution, public admission, two fulfilled obligations, protected witness | clear broken compact and reopen balanced recovery | partial result contains incidents; expiry advances dominion or sealing pressure by active posture |
| `ireland_mission_reconcile_regional_compacts` | 150 days | five local records, common rights floor, resolve two contradictory duties | Five Courts component ready | four compatible compacts retain regional route but block convergence; coercion invalidates the relevant mandate |
| `ireland_mission_extract_from_a_protected_site` | 90 days | security and industrial commitment at one named site | one strong timed benefit and an immediate due restitution obligation | partial extraction gives only intelligence; failure damages site, Trust, and Veil Stability and opens breach event |
| `ireland_mission_survive_the_first_convergence_review` | 180 days | keep every final threshold, fulfil one crown duty, settle one veto, fulfil two compact obligations, protect one site, avoid patron capture | set final convergence completion, replace component spirits with the convergence form, archive evidence | partial result extends review once with named deficits; failure separates components and reopens their recovery actions without deleting their histories |

Dynamic action costs use the existing scarcity pattern. Low-pressure actions cost
`15`, watch pressure costs `20`, and severe pressure costs `25`. Command-heavy
actions also require `20/30/40` command power. Only the constant table owns these
tiers.

## Events

Create `events/ireland_exceptional_route_events.txt` with the namespace already
used by `ireland_events`. Reserve exactly `438` through `460` for this tranche.
Every event option must show its route-value changes, obligation, unlock, and
disqualifier in the tooltip. Reports and rumours are not written as proof until
the verified transition.

| ID | Purpose | Required choice structure |
| ---: | --- | --- |
| `438` | claimant credentials board | independent audit, conditional admission, public rejection, or sponsor capture |
| `439` | royal household accounts | publish and narrow, fund transparently, hide patronage, or empower a court party |
| `440` | the stone gives an answer | accept witnessed obligation, demand wider verification, seal the evidence, or fabricate, with fabrication permanently disqualifying convergence |
| `441` | crown under party direction | accept controlled pageantry, protect a legal household, call opposition witnesses, or abolish the project |
| `442` | palace break or constitutional rescue | independent succession, public convention, abolition, or failed seizure |
| `443` | first geis | one of three affordable named duties or refusal, never a free reward |
| `444` | provincial powers convention | federal budget, confederal council, sovereign orders, or adjournment |
| `445` | Ulster seat | lawful participation, protected empty chair, special status, or invented mandate failure |
| `446` | five budgets | equal contribution, capacity-weighted contribution, one conditional exemption, or fiscal split |
| `447` | federal or confederal ratification | common law, looser compact, defer for mandates, or impose and create failure |
| `448` | the middle decides | meeting-place arbitration, federal district symbolism, sovereign fifth claim, or rejection |
| `449` | Rival Irelands | disarm and reconvene, negotiate confederation, accept rivalry, or request foreign help and become patron-exposed |
| `450` | terms of contact | compact, containment, exploitation, or human inquiry, mirroring event `437` state without reopening the reveal |
| `451` | courts beneath the hills | rights-bounded standing, limited site jurisdiction, submission, or refusal and grievance |
| `452` | Fian muster | properly equip service, civilian service corps, postpone, or fraudulent proclamation |
| `453` | a province makes its own compact | ratify locally, place under federal framework, renegotiate, or coerce and lose mandate |
| `454` | state seizes a mound | administrative custody, reversible extraction, full seizure, or restitution |
| `455` | breach by design | contain damage, pay restitution, double down toward dominion, or conceal and worsen Veil loss |
| `456` | sealed-site emergency review | civil release, narrower perimeter, permanent sealing, or uncontrolled release |
| `457` | Crown and Provinces Convention | define succession, veto, finance, and command, with no automatic territorial authority |
| `458` | High King of Two Irelands | bind crown to human law and geasa, submit to mound sovereignty, defer, or fail on broken obligation |
| `459` | Five Courts arbitration | common rights floor, provincial autonomy, unresolved contradiction, or central coercion |
| `460` | Three Orders review | begin full review, postpone with named deficit, separate components, or illegitimate imposition failure |

Use existing event families `214`, `216` through `219`, and `437` as entry and
pressure events. Do not duplicate their reveals.

## Ideas, identity, and persistent state

Keep the existing three-spirit ceiling. Every item below replaces another item
in the governing, organised-society, or security slot through
`ireland_refresh_route_spirits`. Do not add a fourth persistent spirit.

New same-slot idea forms:

- `ireland_spirit_governing_five_provinces_confederation`
- `ireland_spirit_governing_five_provinces_empty_chair`
- `ireland_spirit_governing_five_provinces_fifth_province`
- `ireland_spirit_governing_high_king_unbounded`
- `ireland_spirit_governing_otherworld_tuatha`
- `ireland_spirit_security_otherworld_fianna`
- `ireland_spirit_society_otherworld_regional_courts`

Reuse the existing constitutional, sacral, captive, federal, pentarchy, rival,
compact, containment, dominion, breach, and convergence idea forms. Modifiers
must be mixed and in five-point increments. Route strength is chiefly delivered
through fulfilled decisions, not permanent modifier inflation.

Do not add durable route profiles. Preserve the exact 30-profile framework in
`ireland_sync_route_profile`. Use conclusion flags beneath the existing broad
profiles. Add these mutually exclusive conclusion flag families:

- High King: `ireland_conclusion_high_king_independent_household`,
  `ireland_conclusion_high_king_crown_rescued`,
  `ireland_conclusion_high_king_captive_throne`,
  `ireland_conclusion_high_king_living_land`,
  `ireland_conclusion_high_king_unbounded_sacred_rule`
- Five Provinces: `ireland_conclusion_five_provinces_federal`,
  `ireland_conclusion_five_provinces_empty_chair`,
  `ireland_conclusion_five_provinces_confederation`,
  `ireland_conclusion_five_provinces_pentarchy`,
  `ireland_conclusion_five_provinces_fifth_province`,
  `ireland_conclusion_five_provinces_rival_irelands`
- Otherworld: `ireland_conclusion_otherworld_compact`,
  `ireland_conclusion_otherworld_tuatha_sovereignty`,
  `ireland_conclusion_otherworld_fianna_guardianship`,
  `ireland_conclusion_otherworld_human_sovereignty`,
  `ireland_conclusion_otherworld_sealed_state`,
  `ireland_conclusion_otherworld_dominion`
- convergence: `ireland_conclusion_crown_and_five_provinces`,
  `ireland_conclusion_high_king_two_irelands`,
  `ireland_conclusion_five_courts_otherworld`,
  `ireland_conclusion_fivefold_high_kingdom_two_irelands`

Add cosmetic identities only where the governing order is materially different:

- `IRE_IRELAND_CAPTIVE_THRONE`
- `IRE_IRELAND_CONFEDERATION`
- `IRE_IRELAND_FIFTH_PROVINCE`
- `IRE_IRELAND_RIVAL_PROVINCES`
- `IRE_IRELAND_TUATHA_SOVEREIGNTY`
- `IRE_IRELAND_FIANNA_GUARDIANSHIP`
- `IRE_IRELAND_SEALED_STATE`
- `IRE_IRELAND_CROWN_AND_PROVINCES`
- `IRE_IRELAND_HIGH_KING_TWO_IRELANDS`
- `IRE_IRELAND_FIVE_COURTS_OTHERWORLD`

Reuse the existing sacral, pentarchy, compact, dominion, federation, and final
convergence identities when their meanings match exactly. Empty Chair retains
the federal identity with distinct conclusion text and spirit.

## Scripted helpers

Implement these reusable helpers rather than repeating threshold blocks:

Scripted effects:

- `ireland_initialize_high_kingship_values`
- `ireland_initialize_five_provinces_values`
- `ireland_refresh_provincial_mandates`
- `ireland_initialize_otherworld_obligations`
- `ireland_refresh_exceptional_route_state`
- `ireland_commit_exceptional_conclusion`
- `ireland_close_exceptional_route_decisions`

Scripted triggers:

- `ireland_high_king_clean_constitutional_conclusion`
- `ireland_high_king_sacral_conclusion_ready`
- `ireland_high_king_captured_failure_ready`
- `ireland_five_provinces_federal_conclusion_ready`
- `ireland_five_provinces_empty_chair_ready`
- `ireland_five_provinces_confederation_ready`
- `ireland_five_provinces_sovereignty_conclusion_ready`
- `ireland_otherworld_balanced_conclusion_ready`
- `ireland_otherworld_tuatha_ready`
- `ireland_otherworld_fianna_ready`
- `ireland_otherworld_exploitation_ready`
- `ireland_crown_five_provinces_convergence_ready`
- `ireland_high_king_otherworld_convergence_ready`
- `ireland_five_courts_convergence_ready`
- `ireland_three_orders_convergence_ready`

Update `docs/ireland_dynamic_effects.md` with scope, inputs, outputs, defaults,
side effects, and examples for each helper.

## AI contract

Historical AI has factor `0` on every concealed commitment and convergence
focus. It may complete ordinary cultural research and close unexplained incidents
without validating an impossible route.

Nonhistorical AI uses the existing broad profiles. Target relative selection
weights are centralised once per decision point:

| Choice | Base weight | Mandatory zero conditions | Positive factors |
| --- | ---: | --- | --- |
| independent household | 10 | captured sponsor already controls convention | functioning Dáil, legitimacy `60`, low Household Reach |
| captured crown | 4 | plural government or sponsor-independent claimant | authoritarian family, high Household Reach, high settlement |
| sacral crown | 3 | no hidden permission, no verified stone result, fabricated evidence | affordable obligations, site stewardship `60`, legitimacy `65` |
| federal republic | 10 | fewer than four valid mandates | high Cohesion, funded budget, lawful Ulster route |
| confederation | 7 | fewer than four willing voices | uneven capacity, repeated vetoes, valid shared rights |
| provincial sovereignty | 3 | historical mode or low regional evidence | high Mide mandate, high Middle Balance, absurd permission |
| balanced compact | 10 | no verified entry or trust below `45` | trust and veil above `60`, plural rights profile |
| containment | 6 | no verified entry | authoritarian security, low veil, limited obligations |
| exploitation | 2 | plural profile, trust already broken without repair capacity, or no material capacity | authoritarian or desperate government, high command capacity |
| Tuatha-associated claim | 4 | no source-qualified evidence or rights floor | left-of-centre sovereignty and affordable duties |
| Fianna service | 5 | insufficient equipment, manpower, supply, or command | readiness and equipment surplus, one feasible service objective |
| regional courts side lane | 6 | fewer than four lawful voices | valid federal/confederal route and high regional participation |
| final convergence | 1 | any exact disqualifier or unmet component floor | every component complete and review obligations affordable |

AI never accepts a geis it cannot fulfil, invents an Ulster mandate, proclaims an
unequipped Fian, treats a failed extraction as a free benefit, or chooses a
convergence focus while a recovery mission is active. On failure it prioritises
penance, renewed convention, confederation, component separation, or civil
restoration over optional focuses.

## Localisation and writing direction

This addendum supplies direction, not final localisation prose. Every new focus,
decision, mission, idea, event, cosmetic identity, trigger tooltip, effect
tooltip, and failure state needs English localisation in UTF-8 with BOM and no
`:0` key versioning.

Writing rules:

- Public pre-reveal text speaks of records, testimony, place, damage, weather,
  custody, and obligation. It does not announce an Otherworld route.
- Post-reveal text can identify impossible actors, but it distinguishes each
  local court, guardian, literary association, and human interpreter.
- High Kingship text distinguishes election, guardianship, household law,
  sacral obligation, and party captivity. It does not present a living claimant
  as historically legitimate without research.
- Five Provinces text presents a modern negotiated institution inspired by
  historical geography. It does not claim that a fixed five-province federal map
  survived into 1936.
- Mide is a meeting-place and institutional claim. Ulster always names the
  legal-access and consent problem.
- Fianna and Tuatha terms are explicitly literary, folkloric, or absurd-route
  framing, not evidence of historical twentieth-century institutions.
- No invented proverb, traditional quote, genealogy, or sacred formula.
- Failure text names what failed and what recovery remains. It does not call a
  partial result a victory.

## Icons, report art, flags, and animation

Every new focus receives `GFX_focus_<focus_id>` in `interface/ireland_icons.gfx`,
a corresponding shine definition, and a unique DDS at
`gfx/interface/goals/ireland/goal_<focus_id>.dds`, except where the following
registered sprite already matches exactly:

- `ireland_guardians_of_two_irelands` uses
  `GFX_focus_ireland_otherworld_guardians`
- `ireland_the_state_owns_the_mounds` may use
  `GFX_focus_ireland_otherworld_statecraft` only if the final art review confirms
  it depicts administrative exploitation rather than generic magic
- `ireland_crown_and_five_provinces` uses
  `GFX_focus_ireland_crown_province_convergence`
- `ireland_high_king_of_two_irelands` uses
  `GFX_focus_ireland_otherworld_convergence`
- `ireland_five_courts_of_the_otherworld` uses
  `GFX_focus_ireland_fivefold_obligation`
- the full convergence uses
  `GFX_focus_ireland_convergence_order_capstone`

Create new static report images for the captive throne, palace break, Empty
Chair, Rival Irelands, Tuatha courts, Sealed State, Crown and Provinces, High King
of Two Irelands, and Five Courts. Reuse existing generated Fianna, compact,
verification, breach, Five Provinces, and final convergence report art only when
the manifest subject matches the event.

Create normal, medium, and small flags for each new cosmetic identity listed
above. The asset manifest must record source or generation provenance, intended
classification, dimensions, final DDS path, sprite or cosmetic consumer, and
static fallback.

Reuse these existing animated transition families with their static fallbacks:

- `GFX_ireland_hidden_evidence_seal_reveal_animated`
- `GFX_ireland_high_kingship_crown_selection_animated`
- `GFX_ireland_five_provinces_compact_animated`
- `GFX_ireland_verified_otherworld_entry_animated`
- `GFX_ireland_compact_breach_warning_animated`
- `GFX_ireland_convergence_conclusion_seal_animated`

No new animation is required. Existing optional audio briefs remain optional and
uncleared. No focus, event, mission, or acceptance test depends on audio.

## Research basis and attribution limits

Implementation and writing may use these researched connections:

- The Royal Sites of Ireland material supports associations between Tara and
  kingship or assembly, and Uisneach and a symbolic meeting place. It does not
  prove continuous high monarchy or a fixed 1936 federal constitution.
- The National Folklore Collection Schools' Collection provides independently
  gathered 1937 to 1939 local records across counties. It supports regional
  evidence and differing accounts, not a single canon.
- CELT editions of *Cath Maige Tuired* and *Acallamh na Senórach* support literary
  vocabulary and narrative inspiration. They are not evidence that Tuatha or
  Fianna bodies existed as twentieth-century political or military institutions.
- The existing focus-tree text research on *Lebor na Cert*, Ard-Rí, Tara,
  Uisneach, Emain Macha, Dún Ailinne, Cashel, and Rathcroghan supplies title and
  institutional vocabulary subject to its existing caveats.

Primary web references reviewed for this addendum:

- Royal Sites of Ireland, `https://royalsites.ie/about`
- Hill of Tara, `https://royalsites.ie/sites/hill-of-tara`
- Hill of Uisneach, `https://royalsites.ie/sites/hill-of-uisneach`
- Dúchas, Schools' Collection, `https://www.duchas.ie/en/info/cbe-collections`
- CELT, *Cath Maige Tuired*, `https://celt.ucc.ie/document/T300010/`
- CELT, *Acallamh na Senórach*, `https://celt.ucc.ie/published/G303000/index.html`

Uncertain claims remain inspiration only. No quotation or close paraphrase is
authorised by this plan. If final text needs a quotation, route it through the
quote-research workflow and retain the existing source-clearance rules.

## Failure, recovery, and cleanup

Every conclusion helper clears only mutually exclusive active choices and
temporary mission state. It retains completed history, fabricated-evidence
history, patron history, broken obligations, and failure history for AI,
achievements, and final review.

Required recovery routes:

- captive crown: household audits, break mission, independent succession,
  public convention, or abolition
- unbounded sacred rule: fulfil penance, limit the crown through council,
  abdicate, or submit the sacred office to a valid compact
- failed federation: renewed budgets, mandate convention, confederation, lawful
  dissolution, or stable Empty Chair
- Rival Irelands: disarm provincial guards, settle foreign patron pressure, and
  restore common law before any renewed conclusion
- broken compact: restitution, public admission, fulfilled obligations, witness
  protection, and site repair
- sealed state: release archives and witnesses, narrow perimeters, and restore
  civil authority before human-stewardship recovery
- deliberate exploitation: surrender the timed extracted benefit and repair the
  named site before compact recovery
- failed convergence: separate the three component orders cleanly, preserve
  their valid individual conclusions, and reopen only the failed component's
  recovery decisions

No failure recovery grants the terminal focus for free. Recovery must satisfy
the terminal trigger or open an alternate terminal focus.

## Acceptance scenarios

Implementation is accepted only when all scenarios below have source and
render evidence:

1. Historical AI never reveals or selects an exceptional commitment.
2. The rendered tree contains exactly 256 unique focus IDs, exactly three roots,
   the five public gateways still at `y = 14`, no overlaps, no invalid
   prerequisites, and no connector from a hidden conclusion into an unrelated
   public family.
3. A clean elective or guardian crown reaches the household conclusion, retains
   Parliament and succession play, and cannot also take captured or sacral
   terminal focuses.
4. An elective crown can pass the verified stone event, fulfil a geis and circuit,
   and reach Living Land. Broken obligations instead lead to penance or unbounded
   failure.
5. Party capture makes the rescue and Captive Throne outcomes exclusive. Rescue
   removes the captive spirit, while failure preserves its penalties and blocks
   convergence.
6. Federal play with lawful Ulster participation reaches a funded federal
   conclusion. The same route without consent can reach a stable Empty Chair but
   receives no northern core, claim, ownership, or mandate.
7. Confederation has recurring contributions and vetoes distinct from the
   federal route.
8. Pentarchy, Fifth Province, and Rival Irelands are mutually exclusive and use
   mandates, budget, guards, and Middle Balance rather than creating free states
   or units.
9. Balanced Otherworld play maintains trust, veil, rights, sites, and named
   obligations. Its benefits expire or weaken on breach.
10. Tuatha-associated sovereignty records a specific court and preserves the
    human-rights floor. It is not presented as one supernatural nation.
11. Fianna certification fails when the formation lacks manpower, equipment,
    training, supply, command, or service completion. No script-created division
    or stockpile appears.
12. Regional court play records distinct local terms. Four courts give a partial
    outcome and five lawful courts enable convergence.
13. Exploitation gives only a timed benefit, damages Trust and Veil Stability,
    creates restitution, and can reach dominion or breach without free resources.
14. Containment can end under civil law or become a Sealed State. Neither result
    erases verified evidence.
15. Each pair convergence is separately selectable, fires its event, owns only
    its proper flags, and keeps recurring component obligations.
16. The full convergence is reachable only through the coherent elective,
    five-voice, balanced-compact playthrough and only after its 180-day review.
17. A failed full review preserves valid component conclusions, records the
    failure, cleans temporary missions, and reopens recovery without duplicating
    spirits or decisions.
18. At all times the route has no more than three persistent spirits and remains
    within the existing 30 durable profiles.
19. Every new player-facing ID has localisation, every new sprite consumer loads,
    every distinct cosmetic identity has three flag sizes, and every event image
    has a manifest entry and static fallback.
20. No new core, ownership effect, annexation, war goal, free war, free division,
    free manpower, free equipment, or magical resource deposit is present in the
    tranche.

## Implementation order

1. Add constants, variables, conclusion flags, helpers, and exact triggers.
2. Reflow the existing exceptional nodes, add the 38 focus blocks, and render the
   256-focus tree before wiring rewards.
3. Implement events `438` through `460` and the decision and mission lifecycles.
4. Add same-slot idea forms, identities, flags, localisation, and AI weights.
5. Produce and wire the static focus, report, and flag assets. Reuse only the
   exact matching registered sprites listed above.
6. Run focus, decision, country-package, localisation, and feature-completion
   audits against the acceptance scenarios.
7. Promote the accepted design into the country-package specs and archive this
   addendum as implemented. Do not leave the plan and source specification in
   disagreement.

## Promotion map

This file remains under `docs/plans/ireland_country_package/improvement_loop/`
until the parent accepts and implements it. Once accepted, merge:

- focus graph and reveal rules into `campaign_architecture.md`
- values, decisions, missions, failures, and recovery into
  `systems_and_lifecycles.md`
- AI, balance, text, and asset requirements into
  `ai_balance_assets_and_text.md`
- implementation IDs and validation proof into `implementation_matrix.md`

The detailed historical and concealed-route source remains the existing
`docs/specs/ireland_focus_tree/` suite. This addendum adapts it to the current
country-package geometry. It does not supersede that source.

## Resolution state

The previous country-package improvement addendum was promoted and implemented
at `89ff719`, so this pass is permitted. This addendum is unresolved until the
parent explicitly accepts, implements, queues with a reason, or rejects it. No
gameplay file, localisation file, asset, specification, or thumbnail is changed
by this planning pass.
