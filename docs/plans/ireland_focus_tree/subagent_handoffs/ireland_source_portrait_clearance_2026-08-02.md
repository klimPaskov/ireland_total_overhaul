# Ireland sourced portrait clearance handoff — 2026-08-02

## Scope and result

This handoff covers only P-15, P-16, P-24, P-26, P-31, P-32, P-38, P-39, P-41, P-45, P-48, P-50, P-54, P-55, and P-57. All 15 rows have concrete repo-local provenance/evidence and are still explicitly `blocked`; none reached C3/C4. No final DDS was created and no gameplay, GFX wiring, or unrelated asset was edited.

Primary package:

`assets/ireland_focus_tree/sourced/research_2026-08-02/sixth_clearance_portraits/`

The package manifest is `provenance_manifest.json`; per-item notes are under `evidence/`; review derivatives are under `processed_png_review/`; the visual review sheet is `contact_sheet_review.png`; and the sprite-surface note is `gfx_handoff.md`.

## Row handoff

| ID | Source tier / clearance | Concrete local source or evidence | Processed review | Blocker / next action |
|---|---|---|---|---|
| P-15 John Leydon | 9 / C2 | `source_originals/P-15_john_leydon_1979_wikipedia.png`; DIFP pages | `processed_png_review/P-15_john_leydon_review_156x210.png` | 1979, non-free, unknown photographer/rights. Do not ship without permission and era approval. |
| P-16 Thekla Beere | 8 / C2 | `source_originals/P-16_thekla_beere_irishexaminer_department_of_justice.jpg` | `processed_png_review/P-16_thekla_beere_review_156x210.png` | Exact candidate but date, photographer, image rights, and permission unresolved. |
| P-24 Luke Duffy | 9 / C2 | `source_originals/P-24_luke_duffy_corran_herald_home_farm_c1920s.jpg`; full PDF/rendered pages retained | `processed_png_review/P-24_luke_duffy_review_156x210.png` | Best new candidate: captioned circa-1920s exact-person image. Need image-level archive/rights confirmation. |
| P-26 Patrick Cogan | 9 / C1 | `source_originals/P-26_patrick_cogan_history_ireland_group_photo.png` | none | Group members are not labelled at portrait level; no defensible crop. |
| P-31 Michael Browne | 5 / C2 | `source_originals/P-31_michael_browne_1973_galway_library_connacht_tribune.jpg` | `processed_png_review/P-31_michael_browne_review_156x210.png` | Exact 1973 candidate; late and rights chain unresolved. |
| P-32 Alfred O’Rahilly | 4 / C2 | `source_originals/P-32_alfred_orahilly_ucc_portrait007.jpg` | `processed_png_review/P-32_alfred_orahilly_review_156x210.png` | UCC `UCCHS.Portrait007`, 1949, © UCC; written permission required. |
| P-38 Stephen Hayes | 8 / C2 | `source_originals/P-38_stephen_hayes_erenow_topfoto_image008.jpg` | `processed_png_review/P-38_stephen_hayes_review_156x210.png` | Captioned left subject; two-person scene, © Topfoto, date/permission unresolved. |
| P-39 Hugh McAteer | 11 / C2 | `source_originals/P-39_hugh_mcateer_ruc_reward_poster.jpg` | `processed_png_review/P-39_hugh_mcateer_review_156x210.png` | Excellent 18 Jan 1943 labelled poster panel; underlying scan/photo rights unresolved. |
| P-41 Harry White | 1 / C2 | `source_originals/P-41_harry_white_military_archives_H04_01.jpg`; H04_02 context | `processed_png_review/P-41_harry_white_review_156x210.png` | Official archive candidate; date not stated and Military Archives permission required. |
| P-45 Mick Fitzpatrick | 1 requested route / C1 evidence | `source_pages/P-45_mick_fitzpatrick_wikipedia_identity.html`; wrong-person Oireachtas page retained | none | No exact portrait found. Do not use the later Michael Fitzpatrick avatar. |
| P-48 Roddy Connolly | 8 / C2 | `source_originals/P-48_roddy_connolly_wikipedia_1966.jpg`; RTÉ and Military Archives pages | `processed_png_review/P-48_roddy_connolly_review_156x210.png` | RTÉ item 94D00030, 1966, Rights Reserved / Free Access; permission required and late. |
| P-50 Michael “Mick” Price | 4 / C1 evidence | `source_originals/P-50_LOC_Indianapolis_Times_1932-11-23_page_2_0533.jp2` + ALTO | none | LOC page supports period identity context but contains no Price portrait. |
| P-54 P. J. Coughlan | 1 / C1 | `source_pages/P-54_P-55_nli_eoin_oduffy_papers.html` | none | NLI Eoin O’Duffy Papers references exact identity circa 1936, but no portrait object. |
| P-55 Liam D. Walsh | 1 / C1 | `source_pages/P-54_P-55_nli_eoin_oduffy_papers.html` | none | NLI finding aid references papers 1940–43, but no portrait object. |
| P-57 Tomás Ó Dochartaigh | 1 / C2 | `source_originals/P-57_tomas_o_dochartaigh_history_ireland_military_archives.jpg` | `processed_png_review/P-57_tomas_o_dochartaigh_review_156x210.png` | Exact Military Archives-attributed 1944-context halftone; permission/resolution unresolved. |

## Source and rights notes

- `P-24` is a concrete historical image candidate, but the scan’s 2020/21 publication does not give a reusable image licence. The single-person caption does not carry the adjacent group image’s separate Drapers Assistant Mandate Archive credit.
- `P-32` is an exact university-collection portrait, but UCC’s © notice prevents treating the local copy as cleared.
- `P-41` and `P-57` have official Military Archives provenance routes; archive attribution is not an open licence. The local package records the archive media/reproduction page and the permission blocker.
- `P-48` has a stronger exact still than the prior group photograph, but RTÉ’s Rights Reserved / Free Access wording is not permission to redistribute the still.
- `P-45`, `P-50`, `P-54`, and `P-55` are identity/provenance-only rows in this pass. No portrait stand-in was generated or selected.

## Main-agent wiring handoff

Proposed sprite tokens remain the canonical manifest names `ireland_portrait_p_15` through `ireland_portrait_p_57` for the assigned IDs. Suggested GFX surface is `interface/slopx_ireland_sourced_assets.gfx`, with final files intended for `gfx/leaders/ireland/` only after a row is cleared. `gfx_handoff.md` contains the complete no-DDS table. Do not wire any review PNG or source image into runtime.

## Completion state

The bounded research package is complete as a clearance handoff: 15/15 rows have source tier, clearance state, provenance/licence note, era-fit note, uncertainty, and repo-local source/evidence. The requested runtime portrait asset goal remains blocked for all 15 until rights/identity/source gaps are resolved.
