# Missing Ireland real-portrait source handoff — 2026-08-14

## Result

The fresh source/rights pass is complete for the exact requested gaps:

- P-26 — Patrick Cogan
- P-45 — Mick Fitzpatrick
- P-55 — Liam D. Walsh
- RC-PORTRAIT-02 — Father Edward Cahill (route extension outside the canonical P-01–P-60 budget)

No requested portrait reached production clearance. No source original was copied into the repository, no processed PNG was made, no DDS was converted, and no `.gfx` file was edited. This is an evidence-backed source/rights block, not a wiring omission.

The detailed dated manifest is [manifest.json](../../../../assets/ireland_missing_portrait_sources_2026-08-14/manifest.json). The parent-facing sprite/path handoff is [gfx_handoff.md](../../../../assets/ireland_missing_portrait_sources_2026-08-14/gfx_handoff.md), and the non-raster candidate contact-sheet index is [candidate_contact_sheet.md](../../../../assets/ireland_missing_portrait_sources_2026-08-14/candidate_contact_sheet.md).

## Source and rights findings

### P-26 — Patrick Cogan

The official Oireachtas record and biographical cross-check establish the intended Wicklow Clann na Talmhan politician. History Ireland's Clann na Talmhan article exposes two period group/context images: an early gathering in Athenry and members of the parliamentary party. Neither caption maps Patrick Cogan to a face. The underlying photographer, holding institution and image date are not exposed. History Ireland terms restrict publishing, distributing or reproducing content without permission.

Disposition: blocked at C1. The images are not an exact portrait source and cannot be cropped by inference.

### P-45 — Mick Fitzpatrick

The official Oireachtas record establishes the 1893–1968 TD. Brian Hanley's *The IRA 1926–1936* is the strongest exact identity lead: its captions identify Mick Fitzpatrick in 1932/1930s group plates. The publisher and mirror identify the book as copyrighted/all rights reserved, and the relevant photographs are credited to private courtesy of Maurice Twomey Jr. No standalone image bytes or permission for mod redistribution were found. A Tipperary Historical Journal group reference names a different Michael Fitzpatrick (brother of Sean), and the Fitzpatrick Multimedia catalogue's reviewed wedding image is a different family; both were rejected.

Disposition: blocked at C1. The book reference is useful historical evidence but not a reusable portrait asset.

### P-55 — Liam D. Walsh

The National Library of Ireland Eoin O'Duffy Papers and exact-name catalogue searches establish the Captain Liam D. Walsh correspondence/cuttings context, but no individual portrait object is exposed. A South Dublin Auction listing titled as a photograph of Liam Walsh in IRA uniform describes a later South Dublin IRA member who joined in 1953 and died in 1970. That is not the canonical Captain associated with the 1930s Irish Brigade/Blueshirts context, and an auction listing is not a reuse grant. ArchivUL/Irish Brigade Association material reviewed is correspondence, not a portrait.

Disposition: blocked at C1. No name-only or later-person image may be substituted.

### RC-PORTRAIT-02 — Father Edward Cahill

Irish Jesuit Archives confirms the exact Edward J. Cahill identity and dates (1868–1941). Three exact portrait reproductions were located for rights review:

1. History Ireland's 300x349 `Cahill-photo.jpg`, captioned as Edward Cahill SJ. The WordPress media record exposes no photographer, archive, credit or copyright field. History Ireland terms prohibit publishing/distributing/reproducing content without permission.
2. Centro San Giorgio's 360x252 black-and-white portrait, captioned in Italian as Padre Edward Cahill SJ. No photographer, archive or reuse licence is stated.
3. Virgo Sacrata's small sepia/halftone portrait on a commercial book page. No photographer, archive or reuse licence is stated.

Irish Jesuit Archives also records `IE IJA SC/CRES/3/165`, a 17 March 1915 group photograph that maps Cahill to the pavement. It is not an individual portrait, and the archive requires written permission for reproduction. None of these leads is cleared for a mod texture.

Disposition: blocked at C1 pending written permission or a rights-cleared archival master.

## Asset production state

| Output | Count | Reason |
| --- | ---: | --- |
| Preserved source originals | 0 | Every exact/context lead remained rights-blocked, identity-incomplete, or both |
| Processed portrait PNGs | 0 | No source passed the identity and rights gate |
| Final DDS files | 0 | The converter was not run on an uncleared source |
| Visual contact sheet | 0 | No unlicensed or identity-ambiguous candidate was retained in the repository |
| `.gfx` edits | 0 | Parent owns wiring, and no final texture exists to register |

The research contact-sheet index lists every reviewed lead without embedding restricted images. Existing approved leader/advisor contact sheets are unchanged.

## Parent wiring handoff

Suggested target surface: `interface/ireland_sourced_assets.gfx`.

Proposed sprite names and final paths after clearance:

| Slot | Sprite name | Final DDS path | Target |
| --- | --- | --- | --- |
| P-26 | `GFX_ireland_portrait_p_26` | `gfx/leaders/ireland/ireland_portrait_p_26.dds` | 156x210 |
| P-45 | `GFX_ireland_portrait_p_45` | `gfx/leaders/ireland/ireland_portrait_p_45.dds` | 156x210 |
| P-55 | `GFX_ireland_portrait_p_55` | `gfx/leaders/ireland/ireland_portrait_p_55.dds` | 156x210 |
| RC-PORTRAIT-02 | `GFX_ireland_portrait_father_edward_cahill` | `gfx/leaders/ireland/ireland_portrait_father_edward_cahill.dds` | 156x210 |

There are no ready-to-copy sprite definitions because registering absent textures would create false completion. Once a source is cleared, preserve its permitted original, create the 156x210 RGBA crop using the established portrait workflow, run `.agents/skills/hoi4-feature-assets/tools/convert_to_dds.py`, append provenance/rights to the canonical manifest, and then wire the corresponding sprite in the parent-owned surface.

## Required follow-up

The parent needs a written image-use permission, explicit public-domain/Creative Commons/mod-reuse evidence, or a rights-cleared archive master for each portrait. The evidence must identify the exact person at face level. No group member, generic avatar, same-name person, later person, book scan, auction scan, or generated likeness is an acceptable fallback.

## Simplifications, omissions, and blockers

No fallback or identity substitution was used. The only omission is the production package itself, which remains correctly blocked because all exact image leads lack usable rights or sufficient face-level mapping. The canonical rows remain C1-blocked; this dated supplemental manifest records the new research rather than silently promoting any source.
