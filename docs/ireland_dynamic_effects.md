# Ireland Total Overhaul dynamic scripted effects

Feature slug: `ireland_focus_tree`.

This file records reusable dynamic helpers added for the Ireland runtime. Inputs and outputs are explicit so later route files do not duplicate arithmetic, scope-sensitive cleanup, or material gates.

## Historical-AI route guard

### `ireland_alternate_focus_ai_allowed`

- Scope: country/focus availability.
- Inputs: the current AI state and the global Historical AI Focuses game rule.
- Output: true for a human-controlled country or for non-historical AI; false
  for an AI country while Historical AI Focuses is enabled.
- Usage: add `ireland_alternate_focus_ai_allowed = yes` to the
  `available` block of every alternate route-entry focus. This preserves
  player choice while preventing a historical AI profile from entering an
  alternate route.
- Side effects: none.

## Ireland action scarcity charges

Decision costs are authored per action. The decision's confirmation text shows
its Political Power, Command Power, every physical input charged by the
completion effect, and the live state value that controls its scarcity band.
Watch values add 5 Political Power, 5 Command Power, and 1 Action Burden;
severe values add 10 Political Power, 10 Command Power, and 2 Action Burden.
Action Burden is the visible 0-to-5 measure of administrative and public
strain. There is no global highest-shortage preview: an action charges only
the named state value in its own completion effect, so the preview cannot
promise a surcharge that belongs to a different action.

### `ireland_apply_action_scarcity_severe_surcharge`

- Scope: country; called once by an Ireland action's `complete_effect` when
  the Social Consent and live-ledger scarcity band is severe.
- Inputs: the owning action's current
  `ireland_action_political_cost`,
  `ireland_action_command_cost`, and
  `ireland_action_burden` variables, plus the shared
  `action_surcharge_severe` and `action_burden_surcharge_severe` constants.
- Outputs: adds the shared +10 Political Power, +10 Command Power, and +2
  burden surcharge to the live action ledger, then charges -10 Political
  Power and -10 Command Power. Each decision retains its own authored base
  costs and dynamic cost localisation.
- Defaults: do not call outside the severe branch or more than once for the
  same action. The helper does not select a route or create a mission.
- Side effects: no territory, core, industry, equipment, unit, fuel,
  shipping, administration, office, recognition, alignment, or political
  victory reward is granted.
- Usage: call after the action-specific base cost has been recorded and before
  the action's physical commitment and mission activation are resolved.

### `ireland_apply_action_scarcity_watch_surcharge`

- Scope: country; called once by an Ireland action's `complete_effect` when
  the Social Consent and live-ledger scarcity band is watch.
- Inputs: the same three owning-action ledger variables, plus the shared
  `action_surcharge_watch` and `action_burden_surcharge_watch` constants.
- Outputs: adds the shared +5 Political Power, +5 Command Power, and +1
  burden surcharge to the live action ledger, then charges -5 Political
  Power and -5 Command Power. The action's distinct base values remain
  unchanged.
- Defaults: do not call outside the watch branch or more than once for the
  same action. The zero-surcharge branch calls neither helper.
- Side effects: ledger arithmetic only; no route, map, material, office, or
  recognition result is created by the helper.
- Usage: call after the action-specific base cost has been recorded and before
  the action's physical commitment and mission activation are resolved.

## Channel and cooperation admission triggers

### `ireland_update_neutrality_partner_depth`

- Scope: country; called by the Ireland daily runtime after foreign-channel cleanup.
- Inputs: the five named partner channels (British, American, German, Vatican, and neutral states), their recorded channel/action/mission completion flags, and Foreign Exposure.
- Outputs: twenty persistent partner/channel high-water variables, each bounded by the authored cooperation-depth ladder `0` no organised channel, `1` administrative contact, `2` technical cooperation, `3` operational liaison, and `4` undeclared co-belligerency; also updates the derived maximum used by achievement A-03.
- Defaults: all twenty records begin at `0`. Focus-created channel flags can establish only depth `1`; named actions and full mission records advance the relevant channel to `2` or `3`; depth `4` requires a named operational record plus Foreign Exposure at `75` or more.
- Side effects: none beyond ledger variables and the achievement history extrema. It does not grant access, alignment, recognition, territory, cores, industry, equipment, units, fuel, shipping, administration, offices, or political power. The maximum is an audit/achievement projection, not a replacement for partner-specific records.
- Usage: call once per daily Ireland runtime after `ireland_sync_foreign_channels`; never substitute visible foreign-reaction count for a cooperation depth.

### `ireland_any_valid_diplomatic_channel`

- Scope: country; used by the weather, internment, and external-creditor admission gates.
- Inputs: an open British, American, German, or Vatican channel with its named partner still valid, or the neutral-states channel.
- Output: true only while at least one current diplomatic route exists; an old reaction window or route flag alone is insufficient.
- Defaults: false at the opening, after the named state actor capitulates, or after the channel lifecycle archives the route.
- Side effects: none; it does not open a channel, add leverage, create aid, or resolve an incident.
- Usage: call the narrower action-owned triggers below when a decision needs a concrete diplomatic route.

### `ireland_internment_diplomatic_channel_valid`

- Scope: country; intended caller is `ireland_action_release_or_exchange_internees`.
- Inputs: `ireland_any_valid_diplomatic_channel` plus the active internment law and incident owned by the decision.
- Output: true only when a live channel can carry a release, exchange, parole, or repatriation disposition.
- Defaults: false for an internment flag without a sponsor route or for a date-only neutrality window.
- Side effects: none; the action still owns Neutrality Integrity, incident closure, public trust, and foreign-reaction consequences.
- Usage: keep legal authority and diplomatic capacity separate so camp cleanup cannot be presented as an unbacked political reward.

### `ireland_external_creditor_channel_valid`

- Scope: country; intended caller is `ireland_action_merge_tax_and_debt_administration`.
- Inputs: a valid British, American, or neutral-states creditor route.
- Output: true only while an external-obligation channel exists for the Northern tax and debt administration review.
- Defaults: false before a creditor route is opened or after its state actor is invalidated.
- Side effects: none; the action retains its administration, control, ledger, and dynamic cost burdens and grants no debt relief or foreign recognition.
- Usage: pair with the state-119 control and administrative-reach gates; do not treat occupation or an external-creditor variable as a diplomatic agreement by itself.

### `ireland_weather_cooperation_depth_valid`

- Scope: country; intended caller is `ireland_action_share_a_controlled_weather_report`.
- Inputs: a live weather incident, a completed G2 cooperation record, or a valid diplomatic channel, plus Coastal and Air Warning at the shared bottleneck threshold.
- Output: true only when Blacksod data has both a reason to matter and enough warning capacity to release it safely.
- Defaults: false for a post-1939 date alone, a station name without staff, or a route without warning capacity.
- Side effects: none; the action still consumes staff and Support Equipment, launches the dated reporting mission, and owns exposure, aviation-safety, Integrity, and foreign reaction.
- Usage: keep public/equal weather release possible through the incident branch while requiring a real cooperation route for controlled sharing.

### `ireland_record_diplomatic_channel_burden`

- Scope: country; called by `Release or Exchange Internees`, `Share a Controlled Weather Report`, `Answer a Foreign Access Request`, and `Recognise a Liberated Authority` after their own legal, incident, route, map, and material gates pass.
- Inputs: the current action's successful diplomatic or access disposition and any open British, American, German, or Vatican channel whose named partner remains valid. The neutral-states channel is intentionally treated as a forum rather than a sponsor.
- Output: adds 5 Foreign Exposure; adds 3 leverage to the first valid named state channel in the existing British/American/German/Vatican priority order; neutral-state or local-authority use records exposure without inventing sponsor leverage. All five external ledgers are clamped to the shared 0-100 range.
- Defaults: no source-specific leverage when all named channels are closed or invalid, even if an old reaction subject or a neutral forum keeps the action admissible.
- Side effects: none beyond the two live ledgers; it grants no access, alignment, recognition, territory, core, industry, equipment, unit, fuel, shipping, administration, office, or political power.
- Usage: call only after the owning decision has charged its dynamic Political Power/Command Power and physical inputs and has recorded the action-specific outcome. British Northern negotiation uses its own 3 Exposure/4 British Leverage constants because it is an explicitly British bargain rather than a multi-channel response.

## Frank Ryan lifecycle gates

### `ireland_frank_ryan_civil_route_authority`

- Scope: country; shared by every Frank Ryan lifecycle gate and by route recruitment/retirement.
- Inputs: either the civil IRA profile with Authority Before Arms and no Army Council path, or the plural Congress profile after completing the Plural Republic.
- Output: true only while an accountable civil republican route can own Ryan's custody, return, public hearing, and later role.
- Defaults: false for GHQ, Congress vanguard, generic communist, historical, absurd, uncommitted, and closed-route profiles.
- Side effects: none; it does not choose a route, complete a focus, recruit a character, or satisfy any stage of the return chain.
- Usage: require this gate both when opening the P11 extension and when retaining Ryan after recruitment, so an authoritarian route transition retires him.

### `ireland_frank_ryan_survival_inquiry_available`

- Scope: country; shared by the event dispatcher and P11 event .434.
- Inputs: valid civil IRA or plural Congress authority, completion of the original three-node P11 leadership crisis, the dated post-August-1940 to pre-June-1944 survival-verification window, and the absence of route closure, prior confirmation, or an already recruited Ryan.
- Output: true only while an Irish civil authority can establish that Frank Ryan survived Russell's return voyage and remains in German custody.
- Defaults: false for Congress, Army Council, generic communist, closed-route, pre-August-1940, and post-historical-death entry. A portrait or route flag is never sufficient.
- Side effects: none. Event .434 owns the German Leverage and Foreign Exposure consequences and may close the chain without making Ryan available.
- Usage: keep the identical gate in dispatch and the triggered event so Ryan cannot be introduced through a direct event call or route activation.

### `ireland_frank_ryan_return_available`

- Scope: country; shared by the event dispatcher and P11 event .435.
- Inputs: confirmed survival, valid civil IRA or plural Congress authority, Intelligence Readiness 35, Neutrality Integrity 50, at least 35 Political Power, and either a valid German custodian or a no-war recorded end to the major war.
- Output: true only while Ireland can organise a return under its own warrants and bear the named diplomatic and security costs.
- Defaults: false when German custody is merely inferred, the state lacks intelligence or neutrality capacity, the political cost is unaffordable, the chain was refused, or military command controls the route.
- Side effects: none. The event charges 35 Political Power, raises German Leverage and Foreign Exposure, lowers Neutrality Integrity, and records release plus an independent health review; the trigger grants none of those results.
- Usage: pair the trigger with the event's durable survival and return records; never recruit Ryan from the route profile itself.

### `ireland_frank_ryan_political_recovery_available`

- Scope: country; shared by the event dispatcher and P11 event .436.
- Inputs: confirmed survival, return, and health review; valid civil IRA or plural Congress authority; Social Consent 50; the corresponding Civil Republican Authority or Congress Coalition Cohesion at 55; and the absence of sponsor-dependence or permanent-foreign-veto failures.
- Output: true only when a constituent civil authority can hear a public repudiation of Axis tutelage and judge Ryan's political recovery.
- Defaults: false for a private undertaking, foreign client state, Army Council route, low public authority, or incomplete return.
- Side effects: none. Event .436 owns the public break, German Leverage reduction, Foreign Exposure, consent/neutrality response, success/failure record, and chain closure.
- Usage: all four durable success records—survival, return, Axis break, and political recovery—must exist before the route lifecycle recruits Ryan.

## `ireland_has_regional_contribution_force`

- Scope: country; intended caller is Ireland regional-order decisions and mission objectives.
- Inputs: division placement in states `113`, `134`, or `135`, the named Dublin, Western Seaboard, and Cork/Munster contribution regions.
- Output: true only while at least one division is physically present in one of those named regions.
- Defaults: no division is created, moved, supplied, or attached by the trigger.
- Side effects: none; the trigger only gates the league proposal and member-contribution schedule.
- Usage: combine with the ratified-charter, military-contribution, sovereignty-safeguard, and material gates before presenting a regional defence commitment.

### `ireland_compact_obligation_authority`

- Scope: country; intended caller is `ireland_action_fulfil_a_compact_obligation` and the five-site compact objective.
- Inputs: the committed Otherworld route, the balanced compact path, the activated Compact Steward office, all four Otherworld cultural thresholds (`45/75/60/70` for Language Service, Archival Record, Regional Participation, and Site Stewardship), and a division physically present in state `134` or `135`.
- Output: true only while a named human authority can deliver the five-site obligation without replacing ordinary administration with an abstract route flag.
- Defaults: false for a regional-order, Atlantic, Five Provinces, containment, or dominion route alone; false when cultural capacity falls below the authored component thresholds; and false when no Irish division occupies the Gaeltacht or Atlantic Islands detail area.
- Side effects: none; the trigger creates no division, equipment, manpower, cultural capacity, territory, cores, offices, recognition, or exceptional military power. The owning action still commits 500 manpower and 20 Support Equipment, pays its dynamic Political Power/Command Power burden, and launches the dated mission.
- Usage: pair the authority trigger with the existing state-control, infrastructure, industry, consent, Compact Trust, and mission-capacity gates. The map objective rechecks the physical force and cultural components so a unit cannot be moved away after launch and still satisfy the obligation.

### `ireland_historic_site_admission_valid`

- Scope: country; intended caller is `ireland_action_protect_a_historic_site`.
- Inputs: full control of state `135`, a serious-culture or archive lane, regional participation, Social Consent `35`, one rights-bearing constituency at the cultural rights floor, 250 manpower, 5 Trucks, and 10 Support Equipment maintenance kits.
- Output: true only while the named site can be guarded, transported to, locally supported, and maintained. The direct action calls the same trigger again before recording its Cultural Capacity result.
- Defaults: false for a Dublin-only cultural flag, a stewardship result used as a circular shortcut, missing local support, or missing maintenance supplies.
- Side effects: none; the trigger creates no site, ownership, core, cultural evidence, manpower, transport, or equipment. The decision owns the charges and cultural result.
- Usage: keep the H/P cultural action separate from later Site Stewardship and concealed-route conclusions; use the trigger for both visible admission and the direct-result guard.

### `ireland_marine_patrol_craft_coverage_valid`

- Scope: country; intended caller is `ireland_map_objective_patrol_the_neutral_approaches_met`.
- Inputs: `ireland_marine_patrol_craft_committed`, set by Organise Marine Patrols after its 3-Convoy charge.
- Output: true only while one dedicated coastal patrol-craft coverage allocation is bound to the active patrol operation.
- Defaults: false before the action commits the allocation and after cancellation, timeout, full/partial result, failure/escalation, action removal, or route cleanup.
- Side effects: none; it does not spawn, move, delete, or mutate a unit and does not create merchant shipping. The flag is an action-specific coverage abstraction tied to the charged Convoy-equivalent craft allocation.
- Usage: pair with the existing port, industrial, naval-repair, shipping-authority, warning/rescue, readiness, action, and mission proofs. The map objective must recheck it rather than treating a Convoy stockpile or a merchant-service flag as a patrol craft.

## Readiness operational-plan and force proofs

### `ireland_has_northern_operational_force`

- Scope: country; intended callers are the Dublin–Belfast corridor, Plan W, and Belfast occupation actions and mission objectives.
- Inputs: at least one Irish division physically deployed in state `113` or state `119`.
- Output: true only while a real formation covers the named southern or Northern operational belt.
- Defaults: false when the player has only a readiness value, a plan flag, or a paper campaign record.
- Side effects: none; the trigger creates, moves, supplies, or disbands no unit and grants no territory or core.
- Usage: combine with the railway, depot, control, supply, and civilian-passage proofs for the linked map objective.

### `ireland_demobilisation_force_tier_selected`

- Scope: country; intended caller is the readiness demobilisation authority and its map objective.
- Inputs: completion of Activate a Cadre Reserve, Expand the Local Security Force, or Expand the Local Defence Force.
- Output: true only when a named mobilisation tier has been authorised through an existing action.
- Defaults: false for a generic mobilisation value or an independently placed division without a selected tier record.
- Side effects: none; it does not change the mobilisation law, force size, equipment, or readiness ledger.
- Usage: pair with `ireland_has_demobilisable_cadre` so a tier record cannot stand in for a deployed force.

### `ireland_has_demobilisable_cadre`

- Scope: country; intended caller is Demobilise a Force Tier and Demobilise Without Losing the Cadre.
- Inputs: a selected mobilisation tier, at least one Irish division in states `113`, `119`, `134`, or `135`, and the completed Strategic Depot record.
- Output: true only while personnel and the physical formation have a named depot/records basis for orderly release.
- Defaults: false before a real tier, formation, or depot exists.
- Side effects: none; the action owns the release, equipment recovery, pay settlement, veteran record, mission timer, and failure consequences.
- Usage: keep the readiness action separate from the postwar veteran-settlement programme; this proof authorises the first demobilisation step only.

### `ireland_operational_plan_authority`

- Scope: country; intended caller is Protect an Operational Plan and the Protect Plan W map objective.
- Inputs: either a completed Plan W liaison with a completed G2 liaison, a live British channel, and a valid British partner; a Northern war plan with a local partner; a completed coercive Northern plan with its route-valid cause; or an occupation authority with provisional or integration review.
- Output: true only while a named operational plan and its legal, diplomatic, or local authority remain live.
- Defaults: false for `ireland_readiness_plan`, a low component, invasion danger, or a generic foreign-reaction window by itself.
- Side effects: none; it creates no access, guarantee, unit, depot, map control, foreign leverage, or intelligence.
- Usage: combine with the physical division, Dublin arms/air, Strategic Depot, and warning-readiness proofs. The linked mission still records exposure, plan compromise, partial success, failure, escalation, and cleanup.

### `ireland_demobilisation_authority`

- Scope: country; intended caller is Demobilise a Force Tier and its linked mission.
- Inputs: no active war, plus postwar review, a recorded major-war end, or the completed demobilisation-readiness milestone with invasion danger and war spillover cleared.
- Output: true only when an orderly release window exists; a low readiness component alone is not sufficient.
- Defaults: false during active war, spillover, invasion danger, or before the postwar/falling-danger authority.
- Side effects: none; the caller owns pay, equipment recovery, veteran-state records, mission outcomes, and route cleanup.
- Usage: pair with `ireland_has_demobilisable_cadre`, Strategic Depot, arms-factory, command-readiness, and mobilisation floors.

## Foreign procurement authority proofs

### `ireland_has_named_provision_shortage`

- Scope: country; intended caller is the British supply contract authority and the British source branch of Procure Rifles and Support Equipment.
- Inputs: any one of Food, Energy, Transport, or Maritime Provision below the named-shortage cap.
- Output: true only while a current Provision component identifies a concrete shortage that a contract could address.
- Defaults: false when Provision is merely below its display average but no component is in the named-shortage band.
- Side effects: none; the trigger changes no Provision, cargo, convoy, credit, or foreign leverage.
- Usage: combine with the British channel, valid partner, finance/rural-credit, and sovereignty/access safeguards. The delivery mission rechecks the contract and route records without requiring the shortage to remain after cargo arrives.

### `ireland_british_supply_contract_authority`

- Scope: country; intended callers are Renegotiate a British Supply Contract and its British branch in Procure Rifles and Support Equipment.
- Inputs: live British channel and partner, named Provision shortage, Finance Safeguards or Rural Credit, and sovereignty or access safeguards.
- Output: true only when a British cargo bargain has a shortage, finance, and bounded-access basis.
- Defaults: false for a date, British flag, leverage value, or open mission capacity by itself.
- Side effects: none; the caller pays its convoy, political/command, exposure, and leverage costs and opens the dated delivery mission.
- Usage: pair with the British port/infrastructure map objective and active source record. It does not grant British aid, access, equipment, territory, or Northern control.

### `ireland_american_procurement_authority`

- Scope: country; intended callers are Send an American Procurement Mission and the American branch in Procure Rifles and Support Equipment.
- Inputs: live American channel and partner, external-creditor route, Finance Safeguards/Rural Credit/Domestic Manufacturing, and Foreign Access law or sovereignty/access safeguards.
- Output: true only when an American cargo or credit mission has shipping, finance, and legal authority.
- Defaults: false for an open American flag, a generic foreign-reaction window, or a convoy stockpile without a creditor and legal record.
- Side effects: none; the caller pays its convoy, political/command, exposure, and leverage costs and opens the dated procurement mission.
- Usage: pair with the Dublin industrial/naval receiving map objective and active American source record. It does not grant dollars, equipment, factories, access, recognition, or alignment.

### `ireland_german_delivery_authority`

- Scope: country; intended callers are Demand Proof of German Delivery, the German branch in Procure Rifles and Support Equipment, and Test a German Arms Promise.
- Inputs: live German channel and partner, completed Receive a German Emissary record, and sovereignty safeguards or Security Under Law.
- Output: true only while a named German promise exists and an independence/security boundary can test it.
- Defaults: false for a German channel, leverage value, or foreign reaction by itself.
- Side effects: none; the caller pays political/command/exposure costs and opens a time-bounded proof mission.
- Usage: pair with the Shannon/western-infrastructure and Leinster-arms-factory map objective. The test never adds equipment until the mission result and never creates a client relationship automatically.

### `ireland_vatican_relief_authority`

- Scope: country; intended callers are Seek Vatican Humanitarian Mediation and Conclude a Vatican Relief Mediation.
- Inputs: live Vatican channel and partner plus war, an active neutrality incident, a completed diaspora-relief network, a completed Church-service audit, or the postwar foreign review.
- Output: true only while a named humanitarian, Church-network, or international-isolation cause exists for mediation.
- Defaults: false for Vatican leverage, a date, a generic foreign-reaction window, or Church influence without a case or external crisis.
- Side effects: none; the action records the case and pays its political/command/exposure/leverage burden before the mission resolves.
- Usage: the mission's Dublin industrial site, Social Consent, active-case, and partner checks remain separate, and the action never grants the Vatican a domestic veto, a subject, aid, equipment, or recognition.

## Intelligence and foreign-agent admission triggers

### `ireland_g2_partner_or_northern_plan`

- Scope: country; intended caller is the G2 liaison action.
- Inputs: a live British, American, German, Vatican, or neutral-states channel, or the authored Northern war plan.
- Output: true only while at least one valid intelligence mandate exists; partner channels also require the named actor to exist and not be capitulated.
- Defaults: false at the opening and after the relevant actor channel is closed.
- Side effects: none; this trigger does not open a channel, raise leverage, grant intelligence, or create a Northern claim.
- Usage: consume through `ireland_g2_liaison_authority` rather than duplicating actor-validity checks in a decision.

### `ireland_g2_liaison_authority`

- Scope: country; intended caller is `ireland_action_open_a_g2_liaison_channel`.
- Inputs: the valid-channel/Northern-plan trigger plus either sovereignty and review safeguards or the Security Under Law legal chain.
- Output: true only when the liaison has a partner or operational purpose and a written Irish control/review basis.
- Defaults: false before safeguards, Security Under Law, a valid channel, or the Northern plan exists.
- Side effects: none; the action still consumes its Support Equipment, Command Power, Political Power, and readiness burden through the owning decision. The owning action records 5 Foreign Exposure and adds 3 leverage to the named British, American, German, or Vatican channel when that channel carries the liaison; a Northern-plan liaison carries the exposure without sponsor leverage.
- Usage: keep Irish control, exposure review, information-scope, and source-specific leverage requirements visible in the decision tooltip; do not replace them with a generic intelligence score.

### `ireland_veteran_settlement_capacity`

- Scope: country; intended caller is `ireland_action_demobilise_and_settle_veterans`.
- Inputs: Administrative Reach, Labour Organisation, and one completed housing, reconstruction, or veteran-employer capacity flag.
- Output: true only when veterans can be absorbed through a named civic or labour institution rather than being removed from the rolls by a manpower payment alone.
- Defaults: false until the administrative and labour thresholds are met and a named capacity exists.
- Side effects: none; the owning action still reserves two civilian factories, consumes Infantry Equipment and manpower, and launches the dated settlement mission.
- Usage: pair with the 300-day mission and the capped cancellation refund; this trigger never creates units, equipment, housing, employment, or free political power.

### `ireland_un_admission_authority`

- Scope: country; intended caller is the UN application action and its admission map objective.
- Inputs: the completed postwar foreign review, a resolved FR11 admission reaction or a closed H17 United Nations chain, and Diplomatic Recognition at least 50.
- Output: true only when a named external/world-organisation position exists; a postwar date or generic foreign posture alone is insufficient.
- Defaults: false before the review and a partner-position record are present.
- Side effects: none; the application still launches the 365-day mission, and full or partial admission remains contingent on its objective and reaction outcomes.
- Usage: combine with the naval-base, Neutrality Integrity, control, and foreign-posture map requirements so recognition and membership are never awarded as free political rewards.

### `ireland_foreign_agent_case_ready`

- Scope: country; intended caller is `ireland_action_turn_or_intern_a_foreign_agent`.
- Inputs: the active intelligence incident family and either Security Under Law or National Emergency legal authority.
- Output: true only when an identified intelligence case and a legal order coexist.
- Defaults: false when the country merely has intelligence capacity, a foreign channel, or a generic readiness deficit.
- Side effects: none; the action remains responsible for its security-staff commitment, intelligence improvement, foreign reaction, and route cleanup.
- Usage: require this trigger before offering surveillance, controlled use, internment, expulsion, or prosecution outcomes.

## Readiness authority admission triggers

### `ireland_coastwatch_service_active`

- Scope: country; intended caller is `ireland_action_build_a_coastwatch_sector_network`.
- Inputs: the Coastwatch focus/service flag.
- Output: true only while the Marine and Coast Watching Service has been established through the Coastwatch preparation route.
- Defaults: false at the opening and before the Coastwatch service is authorised.
- Side effects: none; the action still requires the named western sector, infrastructure connection, staff, equipment, mission capacity, and dynamic costs.
- Usage: keep the service gate separate from the later sector mission so one operational sector does not masquerade as the national service.

### `ireland_folklore_collection_authority`

- Scope: country; intended callers are `ireland_action_expand_folklore_collection` and the `Collect A National Folklore Cycle` map objective.
- Inputs: the serious-culture or archive lane, a school/language network, archival groundwork, and historic-site custody through their focus or named action records.
- Output: true only when the Irish Folklore Commission's collector operation has a documented institutional, archival, and custody basis.
- Defaults: false for a Cultural Capacity value, a single manuscript, a generic route flag, or the mission slot alone.
- Side effects: none; the action separately commits 250 manpower and 5 Trucks, pays dynamic Political/Command Power, and launches the 180-day mission.
- Usage: pair with Connacht control/infrastructure, the active action and mission flags, and the concealed-evidence-region map proof. Cancellation uses refund code 34 and returns only 175 manpower and 3 Trucks.

### `ireland_cultural_congress_authority`

- Scope: country; intended callers are `ireland_action_hold_a_provincial_cultural_congress` and the `Hold A Five-Region Cultural Congress` map objective.
- Inputs: the serious-culture or archive lane, a regional-participation record or component at least 30, and at least one rights-bearing constituency at least 35 through Minority Confidence, Labour Organisation, or Church influence.
- Output: true only while a Dublin congress can receive regional delegates with a recorded participation and rights basis.
- Defaults: false for a Dublin venue, a truck stockpile, Cultural Capacity alone, or a concealed-evidence count without regional institutions.
- Side effects: none; the action still commits 5 Trucks, pays dynamic Political/Command Power, and launches the 180-to-270-day mission.
- Usage: pair with the three-state control/building map proof, active action and mission flags, and the multi-region evidence count. The existing cultural-congress cancellation path returns only the capped 3-Truck share.

### `ireland_restoration_evidence_authority`

- Scope: country; intended callers are `ireland_action_test_a_restoration_claim` and the `Verify The Restoration Evidence` map objective.
- Inputs: the serious-culture or archive lane; completed Cultural Service and Diaspora Exchange review channels; named archival provenance through the archive record or provincial-archive survey; site custody through Site Stewardship or the historic-site action; royal evidence thresholds of 4 credible classes, 3 categories, and 3 regions; a live war, neutrality incident, foreign-reaction window, Northern settlement failure, or emergency review; and no recorded evidence disqualifier.
- Output: true only while the restoration claim has independent provenance, review, custody, and an unusual campaign context capable of supporting an H-to-P or P-to-A transition.
- Defaults: false for Cultural Capacity alone, the concealed-evidence region counter alone, the action/mission slot alone, or a single manuscript or historic site.
- Side effects: none; the action retains its dynamic Political/Command Power burden, while the map objective still requires full Leinster control, an industrial complex, a naval base, and the active claim and mission flags.
- Usage: call from both the action admission block and the map objective. Keep `ireland_independent_evidence_ready` downstream of a full restoration record so this helper does not create a circular admission gate. The restoration mission lifecycle centralizes its full/partial/panic evidence floors and writes explicit timeout classifications; panic containment and failed-restoration archiving consume those classifications and clear their transient flags while preserving mission-result history.

### `ireland_concealed_transition_authority`

- Scope: country; intended callers are the Hidden Evidence Council admission block and the runtime derivations for concealed A-route conclusions.
- Inputs: restoration-evidence authority; the full `Verify the Restoration Evidence` mission record; independent evidence; hidden-content permission and its enabled game rule; and no failure class, route closure, archive, or restoration-cleanup flag.
- Output: true only when a completed independent restoration review can authorize the concealed H/P-to-A handoff. It deliberately omits the council-complete flag so the council can call it before completion; every downstream impossible-route derivation must add that durable council flag explicitly.
- Defaults: false for partial or cancelled review, any false-lead/fraud/panic/route-closure result, cleanup completion, GUI reveal alone, hidden permission alone, or the ordinary plausible cultural route.
- Side effects: none. The council completion sets `ireland_concealed_evidence_revealed` as a presentation/reveal state and does not add hidden evidence.
- Usage: pair with `has_country_flag = ireland_action_convene_a_hidden_evidence_council_complete` when deriving the shared High-King/Five-Provinces impossibility layer and `ireland_verified_impossible_reveal`. Otherworld uses its route-specific archive-reveal and impossible-confirmed flags. Preserve the separate constitutional High Kingship and federal Five Provinces P-route gates.

### `ireland_commit_otherworld_archive_reveal`

- Scope: country; intended caller is the four-option `ireland_events.437` archive-reveal event.
- Inputs: the event's completed investigation, independent witnesses, Otherworld evidence ledger, unusual campaign condition, Hidden Evidence Council, and `ireland_concealed_transition_authority` trigger.
- Output: records the explicit impossible result, the route-specific verified-impossibility boundary, and the compact/containment lanes needed for the post-reveal focuses.
- Defaults: the helper is not a trigger and must not be called from a focus completion, GUI click, passive daily refresh, or a pre-reveal decision. The event is the only Otherworld caller.
- Side effects: sets `ireland_otherworld_archive_reveal_complete`, `ireland_otherworld_impossible_confirmed`, `ireland_otherworld_compact_ready`, and `ireland_otherworld_containment_ready`. It deliberately does not write the shared `ireland_verified_impossible_reveal` flag, which belongs to the High-King/Five-Provinces reveal layer and convergence. The event applies the selected public-knowledge, consent, settlement, neutrality, and exposure consequences and clears its ephemeral option flags in `after`.
- Usage: call once from the four choices of `ireland_events.437`; keep the compact and containment focus availability checks on `ireland_otherworld_archive_reveal_complete` and the dominion/readiness checks on `ireland_otherworld_impossible_confirmed` so no focus can bypass the explicit H/P-to-A event.

### `ireland_harbour_defence_authority`

- Scope: country; intended caller is `ireland_action_install_harbour_defences`.
- Inputs: full control of state 135 plus a port-defence authority, Treaty Port transfer, or already-completed port-defence project flag.
- Output: true only when Irish control and a valid authority coexist at the named Cork harbour objective.
- Defaults: false before the harbour is transferred or a valid port authority is recorded.
- Side effects: none; it does not transfer territory, create a building, grant a core, or complete the Treaty Port mission.
- Usage: pair with the direct artillery, support-equipment, manpower, civilian-factory, and mission gates in the action.

### `ireland_marine_patrol_authority`

- Scope: country; intended caller is `ireland_action_organise_marine_patrols`.
- Inputs: the Marine Service readiness route or an Irish, chartered, purchased, renewed, or publicly marked shipping route.
- Output: true while a maritime patrol authority or an equivalent named route exists.
- Defaults: false before the Marine Service or a concrete shipping route has been established.
- Side effects: none; the action separately requires full Cork control, port industry, patrol materials, naval experience, and the dated mission.
- Usage: preserve route-equivalent play for neutral shipping without treating a bare convoy stockpile as a patrol service.

### `ireland_treaty_port_operational_authority`

- Scope: country; intended caller is the `Defend A Treaty Port` map objective.
- Inputs: harbour-defence authority, a naval base in state 135, a live Treaty Port/port-defence project record, and a Coastwatch, coastwatch-sector, or Air Warning network.
- Output: true only while the named Cork/Munster harbour can be defended through a real port platform and connected warning chain.
- Defaults: false for state control, an industrial complex, command readiness, or a stale port flag by itself.
- Side effects: none; it does not create guns, crews, magazines, access, a treaty port, territory, or a core.
- Usage: pair with the active harbour-defence action and mission flags, the industrial-complex proof, and the command/warning readiness floors. The mission remains responsible for repair, crew, magazine, failure, escalation, and cleanup outcomes.

### `ireland_neutral_approaches_operational_authority`

- Scope: country; intended caller is the `Patrol The Neutral Approaches` map objective.
- Inputs: Marine Patrol authority, an Irish or named chartered/purchased/renewed/publicly marked shipping route, a Coastwatch/coastwatch-sector/Air Warning rescue-and-warning service, and Neutrality Integrity above the authored approaches floor.
- Output: true only while a concrete coastal sector and port can sustain the named patrol operation.
- Defaults: false for a convoy stockpile, neutrality value, naval base, or Marine Service flag without a route and warning/rescue service.
- Side effects: none; it does not create craft, fuel, crews, rescue capacity, inspections, shipping, access, territory, or cores.
- Usage: pair with the active marine-patrol action and mission flags, the Munster industry/naval-base and Leinster naval-base map proofs, and the maritime-protection readiness floor. The mission owns the fuel, crew, inspection, rescue, loss, confrontation, escalation, and cleanup outcomes.

### `ireland_air_intercept_response_authority`

- Scope: country; intended caller is `ireland_action_intercept_an_airspace_violation`.
- Inputs: the Air Warning preparation route, or command authority together with an owned state-113 air base.
- Output: true only when a warning network or a credible Air Corps launch authority is available for the live incident.
- Defaults: false before warning preparation or an operational command/air-base pairing.
- Side effects: none; fighters, fuel, the active incident, foreign reaction, and forced-landing follow-up remain owned by the decision.
- Usage: keep airspace response admission distinct from the incident flag so an incident cannot be intercepted by an abstract stockpile alone.

## Occupation and regional authority admission triggers

### `ireland_paramilitary_disarm_authority`

- Scope: country; intended caller is `ireland_action_disarm_paramilitary_organisations`.
- Inputs: a division physically deployed in state 119, Intelligence Readiness above the investigation floor, and one of the Public Order, Security Under Law, or Vet and Rebuild Policing legal authorities.
- Output: true only while the Derry and Foyle disarmament operation has an Irish security force, intelligence basis, and reviewable legal mandate.
- Defaults: false before a Northern unit is staged, intelligence work is admitted, or a lawful policing chain exists.
- Side effects: none; the action still consumes 1,000 manpower, Command Power, Political Power, and its dynamic security burden. It does not alter Northern control, occupation, settlement, integration, or cores.
- Usage: keep unit presence and legal admission separate from the generic occupation flag so a paper authority cannot disarm a region without an operational force.

### `ireland_protectorate_authority_valid`

- Scope: country; intended caller is `ireland_action_offer_a_protectorate_treaty`.
- Inputs: a recognised liberated authority, Northern war plan, completed coercive campaign, or Northern wartime bargain.
- Output: true only while a concrete authority exists that can request or be offered a protectorate treaty.
- Defaults: false for a route flag, claim, or diplomatic aspiration alone.
- Side effects: none; the action opens the 14-day foreign-reaction window and records treaty obligations without granting subject status, territory, cores, industry, equipment, units, fuel, shipping, administration, alignment, offices, or recognition.
- Usage: combine with the route-family, state-113, British-Flexibility, capacity, and dynamic cost gates in the decision; the foreign-reaction family owns the external response.

### `ireland_liberated_authority_cause_valid`

- Scope: country; intended caller is `ireland_action_recognise_a_liberated_authority`.
- Inputs: active war, war spillover, foreign-sponsor collapse, a Northern local-authority mandate, or a Northern wartime bargain.
- Output: true only when a war, collapse, or authored local mandate supplies the concrete political cause for recognising an external or liberated authority.
- Defaults: false in the opening and for a regional route flag, cultural contact, or diplomatic ambition alone.
- Side effects: none; the action still pays its bounded Infantry Equipment and Convoy package and owns aid, legitimacy, foreign reaction, mission, and cleanup records. No subject, territory, core, unit, or recognition is granted for free.
- Usage: keep the cause admission separate from the regional route and state-113 map gates; the recognition action records the external authority after the cause exists.

### `ireland_northern_local_partner_valid`

- Scope: country; intended callers are `ireland_action_open_cross_border_confidence_measures` and `ireland_action_invite_northern_delegations`.
- Inputs: opened Northern contacts, a local-authority mandate, an IRA local-mandate record, a trade-corridor record, or an open Northern negotiation.
- Output: true only when at least one named local partner or local mandate exists for cross-border work.
- Defaults: false for the claim, a generic Northern route, or a Dublin-only diplomatic flag.
- Side effects: none; the caller still owns staff, transport, map, consent, mission, and cleanup costs.
- Usage: pair with the relevant Border Belt or Belfast map objective so a local-partner record does not substitute for physical access or safe travel.

### `ireland_neutral_consultation_partners_valid`

- Scope: country; intended caller is `ireland_action_convene_a_neutral_states_consultation`.
- Inputs: an open, non-capitulated Vatican channel and the separate neutral-states forum channel.
- Output: true only when the named small-state mediator and neutral-state forum provide two distinct valid partners for the consultation.
- Defaults: false when the action has only the general foreign-safeguards flag, one channel, or a dead Vatican partner.
- Side effects: none; the consultation still consumes its dynamic Political Power and Command Power costs and opens the foreign-reaction window without granting alignment, recognition, territory, cores, industry, equipment, units, fuel, shipping, administration, offices, or free supply.
- Usage: keep the two-partner proof separate from the Dublin map objective and Neutrality Integrity/cost bands so the action cannot count one focus-created channel twice.

### `ireland_foreign_access_request_partner_valid`

- Scope: country; intended caller is `ireland_action_answer_a_foreign_access_request`.
- Inputs: one of the five named N07 access-incident source flags, a live valid foreign channel or the recorded N07 reaction subject, and the sovereignty-mandate or sovereignty-safeguard record.
- Output: true only while a concrete foreign access request can be answered under an Irish legal mandate at the Treaty Port Complexes.
- Defaults: false for a date alone, a generic neutrality incident, an unscoped access law, a dead sponsor, or a foreign channel without a named incident source.
- Side effects: none; the decision owns the bounded response, dynamic political and command costs, leverage/public-consent consequences, foreign reaction, incident closure, and cleanup.
- Usage: combine with the active foreign-access law, state-135 map objective, capacity, Neutrality Integrity, and dynamic cost gates; do not let a generic post-1939 date substitute for the requesting actor.

### `ireland_atlantic_charter_partners_valid`

- Scope: country; intended caller is `ireland_action_draft_an_atlantic_consultation_charter`.
- Inputs: two distinct live state-level channels drawn from British, American, German, Vatican, and neutral-state diplomacy; state channels also require their named partner to remain valid.
- Output: true only while at least one explicit pair of willing state channels can support the Atlantic consultation charter.
- Defaults: false for a route flag, a stale foreign-reaction actor count, diaspora organisations alone, or one channel counted twice.
- Side effects: none; the charter remains a bounded consultation document and grants no faction entry, alignment, recognition, territory, cores, industry, equipment, units, fuel, shipping, administration, offices, or free supply.
- Usage: pair with the Dublin map objective, Maritime Access/capacity and dynamic scarcity gates; keep the pair list explicit because foreign-reaction actor counts are window-scoped state.

### `ireland_sponsor_agreement_recorded`

- Scope: country; intended caller is `ireland_failed_sponsor_agreement_valid` and the sponsor-termination decision.
- Inputs: completion records for the British Supply, American Procurement, German Arms Promise, or Vatican Relief agreement chains.
- Output: true only after at least one named sponsor agreement has actually been opened and recorded.
- Defaults: false at the opening, for a generic foreign-reaction window, or for a regional route flag without an agreement chain.
- Side effects: none; the trigger does not open a channel, grant leverage, or create aid.
- Usage: combine with concrete failure evidence before exposing sponsor recovery work; do not use action visibility or a source-country tag as agreement proof.

### `ireland_failed_sponsor_agreement_valid`

- Scope: country; intended caller is `ireland_action_terminate_a_failed_sponsor_agreement`.
- Inputs: one recorded sponsor agreement plus its matching channel invalidation, delivery-mission failure, foreign sponsor collapse, German sponsor-collapse refusal record, or durable dependency-failure flag. `ireland_sync_ai_overlays` records the durable dependency flag once source leverage exceeds the shared dependency ceiling or the named German collapse refusal is recorded.
- Output: true only while a named agreement has a recoverable failure state that can justify closing access and replacing the supply route.
- Defaults: false before an agreement, after a merely open reaction window, or when only a generic foreign-exposure value is present.
- Side effects: none; the decision closes only the evidenced source channels, reduces their leverage, applies the bounded Transport/Maritime Provision and Supply/Equipment Readiness shock, and opens replacement diplomacy.
- Usage: keep source-specific failure records paired with their agreement histories; the action grants no replacement aid, equipment, units, fuel, shipping, territory, cores, alignment, offices, or recognition for free.

## Coercive Northern campaign scripted triggers

### `ireland_coercive_northern_route_legitimacy`

- Scope: country; intended caller is the Northern Settlement decision surface.
- Inputs: one committed revolutionary or militarist route and its earned command proof: IRA Northern command/policy/authority, Republican Congress mandate/path, O'Duffy command/order, Ailtirí state capture, or Dillon safeguards and military contribution.
- Output: true only when the current route has a route-specific authority record suitable for an offensive Northern plan.
- Defaults: false before route commitment or before the route-specific command proof is earned.
- Side effects: none; this trigger grants no claim, control, occupation, settlement, integration, core, unit, equipment, fuel, shipping, office, or recognition.
- Usage: combine with `ireland_coercive_northern_border_support` and `ireland_coercive_northern_military_cause` rather than using the route flag alone.

### `ireland_coercive_northern_border_support`

- Scope: country; intended caller is the same Northern campaign gate.
- Inputs: Northern command contact, IRA policy/authority, Congress mandate, local authorities, trade corridor, wartime bargain, or the later Northern stage review.
- Output: true only when a border, corridor, or operational support record exists. It does not impose a nationalist-consent threshold because the coercive route's consent test is deliberately separate from its legitimacy test.
- Defaults: false at the opening Northern values and before a named Northern preparation record.
- Side effects: none.
- Usage: keep this proof separate from the campaign's Readiness, Mobility, Provision, and material gates so blocked causes remain readable in the tooltip.

### `ireland_coercive_northern_military_cause`

- Scope: country; intended caller is the same Northern campaign gate.
- Inputs: the authored Northern war plan, its wartime-bargain completion, the produced Northern settlement-failure recovery signal, or the country's active war state.
- Output: true only when the campaign has a recorded military opportunity or crisis rather than a claim alone.
- Defaults: false while the country has only the Northern contact, claim, or negotiation flags.
- Side effects: none.
- Usage: combine with route legitimacy and border support through `ireland_coercive_northern_campaign_cause_valid`.

### `ireland_coercive_northern_campaign_cause_valid`

- Scope: country; final composite trigger consumed by `Plan a Coercive Northern Campaign`.
- Inputs: the three trigger families above.
- Output: true only when route authority, border support, and a military cause are all present.
- Defaults: false until all three proof classes are earned.
- Side effects: none; the linked decision still performs the explicit material charge and activates the separate `Take and Hold Belfast` mission.
- Usage: call as `ireland_coercive_northern_campaign_cause_valid = yes` inside the decision's available block.

## `ireland_recompute_provision`

- Scope: country; intended caller is IRE.
- Inputs: `ireland_provision_food`, `ireland_provision_energy`, `ireland_provision_transport`, and `ireland_provision_maritime`.
- Outputs: `ireland_provision_display` and severe/dual/zero bottleneck flags.
- Defaults: canonical opening components `55/25/40/30`, display `38`.
- Side effects: clamps display to the shared `0..100` range; does not add equipment, factories, fuel, shipping, or political power.
- Usage: `ireland_recompute_provision = yes` after a provisioning action or on the Ireland monthly hook.

## `ireland_recompute_readiness`

- Scope: country; intended caller is IRE.
- Inputs: seven Readiness component variables.
- Outputs: `ireland_readiness_display` and component bottleneck flags.
- Defaults: canonical opening components `25/8/20/12/5/5/30`, display `15`.
- Side effects: records equipment, supply, warning, and maritime bottlenecks; does not create free units or stockpiles.

## `ireland_commit_route`

- Scope: country; caller sets `ireland_route_commitment_input` before invocation.
- Inputs: route commitment input and current Settlement.
- Outputs: clamped route commitment, cleared momentum contributors, 180-day review flags.
- Side effects: resets pending Settlement-stage confirmation state and clears temporary route review targets. It does not create a leader, law, office, territory, core, or recognition.

## `ireland_record_mission_result`

- Scope: country.
- Inputs: active mission flag and result code (`1` full, `2` partial, `3` failure, `4` cancelled, `5` escalated).
- Outputs: mission result counters and a deferred mission-capacity rebuild request.
- Side effects: decrements the active mission count and clears mission target event targets. Capacity is rebuilt on the next initialized `on_daily_IRE` pass, after the decision engine has cleared the terminal mission flag, so the just-finished mission cannot be counted as active.

## `ireland_refund_cancelled_material_inputs`

- Scope: country; called by the physical-input mission cancellation paths in `common/decisions/ireland_decisions.txt`, including the Charter Foreign Tonnage alias of the Essential Cargo Route mission.
- Inputs: `ireland_cancel_refund_code`, the matching action's durable completion flag, and its one-time material-refund guard.
- Outputs: a floor-of-70-percent refund for the recoverable equipment, convoys, trains, manpower, fuel, or Naval Experience paid by the linked action; the refund guard is recorded and the code is cleared. The operational fuel/train layers for command exercises, essential-cargo rerouting, motorised corridors, and the Belfast campaign use the same capped path.
- Defaults: no refund occurs for a missing code, an action that never completed, or a repeated cancellation path. The harvest branch returns 14 Support Equipment and 105 Fuel against its 20-equipment/150-fuel commitment; the electoral-register branch returns 175 manpower against its 250-manpower staff commitment; the Border Belt confidence branch returns 175 manpower against its 250-manpower commitment; the rail branch returns 3 Trains and 175 manpower against its 5-train/250-manpower commitment; the coastwatch branch returns 14 Support Equipment and 175 manpower against its 20-equipment/250-manpower commitment; the Belfast-industry branch returns 70 Support Equipment, 35 Trucks, and 175 Fuel against its 100/50/250 commitment; the charter-origin branch returns 7 Convoys and 175 manpower against its 10-Convoy/250-manpower commitment; the procurement-origin branch returns 3 Convoys against its 5-Convoy commitment; the county-tillage branch returns 3 Trucks and 175 manpower against its 5-Truck/250-manpower commitment; neutral-shipping marking returns 7 Support Equipment against its 10-equipment commitment; ration books return 350 manpower against their 500-manpower commitment; the emergency-turf branch returns 3 Trucks and 525 manpower against its 5-Truck/750-manpower commitment; the cadre-reserve branch returns 70 Infantry Equipment, 17 Support Equipment, and 700 manpower against its 100/25/1,000 commitment; the veteran-settlement branch returns 70 Infantry Equipment and 700 manpower against its 100/1,000 commitment; and the compact-obligation branch returns 14 Support Equipment and 350 manpower against its 20/500 commitment. Quantity constants are defined in `common/script_constants/ireland_constants.txt` and are intentionally lower than the original charges.
- The current cultural-congress branch returns 3 Trucks against its 5-Truck transport commitment; the western-portfolio branch returns the same capped transport fraction; the aircrew-internment branch returns 175 manpower against its 250-manpower guard commitment; the Blacksod-station branch returns 175 manpower and 7 Support Equipment against its 250-manpower/10-equipment commitment; and the member-contribution branch returns 14 Support Equipment against its 20-equipment commitment. Quantity constants are defined in `common/script_constants/ireland_constants.txt` and are intentionally lower than the original charges.
- Side effects: restores only the listed physical inputs; it does not refund Political Power, Command Power, factory time, ledgers, map control, occupation, settlement, integration, cores, offices, alignment, recognition, or mission progress. The caller records the cancellation result and then performs ordinary mission cleanup.
- Usage: set the matching `constant:ireland.mission_refund_code_*`, call `ireland_refund_cancelled_material_inputs = yes`, then clear the mission's active, complete, and partial flags. The linked action clears its refund guard before a new commitment is paid.

## `ireland_evaluate_mission_objectives`

- Scope: country; called at the start of the initialized daily Ireland tick.
- Inputs: each active mission's named state objective and its live ledger threshold.
- Outputs: one full or partial objective flag for each of the 54 mission families; the full flag is reserved for the higher threshold and the partial flag for the recovery threshold.
- Defaults: objective checks are bounded to the state/resource or political condition named by the mission definition and never award territory, cores, equipment, units, factories, fuel, shipping, offices, alignment, or recognition.
- Side effects: records only transient terminal objective flags; the owning mission's full/partial/failure effects remain responsible for rewards, escalation, and historical result records.
- Usage: call before mission capacity rebuilds and before mission terminal evaluation in `on_daily_IRE`.

## `ireland_sync_political_gate_flags`

- Scope: country; intended caller is initialized IRE on the daily and monthly hooks.
- Inputs: recorded election mission results, completed focus handoffs, live Dáil, consent, stakeholder, Provision, Readiness, security, cultural, Northern, and foreign ledgers.
- Outputs: durable normal-route readiness flags, current crisis and radical-transition signals, dated Ailtirí gates, explicit H/P-to-A evidence confirmations, and late H/P handoffs for Dillon, IRA command, Northern deferment, defence, economy, vocational, and postwar review work.
- Defaults: no political route readiness is present merely because a seat, stakeholder, or cultural variable was initialized; each flag is earned from the named preceding focus, mission, crisis, or live threshold.
- Side effects: records route-access state only. It does not grant political power, industry, equipment, units, fuel, shipping, territory, cores, offices, alignment, recognition, or foreign access. Current crisis signals clear when their live failure condition recovers; durable route-failure history remains recorded.
- Usage: call after `ireland_sync_route_gate_flags` and before laws, spirits, leaders, AI priorities, or event gateways are refreshed.

## `ireland_update_achievement_history`

- Scope: country; called by the daily Ireland achievement tracker.
- Inputs: witnessed route flags, law stages, mission result records, office ledgers, foreign reaction records, Northern integration values, evidence provenance, and obligation memories.
- Outputs: irreversible achievement-history flags for the 32-entry Ireland ledger; the helper never clears a failure after a later recovery.
- Defaults: the support-agreement clock is `365` days after the named confidence-and-supply action; all other history begins unset and is earned from a concrete transition.
- Side effects: records explicit emergency, clerical, neutrality, Northern, evidence, obligation, foreign-control, ratification, and route-overthrow disqualifiers; it grants no industry, equipment, units, fuel, shipping, territory, core, office, recognition, or alignment.
- Usage: `ireland_update_achievement_history = yes` at the end of `ireland_update_achievement_trackers`.

## `ireland_sync_operational_state`

- Scope: country; intended caller is initialized IRE on the daily and monthly hooks.
- Inputs: the four Provision components, seven Readiness components, emergency/repeal route flags, war state, Security Loyalty, and the active neutrality incident source flags.
- Outputs: live National Emergency and External Emergency flags, command/security/mobilisation collapse signals, and the active incident-family flag consumed by laws and incident decisions.
- Defaults: no emergency or collapse flag is active at the canonical opening values; a zero component or war opens the relevant emergency state, while a recovered component clears the live failure signal after repeal.
- Side effects: synchronises only state flags; it grants no political power, equipment, units, factories, fuel, shipping, territory, cores, offices, alignment, or recognition. The separate achievement-history helper observes failures before recovery.
- Usage: `ireland_sync_operational_state = yes` after ledger recomputation in `on_daily_IRE`/`on_monthly_IRE`.

## `ireland_sync_neutrality_incident_family`

- Scope: country; normally called by `ireland_sync_operational_state`.
- Inputs: the generic active neutrality incident flag and one of the 48 numbered source flags.
- Outputs: exactly one of the nine active incident-family flags: airspace, shipping, internment, intelligence, weather, trade, access, censorship, or border.
- Defaults: all family flags are cleared when no incident is active.
- Side effects: removes stale family state after cleanup so law stages, mission caps, decisions, and event follow-ups cannot read a previous incident type.
- Usage: call the parent operational helper rather than duplicating the numbered source mapping.

## Persistent spirit family cleanup

### `ireland_remove_governing_spirit_forms`

- Scope: country; intended caller is `ireland_refresh_route_spirits` before installing a route trio or a governing-order failure.
- Inputs: none. The helper owns the complete registry of opening, durable-profile, named-failure, and generic-failure forms in the governing family.
- Outputs: no variables or flags. After execution, no governing-family spirit remains active.
- Defaults: safe when the country has no governing-family spirit or when several stale forms survived a prior route transition.
- Side effects: removes only governing-family ideas; it does not alter the organised-society or security/external-position families, routes, profiles, laws, offices, ledgers, or material state.
- Usage: `ireland_remove_governing_spirit_forms = yes`, followed immediately by one selected governing idea when the family should remain populated.

### `ireland_remove_society_spirit_forms`

- Scope: country; intended caller is `ireland_refresh_route_spirits` before installing a route trio or an organised-society failure.
- Inputs: none. The helper owns the complete registry of opening, durable-profile, named-failure, and generic-failure forms in the society family.
- Outputs: no variables or flags. After execution, no organised-society spirit remains active.
- Defaults: safe when the country has no society-family spirit or when several stale forms survived a prior route transition.
- Side effects: removes only organised-society ideas; it does not alter governing order, security/external position, routes, profiles, laws, offices, ledgers, or material state.
- Usage: `ireland_remove_society_spirit_forms = yes`, followed immediately by one selected society idea when the family should remain populated.

### `ireland_remove_security_spirit_forms`

- Scope: country; intended caller is `ireland_refresh_route_spirits` before installing a route trio or a security/external-position failure.
- Inputs: none. The helper owns the complete registry of opening, durable-profile, named-failure, and generic-failure forms in the security family.
- Outputs: no variables or flags. After execution, no security/external-position spirit remains active.
- Defaults: safe when the country has no security-family spirit or when several stale forms survived a prior route transition.
- Side effects: removes only security/external-position ideas; it does not alter governing order, organised society, routes, profiles, laws, offices, ledgers, occupation state, or material state.
- Usage: `ireland_remove_security_spirit_forms = yes`, followed immediately by one selected security idea when the family should remain populated.

## Ireland lifecycle registry

The following country-scoped helpers live in `common/scripted_effects/ireland_runtime.txt` and are called from `on_daily_IRE` or the owning action/focus:

- `ireland_rebuild_mission_counters`: scans all 54 active mission flags, rebuilds thirteen named category counters and their 2/3/4/12-cap policy, then reserves one global slot for live constitutional, provision, invasion, neutrality-incident, Northern, occupation, or route-review work. Critical mission families are the only activations exempted from that reservation, and only while their corresponding need flag is set; routine missions already running are allowed to finish or fail under their own deadlines.
- `ireland_cleanup_mission_objectives`: clears transient active/full/partial flags for all 54 mission families during route archival while preserving durable result-history flags.
- `ireland_dispatch_event_programme`: validates the bounded 100–735 next-entry cursor and walks the 457 ordered launch slots from that position. An ineligible slot advances to its successor during the same monthly scan. An eligible slot stores its successor, launches one report, and stops further admission. The final slot wraps to event 100, and a one-pulse cooldown after a successful launch limits the programme to six reports per year. The foreign-response range remains outside this catalogue behind its dedicated cursor sentinel.
- `ireland_sync_route_profile`: selects the durable H/P/A AI profile from committed route and hidden evidence flags, then calls `ireland_enforce_hpa_boundary`.
- `ireland_enforce_hpa_boundary`: clears contradictory H/P/A classification and active-route flags after profile synchronisation. Historical routes have neither plausible nor absurd active status; plausible routes have only the plausible active status; absurd routes have only the absurd active status. It never grants hidden permission or verifies impossible evidence.
- `ireland_sync_route_gate_flags`: derives the Clann Agrarian Support Bloc and constitutional vocational mandate gates from their dated/prerequisite flags, Agrarian Cohesion, Social Consent, and Minority Confidence.
- `ireland_sync_political_gate_flags`: derives election, succession, Fine Gael, Costello, Labour, defence, crisis, radical/corporate, clerical, dated Ailtirí, hidden-convention, Dillon, IRA command, defence/economy, and postwar handoffs from authored work and live thresholds.
- `ireland_sync_law_registry`: derives all 17 canonical law ladders from dated route, crisis, action, mission, Northern, and foreign-access records; writes staged variables plus active, public-entry, due-review, abuse, and exit flags.
- `ireland_sync_office_registry`: rebuilds the fifteen canonical office ledgers, separates leadership and movement vacancies, and exposes route/Northern vacancy overlays without silently promoting a character into another office.
- `ireland_refresh_route_spirits`: removes stale route variants, installs one evolving variant in each of the three persistent spirit families, then applies at most one ordered named failure override per family.
- `ireland_activate_route_leader`: retires the prior active leader, recruits/promotes the route leader, and records a one-time transition.
- `ireland_sync_route_identity`: clears the previous cosmetic identity and applies one of the 18 registered route tags.
- `ireland_sync_northern_ledger`: derives control, occupation, settlement, integration, and review ledgers from actual state control and named policy flags.
- `ireland_sync_named_northern_objectives`: rebuilds the Border Belt district count and matched health-service work count from the five named district records and four named service actions. It is called before mission-objective evaluation so the Cross-Border Health Service mission cannot complete from a Dublin-only building check. It records proof counters only; it does not change Northern control, occupation, settlement, integration, or cores.
- `ireland_sync_foreign_channels`: validates the British, American, German, and Vatican partner scopes each day. A missing or capitulated actor clears its open channel, records an actor-specific invalidation and foreign-access failure, and preserves leverage/reaction history for recovery and postwar review. It grants no aid, equipment, units, territory, cores, offices, alignment, or recognition.
- `ireland_sync_northern_final_review_proofs`: rebuilds the 13 named Northern final-review proof flags from current state control, law stages, consent floors, durable full mission records, named decisions, resistance, guarantees, withdrawal safeguards, demobilisation, and the 180-day sustained-security review. It does not grant a claim, control, occupation, settlement stage, integration stage, or core.
- `ireland_apply_northern_core_review`: grants the state 119 core only after the strict final-review trigger passes; otherwise records a blocked review.
- `ireland_sync_ai_overlays`: derives the ten temporary AI overlays from election, crisis, material, war, Northern, sponsor, leadership, postwar, and conclusion-review state, then clears them when their trigger closes.
- `ireland_update_achievement_trackers`: records durable minima, maxima, route conclusions, mission records, and witnessed war/neutrality history.
- `ireland_update_achievement_history`: records durable route, law, office, evidence, obligation, Northern, ratification, and failure history, including expiry of temporary confidence-and-supply support.
- `ireland_sync_operational_state`: derives emergency, command, mobilisation, security, and neutrality-family state from live ledgers and numbered incident sources.
- `ireland_open_event_gateways`: opens or closes the route event programme and maintains family gateways.
- `ireland_dispatch_foreign_reaction_response`: selects one unresolved eligible actor response after four quiet days in a reaction window. Previously shown actor nodes remain durable campaign records; undisplayed nodes remain available to later windows.

Canonical variables are authoritative and are read directly by the decision and runtime consumers. The legacy decision-facing names remain compatibility aliases refreshed from them after each daily tick; they never overwrite provision, readiness, Northern, or consent values.

## `ireland_open_foreign_reaction_window`

- Scope: country.
- Inputs: none; actor-specific caller effects set reaction score and targets.
- Outputs: a 14-day active window, a one-response broker state, and digest state.
- Side effects: starts a 120-day global reaction-programme cooldown, presents at most one actor report, and schedules one aggregate digest only when additional reactions exist. It does not grant diplomatic access or recognition by itself.

## `ireland_record_foreign_rc01_observation`

- Scope: country; called by the RC-01 neutral-shipping response.
- Inputs: live Neutrality Integrity and Readiness intelligence coverage.
- Outputs: persistent observation count, target flag, source-confidence value, and bounded review timer.
- Defaults: confidence is the mean of the two live ledgers; the review timer is the canonical 14-day reaction window.
- Side effects: records concern only; it does not change leverage, stockpiles, territory, cores, recognition, or access.

## `ireland_resolve_foreign_digest_reactions`

- Scope: country; called when the 14-day foreign reaction window reaches its review boundary.
- Inputs: the prepared actor ledger, capability-valid event flags, the current-window response flags, visible response count, persistent accepted/refused history only as event memory, and the six severe classes that cannot be hidden.
- Outputs: durable digest-pending count, total eligible response count, twelve primary-class counters, actor-family digest flags for hidden non-severe nodes only, severe-response hold state, timed saturation flags, and event-memory flags for resolved nodes.
- Defaults: four ordinary responses may remain visible; eligible non-severe responses beyond that cap enter the digest while an ultimatum, mobilisation, sponsor collapse, occupation threat, or postwar admission keeps the window open until its visible node resolves.
- Side effects: records only eligible actor/class responses and their persistent pressure; per-window flags prevent old response history from replaying into a later ledger, while persistent accepted/refused flags remain available to their follow-up chains. It does not manufacture a fixed response total or invent aid, equipment, units, territory, cores, offices, recognition, or alignment. It clears no severe node into a digest.

## `ireland_prepare_foreign_reaction_ledger`

- Scope: country; called once after a reaction window opens and again only if the ledger was not prepared.
- Inputs: the eight matrix score inputs — trigger severity, strategic stake, existing actor-specific leverage or commitment, legal/treaty exposure, domestic constituency, opportunity/threat, actor saturation inside sixty days, and actor inability/invalidity — plus live route, partner, access, institution, Northern, neutrality, postwar, sponsor, and evidence flags.
- Outputs: twelve separate actor-validity flags, twelve actor-specific scores and observations, capability-valid event flags for the 30 mapped reaction nodes, expected actor/class counters, and the aggregate display score as the mean of valid actor scores.
- Defaults: no response node exists for an invalid actor or an actor below the class threshold; chained nodes require their predecessor; observation-tier actors are retained as RC-01 review records rather than popup events.
- Side effects: records source-specific commitments and invalidation state without merging foreign actors. It grants no access, aid, equipment, units, territory, cores, offices, recognition, alignment, or diplomatic status.

## `ireland_sync_national_settlement_bop`

- Scope: country.
- Inputs: authoritative Settlement variable `-100..100`.
- Outputs: native BOP presentation at `-1..1` using a meta effect.
- Side effects: changes only the BOP display value; route and law effects remain in their owning callers.

## `ireland_sync_cultural_evidence`

- Scope: country; intended caller is initialized IRE on daily/monthly ticks or a concealed-evidence inspection request.
- Inputs: Cultural Capacity, named H/P cultural completion flags, full mission records, Northern cultural contacts, public knowledge, accepted obligations, and durable disqualifier history.
- Outputs: four public culture components, public lane flags, concealed credible/category/region/disqualifier/obligation/public-knowledge counters, the hidden-evidence gate, and the independent-evidence-ready flag. The GUI inspect action owns the separate revealed flag.
- Defaults: capacity `30`, public components `30/27/25/22`, public knowledge `20`, and no concealed records.
- Side effects: clamps all displayed counters and records one-time obligation projections; it never grants hidden route access, territory, cores, industry, equipment, units, fuel, shipping, offices, recognition, or alignment by itself.
- Usage: call from the Ireland daily/monthly hook and from `ireland_sync_gui_requests` when the evidence ledger requests inspection; the latter clears the inspection request after recomputation while the scripted-GUI inspect action controls disclosure.

## `ireland_sync_plebiscite_state`

- Scope: country.
- Inputs: the authored plebiscite campaign-open flag and passed/rejected/recovered result flags.
- Outputs: synchronized generic and Northern plebiscite-open flags.
- Side effects: closes both open states and the campaign flag after any recorded result; it does not decide the result and does not change Northern control, occupation, settlement, integration, or cores.
- Usage: call before Northern GUI projection and after the result event's outcome flags are written.

## `ireland_sync_gui_requests`

- Scope: country; consumed on the Ireland daily tick.
- Inputs: conditions-review, Northern-review, and concealed-evidence-inspection request flags plus row selections set by the three scripted GUI surfaces.
- Outputs: refreshed live projections, GUI dirty counters, and persisted last-reviewed row state for each ledger.
- Side effects: consumes each request once, runs only the owning recomputation/review helpers, and keeps the GUI a projection of authoritative ledgers rather than a second gameplay state machine.
- Usage: call after the main daily ledger synchronization and before the event/achievement gateway pass.

## `ireland_sync_ai_priority_flags`

- Scope: country; consumed on the Ireland daily/monthly tick.
- Inputs: durable route-profile flags and the ten temporary AI overlays.
- Outputs: thirteen category-priority flags covering settlement/government, elections, organised society, cultural/archive work, underground politics, Provision, Readiness, Neutrality incidents, foreign relations, Northern work, occupation/integration, regional/external work, and postwar conclusions.
- Side effects: clears stale priorities before deriving the current route and overlay priorities; it never creates political power, equipment, units, territory, cores, recognition, or alignment.
- Usage: call before the action and mission AI weights are evaluated.

## `ireland_sync_ai_decision_utility`

- Scope: country; called by `ireland_sync_ai_priority_flags` on the initialized daily/monthly Ireland hooks.
- Inputs: the active route profile, emergency and war state, election/constitutional/review deadlines, mission-capacity reservation flags, live Provision and command-collapse state, Social Consent, Foreign Exposure, and durable full/partial/failure/escalation mission records.
- Outputs: profile-sensitive Social Consent and Foreign Exposure safety thresholds plus derived deadline, dependency, conclusion, recovery, material-safety, consent, exposure, normal-band, and maintenance-band utility flags.
- Defaults: prudent routes require `50` Consent and avoid exposure at `60`; pragmatic, radical, and direct-survival states use the scoped canonical floor/ceiling constants. A review becomes deadline pressure only inside its final `60` days.
- Side effects: clears and rebuilds AI-only scoring state. Full mission records remain neutral after their normal terminal cleanup; unresolved partial records and unrecovered failure/escalation records create recovery pressure. It does not change a decision's availability, map objective, costs, mission duration, result, escalation, cooldown, target, route, or cleanup.
- Usage: the 140 actions and 54 missions consume these flags through their existing `ai_will_do` blocks. Critical mission families and their launch actions receive the `70` critical score band; other candidates receive the `35` normal or `15` maintenance band. Action blocks also subtract eight points per authored Action Burden level through shared constants. Their owned `days_re_enable` gates remain the exact same-family repetition control, while `ireland_mission_capacity_rebuild_pending` suppresses blind replacement selection during terminal mission cleanup.

## `ireland_sync_ai_domain_flags`

- Scope: country; called after category priorities are derived.
- Inputs: the active durable profile and any of the ten temporary overlays.
- Outputs: mutually cleared primary and supporting domain flags for all thirteen decision categories.
- Defaults: each durable profile names one primary domain and its route-support domains; overlays add urgent domains while preserving the route profile.
- Side effects: none beyond AI-only flags. It does not open content, alter availability, or bypass physical, political, map-objective, mission-capacity, or cleanup gates.
- Usage: decision `ai_will_do` blocks apply the matrix's `+30` primary and `+15` supporting bonuses after this helper runs.

## `ireland_sync_ai_candidate_ledger`

- Scope: country; called after the domain and shared utility layers on the initialized Ireland daily/monthly hooks.
- Inputs: the durable profile roster, temporary overlays, thirteen category priorities, live bottlenecks, failure/recovery flags, reserved-slot flags, review deadlines, foreign-reaction state, Northern occupation state, and postwar state.
- Outputs: one cause, repair, and dependency flag for each of the thirteen decision categories; the active six-stance normal/crisis willingness floors; and the shared expected-utility envelope used to decide whether a prioritized candidate is worth evaluation.
- Defaults: the six floors are `25/5` cautious constitutional, `15/0` pragmatic constitutional, `10/-10` radical survival, `5/-15` authoritarian command, `20/0` concealed stewardship, and `0/-25` desperate/self-destructive. A candidate must belong to a prioritized category with live cause, repair, or dependency pressure and meet at least the crisis floor; normal-band work must meet the normal floor.
- Side effects: clears and rebuilds AI-only ledger flags and variables. It never opens a route, grants hidden permission, changes an action or mission's availability, creates a resource, changes a mission cap, or bypasses Northern integration/core review.
- Usage: `ireland_ai_utility_candidate_pressure`, `ireland_ai_utility_dependency_necessary`, and `ireland_ai_utility_recovery_priority` consume the category ledger; the existing 194 authored action/mission blocks then apply their named domain, burden, deadline, material, foreign, consent, conclusion, and cleanup modifiers.

## `ireland_h14_full_terms_met`

- Scope: country; intended callers are the final H14 cabinet event options.
- Inputs: a valid British implementing partner and open channel, completed defence estimates, command audit and command structure, Readiness 35, British Flexibility 45, Nationalist Consent 50, and Unionist Consent 20 or enforceable Northern safeguards.
- Output: true only while the documented full-unity implementation threshold remains live at final resolution.
- Defaults: false after sponsor invalidation, channel closure, readiness or consent deterioration, or before the preparation records exist.
- Side effects: none; the trigger does not grant a unity result, Northern control, occupation, settlement, integration, core, equipment, unit, office, or recognition.
- Usage: use it to gate the H14 federal, unitary, postwar-pledge, and defence-cooperation options. The final event owns the distinct outcome flags; the Northern focus separately requires a full-unity result and consumes its ready handoff.

## Ireland logistics objective contracts

## Coastwatch sector lifecycle effects

### `ireland_recompute_coastwatch_posts`

- Scope: country.
- Inputs: the six sector post-allocation variables and the canonical historical total of `83` posts.
- Outputs: `ireland_coastwatch_posts_established`, clamped to the historical total.
- Defaults: all six sector allocations begin at `0` during Ireland campaign initialisation.
- Side effects: none beyond the aggregate ledger; it does not create equipment, manpower, units, territory, cores, or naval capacity.
- Usage: called before and after a Coastwatch mission result so partial allocations can be replaced by a later full result.

### `ireland_prepare_coastwatch_sector`

- Scope: country.
- Inputs: the six durable `ireland_coastwatch_sector_*_operational` records.
- Outputs: `ireland_coastwatch_active_sector`, selecting the first uncompleted sector in canonical order: northwest/Donegal, Galway/western islands, southwest/Berehaven, Cork/south coast, east coast/Dublin, and border loughs/Northern interface.
- Defaults: sector `0` when all six operational records already exist; the action admission gate prevents a launch in that state.
- Side effects: none beyond the active mission pointer.
- Usage: called by `Build a Coastwatch Sector Network` immediately before the linked mission is activated. The pointer is cleared by every terminal mission result and cancellation.

### `ireland_record_coastwatch_sector_result`

- Scope: country; called by the Coastwatch mission's full, partial, failure, and escalation terminal effects.
- Inputs: the active sector pointer, `ireland_mission_result`, the six sector allocation ledgers, and the number of sectors already completed.
- Outputs: one sector's post coverage, observer training, communications reliability, aircraft/vessel recognition, weather reporting, rescue access, security exposure, and operational flag. Full success advances the six-sector record; partial success records a retryable lower band; failure/escalation leaves the active sector blind or exposed.
- Defaults: full component score `100`, partial component score `50`, operational security exposure `15`, partial exposure `45`, and failure exposure `80`; the post share is calculated from the remaining portion of the fixed `83`-post total and remaining sectors.
- Side effects: increments the completed-sector count only on full success, recomputes total posts, and leaves air warning, harbour defence, and marine-patrol histories untouched. It grants no free material, unit, territory, core, office, recognition, alignment, or access.
- Usage: call after the mission result is recorded and before mission flags are cleared. Do not call for cancellation, because cancellation refunds its material inputs without writing a sector result.

The following twelve country-scope scripted triggers are side-effect-free physical contracts. Their outputs are booleans only. Admission siblings include route, category, control, platform, capacity, and material gates; full/partial siblings include active action/mission provenance and the live objective bands. The cargo capacity helper is intentionally physical-only so the action can combine it with its normal category, route, law, office, and dynamic-cost gates without making mission result evaluation self-contradictory.

| Trigger | Inputs and output | Side effects / usage |
| --- | --- | --- |
| `ireland_rail_corridor_admission_valid` | Original IRE, unarchived Provision route, launchable mission, full control and infrastructure in states `113`/`135`, 5 Trains, 250 manpower, 200 Fuel, one available civilian factory, and the existing component/category gates; true when rail launch admission is valid. | None. Shared by the rail action admission and AI safety test. |
| `ireland_rail_corridor_full_valid` / `ireland_rail_corridor_partial_valid` | Active rail action and mission, full control of `113`/`135`, and Transport Serviceability `50`/`35`; full additionally requires the railway connection and level 1 at both endpoints, while partial accepts the connection or both endpoint levels. | None. Full is evaluated before partial by runtime, mission availability, and map-objective projection. |
| `ireland_essential_cargo_route_capacity_valid` | Full control and industrial complex in state `135`, a railway connection to `113`, a live Irish/chartered/foreign/neutral merchant route, 5 Convoys, 2 Trains, 200 Fuel, and naval-base capacity level `1/2/3` according to whether zero/one/both named maritime missions are active. | None. Shared by the cargo action and AI capacity test; it does not alter port capacity. |
| `ireland_essential_cargo_full_valid` / `ireland_essential_cargo_partial_valid` | Active cargo action and mission plus Maritime Access `50`/`35`; full uses the complete capacity contract, while partial requires the state-135 port and either a valid merchant route or the railway. | None. Full is evaluated before partial and neither outcome creates shipping. |
| `ireland_command_district_force_commitment_valid` | Original IRE, unarchived Readiness route, launchable mission, full control/platform in state `113`, at least one division, Supply Readiness `20`, 50 Infantry Equipment, and 250 Fuel with category and emergency gates. | None. Shared by the command action and AI force/material test. No helper creates or moves a division. |
| `ireland_command_district_exercise_full_valid` / `ireland_command_district_exercise_partial_valid` | Active action and mission, full-control arms/infrastructure platform, one/two divisions, Command `35/50`, and Supply `20/35` for partial/full bands. | None. Full is evaluated before partial; result recording leaves unit deployment untouched. |
| `ireland_belfast_contract_admission_valid` | Original IRE, unarchived Northern route, occupation/provisional/integration authority, launchable mission, full control/platform in state `119`, Labour Cooperation `30`, two available civilian factories, 100 Support Equipment, 50 Trucks, and 250 Fuel. | None. Shared by the Belfast action and AI admission/safety test. The action owns the two-factory reservation. |
| `ireland_belfast_industry_full_valid` / `ireland_belfast_industry_partial_valid` | Active action and mission, full-control industrial/infrastructure platform, Labour Cooperation `45/30`, and Industrial Capacity `55/40` for full/partial bands. | None. Full is evaluated before partial; cancellation releases the reservation and returns only the documented material caps. |

Usage contract: the four action blocks call their admission helper inside the visible requirement tooltip; the four mission blocks use the same full/partial helpers for availability; `ireland_evaluate_mission_objectives` uses full before partial; and each mission's existing cancellation/refund and route cleanup remains authoritative. These helpers never grant political power, equipment, units, fuel, shipping, factories, territory, recognition, or cores.

## Dillon mandate and safeguard helpers

### `ireland_dillon_named_vote_gate_strict`

- Scope: country; used by the named Dáil decision gate and the final Dillon
  war-entry event.
- Inputs: the base `ireland_dillon_named_vote_gate` plus the live
  `ireland_intervention_mandate` at the shared 90-point Dillon mandate
  constant.
- Output: true only when the explicit named vote is recorded and the mandate
  remains at or above the required threshold. The invasion-danger exception is
  intentionally not part of this helper.
- Defaults: false when the vote is only pending, the route has lost its
  mandate, or the named vote flag was cleared by cleanup.
- Side effects: none; this is a gate, not a vote setter or a political-power
  store.
- Usage: keep the direct-attack exception confined to the final war-entry
  trigger's separate logic; never use it to synthesize Dáil assent.

### `ireland_advance_dillon_mandate` / `ireland_setback_dillon_mandate`

- Scope: country; called by the authored F04 flavour choices and P04 Dillon events.
- Inputs: Social Consent for an intervention argument, and Neutrality Integrity plus British Leverage for a setback.
- Outputs: a clamped `ireland_intervention_mandate` change using the shared Dillon gain/loss constants. The effect is invoked only by a named event choice, so the mandate is not a passive political-power store.
- Defaults: the campaign starts at `0`; every public argument scales with the current consent ledger, while each setback scales with current exposure and coercive pressure.
- Side effects: none beyond the mandate variable; event options retain ownership of readiness, settlement, leverage, foreign-reaction, and route-memory consequences.
- Usage: call the advance helper for documented aggression, guarantees, army, shipping, and campaign arguments; call the setback helper for the opposing choice. Do not call either from a daily tick.

### `ireland_sync_dillon_route_state`

- Scope: country; called after law-registry refresh on the Ireland daily and monthly hooks.
- Inputs: route commitment, the public P04 platform result, full reserve/command/contribution mission records, named access and guarantee actions, foreign safeguard record, active trade/foreign-access/guarantee laws, Northern policy or deferment, and the live Dillon political gate.
- Outputs: `ireland_dillon_mandate_complete`, `ireland_dillon_vote_passed`, and the ten detailed safeguard flags. `ireland_dillon_safeguards_ready` is true only while all ten records are simultaneously live.
- Defaults: a Dillon caucus never creates safeguards by itself; missing or revoked underlying records clear their derived flag. The sovereignty base flag is available only from a sovereignty mandate, foreign safeguard record, or named unitary charter.
- Side effects: clears route-specific derived flags after route closure or outside Dillon. It grants no equipment, units, territory, cores, offices, shipping, factories, alignment, or recognition.
- Usage: the public dissent focus opens the route, the caucus focus records the caucus, the daily sync records the named vote after its political gate, and the war-assent focus still checks the complete Part 2 plus Part 4 gate.

### `ireland_sync_dillon_crisis_boundary`

- Scope: country; called after the native law and Dillon state syncs.
- Inputs: the native `ireland_national_settlement` balance of power and its `ireland_armed_dual_authority_range`.
- Outputs: a live `ireland_dual_authority_crisis_active` flag and the constitutional-crisis block used by the final Dillon gate.
- Defaults: the flag clears when the balance leaves the armed dual-authority range; no numeric proxy replaces the native balance-of-power check.
- Side effects: none beyond crisis flags; it does not move the balance or choose a constitutional route.
- Usage: keep this helper after `ireland_sync_law_registry` so the war-assent gate sees the current legal and balance state.
## Integrated Maritime Service

### `ireland_ensure_integrated_maritime_service`

- Purpose: idempotently add the visible `ireland_integrated_maritime_service`
  country dynamic modifier.
- Scope: Ireland country scope.
- Inputs: the country's current dynamic-modifier registry; no arguments.
- Outputs: adds the modifier only when it is absent.
- Defaults: campaign initialization owns and zeroes the modifier's nine backing
  variables. An undefined backing variable is still evaluated as zero by the
  engine, keeping history-driven focus completion safe.
- Side effects: none beyond adding the modifier. It does not change a reward
  variable, ledger component, flag, idea, building, or unit.
- Usage: call `ireland_ensure_integrated_maritime_service = yes` in a hidden
  country effect before incrementing any maritime reward variable. Naval Staff
  and Marine Service reconstruction both call it so repeated execution remains
  safe.

## Parliament action executors

The opening Oireachtas programme has one guarded executor per action. Both the
scripted-GUI click and the sequential native decision call that executor, so
the availability gate, political-power debit, record helper, and completion
lock have one owner. All tuning values live in
`common/script_constants/ireland_constants.txt`.

`ireland_update_parliament` also projects each action into one of four
centralized frame constants: locked, current but unaffordable, current and
available, or complete. It reads the same `*_action_current` and
`*_action_available` triggers used by the controller paths and refreshes the
single non-overlapping status seal during Ireland's existing daily political
sync.

| Effect | Purpose and scope | Inputs and outputs | Defaults and side effects | Usage |
| --- | --- | --- | --- | --- |
| `ireland_execute_parliament_dail_action` | Executes the opening Dáil sitting in Ireland country scope. | Reads `ireland_parliament_dail_action_available`; calls `ireland_record_parliament_dail_session` without a political-power charge. | Does nothing when the gate is false. The record helper adds routine votes, Dáil Mandate, Cabinet Cohesion, Social Consent, and the completion flag. | Called by both the Dáil button and native Dáil decision. |
| `ireland_execute_parliament_seanad_action` | Secures Seanad support in Ireland country scope. | Reads `ireland_parliament_seanad_action_available`; deducts the Seanad PP cost and calls `ireland_record_parliament_seanad_support`. | Does nothing when the gate is false. The record helper adds government seats, Social Consent, Cabinet Cohesion, and the completion flag. | Called by both the Seanad button and native Seanad decision. |
| `ireland_execute_parliament_confidence_action` | Records the confidence-and-supply compact in Ireland country scope. | Reads `ireland_parliament_confidence_action_available`; deducts the confidence PP cost and calls `ireland_record_parliament_confidence_compact`. | Does nothing when the gate is false. The record helper adds external support, routine votes, Dáil Mandate, Social Consent, Cabinet Cohesion, and the completion flag. | Called by both the confidence button and native confidence decision. |
| `ireland_execute_parliament_budget_action` | Passes the joint opening budget in Ireland country scope. | Reads `ireland_parliament_joint_budget_action_available`; deducts the budget PP cost and calls `ireland_record_parliament_joint_budget`. | Does nothing when the gate is false. The record helper adds Stability, Administrative Reach, Dáil Mandate, Cabinet Cohesion, and the completion flag. | Called by both the budget button and native budget decision. |

## Territorial-policy admission triggers

### `ireland_atlantic_claim_enforcement_ready`

- Scope: Ireland country scope.
- Purpose: canonical material and political admission gate for every coercive
  Atlantic preparation.
- Inputs: peace, the Atlantic enforcement and readiness conclusions, Dublin
  control, a Dáil majority, and the centralized manpower, infantry equipment,
  support equipment, convoy, fuel, and Command Power thresholds.
- Output: true only while every shared readiness requirement is live. Target
  ownership, control, faction relation, reach, and relative strength remain
  decision-specific checks because they require a state-controller scope.
- Defaults and side effects: false on any missing proof; no side effects.
- Usage: call from both decision availability and the completion-time
  revalidation limit before issuing a claim or timed war goal.

### `ireland_can_launch_postwar_mission`

- Scope: Ireland country scope.
- Purpose: shared admission gate for the Atlantic settlement review mission.
- Inputs: conclusion state, the active-mission marker, and the global mission
  capacity maintained by `ireland_update_mission_capacity`.
- Output: true only while a new postwar mission can reserve a real mission
  slot. The decision separately requires a free postwar-category slot and at
  least one relevant controlled holding or subject relationship.
- Defaults and side effects: false after conclusion, while the mission is
  active, or when global capacity is full; no side effects.
- Usage: check at decision availability, cancellation, and completion. Set the
  active marker, activate the mission, and immediately call
  `ireland_update_mission_capacity`; repeat the capacity update on every
  terminal or cleanup path.

### `ireland_clear_territorial_diplomacy_targets`

- Scope: any country scope; normally called from the Ireland result event.
- Purpose: remove the saved requester, target-controller, and target-state
  pointers used by the Ulster ultimatum, Belfast compact, and Highlands
  settlement event chains.
- Inputs: the three global event targets created by the initiating territorial
  decision.
- Outputs: clears all three pointers. The caller remains responsible for
  clearing its pending/active country flags and applying any outcome-specific
  cooldown.
- Defaults and side effects: no political, territorial, diplomatic, or
  material effect. It is safe to call on a stale or already-cleared target.
- Usage: call on every terminal accept, refusal, counteroffer resolution, and
  stale-target/refund branch; never from a daily or monthly on-action.

### `ireland_consume_atlantic_enforcement_reserves`

- Scope: Ireland country scope.
- Purpose: consume the material deployment committed when a coercive Atlantic
  diplomatic or claim operation actually launches.
- Inputs: the caller must first pass
  `ireland_atlantic_claim_enforcement_ready` and its live target-specific
  completion checks.
- Outputs: removes 1,000 manpower, 200 infantry equipment, 20 support equipment,
  5 convoys, 250 fuel, and 10 Command Power using centralized script constants;
  prints the matching player-facing effect tooltip.
- Defaults and side effects: it performs no admission check, target selection,
  claim, war goal, flag, or refund. A cancelled or invalid preparation must not
  call it.
- Usage: call once inside the successful completion branch immediately before
  saving a territorial demand target or issuing a staged claim war goal.

### `ireland_atlantic_settlement_all_relevant_resolved`

- Scope: Ireland country trigger; used by the Atlantic settlement mission.
- Purpose: require each currently controlled Atlantic holding and each current
  Scottish/Welsh subject to have its own resolution record.
- Inputs: state-specific rights/integration flags and subject-specific
  protectorate flags.
- Output: true only when no relevant controlled state or eligible subject is
  unresolved. Losing a holding or subject removes it from the requirement.
- Side effects: none. This trigger does not close the mission or clear a flag.

## Postwar family conclusion architecture

The postwar family layer separates material foundation, family settlement,
terminal evaluation, report presentation, recovery, and route archival. The
review evaluator is not terminal: a full or partial report must explicitly
accept its result before the route is closed and archived. Blocked and failed
reports keep the route playable and open one family recovery action.

### Shared postwar constants

The `ireland` script-constant category owns the postwar timing and project
reservation values:

| Constant | Value | Used by |
| --- | ---: | --- |
| `postwar_family_settlement_days` | 180 | five one-time family settlement actions (`days_remove`) |
| `postwar_family_recovery_days` | 120 | five family recovery actions (`days_remove`) |
| `postwar_family_factory_use` | 1 | settlement/recovery project `civilian_factory_use` modifier |
| `postwar_family_review_days` | 180 | `ireland_begin_conclusion_review` countdown |

Do not duplicate these values in a decision, event, or scripted helper.

### `ireland_family_postwar_settlement_complete`

- Scope: Ireland country trigger.
- Purpose: canonical completion gate for the one family-specific postwar
  settlement project.
- Inputs: initialized Ireland scope and the shared country flag
  `ireland_family_postwar_settlement_complete`, set by exactly one of the five
  family settlement actions.
- Output: true when the shared institutional settlement is recorded. The
  trigger does not infer completion from a route, ideology, capstone, or mission
  result.
- Defaults and side effects: false before the action completes; no side effects.
- Usage: use in terminal-report success options and
  `ireland_archive_successful_route`, not as a substitute for the foundation
  requirements.

### `ireland_has_active_route_review_critical_mission`

- Scope: Ireland country trigger.
- Purpose: distinguish the route-review mission queue from unrelated
  constitutional, component, invasion, neutrality, Northern, occupation, and
  routine critical missions.
- Inputs: active flags for the six-month settlement review, constituent
  authority, wartime rationing, demobilised forces, Republic/Commonwealth
  settlement, United Nations admission, and national reconstruction missions.
- Output: true while any named route-review critical mission is active.
- Defaults and side effects: false when all listed missions are terminal or have
  not started; no side effects.
- Usage: `ireland_postwar_foundation_ready` uses the trigger so a family
  settlement project cannot start while a route-review objective is unresolved.

### Family recovery surface triggers

The evaluator maps each recovery action's durable `ireland_postwar_*` repair
record back to only the surfaces that action owns. Every mapping also requires
`ireland_family_conclusion_recovery_complete`, so a similarly named flag cannot
silently bypass a review before the action completes:

- `ireland_family_postwar_government_repair_recorded`: democratic coalition,
  communist Congress, or restoration Crown Council repair.
- `ireland_family_postwar_law_repair_recorded`: democratic coalition repair.
- `ireland_family_postwar_defence_repair_recorded`: communist Congress or
  fascist directorate repair.
- `ireland_family_postwar_economy_repair_recorded`: oligarchic producer-estate
  repair.
- `ireland_family_postwar_identity_repair_recorded`: restoration Crown Council
  repair.

These are country triggers with no side effects. They are evaluator-only
admission proofs; they do not set, clear, or rewrite the underlying route
surface flags.

### `ireland_postwar_foundation_ready`

- Scope: Ireland country trigger; intended callers are the five family
  settlement decisions and their AI weights.
- Purpose: require the dated, material postwar foundation before a family can
  convert its route proof into an institutional settlement.
- Inputs: initialized, unarchived Ireland; date after `1946.1.1`; peace or the
  recorded `ireland_major_war_ended` flag; completed emergency declaration
  review; full/partial records for rationing, demobilisation, and national
  reconstruction; a full/partial Republic/Commonwealth settlement mission;
  and a full/partial United Nations admission mission or the explicit
  `ireland_postwar_alternate_order_resolved` flag when
  `ireland_un_admission_authority` is false. It also requires no active
  `ireland_has_active_route_review_critical_mission` mission.
- Output: true only when all material foundation records are present. The date
  opens the era but never substitutes for mission or institutional proof.
- Defaults and side effects: false before any requirement is met; no side
  effects.
- Usage: put `ireland_postwar_foundation_ready = yes` in settlement action
  `available` and `ai_will_do` blocks. The caller still owns family/capstone
  visibility and the settlement action's completion flags.

### `ireland_begin_conclusion_review`

- Scope: Ireland country effect.
- Inputs: no parameters; the caller must have completed the relevant settlement
  or family recovery action. The helper reads
  `ireland_family_conclusion_recovery_complete` when a recovery action has just
  repaired a blocked/failed result.
- Outputs: starts the 180-day `ireland_conclusion_review_days` countdown and
  clears the due marker. After a recovery action, it also sets
  `ireland_route_failure_recovered`; this preserves `ireland_route_failure`
  history while allowing the next evaluation to classify the repaired route as
  partial instead of failed.
- Defaults and side effects: no-op while a review is already active or while
  `ireland_conclusion_recovery_open` remains set; no route closure, archival,
  cleanup, or report dispatch.
- Usage: call at the end of every family settlement/recovery action, after its
  own institutional flags are set. A recovery caller must clear
  `ireland_conclusion_recovery_open` before calling it.

### `ireland_open_family_conclusion_recovery`

- Scope: Ireland country effect.
- Inputs: current `ireland_route_conclusion_blocked` or
  `ireland_route_conclusion_failed` result; no parameters.
- Outputs: sets `ireland_conclusion_recovery_open`, clears the prior recovery
  completion/recovered markers for the new cycle, and clears the review timer so
  no second 180-day review can begin before a recovery action completes.
- Defaults and side effects: no-op after route archival or when the current
  result is full/partial. It does not clear any named blocked-surface flag or
  durable failure history, and it does not call route cleanup.
- Usage: called by `ireland_finalize_route_conclusion` before dispatching a
  blocked/failed family report. The matching recovery action clears the open
  flag, sets `ireland_family_conclusion_recovery_complete`, clears only its
  named blocked surfaces, and calls `ireland_begin_conclusion_review`.

### `ireland_dispatch_family_conclusion_event`

- Scope: Ireland country effect; direct terminal-report dispatch.
- Inputs: one mutually exclusive family flag among
  `ireland_family_democratic`, `ireland_family_communist`,
  `ireland_family_fascist`, `ireland_family_oligarchic`, and
  `ireland_family_restoration`.
- Outputs: fires exactly one triggered-only report event from the
  `ireland_country_conclusion` namespace: `.1` democratic, `.2` Congress, `.3`
  Blueshirt, `.4` producer-estate, or `.5` restoration.
- Defaults and side effects: no-op when no family flag is present. The ordered
  `else_if` chain prevents multiple report events even if a malformed scope has
  more than one family flag. It does not add a world scan, generic dispatcher
  candidate, event target, or `fire_only_once` guard.
- Usage: call once at the end of `ireland_finalize_route_conclusion`, after the
  result flags and recovery-open state are set. Report options own durable
  report records and decide whether to archive or keep recovery open.

### `ireland_archive_successful_route`

- Scope: Ireland country effect; terminal success option only.
- Inputs: `ireland_route_conclusion_review_complete`, full or partial result,
  `ireland_family_postwar_settlement_complete`, and a closed recovery state.
- Outputs: consolidates foreign reactions and neutrality incidents, sets
  `ireland_route_cleanup`, `ireland_route_closed`, and
  `ireland_route_archived`, runs `ireland_cleanup_route_state`, rebuilds mission
  counters, and requests spirit/profile synchronisation.
- Defaults and side effects: no-op when the result is blocked/failed, the family
  settlement is missing, recovery is open, or the route is already archived.
  This is the only P0 conclusion helper that sets route closure/archive flags.
- Usage: call from the full/partial option of the matching
  `ireland_country_conclusion.1-.5` report after the option records its durable
  family report flag. Never call it from the evaluator, a blocked/failed option,
  a daily scan, or a generic event dispatcher.

### Caller contract for the alternate-order branch

`ireland_postwar_alternate_order_resolved` is an explicit external record, not
an automatic fallback. The United Nations admission caller may set it only when
`ireland_un_admission_authority` is false and the world state makes the named
United Nations path invalid. Skipping the mission while a valid United Nations
authority exists must not set the flag. This keeps the foundation trigger
auditable and prevents a date-only shortcut.

## Exceptional route lifecycle helpers

### `ireland_initialize_high_kingship_values`

- Scope: Ireland country effect.
- Purpose: initialises Royal Legitimacy, Royal Obligation Burden, and Household Reach once at the High Kingship gateway.
- Inputs/outputs: no inputs; writes the three canonical values and an initialization flag.
- Defaults and side effects: no-op after initialization; creates no crown, unit, claim, or cosmetic identity.
- Usage: call from the High Kingship evidence gate and `ireland_refresh_exceptional_route_state`.

### `ireland_initialize_five_provinces_values`

- Scope: Ireland country effect.
- Purpose: initialises Federal Cohesion, the provincial mandate ledger, and Middle Balance.
- Inputs/outputs: no inputs; writes the seven ledger variables and an initialization flag.
- Defaults and side effects: no-op after initialization; the Ulster mandate remains zero until a lawful Northern-access flag exists.
- Usage: call from the Five Provinces entry and the shared refresh helper.

### `ireland_refresh_provincial_mandates`

- Scope: Ireland country effect.
- Purpose: clamps provincial values and recognises Ulster only through lawful settlement, convention, cultural delegation, or special status.
- Inputs/outputs: provincial values and lawful-access flags; outputs a clamped ledger and, where lawful, a valid Ulster mandate.
- Defaults and side effects: never derives a mandate from core, claim, occupation, or ownership.
- Usage: call after provincial focus, event, and decision changes.

### `ireland_initialize_otherworld_obligations`

- Scope: Ireland country effect.
- Purpose: initialises the named-obligation count, broken-obligation count, Fian Readiness, and regional compact count.
- Inputs/outputs: no inputs; writes the four values and initialization flag.
- Defaults and side effects: creates no formation, manpower, equipment, or stockpile.
- Usage: call at verified Otherworld entry and via the shared refresh helper.

### `ireland_pay_exceptional_action_cost` / `ireland_pay_exceptional_command_cost`

- Scope: Ireland country effect.
- Purpose: deduct the 15/20/25 political-power and 20/30/40 command-power tiers from a caller-selected pressure anchor.
- Inputs/outputs: temporary `ireland_exceptional_cost_anchor`; deducts the matching resource tier.
- Defaults and side effects: does not change route state or grant a benefit; callers own availability checks.
- Usage: set the action-specific anchor immediately before invoking the payment helper.

### `ireland_commit_exceptional_conclusion`

- Scope: Ireland country effect.
- Purpose: converts completed exceptional terminal focus history into active conclusion flags.
- Inputs/outputs: exceptional completed focuses and the existing final-convergence record; outputs conclusion flags.
- Defaults and side effects: preserves focus, patron, fabrication, and failure history; never grants territory, cores, wars, units, equipment, or recovery.
- Usage: call from terminal focus rewards and the shared refresh helper.

### `ireland_close_exceptional_route_decisions`

- Scope: Ireland country effect.
- Purpose: clears active exceptional missions and temporary due-benefit flags when an exceptional component closes.
- Inputs/outputs: active mission and due flags; removes only stale activation state.
- Defaults and side effects: preserves completed and failure records for AI and convergence review.
- Usage: call on failed convergence, explicit component separation, or route cleanup.

### `ireland_refresh_exceptional_route_state`

- Scope: Ireland country effect.
- Purpose: the single idempotent refresh for route initialization, mandate legality, conclusion recognition, existing profile/spirit refresh, same-slot exceptional forms, and cosmetic identity.
- Inputs/outputs: route values, flags, and focus history; outputs clamped values, conclusion flags, a valid three-spirit trio, and any materially distinct cosmetic identity.
- Defaults and side effects: no global on-action, core, state, war, unit, stockpile, or resource effect.
- Usage: call after every exceptional focus, action, event option, and mission outcome.
