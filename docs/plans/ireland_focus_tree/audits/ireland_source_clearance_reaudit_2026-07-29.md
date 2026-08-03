# Ireland source-clearance re-audit

Date: 2026-07-29
Feature: `ireland_focus_tree`
Namespace: `slopx`

## Same-day follow-up

The result table and findings below record the first 2026-07-29 re-audit.
Subsequent bounded C1-portrait, C1 portrait round-2A/2B, and Treaty Port passes
supersede its numeric totals:

| Family | Required | Complete | Needs review | Blocked |
| --- | ---: | ---: | ---: | ---: |
| Real-person portraits | 60 | 11 | 32 | 17 |
| Symbol/document packages | 40 | 7 | 0 | 33 |
| Sourced event/news slots | 69 | 29 | 0 | 40 |
| Total | 169 | 47 | 32 | 90 |

The current clearance-state totals are 76 C1, 14 C2, 54 C3, and 25 C4.
P-15, P-24, P-31, and P-51 advanced to C2 documentary evidence without a
usable portrait object. P-42 Jim O'Donovan is a C3 review package and remains
outside runtime. Its source evidence and the other newly recovered portrait
objects are preserved under
`docs/portraits/research_2026-07-29/c1_recheck/`.

The round-2A pass advanced P-16 Thekla Beere, P-32 Alfred O'Rahilly, and P-33
John Hayes to C2 documentary evidence and P-20 William O'Brien to a C3 review
package based on the exact August 1918 A. H. Poole/National Library of Ireland
object. P-26 Patrick Cogan remains C1 blocked because the preserved group
photograph has no face-to-person identification. All source originals and page
records from that pass are preserved under
`docs/portraits/research_2026-07-29/c1_recheck_round2_a/`; none of the C2 or C3
review derivatives is wired into runtime.

The round-2B pass advanced P-38 Stephen Hayes, P-39 Hugh McAteer, P-41 Harry
White, P-48 Roddy Connolly, and P-57 Tomás Ó Dochartaigh to C2 documentary
evidence. P-45 Mick Fitzpatrick, P-50 Michael Price, P-54 P. J. Coughlan, and
P-55 Liam D. Walsh remain C1 because no exact person-level portrait was
established. Every recovered source object and rejection record is preserved
under `docs/portraits/research_2026-07-29/c1_recheck_round2_b/`; no processed or
runtime portrait was created from that pass.

EV-SRC-021, EV-SRC-039, and EV-SRC-057 advanced to complete C3/C4 packages
from distinct Treaty Port source objects. Their final DDS files are under
`gfx/event_pictures/ireland/` and their sprites are registered in
`interface/slopx_ireland_sourced_assets.gfx`. They remain without
event-picture consumers because their canonical slot labels do not match the
current event-family semantics; no unrelated event was assigned merely to
consume cleared art. The detailed evidence is in
`assets/source_research_handoffs/event_treaty_ports_recheck_2026-07-29.md`.

The current machine-readable manifest and
`docs/plans/ireland_focus_tree/assets/clearance_audit.md` are authoritative
where the historical body below differs.

## Result

The authoritative source manifest still contains all 169 required rows:

| Family | Required | Complete | Needs review | Blocked |
| --- | ---: | ---: | ---: | ---: |
| Real-person portraits | 60 | 11 | 30 | 19 |
| Symbol/document packages | 40 | 7 | 0 | 33 |
| Sourced event/news slots | 69 | 26 | 0 | 43 |
| Total | 169 | 44 | 30 | 95 |

Clearance-state totals are:

- C1 provenance identified: 93;
- C2 restricted or review pending: 2;
- C3 cleared with conditions: 50;
- C4 cleared for unrestricted project use: 24.

The feature is not source-clearance complete. This audit records bounded
progress without converting quarantine or review files into shipping art.

## Portrait result and preservation

The blocked-portrait research pass recovered exact source originals for P-37
Seán Russell, P-59 J. J. Walsh, and P-60 Oliver J. Flanagan.

- P-59 is C4 complete. Its runtime file is
  `gfx/leaders/ireland/leader_j_j_walsh.dds`.
- P-37 and P-60 are C3 review packages and remain outside runtime.
- All three recovered originals are preserved under
  `docs/portraits/research_2026-07-29/blocked_queue/`.
- The earlier 39 source-original files under `docs/portraits/source_originals/`
  mirror their staging sources byte-for-byte, including the nested P-35
  Maurice Twomey source.
- No generated, reconstructed, statue, reenactment, film-still, or
  wrong-person likeness was substituted.

The contact sheet confirms that the Walsh crop is clean and centered. The
Russell source is markedly dark and the Flanagan source is a newspaper
halftone; their visual limitations reinforce the decision to keep them
review-only in addition to their C3 rights conditions.

## Symbol/document result

The bounded symbol pass recovered a larger staging package. Parent review
promoted only three independently verified public-domain rows:

- S-16: exact 1933-1934 O'Duffy/Blueshirt photograph;
- S-39: Wakeman's 1903 plan of Tara;
- S-40: the 1904/1905 Stone of Divisions illustration from *Romantic Ireland*.

Their final DDS files are under `gfx/interface/ireland/sourced/` and their
sprites are registered in `interface/slopx_ireland_sourced_assets.gfx`.

The remaining symbol files stay in source/review staging. A processed PNG,
staging DDS, or contact-sheet label is not treated as clearance. Exact
per-row dispositions and restrictions are recorded in
`docs/plans/ireland_focus_tree/assets/source_research_handoffs/symbol_blocked_queue_2026-07-29.md`.

## Event/news result

Both blocked event/news queues were researched:

- EV-SRC-001 through EV-SRC-034:
  `docs/plans/ireland_focus_tree/assets/source_research_handoffs/event_blocked_queue_001_034_2026-07-29.md`;
- EV-SRC-035 through EV-SRC-069:
  `docs/plans/ireland_focus_tree/assets/source_research_handoffs/event_blocked_queue_035_069_2026-07-29.md`.

No remaining event/news row reached runtime-safe C3 or C4 clearance. The
recovered exact objects are restricted by Royal Irish Academy/DIFP, Military
Archives, Met Éireann, Dúchas/NFC/UCD, or later-art/low-resolution conditions;
other rows still lack a distinct exact image object. Official legal-text and
Hansard alternatives remain subject substitutions and were not silently used
as the requested archival image.

The review previews under `assets/ireland_focus_tree/sourced/research_2026-07-29/events_*/`
are quarantine evidence only. No final DDS or runtime registration was made
from either queue.

## Runtime-boundary and manifest checks

The re-audit verified:

- all 169 manifest IDs are unique and retain the exact 60/40/69 family budget;
- every non-blocked row has an existing source, processed PNG, and final DDS;
- every recorded non-blocked final DDS hash matches the file on disk;
- every complete row resolves to the standard runtime `gfx/` tree;
- P-37 and P-60 resolve only to temporary review staging;
- all three newly promoted symbol/document DDS files match their manifest
  hashes and dimensions;
- no `.gfx` or `.gui` texture path points into `assets/`;
- the three promoted symbol/document crops contain no visible chroma-key
  residue or alignment defect.

No HOI4 launch or live scenario was used. Live testing is excluded from the
goal completion gate by user direction.

## Remaining source authority

Completion still requires a defensible disposition for:

- 19 blocked portraits;
- 30 C3 portrait reviews;
- 33 blocked symbol/document packages;
- 43 blocked sourced event/news rows;
- the review-gated Daniel Morrissey route-extension portrait and blocked
  Father Edward Cahill route-extension portrait.

Required external actions include object-level archive permissions, acceptance
of recorded C3 redistribution conditions, or discovery of distinct C4
alternatives. Generated likenesses and generic historical substitutes remain
forbidden.
