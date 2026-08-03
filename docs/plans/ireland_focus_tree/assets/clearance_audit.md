# Ireland focus tree source and clearance audit

## Current manifest reconciliation: 2026-08-03

The machine-readable `source_manifest.json` is the current authority after the
M2/A2/C3 reconciliation, the earlier user-approved conditional source
promotions, the 2026-08-02 round-12 conditional promotion, the round-13 exact
Mick Price portrait promotion, the round-14 exact P. J. Coughlan portrait
promotion, the round-15 exact Michael Browne portrait promotion, and the
round-24 exact John Leydon portrait promotion. It records 166 `complete`, 0
`needs_user_review`, and 3 `blocked` rows: portraits 57/0/3, symbols/documents
40/0/0, and event/news 69/0/0. Clearance states are C1 3, C2 0, C3 135, and
C4 31. P-26, P-45, and P-55 remain blocked without an exact portrait object.
For all 57 complete portrait rows, the manifest `source_path` now points to an
unmodified original stored directly under `docs/portraits/`; the old `assets/`
locations are retained only as `source_staging_path` evidence. Processed PNGs
remain derivatives in temporary staging and final DDS files remain under the
standard runtime `gfx/` tree.
Round 16 recorded and rejected the NLI Poole POOLEWP
3272 Liam Walsh lead because its Waterford sitter does not establish the
canonical Dublin Captain Liam D. Walsh identity; the manifest and runtime
consumer set are unchanged.
Every complete sourced event/news row now has a semantically matched event
consumer, and 56 of the 57 complete portrait rows have character consumers in
the Ireland route-character package. P-15 is intentionally registration-only
under its conditional local-mod source package; no unrelated gameplay consumer
was invented for it.
EV-SRC-041 is complete as the official FRUS 1940 Vol. III Document 161
package, and EV-SRC-004, EV-SRC-022, EV-SRC-040, and EV-SRC-058 are complete
as four distinct official FRUS neutrality packages; their source and runtime
evidence are in the dated handoffs under
`assets/source_research_handoffs/`. The two symbol/document rows S-24 and S-27
were already complete under explicit conditional C3 approval; S-06 and S-08
are complete as exact-period C3 alternates, and S-15, S-20, S-23 and S-26 are
complete under the project owner's 2026-08-02 conditional approval. S-33 is
now complete as an exact C3 National Library of
Ireland Spike Island handover photograph; its processed PNG, staging DDS,
runtime DDS and controlled attribution are recorded in the final-clearance
handoff. EV-SRC-055 is the
complete C3 Oireachtas Constitution (Consequential Provisions) Bill package;
its source, crop, hashes, licence conditions, and runtime consumer are in
`assets/source_research_handoffs/EV055_Oireachtas_clearance_2026-08-01.md`.
EV-SRC-059 is now complete under conditional C3 clearance for the exact
UWM/AGSL Admiralty Chart 1765 source and F17 Cork ports consumer; its source,
metadata, hash, rights conditions, and runtime wiring are in
`assets/source_research_handoffs/EV059_UKHO_chart_clearance_2026-08-01.md`.
The separate Daniel Morrissey route extension is complete under conditional C3
local-mod scope outside the 169-row manifest; its NLI and Wikimedia credits
remain required and it is not an unrestricted redistribution asset. The
optional `RC-PORTRAIT-02` Father Edward Cahill extension is also outside the
canonical 169-row budget, remains C1 `blocked` without an exact portrait
object, and has no runtime consumer; the Clerical-Lay Guardianship collective
office/emblem remains the canonical implementation. Round 12 retained its
exact preserved source objects as C3 local-mod packages under the user's
explicit project-owner instruction. Round 13 promoted P-50 Michael Price
from an exact face-mapped 1921 group photograph, round 14 promoted P-54 P. J.
Coughlan from an exact caption-mapped 1936 Irish Brigade group photograph, and
round 15 promoted P-31 Michael Browne from the captioned UCD/RTÉ Commission on
Vocational Organisation photograph. Round 24 promoted P-15 John Leydon from
the exact caption-mapped 30 April 1940 Catholic Archives delegation object.
Round 25 rechecked the direct History Ireland group-photo object for P-26 and
confirmed that it does not map Cogan's face or expose an image-level licence.
Round 26 rechecked the remaining Fitzpatrick and Walsh leads and found no
face-mapped, rights-defensible source object; the negative-evidence handoffs
are recorded under `assets/source_research_handoffs/`. The three current
portrait blockers are P-26, P-45, and P-55; the round-24 handoff records the
exact source, crop, preservation path, and runtime DDS.
Round 27 also rejected the History Ireland Republican Congress newspaper-cover
illustration as a non-portrait context image for P-45; its object and hash are
recorded in the round-27 handoff without any promotion.
Round 28 checked the official Oireachtas image endpoints for P-26 and P-45 and
found the same generic 80x80 `Avatar` SVG for both, not person-specific source
portraits. It also checked the History Ireland Blueshirt rally image for P-55;
the article names Walsh in its surrounding text, but the displayed group
photograph maps only O'Duffy and supplies no Walsh face locator. None of these
objects is eligible for promotion. The object hashes and temporary research
paths are recorded in the round-28 handoff; no new file was added to
`docs/portraits`.
Round 29 rechecked P-26 and P-45 through the Carlow bibliography, official
Oireachtas records, NLI leads, and the Hanley/Maurice Twomey caption trail. The
research produced no exact original image bytes, person-level face mapping, or
defensible local-mod reuse boundary. No asset, derivative, manifest source, or
GFX entry was created; the three blocked portrait rows remain P-26, P-45, and
P-55. The dated handoff is
`assets/source_research_handoffs/portrait_exact_object_search_round29_p26_p45_2026-08-03.md`.

The dated count tables and prose below preserve earlier source-clearance
snapshots for traceability. They must not override the current manifest or the
re-audit in
`../audits/ireland_review_row_route_portrait_reaudit_2026-08-01.md`.

Audit date: 2026-07-22

Round-7 blocked-source update: 2026-07-29

Reconciled 2026-07-29 after the bounded blocked-portrait, symbol/document,
C1-portrait, C1 portrait round-2A/2B, and Treaty Port event-art research passes.
P-59 J. J. Walsh is
promoted to C4 runtime use; P-37 Seán Russell, P-42 Jim O'Donovan, and P-60
Oliver J. Flanagan are preserved as C3 review packages outside runtime. S-16,
S-39, and S-40 are promoted from independently verified public-domain records.
EV-SRC-021, EV-SRC-039, and EV-SRC-057 are promoted from distinct cleared
Treaty Port source objects. P-20 William O'Brien has an exact A. H. Poole/NLI
1918 C3 review package. P-16 Thekla Beere and P-32 Alfred O'Rahilly retain
exact C2 evidence packages and remain outside runtime. P-33 John Hayes now
has a C3 conditional Commons portrait package and remains outside runtime. The
round-2B pass also preserves exact C2 objects for P-38 Stephen Hayes, P-39
Hugh McAteer, P-41 Harry White, P-48 Roddy Connolly, and P-57 Tomás Ó
Dochartaigh. None has compatible runtime permission. The machine-readable
manifest remains authoritative. The round-3 source passes add review-only
packages for EV-SRC-020, EV-SRC-023, EV-SRC-032, EV-SRC-036, EV-SRC-037,
EV-SRC-038, EV-SRC-041, EV-SRC-050, EV-SRC-054, EV-SRC-056, EV-SRC-059,
EV-SRC-068, S-04, S-11, S-14, S-21, S-24, S-27, S-32, S-34, S-35, S-36,
and S-38. None of those twenty-three candidates is promoted into runtime.
The final round-5 portrait and event/news reviews and the round-4
symbol/document review are preserved in dated handoffs. The portrait pass adds exact NARA Costello, Irish
Capuchin Archives Peadar O'Donnell, and BNE Frank Ryan evidence under
`docs/portraits/`. The symbol pass identifies evidence-supported
public-domain objects for S-13/S-25, S-19, and S-29, plus conditional objects
for S-08 and S-22; official-insignia and alternate-object decisions remain
open. The event/news pass produces no new C4 promotion.

The round-seven source pass advances P-33 John Hayes to conditional C3 review,
aligns EV-SRC-055's exact modern legal-text record to conditional C3 review,
and advances six symbol/document packages to C3 review. S-19 is the sole new
C4 package: its exact public-domain 1903 *An Claidheamh Soluis* object is
registered under runtime `gfx/` with its identity kept distinct from the
controlled NLI 1915 handbill. No other round-seven staging DDS is registered.

The bounded round-six recheck of the remaining 28 blocked event/news rows is
preserved under
`assets/ireland_focus_tree/sourced/research_2026-07-29/blocked_event_news_round6/`
with a 58-file SHA-256 inventory and per-row MD/JSON handoff. It found exact
family evidence for Military Archives lookout/defence collections, Met Éireann
Blacksod material, Dúchas manuscript pages, and Oireachtas constitutional-law
documents, but no safe runtime promotion. DIFP document numbers 3207 and 3260
also failed the named-slot semantic check. All 28 rows retain their canonical
manifest disposition.
Machine-readable manifest: `docs/plans/ireland_focus_tree/assets/source_manifest.json`  
Research surface: `assets/ireland_focus_tree/source_research/`

## Coverage

| Family | Required | Manifest entries | Local source package | Production disposition |
| --- | ---: | ---: | ---: | --- |
| Real-person portraits | 60 | 60 (`P-01`..`P-60`) | source-backed originals and review sheets preserved under `docs/portraits/`; complete canonical originals are flat at the top level, while historical review packages remain dated evidence | 57 complete; 0 needs user review; 3 blocked |
| Historical symbol/document packages | 40 | 40 (`S-01`..`S-40`) | 40 complete packages and the S-01 normal/medium/small runtime flag set; round-12 rows retain conditional C3 attribution and object-use conditions | 40 complete; 0 needs user review; 0 blocked |
| Sourced report/news slots | 69 | 69 (`EV-SRC-001`..`EV-SRC-069`) | 69 complete source outputs; round-12 rows retain exact-object attribution and conditional local-mod boundaries | 69 complete; 0 needs user review; 0 blocked |

Total: 169 manifest entries: 166 complete, 0 needs user review, and 3
blocked. The 69 event/news entries are slots, not permission to reuse one
generic image across unrelated events; each slot retains its own source-family,
crop, era-fit, and controlled-reuse record. No selected source object is
silently reused across unrelated slots.

## Clearance state record

The manifest uses the exact five ledger states and records one state on every entry:

| State | Meaning | Current use |
| --- | --- | --- |
| C0 | Discovered only | research lead; not downloadable/processable as an asset |
| C1 | Provenance identified | identity/source lead; rights unresolved; no final DDS |
| C2 | Restricted or review pending | terms, access, jurisdiction, or approval unresolved; no final DDS |
| C3 | Cleared with conditions | final use only with exact attribution/conditions |
| C4 | Cleared for unrestricted project use | verified public-domain or explicit compatible permission |

Current manifest dispositions: 3 C1 provenance records, 0 C2
restricted/review-pending records, 135 C3 cleared-with-conditions records, and
31 C4 entries. S-02 uses the official Government of Ireland state-harp record
and is C4 for the bounded state-identity reference use; the older Dalway-harp
illustration remains a research candidate only. S-16 uses the exact 1933-1934
Narodowe Archiwum Cyfrowe/Commons Blueshirt photograph. S-39 uses Wakeman's
public-domain 1903 Tara plan. S-40 uses the public-domain Stone of Divisions
illustration from *Romantic Ireland*. Forty-six canonical portraits are
complete C3 conditional packages, ten are complete C4 packages, and four remain
blocked because no exact person-labelled portrait object exists in the
preserved package. Thirty-three symbol/document records are complete C3
packages and seven are complete C4 packages. Fifty-five event/news records are
complete C3 packages and fourteen are complete C4 packages. The round-12
user-approved conditional tranche is recorded per item in the manifest and in
`assets/source_research_handoffs/user_approved_conditional_round12_2026-08-02.md`.
P-50 is additionally recorded in
`assets/source_research_handoffs/portrait_exact_object_search_round13_2026-08-02.md`.
No other record is silently upgraded from a catalogue, contact-sheet label, or
open-web lead.

## Source-tier record

Every manifest entry contains a numeric `source_tier` and the corresponding hierarchy label in the manifest schema:

1. Irish official archives and government repositories  
2. Northern Irish and British official archives  
3. National libraries and major public collections  
4. Universities and recognised research archives  
5. Museums and established heritage institutions  
6. Political, labour, religious, cultural, and institutional repositories  
7. Reputable digitised public-domain repositories  
8. Commercial archives and press agencies  
9. Published academic or documentary works  
10. Private collections and user-provided material  
11. Open-web discovery sources

The existing manifest assigns a tier to every entry, including blocked leads; a
lower tier is not treated as permission. The current machine-readable
distribution is T1 47, T2 18, T3 22, T4 14, T5 6, T6 13, T7 32, T8 9, T9
6, T10 0, and T11 2. The schema still defines all eleven tiers; unused tiers
remain available for future object-level research.

## Technical verification

All 166 complete manifest records and their local processed outputs have the
recorded target
dimensions. EV-SRC-055 now has the processed 210x176 source-derived Oireachtas
scan and matching runtime DDS; EV-SRC-059 now has the processed 210x176
source-derived Admiralty chart crop and matching runtime DDS. Their exact
sources, licence conditions, and consumers are recorded in the dated clearance
handoffs. EV-SRC-004, EV-SRC-022, EV-SRC-040, and EV-SRC-058 now have
processed and runtime DDS pairs from four distinct official FRUS neutrality
records. EV-SRC-004, EV-SRC-022, EV-SRC-040, EV-SRC-041, and EV-SRC-058 now
feed H04 emergency-news events `.112` through `.115` and F15 neutral-markings
event `.655`; the exact source-to-consumer mapping is recorded in
`audits/ireland_event_source_consumer_repair_2026-08-01.md` and the FRUS
clearance handoffs. No unrelated event was rewired to force a source slot.
The separate Daniel Morrissey route extension also has a 156x210 review
candidate. The round-12 event/news and symbol/document rows now have runtime
DDS paths; P-15, P-31, P-50, and P-54 have exact source-derived runtime
portraits. P-26, P-45, and P-55 have no runtime registration. The unprocessed
SVG flag reference is retained as a source candidate only and is not treated
as a final raster asset.

A SHA-256 preservation audit covers the current portrait source package. The
ten round-12 originals, the round-13 P-50 source original, the round-14
P-54 source original, and the round-15 P-31 source original have byte-identical
copies under
`docs/portraits/research_2026-08-02/user_approved_conditional/`,
`docs/portraits/research_2026-08-02/portrait_exact_object_search_round13/P-50_michael_price/`,
and `docs/portraits/research_2026-08-02/portrait_exact_object_search_round14/P-54_pj_coughlan/`,
`docs/portraits/research_2026-08-03/portrait_exact_object_search_round15/P-31_michael_browne/`,
alongside the earlier preserved portrait packages. The current blocked canonical
portrait rows are P-26/P-45/P-55 (no exact person-labelled source object). P-15
is preserved as the original source file directly under `docs/portraits/`.
No promoted sourced leader portrait exists only in temporary `assets/` staging.

The matching canonical HOI4 references were inspected before audit: `assets/vanilla_reference/portraits/leaders/`, `assets/vanilla_reference/event_art/report/`, `assets/vanilla_reference/event_art/news/`, and `assets/vanilla_reference/flags/` with their README/CATALOG guidance. The portrait target is 156x210; report art is 210x176; news art is 397x153; and flags use the documented HOI4 normal/medium/small family.

The 166 complete manifest outputs are registered across the Ireland source-side
asset definitions. P-59 J. J. Walsh is registered as
`GFX_ireland_portrait_p_59` and its final DDS is under
`gfx/leaders/ireland/`. S-16, S-39, and S-40 are registered as
`GFX_ireland_symbol_document_s_16`, `GFX_ireland_symbol_document_s_19`,
`GFX_ireland_symbol_document_s_39`, and `GFX_ireland_symbol_document_s_40`,
with final DDS files under
`gfx/interface/ireland/sourced/`. P-37 Seán Russell, P-42 Jim O'Donovan, and
P-60 Oliver J. Flanagan remain preserved as original source files under
`docs/portraits/` with processed review packages under `assets/`; none is
copied into runtime while its recorded review disposition remains. The round-12
conditional portrait package adds ten exact source-backed registrations with
their external-rights conditions visible in the manifest. P-35
Maurice Twomey is separately registered as a conditional Berkeley/Bancroft
portrait with its CC BY attribution requirement. The cleared Constitution
document is wired to the opening constitutional event as
`GFX_report_event_ireland_report_constitution_1937`; the official state harp is
registered as `GFX_ireland_official_state_harp_reference`; the 1937 Official
Seal of the President is wired to event `slopx_ireland_events.106` as
`GFX_report_event_ireland_report_presidential_seal`; P-50 and P-54 are registered as
`GFX_ireland_portrait_p_50` and `GFX_ireland_portrait_p_54` from their exact
mapped historical group sources;
the flag, Constitution
symbol, de Valera portrait, and Lemass portrait remain separately registered
for their conditional or character-specific uses. The C4 portrait additions
for Norton, Hyde, Mac Eoin, Aiken, MacEntee, and J. J. Walsh are registered in
`interface/slopx_ireland_sourced_assets.gfx`. The S-01 C3 source-derived flag
set is present at `gfx/flags/IRE.tga`, `gfx/flags/medium/IRE.tga`, and
`gfx/flags/small/IRE.tga`; its attribution and official colour/proportion
conditions remain recorded in the manifest. The 54 complete event/news objects
retain their exact source, attribution, and redistribution conditions in each
manifest record and are registered in
`interface/slopx_ireland_sourced_assets.gfx`. EV-SRC-021, EV-SRC-039, and
EV-SRC-057 use distinct Treaty Port records. Their sprites are registered and
consumed by the existing Cobh inventory, Berehaven and Lough Swilly handover,
and named Treaty Port access events `slopx_ireland_events.110`, `.111`, and
`.254`. EV-SRC-003 remains the H03 legal-document anchor on event `.109`.

## Blockers

The dated bullets below preserve earlier pre-round-12 source-clearance
snapshots for traceability and do not override the current manifest summary at
the top of this file. The current remaining portrait blockers are P-26, P-45,
and P-55; P-15 was conditionally promoted in round 24 from the exact
caption-mapped Catholic Archives object, and P-50 was cleared in round 13 from the exact face-mapped Tom
Barry wedding source, P-54 was cleared in round 14 from the exact
caption-mapped Irish Brigade group photograph, and P-31 was cleared in round 15
from the exact caption-mapped Commission on Vocational Organisation photograph.

- The bounded 2026-07-22 audit of P-15 John Leydon, P-16 Thekla Beere,
  P-24 Luke Duffy, P-26 Patrick Cogan, and P-31 Michael Browne found no exact
  portrait with a compatible rights basis. The
  2026-07-29 C1 recheck advanced P-15, P-24, and P-31 to C2 with exact
  documentary provenance, but did not recover a usable portrait object.
P-16 and P-26 remain blocked records. P-33 and the other formerly review-only
rows are not current manifest review rows; no C3/C4 promotion was made from
this dated recheck. The Commons public-domain claim remains
  conditional because the original photographer and first lawful publication
  are not independently corroborated. The wrong-person Seán Hayes
  crop and the Oireachtas avatar placeholder were discarded. Evidence is
  recorded in `portrait_source_research_P15_P16_P24_P26_P31_P33_2026-07-22.md`
  and `source_research_handoffs/portrait_c1_recheck_2026-07-29.md`. Round-7
  evidence is recorded in `source_research_handoffs/blocked_portraits_round7_2026-07-29.md`.
- Fifteen real-person portraits remain blocked: P-15, P-16, P-24, P-26, P-31,
  P-32, P-38, P-39, P-41, P-45, P-48, P-50, P-54, P-55, and P-57. Thirty-five
  source-backed portrait packages are complete under conditional C3 clearance
  and ten are complete C4 records. Biographical pages remain identity leads
  only; no generated likenesses are allowed. The separate Daniel Morrissey
  route extension remains review-gated and is not part of the 169-row manifest.
- Seven symbol/document packages remain blocked: S-09, S-10, S-12, S-17,
  S-18, S-28, and S-30. Twenty-six are complete C3 conditional records and
  seven are complete C4 records. The promoted C3 rows S-06, S-08, S-15,
  S-20, S-23, S-26, and S-33 are included in the complete set under their
  explicit conditional handoffs; S-07, S-24, and S-27 retain their separate
  earlier conditional records. Their uncertainties are not silently converted
  to C4.
- Fifteen sourced event/news slots remain blocked for lack of an exact cleared
  image object: EV-SRC-006, EV-SRC-008, EV-SRC-009, EV-SRC-024, EV-SRC-026,
  EV-SRC-027, EV-SRC-028, EV-SRC-042, EV-SRC-044, EV-SRC-045, EV-SRC-046,
  EV-SRC-060, EV-SRC-062, EV-SRC-063, and EV-SRC-064. Forty event/news rows
  are complete C3 conditional records and fourteen are complete C4 records.
  EV-SRC-055 remains consumed by H01 `.102`, EV-SRC-059 by F17 `.683`, and
  EV-SRC-004/022/040/041/058 by H04 `.112`-.115 and F15 `.655`; the
  event-source consumer audit records the exact mapping. The manifest keeps
  each remaining row's event family, era-fit requirements, crop target,
  research leads, and rejected alternatives; no blocked row is replaced by
  duplicate, generated, or fallback art.
- The round-seven blocked event/news clearance pass is preserved under
  `assets/ireland_focus_tree/sourced/research_2026-07-29/blocked_event_news_round7/`
  with a 69-file SHA-256 inventory, exact source downloads/copies, per-row
  provenance and negative-search records, and a candidate contact sheet. It
  produced no C4 promotion or final DDS. NCAP historical coastwatching leads
  are rights-review candidates only; DIFP text, UCD NFC manuscripts, Met
  Éireann observation images, and the eISB legal text remain outside runtime.
- The separate route extension `RC-PORTRAIT-01` (Daniel Morrissey) has a source-backed candidate but remains `needs_user_review`; `RC-PORTRAIT-02` (Father Edward Cahill) has no verified portrait object. The clerical route uses a collective Clerical-Lay Guardianship office and emblem, as required by the canonical route specification, rather than an invented individual likeness.
- The machine manifest is the authoritative per-item record; stable IDs, source URLs, rights fields, paths, hashes, and clearance states are the fields used by the implementation audit. The corrected human-readable roster remains in `assets/ireland_focus_tree/source_research/canonical_rosters.md`; source clearance is not inferred from display-name rendering.
