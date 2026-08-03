# Ireland user-approved conditional asset re-audit - 2026-08-02

Feature slug: `ireland_focus_tree`
Namespace: `slopx`

This is the non-live audit for the exact source packages promoted under the
user's 2026-08-02 instruction and the subsequent round-13 and round-14 exact
portrait promotions. It covers the manifest, source and processed
files, final runtime DDS files, SHA-256 reconciliation, processed target
dimensions, and source-side GFX registration. It preserves the distinction
between C3 conditional local-mod use and C4 unrestricted project use.

## Manifest result

The authoritative `assets/source_manifest.json` contains 169 entries:

| Family | Complete | Blocked | Review |
| --- | ---: | ---: | ---: |
| Portrait | 57 | 3 | 0 |
| Symbol/document | 40 | 0 | 0 |
| Event/news | 69 | 0 | 0 |
| Total | 166 | 3 | 0 |

Clearance totals are C1: 3, C2: 0, C3: 135, and C4: 31. The 32-row
`user_approved_conditional_2026-08-02` tranche contains ten portraits, seven
symbol/document packages, and fifteen event/news packages. The ten promoted
portrait originals are preserved under
`docs/portraits/research_2026-08-02/user_approved_conditional/source_originals/`.
Round 13 additionally promotes P-50 from an exact, face-mapped 1921 group
photograph, and round 14 promotes P-54 from an exact, caption-mapped 1936 Irish
Brigade group photograph. Their source originals and processed portraits are preserved under
`docs/portraits/research_2026-08-02/portrait_exact_object_search_round13/P-50_michael_price/`
and `docs/portraits/research_2026-08-02/portrait_exact_object_search_round14/P-54_pj_coughlan/`.

## Static checks

- Every complete row has an existing source object, processed PNG, and final
  runtime DDS at its manifest path.
- SHA-256 values for every complete source, processed, and final file match
  the manifest. Hash comparison is case-insensitive because one legacy row
  stores its digest in uppercase.
- Every processed PNG matches the numeric dimensions encoded in its manifest
  `target_size`; the two historical review-only strings retain their explicit
  `review only` suffix. The manifest's
  `dimensions` field is retained source/crop documentation where applicable;
  it is not used as the processed-output assertion.
- `interface/slopx_ireland_sourced_assets.gfx` contains 170 texture references,
  with zero missing files, zero complete rows left unregistered, and no
  runtime texture path under `assets/`.
- `gfx/event_pictures/ireland` contains 121 DDS files: the 69 complete
  sourced event/news rows, the separately manifested S-03 presidential-seal
  crop, and the generated event-picture package.
- `audit_runtime_icon_surfaces.py` reports all ten required icon surfaces
  complete, including focus goals and law stages.

## Remaining exact-source blockers

Three portrait rows remain blocked because the exact person-labelled image
object required by the canonical roster has not been located:

| Row | Person | Reason it remains blocked |
| --- | --- | --- |
| P-26 | Patrick Cogan | The retained source is an unidentified group photograph; selecting a face would be guesswork. |
| P-45 | Mick Fitzpatrick | Identity and context are confirmed, but no individually identified portrait object was located. |
| P-55 | Liam D. Walsh | The NLI papers/context source provides no portrait object. |

P-50 and P-54 are now complete from the exact mapped source objects documented in
`assets/source_research_handoffs/portrait_exact_object_search_round13_2026-08-02.md`
and `assets/source_research_handoffs/portrait_exact_object_search_round14_2026-08-02.md`.
No wrong-person image, generic avatar, generated likeness, or other substitute
was promoted for the three remaining rows. Live HOI4 launch, in-game
testing, fresh saves, and scenario playthroughs are intentionally excluded by
the user's instruction.
