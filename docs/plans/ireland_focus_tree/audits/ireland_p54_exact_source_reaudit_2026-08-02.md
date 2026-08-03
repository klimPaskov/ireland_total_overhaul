# Ireland P-54 exact-source portrait re-audit — 2026-08-02

Feature slug: `ireland_focus_tree`  
Namespace: `slopx`  
Boundary: non-live source, preservation, manifest, runtime-GFX, and hash audit; HOI4 was not launched.

## Source decision

P-54 is complete from the exact historical source reproduced on [Reading the Signs, “Taking Sides”](https://readingthesigns.weebly.com/blog/taking-sides). The page caption explicitly identifies “Col. P. J. Coughlan, Ballineen” as the second person in the middle row of the Southern Irish Brigade group photograph. The page footer declares its photographs and text CC BY-SA 4.0. The source is a reproduction photograph of a historical group photograph; that limitation and attribution remain in the manifest.

No generated likeness, face reconstruction, wrong-person image, generic avatar, or fallback was used.

## Reconciled paths

| Surface | Path or identifier | Result |
| --- | --- | --- |
| Staging source | `assets/ireland_focus_tree/sourced/research_2026-08-02/portrait_exact_object_search_round14/P-54_pj_coughlan/source_originals/irish_brigade_group_photo_reading_the_signs.jpg` | present; 1066x800 source |
| Crop locator | `assets/ireland_focus_tree/sourced/research_2026-08-02/portrait_exact_object_search_round14/P-54_pj_coughlan/evidence/pj_coughlan_face_mapping_crop_locator.png` | present; box `[350,205,495,405]` |
| Processed source derivative | `assets/ireland_focus_tree/sourced/research_2026-08-02/portrait_exact_object_search_round14/P-54_pj_coughlan/processed_png/leader_p_54_pj_coughlan_156x210.png` | present; RGB 156x210 |
| Preserved archive | `docs/portraits/research_2026-08-02/portrait_exact_object_search_round14/P-54_pj_coughlan/` | source and derivative preserved |
| Runtime | `gfx/leaders/ireland/leader_p_54.dds` | present; manifest hash matches |
| Registration | `GFX_ireland_portrait_p_54` in `interface/slopx_ireland_sourced_assets.gfx` | present; runtime path is under `gfx/` |

The source original and processed derivative have exact-byte matches in the
portrait archive. The canonical manifest reports P-54 as `complete` with
`C3 cleared with conditions`; it records the direct source, attribution, crop
box, hashes, and local-mod-only boundary. The current complete/blocked source
totals are 166/3 overall and 57/3 for portraits.

## References

- [Reading the Signs source page](https://readingthesigns.weebly.com/blog/taking-sides)
- [Creative Commons Attribution-ShareAlike 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
- [Southern Star context for Colonel P. J. Coughlan](https://www.southernstar.ie/news/beal-na-blath-motorbike-recovered-4326367)
- Per-item evidence: `assets/ireland_focus_tree/sourced/research_2026-08-02/portrait_exact_object_search_round14/P-54_pj_coughlan/source_evidence.md`
- Source handoff: `docs/plans/ireland_focus_tree/assets/source_research_handoffs/portrait_exact_object_search_round14_2026-08-02.md`
