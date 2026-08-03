# Ireland sourced leader-portrait archive

Feature slug: `ireland_focus_tree`

This folder preserves the source-found leader portraits used by the Ireland
package. It is documentation/source preservation only; it is not an engine
runtime lookup path. As of 2026-08-03 it contains 505 preserved archive,
provenance, and derivative files. The canonical source inputs for the 57 complete
portrait rows are now the unmodified files stored directly in this top-level
folder. No new subfolder is used for portrait sourcing; existing subfolders
are retained as historical archive/research evidence only.

The flat source set contains one exact-byte original per complete canonical row,
with a `P-xx_` prefix. P-15 John Leydon is preserved as
`P-15_john_leydon_catholic_archives_1940.jpg`. The canonical manifest records
each flat `source_path`, its SHA-256, and the old temporary staging path as
`source_staging_path`. The three blocked canonical rows are intentionally
absent from this source set.
The source-dimension audit confirms that none of the 57 flat originals is a
156x210 processed crop; each retains the dimensions of its recovered source
object.

Current manifest disposition (2026-08-03): 57 of the 60 canonical portrait
rows are complete and 3 are blocked. P-15 John Leydon is preserved from the
exact caption-mapped 30 April 1940 Catholic Archives delegation photograph and
is conditionally registered for local-mod runtime use; P-26 Patrick Cogan,
P-45 Mick Fitzpatrick, and P-55 Liam D. Walsh remain blocked because no exact
usable portrait object was found. The other complete source-backed rows are
wired to Ireland character consumers under their recorded conditions. The optional Father Edward Cahill
extension is outside the canonical budget and remains blocked without an exact
portrait.

## Contents

The flat `P-xx_*` files in this top-level directory are the only portrait
source inputs. The directories listed below are legacy provenance or derivative
evidence; current sourcing does not read a processed 156x210 crop from them.

- `source_originals/` — exact source objects copied from the temporary research
  packages. This includes the manifest-backed source packages and additional
  recovered evidence that must survive staging cleanup.
- `processed_png/` — identity-preserving 156×210 HOI4 portrait crops associated
  with the preserved source packages. These are derivatives, not substitutes
  for the originals.
- `research_2026-07-29/blocked_queue/` — three newly recovered source
  originals: P-37 Seán Russell, P-59 J. J. Walsh, and P-60 Oliver J.
  Flanagan. P-59 is C4 and has a runtime DDS; P-37 and P-60 remain C3 review
  packages outside runtime.
- `research_2026-07-29/c1_recheck/` — five additional exact documentary
  objects recovered from the remaining C1 queue: John Leydon, Luke Duffy,
  Bishop Michael Browne of Galway, Jim O'Donovan, and Seán Murray. Leydon,
  Duffy, Browne, and Murray are C2 research evidence and are not runtime
  assets. O'Donovan is a conditional C3 review package whose processed PNG and
  DDS remain in temporary staging because the Commons record carries an
  unresolved United States/public-domain-status warning.
- `research_2026-07-29/c1_recheck_round2_a/` and
  `c1_recheck_round2_b/` — exact recovered source, provenance, restricted, and
  rejection evidence from the second bounded queue review.
- `research_2026-07-29/round4/` — 45 exact downloaded source or provenance
  objects from the fourth review, plus a README and SHA-256 inventory. These
  files preserve the research record without promoting any blocked or
  conditional row.
- `research_2026-07-29/round5_live_clearance_sources/` — five exact source or
  source-page objects from the final live-portrait review: the NARA Costello
  master, the Irish Capuchin Archives Peadar O'Donnell master, and three BNE
  Frank Ryan collection thumbnails. The NARA object is a C4 candidate pending
  the later-date/group-pose policy decision; the Capuchin and BNE objects remain
  rights-restricted research evidence.
- `research_2026-07-29/round6_blocked_portrait_sources/` — the exact Library
  of Congress Seán Murray newspaper page and ALTO record, plus two direct
  Military Archives Harry White source objects and their hash inventory.
- `research_2026-07-29/round7_blocked_portrait_sources/` — the exact John
  Hayes circa-1940s Commons source and source-page record, the exact 1944
  Tomás Ó Dochartaigh campaign-poster source, and their SHA-256 inventories.
  John Hayes is a conditional C3 review package; Ó Dochartaigh remains blocked
  because the poster crop is weak and image-level rights are unresolved.
- `research_2026-08-02/portrait_exact_object_search_round13/P-50_michael_price/`
  — the exact Keogh Brothers Ltd Tom Barry wedding source, its face-mapping
  locator, and the source-derived 156×210 Mick Price portrait. The source
  object and processed portrait are preserved here after the exact sixth-row
  identity mapping was confirmed by Cork City Council and an independent
  history-group reference; the manifest retains the C3 local-mod boundary.
- `research_2026-08-02/portrait_exact_object_search_round14/P-54_pj_coughlan/`
  — the exact Reading the Signs reproduction of the Southern Irish Brigade
  group photograph, its caption-mapping locator, and the source-derived
  156×210 P. J. Coughlan portrait. The caption identifies Coughlan as the
  second person in the middle row; the page declares its photographs and text
  CC BY-SA 4.0, and the manifest retains the C3 local-mod boundary.
- `research_2026-08-03/portrait_exact_object_search_round15/P-31_michael_browne/`
  — the exact RTÉ-published reproduction of the UCD Digital Library
  Commission on Vocational Organisation group photograph, its caption-mapping
  locator, and the source-derived 156x210 Michael Browne portrait. The
  printed caption names Browne as chairman and the fourth front-row subject;
  the manifest retains the C3 local-mod boundary and the undated-photo note.

The historical queue descriptions above are retained for provenance. Current
runtime disposition is governed by the manifest and crosswalk: P-37, P-42,
P-60, P-20, P-33, and the other complete source-backed portraits are not
registration-only rows; their Ireland character consumers are recorded by the
crosswalk. P-15 is now a conditional local-mod runtime package from the exact
1940 archive object, while P-26, P-45, and P-55 have no exact source object.

The canonical per-item source URLs, credits, clearance states, hashes, and
runtime paths remain in
`docs/plans/ireland_focus_tree/assets/source_manifest.json`. Archival
preservation never changes a clearance state. Daniel Morrissey remains a
conditional C3 route extension outside the canonical manifest; Father Edward
Cahill remains blocked outside the canonical budget, and the blocked-queue and
recheck additions retain their own per-item dispositions.

The source manifest now points to the unmodified flat originals in this
top-level folder. The dated preservation packages are archive copies only;
they do not promote a source, grant C4 status, or create a runtime `.gfx`
registration. The manifest retains each former staging location as
`source_staging_path` for provenance.

Generated collective route portraits are intentionally not copied here: this
archive is limited to real portraits found from source.

The bounded 2026-07-29 source rechecks are preserved under
`research_2026-07-29/c1_recheck/`, `c1_recheck_round2_a/`, and
`c1_recheck_round2_b/`. These directories retain exact source objects, source
pages, restricted evidence, and rejection evidence even when no runtime
portrait can be cleared.

The current canonical C3 review packet covers 34 portraits. Its contact sheet
shows the 32 packages available when the sheet was assembled; the later P-33
John Hayes and P-51 Seán Murray packages are linked separately from the packet:
`docs/portraits/ireland_c3_portrait_review_contact_sheet_2026-07-29.png`.
Its conditions and acceptance boundary are summarized in
`docs/portraits/ireland_c3_portrait_review_packet_2026-07-29.md`. Neither file
changes a manifest disposition or promotes review art into runtime.

Final engine assets remain under the standard runtime path
`gfx/leaders/ireland/`. Nothing in `docs/portraits/` is registered by a `.gfx`
file.

## Archive integrity

The 2026-08-03 preservation audit compared SHA-256 hashes for all 57 complete
canonical portrait `source_path` values against the unmodified files directly
under this folder; all 57 matched exactly. Rows whose manifest source is
`not_created` represent identities for which no source object has been found;
they are not silently substituted. P-31, P-50, and P-54 are no longer in that
state: their exact source originals and processed portraits remain recorded by
the dated round-15, round-13, and round-14 packages, while their source inputs
are the flat originals above.
Processed crops and review DDS exports do not count as source preservation.
Git text conversion is disabled for `docs/portraits/**` so downloaded HTML and
mixed-line-ending provenance evidence remain byte-identical across checkouts.
