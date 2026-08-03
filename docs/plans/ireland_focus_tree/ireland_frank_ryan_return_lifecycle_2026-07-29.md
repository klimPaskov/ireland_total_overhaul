# Ireland Frank Ryan return lifecycle

Feature slug: `ireland_focus_tree`
Namespace: `slopx`
Date: 2026-07-29

## Outcome

Frank Ryan is no longer recruited when the civil IRA route is selected. His
character becomes available to an accountable civil IRA or plural Congress
government only after the required durable records exist:

1. survival confirmed after Russell's August 1940 return voyage;
2. an Irish-controlled return and independent health review completed;
3. Axis tutelage publicly broken;
4. political recovery accepted by the civil republican authorities.

The lifecycle extends P11 IRA Leadership Crisis from three to six nodes without
creating a nineteenth crisis family. Events .434-.436 are part of P11 and use
the existing Army Council report/news art. The source inventory is now 493
top-level Ireland event definitions, including the unchanged exact 236 flavour
events.

## Admission and consequences

The survival inquiry requires either the civil IRA profile with Authority
Before Arms or the plural Congress profile after the Plural Republic,
completion of the original P11 nodes, and a window after August 1940 but before
June 1944. The inquiry therefore opens only once the fatal voyage is in the
record and closes before Ryan's historical death. Confirming survival records
German custody and adds 4 Foreign Exposure plus 4 German Leverage. Refusal
permanently closes Ryan's lifecycle.

Return requires Intelligence Readiness 35, Neutrality Integrity 50, 35
Political Power, and either a valid German custodian or a peaceful recorded end
to the major war. An accepted return spends the Political Power, adds 8 Foreign
Exposure and 8 German Leverage, and reduces Neutrality Integrity by 5. Refusal
records coalition rejection and closes the lifecycle.

Political recovery requires Social Consent 50, the relevant Civil Republican
Authority or Congress Coalition Cohesion at 55, a completed health review, and
no sponsor-dependence or permanent-foreign-veto failure. Publicly breaking Axis
tutelage adds 5 Foreign Exposure, removes 12 German Leverage, and restores 5
Social Consent and 5 Neutrality Integrity. A private undertaking closes the
chain without making Ryan available.

None of these outcomes grants industry, equipment, units, fuel, shipping,
supply, administration, alignment, an office, foreign recognition, territory,
a claim, or a core. The successful final event recruits no character directly;
the ordinary route lifecycle rechecks the survival, return, health, Axis-break,
and political-recovery records and recruits Ryan on the next valid sync. Army
Council control, Congress vanguard control, route closure, archival, or cleanup
retires him.

## Historical boundary

The chain follows the canonical research record: Russell died during the 1940
submarine return voyage, Ryan returned to German custody, and any alternate
Irish role therefore requires survival, release, an independent return, and a
public political break with German control. The first P11 event description now
correctly identifies Seán Russell rather than attributing Russell's absence to
Ryan.

## Art and source clearance

No generated or sourced image was added. Runtime event art remains under
`gfx/`, and the Frank Ryan portrait remains the existing P-43 source-backed
consumer. Its `needs_user_review`/C3-with-conditions manifest status is
unchanged and remains a separate completion blocker; this lifecycle does not
promote or replace that portrait. Exact source portrait files remain preserved
under `docs/portraits/`.

## Files

- `common/script_constants/slopx_ireland_constants.txt`
- `common/scripted_triggers/slopx_ireland_triggers.txt`
- `common/scripted_effects/slopx_ireland_runtime.txt`
- `events/slopx_ireland_events.txt`
- `localisation/english/slopx_ireland_l_english.yml`
- `docs/slopx_dynamic_effects.md`

## Validation boundary

Static checks cover unique event IDs, all event localisation references,
dispatcher and event use of the same three gates, the four-record recruit
condition plus health review, route cleanup, constants, H/P/A route
restriction, event counts, and
the unchanged 236 flavour-event floor. HOI4 launch and live playthrough testing
are excluded from the goal by user direction.

A bounded read-only `hoi4.event_inspect` refresh against
`mod_ireland_total_overhaul_65a6b5f140a7` found no blocking diagnostic for event .434. Its
aggregate validation remains partial because the large-workspace event-only
catalogue loads zero scripted helpers and defers workspace-wide lifecycle
projection; the static definition/call comparison above is therefore the
helper-resolution evidence.
