# User portrait replacements handoff — 2026-08-14

## Scope and status

Five final stylized DDS portraits supplied by the user were installed as exact `156x210` leader textures. The user-assigned mappings are Maurice Twomey, Éamon de Valera, Seán Lemass, W. T. Cosgrave, and Douglas Hyde. No source, author, archive, license, public-domain, or other external-rights claim is asserted.

Only the three existing advisor cards were regenerated: Maurice Twomey, Seán Lemass, and Douglas Hyde. No advisor card was created for Éamon de Valera or W. T. Cosgrave. An independent asset reviewer approved the five leader portraits and three advisor cards on 2026-08-14.

## Full leader runtime mappings

| Identity | User source | Source SHA256 | Exact runtime DDS |
| --- | --- | --- | --- |
| Maurice Twomey | `C:\Users\klimp\Downloads\thumbnail\source_portrait_3_00004.dds` | `1a28503cc607d1ac15374641ced8c2e2034730bb366344e11f06c2d6dbff0c61` | `gfx/leaders/ireland/leader_maurice_twomey.dds` |
| Éamon de Valera | `C:\Users\klimp\Downloads\thumbnail\batch\dds\portrait_eamon_de_valera_00001.dds` | `fc78bafb845bb8b8800b4956a5189a47a310e65a3c997d15d27978d83eb6d9a7` | `gfx/leaders/ireland/leader_eamon_de_valera.dds` |
| Seán Lemass | `C:\Users\klimp\Downloads\thumbnail\batch\dds\portrait_sean_lemass_1932_00001.dds` | `1e76a698acbf89b04f6cae012e1c4063610f7b886bbbfcf1f954383b34f026ab` | `gfx/leaders/ireland/leader_sean_lemass.dds` |
| W. T. Cosgrave | `C:\Users\klimp\Downloads\thumbnail\batch\dds\portrait_w_t_cosgrave_00001.dds` | `90e8d57a62653ffa5e941d3ee5da6d96fc7a96a579b3733906f47d1bdd7b5959` | `gfx/leaders/ireland/leader_w_t_cosgrave.dds` |
| Douglas Hyde | `C:\Users\klimp\Downloads\thumbnail\batch\dds\portrait_douglas_hyde_1903_00001.dds` | `2f46b1a8e757b2433a0ea0a469bdc0734bfaff26faa21c52fa04e207a57dd48d` | `gfx/leaders/ireland/leader_douglas_hyde.dds` |

The durable exact source copies, decoded processed previews, package manifest, and review sheets are under `docs/assets/ireland_user_portrait_replacements_2026-08-14/`.

## Advisor runtime mappings

| Identity | Sprite | Runtime DDS | Runtime SHA256 |
| --- | --- | --- | --- |
| Maurice Twomey | `GFX_ireland_advisor_maurice_twomey` | `gfx/interface/ideas/ireland/advisors/advisor_maurice_twomey.dds` | `e2f1a3a22f6761e3f35f3fa6d31deba80ae2c14f2056c9ed95d77dd37543a85f` |
| Seán Lemass | `GFX_ireland_advisor_sean_lemass` | `gfx/interface/ideas/ireland/advisors/advisor_sean_lemass.dds` | `4118d824caa5de8fee5b9ea62b68c19eef9f1573d39cdd11d32c417aad45627f` |
| Douglas Hyde | `GFX_ireland_advisor_douglas_hyde` | `gfx/interface/ideas/ireland/advisors/advisor_douglas_hyde.dds` | `ca31b403efe30d7e3c50d5c9df830cbc45b00524659b2dc2c4bc96dc3f4cf463` |

Per-person artifact paths are stable and listed in the updated advisor manifest:

- native previews: `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_{maurice_twomey,sean_lemass,douglas_hyde}.png`
- nearest-neighbour 4x reviews: `docs/plans/ireland_focus_tree/assets/advisors/review_4x/`
- placement studies: `docs/plans/ireland_focus_tree/assets/advisors/placement_studies/`
- 8x alignment overlays: `docs/plans/ireland_focus_tree/assets/advisors/alignment_8x/`
- transform metadata: `docs/plans/ireland_focus_tree/assets/advisors/metadata/`

## Workflow and exact arguments

The cards were generated with the current Chaos Redux tool:

`C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.agents\skills\chaos-redux-event-assets\tools\create_advisor_icon.py`

Canonical template: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.agents\skills\chaos-redux-event-assets\assets\vanilla_reference\portraits\advisors\advisor_template.png` (SHA256 `8f594ef62afba6fdec58de66a80609350dcfe884320b11e6cb6220f1a0e19f58`).

For each identity, the source was the durable exact package copy and the selected transform was:

```text
--portrait-size 30.477406015014285 45.09450833210553
--portrait-offset 0 0
--rotation -4.76
--study-candidate 30.477406015014285 45.09450833210553 0 0 -4.76
--sepia-strength 0.18
```

The measured opening is center `24.76151027919129, 30.645146882359736`, size `30.477406015014285x45.09450833210553`, rotation `-4.76°`; canonical under-frame bleed is `2px` and resampling edge guard is `1px`. Metadata records `source_pre_crop=false`, `frame_clip=true`, `stretch=false`, zero-rotation exception false, and per-person study/alignment outputs.

## Validation evidence

- All five user DDS sources and installed leader textures: exact `156x210` RGBA, legacy one-level BGRA header, `131168` bytes, alpha extrema `[255,255]`; runtime hashes equal their supplied source hashes byte-for-byte.
- All three advisor outputs: native `65x67` cards, valid 32-bit BGRA DDS, one-level length `17548` bytes, decoded pixels equal their generated native previews.
- All three cards: `opening_alpha_gap_pixels=0`, `inner_edge_alpha_gap_pixels=0`, `exterior_alpha_leak_pixels=0`.
- The supported `convert_to_dds.py` was run against each generated native preview to a staging output; each converter DDS was byte-identical to the current `create_advisor_icon.py` runtime DDS.
- Native cards, 4x reviews, placement studies, and 8x overlays were visually inspected by the producer against the dossier-template geometry. This is not independent approval.

## Independent approval

An independent asset reviewer approved the package on 2026-08-14. The review confirmed the five byte-exact leader replacements, identity pairing, stable sprite consumers, and the three advisor cards' face visibility, crop, scale, rotation, dossier geometry, `65x67` DDS round-trip, and zero opening gaps, inner-edge gaps, or exterior alpha leaks. No fallback, generated likeness, alpha flattening, or identity substitution was used.

## Exact changed files

### Runtime textures

- `gfx/leaders/ireland/leader_maurice_twomey.dds`
- `gfx/leaders/ireland/leader_eamon_de_valera.dds`
- `gfx/leaders/ireland/leader_sean_lemass.dds`
- `gfx/leaders/ireland/leader_w_t_cosgrave.dds`
- `gfx/leaders/ireland/leader_douglas_hyde.dds`
- `gfx/interface/ideas/ireland/advisors/advisor_maurice_twomey.dds`
- `gfx/interface/ideas/ireland/advisors/advisor_sean_lemass.dds`
- `gfx/interface/ideas/ireland/advisors/advisor_douglas_hyde.dds`

### Durable user-provided package

- `docs/assets/ireland_user_portrait_replacements_2026-08-14/manifest.json`
- `docs/assets/ireland_user_portrait_replacements_2026-08-14/gfx_handoff.md`
- `docs/assets/ireland_user_portrait_replacements_2026-08-14/source/leader_maurice_twomey.dds`
- `docs/assets/ireland_user_portrait_replacements_2026-08-14/source/leader_eamon_de_valera.dds`
- `docs/assets/ireland_user_portrait_replacements_2026-08-14/source/leader_sean_lemass.dds`
- `docs/assets/ireland_user_portrait_replacements_2026-08-14/source/leader_w_t_cosgrave.dds`
- `docs/assets/ireland_user_portrait_replacements_2026-08-14/source/leader_douglas_hyde.dds`
- `docs/assets/ireland_user_portrait_replacements_2026-08-14/processed/leader_maurice_twomey.png`
- `docs/assets/ireland_user_portrait_replacements_2026-08-14/processed/leader_eamon_de_valera.png`
- `docs/assets/ireland_user_portrait_replacements_2026-08-14/processed/leader_sean_lemass.png`
- `docs/assets/ireland_user_portrait_replacements_2026-08-14/processed/leader_w_t_cosgrave.png`
- `docs/assets/ireland_user_portrait_replacements_2026-08-14/processed/leader_douglas_hyde.png`
- `docs/assets/ireland_user_portrait_replacements_2026-08-14/review/portraits_contact_sheet_native.png`
- `docs/assets/ireland_user_portrait_replacements_2026-08-14/review/portraits_contact_sheet_2x.png`
- `docs/assets/ireland_user_portrait_replacements_2026-08-14/review/advisor_cards_contact_sheet.png`

### Advisor evidence and manifest

- `docs/plans/ireland_focus_tree/assets/advisors/manifest_current_chaos_redux_2026-08-13.json`
- `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_maurice_twomey.png`
- `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_sean_lemass.png`
- `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_douglas_hyde.png`
- `docs/plans/ireland_focus_tree/assets/advisors/review_4x/advisor_maurice_twomey_4x.png`
- `docs/plans/ireland_focus_tree/assets/advisors/review_4x/advisor_sean_lemass_4x.png`
- `docs/plans/ireland_focus_tree/assets/advisors/review_4x/advisor_douglas_hyde_4x.png`
- `docs/plans/ireland_focus_tree/assets/advisors/placement_studies/advisor_maurice_twomey_study.png`
- `docs/plans/ireland_focus_tree/assets/advisors/placement_studies/advisor_sean_lemass_study.png`
- `docs/plans/ireland_focus_tree/assets/advisors/placement_studies/advisor_douglas_hyde_study.png`
- `docs/plans/ireland_focus_tree/assets/advisors/alignment_8x/advisor_maurice_twomey_alignment_8x.png`
- `docs/plans/ireland_focus_tree/assets/advisors/alignment_8x/advisor_sean_lemass_alignment_8x.png`
- `docs/plans/ireland_focus_tree/assets/advisors/alignment_8x/advisor_douglas_hyde_alignment_8x.png`
- `docs/plans/ireland_focus_tree/assets/advisors/metadata/advisor_maurice_twomey.json`
- `docs/plans/ireland_focus_tree/assets/advisors/metadata/advisor_sean_lemass.json`
- `docs/plans/ireland_focus_tree/assets/advisors/metadata/advisor_douglas_hyde.json`

No `.gfx`, character, gameplay, localisation, spec, thumbnail, or unrelated documentation file was edited. No commit was created.
