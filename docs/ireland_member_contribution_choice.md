# Regional Member Contribution Choice

## Purpose

The Regional Order's `Integrate a Voluntary Member Contribution` action opens a single player/AI selection event. It accepts exactly one concrete contribution under the already-ratified command and sovereignty safeguards, then starts the existing 180-day `Meet the Member Contribution Schedule` mission.

The choice is a paid commitment, not a passive political-power store and not a unit-spawning shortcut. No effect creates, moves, equips, or transfers a division. The action's ordinary political-power and command-power surcharge remains the admission cost; the selected class adds its own physical or ledger input.

## Runtime sequence

1. The action checks the regional charter, defined military contribution, sovereignty safeguards, a real contribution force, the Dublin/Munster map prerequisites, mission capacity, and a class-specific entry reserve for the current Northern Integration Capacity scarcity band.
2. The action pays its named Political Power and Command Power cost, opens event `ireland_events.431`, and activates the existing 180-day mission.
3. The event accepts one of five payloads:
   - troops: 750 manpower, 100 Infantry Equipment, and 20 Support Equipment;
   - ships: 5 Convoys, 250 manpower, and 250 fuel;
   - finance: 30 Political Power after the action cost;
   - intelligence: 10 Command Power and 5 Intelligence Readiness after the action cost;
   - infrastructure: 5 Trains and 5 Trucks.
4. The selected class is stored as an ephemeral class flag while the mission is active. Class-specific scripted triggers evaluate live Readiness, Provision, Dáil mandate, Social Consent, and named state-building conditions for full and partial success.
5. Mission completion, timeout, cancellation, pause, and route cleanup clear the active class. Successful or cancelled runs retain a class history flag so compliance audits can distinguish what was actually offered.
6. Cancellation refunds only the selected payload's recoverable fraction. Finance has no refund because the political-power commitment is spent; intelligence returns the defined command/readiness fraction; physical classes return their 70%-capped inputs through the shared refund helper.

## Script surfaces

- Decision and mission: `common/decisions/ireland_decisions.txt`
- Admission, payload, and result triggers: `common/scripted_triggers/ireland_triggers.txt`
- Payload effects, class history, cleanup, and refunds: `common/scripted_effects/ireland_effects.txt`
- Mission ledger evaluation: `common/scripted_effects/ireland_runtime.txt`
- Selection event: `events/ireland_member_contribution_events.txt`, event `ireland_events.431`
- Tuning: `common/script_constants/ireland_constants.txt`
- Player-facing text: `localisation/english/ireland_l_english.yml`

## Asset and UI contract

No new visual asset is required. The action continues to use `GFX_decision_ireland_integrate_a_voluntary_member_contribution` and the mission continues to use `GFX_mission_ireland_meet_the_member_contribution_schedule`, both registered in `interface/ireland_icons.gfx`. The selection event uses the existing symbolic regional-works report image `GFX_report_event_ireland_report_flavour_federal_works`; it does not introduce a new event-image budget row. Any future class-specific GUI treatment must register new sprites in `interface/` and promote final DDS files to the standard mod `gfx/` tree, with `assets/` used only as temporary staging.

## Future depth

Future expansion can add a second member's separately negotiated schedule only if it receives its own mapped mission family, cap accounting, cancellation code, and cleanup proof. It must not turn this action into a free repeating contribution loop or bypass the command, sovereignty, Northern, or route-review gates.
