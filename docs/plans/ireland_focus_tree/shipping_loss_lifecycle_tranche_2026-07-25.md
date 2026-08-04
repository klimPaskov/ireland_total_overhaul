# Neutral shipping loss lifecycle tranche — 2026-07-25

## Scope

This tranche corrects the source-to-action lifecycle for `Investigate a Neutral Shipping Loss` and its `Investigate a Merchant Sinking` mission. It is a bounded gameplay correction, not a completion claim for the Ireland package.

## Canonical mismatch corrected

The action was using the foreign-access law and access-incident family even though the canonical decision and mission map defines it around an Irish or chartered vessel that has been damaged or sunk. That allowed the action to appear for an unrelated access request and did not require the Marine Service or intelligence capacity named by the map.

The action now requires:

- `ireland_shipping_incident_active` and `ireland_law_trade_shipping_active`;
- Marine Service and Intelligence readiness above the shared value-5 investigation floor;
- full control of state 135, an industrial complex in state 135, and a naval base in state 113;
- the existing neutrality category capacity, dynamic Political Power/Command Power cost, and launchable named mission gates.

The mission map objective uses the same readiness floor and named building proof, so the action cannot commit to a mission whose required maritime and intelligence capacity is absent. No territory, core, equipment, unit, recognition, or political-power store is granted by this correction.

The linked `Mark and Publicise Neutral Shipping` action now also requires an existing Irish, chartered, purchased, or renewed merchant route. Its equal-rules mission cannot be used as a route-creation shortcut.

## Localisation and audit surface

The action descriptions, requirements tooltips, and map-objective tooltip now expose the active shipping incident, trade/shipping law, Marine Service and Intelligence readiness, the named Munster/Leinster proof, and the merchant-route prerequisite. The source-of-truth map and project status record the tranche as partial until live incident, mission, failure, escalation, reaction, and cleanup scenarios are run.

## Remaining risk

This source-only pass does not prove the live dispatch of source events 226–231, the timing of the shipping law transition, the foreign-reaction response after a result, or timeout cleanup in the engine. Those remain explicit validation blockers.
