# National Question and territorial campaign implementation tranche

Status: implemented and validated on 2026-08-14.

## Player-facing campaign

The territorial programme now enters the focus tree through a visible preparation chain rather than appearing as a detached late branch:

1. `ireland_unfinished_national_question`
2. `ireland_border_and_atlantic_dossier`
3. `ireland_test_the_state_instruments`
4. `ireland_define_the_national_question`
5. `ireland_authorise_reunification_instruments`

The three preparation cards grant direct Army and Navy experience, Command Power, a named Border Atlas operation, and a Support Technology bonus. The five political families then select distinct Northern methods before entering their route-specific Atlantic policy.

The territorial lane was compacted into a single readable campaign fan. It preserves the three opening focus trunks and does not add a fourth opening branch.

## Active operations

- The Border Atlas consumes Political Power and Command Power over 35 days, then grants Army and Navy experience and improves the named Northern ledgers.
- The democratic method unlocks the existing material supervised-plebiscite mission. The duplicate low-cost plebiscite launcher was removed.
- Ulster, Highlands, Wales, and Cornwall coercive operations consume the centralized enforcement reserve only after their live completion gates pass: 1,000 manpower, 200 infantry equipment, 20 support equipment, 5 convoys, 250 fuel, and 10 Command Power.
- Wales and Cornwall use distinct accept, military-access counteroffer, refusal, stale-target, cooldown, and cleanup event paths. A claim and 180-day war goal are created only after refusal or Ireland's rejection of a counteroffer.
- Route cleanup clears all Wales and Cornwall pending response flags and the shared saved targets.
- The Atlantic conclusion requires the rights, protectorate, and integration doctrine focuses as separate prerequisites, in addition to the per-holding resolution trigger.

## AI and presentation

- Historical and route-reactive focus plans include the three National Question preparation cards.
- The O'Duffy family and personal-command plans no longer abort on 29 November 1944; they remain active until route cleanup.
- Three distinct generated focus icons and their shine registrations are wired.
- Wales and Cornwall use distinct generated 210x176 report images. Their sources, processed PNGs, DDS files, prompt records, manifest entries, contact sheets, and GFX handoff live under `docs/assets/ireland_territorial_diplomacy/` and `gfx/event_pictures/ireland_territorial_diplomacy/`.

## Validation evidence

- Focus inspection revision `832e9024b0a74bdf`: 218 focuses, 226 connectors, zero crossings, zero connector-through-node cases, zero long connectors, and zero same-row spacing defects. The three new focus sprites, titles, and descriptions resolve. The only Ireland advisory is the pre-existing concealed clerical bridge detour.
- The territorial namespace defines 24 unique top-level events. Every numeric decision reference resolves to a defined event.
- All 112 title, description, option, and custom-effect localisation references used by the territorial event file resolve.
- All seven territorial report-picture references resolve to registered sprites and existing DDS files.

## Remaining country-package tranches

This tranche does not close the larger country-package specification. The next implementation work is the industrial contract input pass, route-specific failure/recovery and late-game conclusions, public-family navigation/reward depth, and AI decision utility. The improvement loop is intentionally deferred until those meaningful implementation tranches are present.
