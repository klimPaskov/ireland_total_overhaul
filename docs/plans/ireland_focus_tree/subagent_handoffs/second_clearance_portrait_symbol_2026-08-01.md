# Second portrait/symbol source-clearance handoff

Date: 2026-08-01

Supersession note (2026-08-02): the two C3 symbol alternates documented here
were subsequently promoted to the standard runtime `gfx` tree under
`assets/source_research_handoffs/runtime_promotion_s06_s08_2026-08-02.md`.
The source-package evidence and C3 conditions below remain authoritative; the
runtime promotion does not make either item C4 or change its alternate-object
boundary.

## Result

Independent re-audit completed for the requested portrait and symbol/document rows. Two exact semantic symbol/document alternates are staged at C3 with conditions:

- S-06: anonymous circa-1932 *President De Valera and his Cabinet* Fianna Fáil poster from Wikimedia Commons, with [Adams auction lot 74299](https://www.adams.ie/74299/FIANNA-FAIL-PRESIDENT-DEVALERA-AND-HIS-CABINET-Colour-printed-poster-showing-photographic-portraits-of-De-Valera-and-nine-members-of-his-cabinet-against-a-shamrock-pattern-Dublin-printed-circa-1?high_estimate=10000&ipp=All&keyword=&low_estimate=1&view=lot_detail) provenance.
- S-08: anonymous June 1922 *Cathal O'Shannon Election Poster* Labour election poster from Wikimedia Commons, with Irish Election Literature provenance.

No portrait row cleared. P-15, P-16, P-24, P-26, P-31, P-32, P-38, P-39, P-41, P-45, P-48, P-50, P-54, P-55, and P-57 remain blocked. S-09, S-10, S-12, S-15, S-17, S-18, S-20, S-23, S-26, S-28, S-30, and S-33 remain blocked. Row-level reasons and URLs are in the package report.

## Files produced

Package root:

`assets/ireland_focus_tree/sourced/research_2026-08-01/second_clearance_portrait_symbol/`

- `research_report.md` — full row-by-row clearance and rejection report.
- `evidence/audit_register.md` — preserved source-original/page hashes and evidence boundary.
- `sources/s06_fianna_fail_1932_poster_original.jpg` — 2000×2198 RGB, SHA-256 `83b2979e22d65c9797e139ce469e673c49427156fe794cc83324947e35589a95`.
- `sources/s08_labour_cathal_oshannon_1922_poster_original.jpg` — 744×963 RGB, SHA-256 `b5a5cce5dddd5253a0b1fa843decec4077987bb67c70f08a6afd8a29262f71ef`.
- `sources/s12_easter_lily_badge_candidate_original.JPG` — 906×1302 RGB, SHA-256 `2c18c6ba7aa1fdec12f8faf3e2d239a2c33f65457876eb7505522460b4acb158`; rejection evidence only.
- `processed_png/s06_fianna_fail_1932_poster_397x153.png` — SHA-256 `656e0ac9cfc6228234bac2b3f242a73f6427b3249379c948704e79c4b6b73573`.
- `processed_png/s08_labour_cathal_oshannon_1922_poster_397x153.png` — SHA-256 `4a999a167b938412b8423c6293ded651f1940932406282afd715022097fb0f0f`.
- `final_dds/ireland_symbol_document_s_06.dds` — 397×153 DDS, SHA-256 `5f799c1fe8f72e0fe3a30849e425caea16860ec9e094226910086fa76a9e2a51`.
- `final_dds/ireland_symbol_document_s_08.dds` — 397×153 DDS, SHA-256 `b293f09343857ed68fedef5effbf505f30b50615fd1b3ce53fd82f382636d705`.
- `dds_review/ireland_symbol_document_s_06_decoded.png` and `dds_review/ireland_symbol_document_s_08_decoded.png` — Pillow DDS decodes, both 397×153, visually matching the processed previews.
- `contact_sheet/candidate_review_s06_s08_s12.png` — 397×564 RGB evidence sheet, SHA-256 `f53b82dbf9fb7d56b98c0e4d2239258109881e3656b8e7716eec8c5d6fa1303f`.

Source-page snapshots and their hashes are listed in `research_report.md`.

## Manifest change

Only `docs/plans/ireland_focus_tree/assets/source_manifest.json` rows S-06 and S-08 were changed. Each now records the exact alternate, source URL, Commons rights determination, provenance, C3 condition, source/processed/DDS hashes, dimensions, crop, and staged-package paths. No EV-SRC row was touched.

At the time of this handoff, the manifest's `final_dds_path` values pointed to
this staged package and no `.gfx` file had been edited. The later parent-owned
promotion copied the two reviewed DDS files to the runtime symbol root and
registered them without changing the source evidence.

## C3 conditions the main agent must preserve

1. S-06 is the Commons/Adams circa-1932 Fianna Fáil poster alternate. It must not be labelled or documented as the NLI vtls000277076 / EPH F58 object. Credit the poster, Commons file, and Adams provenance. The audit relies on the Commons EU anonymous-work public-domain determination and makes no separate US determination.
2. S-08 is the Commons/Irish Election Literature June 1922 Labour/Cathal O'Shannon poster alternate. It must not be labelled or documented as the NLI vtls000544507 / EPH F467/F467a object. Credit the poster, Irish Election Literature, and Commons file. The audit relies on the Commons EU anonymous-work and US pre-1931 public-domain determinations.
3. S-12 must remain blocked. The preserved Commons Easter Lily candidate is a generic calla-lily photograph, not an identified republican badge or period commemorative object.

## Portrait outcome

No real leader source met the required exact-identity and permission threshold. No source was copied to `docs/portraits`; no generated likeness, modern redraw, group-face guess, or rights-unclear archive access copy was promoted.

## Validation boundary

The two processed previews were visually reviewed. Both DDS headers and Pillow decodes report 397×153. No live game test was performed, as requested. Runtime sprite/GFX wiring remains for the main agent after review of the C3 conditions.
