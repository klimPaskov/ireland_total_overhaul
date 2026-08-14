# Ireland political-family lane reflow completion — 2026-08-14

## Result

The five public family gateways and their substantive programmes now form five straight, parallel lanes beneath the established political tree. Focus IDs, rewards, availability requirements, family locks, AI, icons, localisation, and the three opening trunks are unchanged. Four redundant visible prerequisite connectors were removed because their exact former conditions remain in each gateway's `available` block and the National Settlement reveal flag remains authoritative.

The five commitment gateways share row `y = 14`:

- democratic `ireland_republican_government` at `(-24,14)`;
- communist `ireland_congress_reform_bridge` at `(-18,14)`;
- oligarchic `ireland_vocational_constitution` at `(-12,14)`;
- fascist `ireland_oduffy_network_revival` at `(-6,14)`; and
- restoration `ireland_high_king_evidence_gate` at `(0,14)`.

Their aligned programme roots on row `y = 18` are `ireland_republican_ministries`, `ireland_vanguard_organisers`, `ireland_creditor_cabinet`, `ireland_veterans_command_council`, and `ireland_claimants_convention` at the same family x positions. Descendants occupy rows 15–22 within the matching lane. Each family remains hidden until its existing reveal and family flags allow it, so the tree still exposes only three opening trunks.

## Layout evidence

Fresh focus inspection revision `97013150a7474f29` reports:

- 218 focuses and 222 connectors;
- bounds x = -26..21 and y = 0..22, reduced from the pre-reflow x = -42..21;
- zero connector crossings;
- zero connector-through-node intersections;
- zero long connectors;
- zero duplicate coordinates or visible overlaps;
- zero same-row spacing defects, with minimum spacing 2;
- maximum horizontal connector span 6 and maximum vertical span 2.

Inspection artifact:

`hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/cef93413019260f758c5bd8c1d6cd3ba02f4105da571f2ecf98b759c39ce3e00/ff8b072165eb89950c5dcac511e230c7e1ee962b90a7b2a985ec6e815fd8eb5a/focus-inspect.97013150a7474f29.json`

The inspector retains nonblocking detour/staircase advisories in the concealed clerical and Otherworld corridors. Straightening those corridors introduces crossings in the shared evidence area; the zero-crossing authored geometry is retained. The other reported localisation warning belongs to vanilla `continuous_restrict_freedom`.

## Filter and reward-contract closure

The same pass removed 20 unsupported Industry filters, two unsupported Annexation filters, and one unsupported political-character filter. Army, Navy, Air, and Research filters continue to correspond to direct matching effects.

`ireland_settlement_under_law`, `ireland_all_island_workers_republic`, `ireland_belfast_compact`, `ireland_restore_ulsters_place`, and `ireland_atlantic_ambition` are accepted settlement/policy capability handoffs: their durable flags are consumed by the named territorial decisions, event chains, and postwar review rather than being paired with arbitrary free equipment.

## Files changed

- `common/national_focus/ireland_focus_tree.txt` — authored gateway/profile/programme coordinates, four redundant visual prerequisites, and strict filter corrections.
- This handoff and the corrective closure in `final_focus_audit_2026-08-14.md`.

No fallback focus, missing route, reward simplification, or asset substitution was used.
