# Ireland Foreign Procurement Authority Tranche

Feature slug: `ireland_focus_tree`

Date: 2026-07-26

Status: source-level partial implementation; live foreign-reaction and mission evidence remain open

## Purpose

The foreign procurement family now distinguishes an open diplomatic channel from an actionable agreement. The canonical rows require a named shortage, shipping, credit, legal safeguards, an active German promise, or a named humanitarian case depending on the source. The previous source selector and four delivery objectives could rely mainly on channel/partner flags and map buildings.

This tranche does not change the 13 decision categories, 140 actions, 54 missions, or 216 focuses. It does not create aid, equipment, factories, convoys, credit, access, territory, cores, subjects, recognition, alignment, offices, or political power.

## Canonical rows

The implementation follows the foreign leverage and mission rows in:

- `docs/specs/ireland_focus_tree/maps/ireland_focus_tree_decision_and_mission_map.md`
- `docs/specs/ireland_focus_tree/ireland_focus_tree_spec_part_5_decisions_events_and_lifecycles.md` (foreign leverage table)
- `docs/specs/ireland_focus_tree/ireland_focus_tree_spec_part_4_statecraft_and_war.md` (foreign procurement, safeguards, and dependency sections)

The four source contracts are:

- British: a current named Provision shortage, British trade channel/partner, finance or rural-credit basis, and bounded sovereignty/access safeguards.
- American: an American channel/partner, an external-creditor route, finance/rural-credit/domestic-manufacturing basis, and Foreign Access law or sovereignty/access safeguards.
- German: a valid German channel/partner, a completed Receive a German Emissary promise, and sovereignty safeguards or Security Under Law before a delivery proof can be demanded.
- Vatican: a valid Vatican channel/partner plus war, an active neutrality incident, diaspora relief, Church-service dependency, or the postwar foreign review as a named humanitarian/isolation cause.

## Source changes

### Reusable trigger contracts

`common/scripted_triggers/ireland_triggers.txt` adds:

- `ireland_has_named_provision_shortage`
- `ireland_british_supply_contract_authority`
- `ireland_american_procurement_authority`
- `ireland_german_delivery_authority`
- `ireland_vatican_relief_authority`

The contracts are documented in `docs/ireland_dynamic_effects.md`. All are side-effect-free proof triggers. They do not treat dates, leverage values, generic reaction windows, or channel flags as cargo, credit, legal authority, a German promise, or a humanitarian case.

### Decisions

`common/decisions/ireland_decisions.txt` applies the source contracts to:

- Renegotiate a British Supply Contract.
- Send an American Procurement Mission.
- Demand Proof of German Delivery.
- Seek Vatican Humanitarian Mediation.
- The British, American, and German branches of Procure Rifles and Support Equipment.

The existing dynamic Political Power/Command Power, convoy, factory, leverage, exposure, route, law, office, category-capacity, mission-capacity, and cancellation/refund behavior remains in place.

### Missions and map objectives

The four map-objective triggers now recheck the active mission, source record, channel/partner, and source-specific authority. British and American objectives recheck the finance/credit and legal safeguards; German rechecks the prior emissary promise and independence boundary; Vatican rechecks a durable humanitarian-case record. The mission deadlines, full/partial/failure/escalation results, source leverage, and cleanup remain separate.

The Vatican action writes `ireland_vatican_humanitarian_case_recorded` as a durable case-history flag before mission resolution. It is evidence of the accepted case, not a free relief result or an ongoing temporary delegation.

## Localisation

`localisation/english/ireland_l_english.yml` now exposes the source-specific admission differences, current Provision component values for the British shortage preview, and the live mission/source/safeguard requirements for each map objective. The text keeps channel availability distinct from an actionable contract.

## Validation boundary

- Static references confirm the five new helpers are defined and used by the intended source selector, dedicated actions, and four map objectives.
- The canonical counts remain 216 focuses, 13 categories, 140 actions, and 54 missions.
- Localisation remains UTF-8 with BOM after the edit.
- HOI4 was not launched, per the user's instruction. Live channel invalidation, credit/debt behavior, foreign reaction choices, mission completion, delivery materialization, AI queue behavior, and cleanup scenarios remain not-run.

## Remaining boundary

This tranche does not close Treaty Port/neutral-approach depth, the broader 140-action material/safeguard map, source-clearance decisions, or the completion audit's live engine/reference and 22-scenario programme. The overall Ireland overhaul remains incomplete.
