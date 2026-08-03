# Ireland P-50 exact source re-audit — 2026-08-02

Feature slug: `ireland_focus_tree`  
Namespace: `slopx`  
Scope: non-live source, asset, preservation, and registration checks only.

## Result

P-50 Michael (Mick) Price is complete as a `C3 cleared with conditions`
source-backed portrait. The exact source object is the 21 August 1921 Tom
Barry and Leslie Price wedding group photograph, authored by Keogh Brothers
Ltd and linked to National Library of Ireland object `vtls000812410`.

Cork City Council's Archdeacon Thomas Duggan biography publishes the second
standing-row mapping and places Mick Price sixth. The Crumlin & Walkinstown
History Group independently repeats that row sequence. The promoted crop is
the recorded source rectangle `[x=1270, y=600, width=100, height=135]`; it is
resized to 156 × 210 RGB without generating or reconstructing a face.

## Reconciled paths

| Surface | Path | Result |
| --- | --- | --- |
| Source original | `assets/ireland_focus_tree/sourced/research_2026-08-02/portrait_exact_object_search_round13/P-50_michael_price/source_originals/Tom_Barry_and_Leslie_Price_wedding_photo_August_1921.jpg` | exists; byte hash matches manifest |
| Crop locator | `assets/ireland_focus_tree/sourced/research_2026-08-02/portrait_exact_object_search_round13/P-50_michael_price/evidence/mick_price_face_mapping_crop_locator.png` | exists; rectangle retained |
| Processed PNG | `assets/ireland_focus_tree/sourced/research_2026-08-02/portrait_exact_object_search_round13/P-50_michael_price/processed_png/leader_p_50_mick_price_156x210.png` | exists; 156 × 210 RGB; byte hash matches manifest |
| Preserved source | `docs/portraits/research_2026-08-02/portrait_exact_object_search_round13/P-50_michael_price/Tom_Barry_and_Leslie_Price_wedding_photo_August_1921.jpg` | exists; byte-identical to staged source |
| Preserved processed portrait | `docs/portraits/research_2026-08-02/portrait_exact_object_search_round13/P-50_michael_price/leader_p_50_mick_price_156x210.png` | exists; byte-identical to staged processed PNG |
| Runtime DDS | `gfx/leaders/ireland/leader_p_50.dds` | exists; 156 × 210 BGRA DDS; hash matches manifest |
| GFX registration | `interface/slopx_ireland_sourced_assets.gfx` | `GFX_ireland_portrait_p_50` points to `gfx/leaders/ireland/leader_p_50.dds` |

The complete manifest count is now 165/169, with four exact portrait rows
remaining blocked: P-26, P-45, P-54, and P-55. No generated likeness,
generic avatar, wrong-person image, or fallback was introduced for those rows.

## Rights boundary

The Wikimedia Commons source page records the photograph as public domain in
the United States and Ireland and links the NLI object. The mod retains the
project's C3 local-mod boundary rather than treating this external assessment
as C4 or unrestricted redistribution. Required credits are Keogh Brothers
Ltd, National Library of Ireland object `vtls000812410`, Wikimedia Commons,
and the civic face-mapping references.

References:

- <https://commons.wikimedia.org/wiki/File:Tom_Barry_and_Leslie_Price_wedding_photo,_August_1921_(cropped).jpg>
- <https://catalogue.nli.ie/Record/vtls000812410>
- <https://www.corkcity.ie/en/cork-public-museum/exhibitions/people-of-cork/archdeacon-thomas-duggan/>
- <https://www.crumlinwalkinstownhistory.ie/person/una-nolan/>

HOI4 was not launched; live gameplay testing remains outside this goal gate.
