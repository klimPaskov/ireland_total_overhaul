# Ireland missing real-portrait source handoff

Status: blocked for source clearance; no DDS or processed PNG was created.

This handoff covers the three canonical portrait gaps and the separate Father Edward Cahill route extension. The source pass found no image that can be shipped with both face-level identity evidence and documented reuse permission. The parent agent owns final `.gfx` registration and must not wire any of these names until the corresponding source row is cleared.

## Proposed runtime surface

Suggested target `.gfx` file: `interface/ireland_sourced_assets.gfx`

Suggested final runtime root: `gfx/leaders/ireland/`

Leader processing target: `156x210` RGBA portrait, then DDS conversion with `.agents/skills/hoi4-feature-assets/tools/convert_to_dds.py`.

| Slot | Proposed sprite name | Proposed final DDS path | Current state | Clearance gate |
| --- | --- | --- | --- | --- |
| P-26 | `GFX_ireland_portrait_p_26` | `gfx/leaders/ireland/ireland_portrait_p_26.dds` | not created | Face-level Patrick Cogan mapping plus image permission/source provenance |
| P-45 | `GFX_ireland_portrait_p_45` | `gfx/leaders/ireland/ireland_portrait_p_45.dds` | not created | Reusable exact Mick Fitzpatrick image; the cited Hanley/Maurice Twomey Jr. group plates are copyrighted/private |
| P-55 | `GFX_ireland_portrait_p_55` | `gfx/leaders/ireland/ireland_portrait_p_55.dds` | not created | Exact Captain Liam D. Walsh portrait object; name-only records and later South Dublin Liam Walsh are not substitutes |
| RC-PORTRAIT-02 | `GFX_ireland_portrait_father_edward_cahill` | `gfx/leaders/ireland/ireland_portrait_father_edward_cahill.dds` | not created | Written permission or a rights-cleared archival master for the exact Cahill portrait |

## Ready-to-copy sprite snippets

None are supplied. A sprite definition without a final texture would create a missing-asset registration and would conceal the unresolved source/rights gate. After clearance, use this shape with the actual final path:

```text
spriteType = {
	name = GFX_ireland_portrait_p_26
	texturefile = "gfx/leaders/ireland/ireland_portrait_p_26.dds"
}
```

Repeat the same shape for the other proposed names only after the matching DDS exists and the canonical source manifest row is promoted.

## Review evidence

- P-26: History Ireland's Clann na Talmhan article contains historical group photographs, but neither direct image maps Patrick Cogan to a face. The underlying photographer/holding is not exposed, and History Ireland terms restrict reproduction without permission.
- P-45: Brian Hanley's *The IRA 1926–1936* captions identify Mick Fitzpatrick in group photographs, but the book is copyrighted and the image credit is private courtesy of Maurice Twomey Jr.; no redistribution permission or standalone source file was found.
- P-55: National Library of Ireland Eoin O'Duffy Papers establish the exact Captain Liam D. Walsh context but expose letters/cuttings rather than a portrait. A South Dublin auction image is a later 1953–1970 South Dublin IRA member named Liam Walsh and is rejected as the wrong person.
- Father Edward Cahill: History Ireland has an exact 300x349 individual portrait; Centro San Giorgio and Virgo Sacrata display additional exact portrait reproductions. None states a photographer/archive or reuse licence. History Ireland's terms prohibit publishing/distributing/reproducing its content absent permission. Irish Jesuit Archives has an identity-mapped 1915 group photograph but requires written permission and is not an individual portrait.

## Review aids and omissions

The dated source manifest at `docs/assets/ireland_missing_portrait_sources_2026-08-14/manifest.json` contains the URLs, identity mapping, dates, rights status, dispositions, and uncertainties for every lead. No candidate image was copied into the repository, so no visual contact sheet was generated; retaining or circulating the unlicensed/rejected web reproductions would be misleading. The existing approved leader/advisor contact sheets remain unchanged.

## Parent next action

Obtain written permission or a documented public-domain/Creative Commons/mod-reuse grant and face-level identification for each requested person. Then preserve the permitted original, create the 156x210 crop, convert it to DDS, append the full provenance/rights record to the canonical source manifest, and register the parent-owned `.gfx` definitions. Do not use a group member, generic avatar, same-name person, auction scan, book scan, or AI/generated likeness as a fallback.
