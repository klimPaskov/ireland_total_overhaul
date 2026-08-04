# Ireland route-voice localisation tranche — 2026-07-25

## Scope

This tranche replaces repeated main-event copy with route-specific prose and
choices. The text names the actual institutional dispute, keeps relevant live
ledger values in the description where they matter, and makes the two options
express different political commitments rather than generic
measured-versus-delayed language.

## Updated event families

- `constitution_cabinet_draft`
- `constitution_public_consultation`
- `constitution_plebiscite_and_election`
- `constitution_commencement`
- `belfast_dockside_warning`
- `belfast_easter_tuesday_raid`
- `belfast_relief_request`
- `belfast_reconstruction_memory`

The tranche was then extended across the remaining standard event surface:

- the 1937 presidency, 1938 trade, emergency, republic, United Nations,
  church, health, censorship, and postwar institutional families;
- compulsory tillage, rationing, shipping, reconstruction, and trade families;
- Coastwatch, mobilisation, internment, intelligence, Blacksod, command,
  aircraft, airspace, camp, agent, weather, and access families;
- IRA, Republican Congress, O'Duffy, Ailtirí, clerical, High Kingship, Five
  Provinces, and Otherworld crises; and
- Northern border, representation, labour, policing, finance, war-plan,
  occupation, disarmament, provisional-authority, rights, integration, core
  review, federal, unitary, labour, and postwar families.

The verified source-level result is 220 unique standard event descriptions and
217 unique standard `a`/`b` option strings in
`ireland_events`, with all 236 flavour-event descriptions also unique.

The changes are localisation-only. They do not alter event IDs, option keys,
effects, route gates, Northern control, occupation, settlement, integration,
or core eligibility. The prose uses existing dynamic values for the National
Settlement, Social Consent, National Provision, National Readiness, Neutrality
Integrity, Northern integration capacity, Northern security stability, and
British flexibility.

## Remaining localisation gate

The event-surface repetition finding and the repeated action-description
template tails are closed at source level. All 140 action descriptions remain
distinct and now name their route-specific burden, safeguard, incident,
foreign-channel, constitutional, or review commitment; the mission
descriptions still need an objective-by-objective review against the 54
canonical mission families. Local engine/reference checks remain unavailable
because the user asked that HOI4 not be launched.
