# Ireland portrait clearance handoff — 2026-07-22

> Historical research snapshot. The authoritative 2026-07-29 portrait family
> contains 60 rows: 11 complete, 30 `needs_user_review`, and 19 blocked.
> P-37, P-59, and P-60 were recovered after this handoff; their originals are
> preserved under `docs/portraits/research_2026-07-29/`. P-59 is C4-complete;
> P-37 and P-60 remain review-gated. The current
> `docs/plans/ireland_focus_tree/assets/source_manifest.json` overrides every
> historical count below.

## Scope and disposition

This handoff covers only the remaining real-person portrait source research. Its original batch remains C3/review-gated as described below. A later parent integration pass separately validated five already-packaged exact Commons objects and promoted them to C4 in the authoritative manifest; that promotion is recorded here so this handoff is not mistaken for the current count.

## Parent integration addendum — 2026-07-22

The authoritative manifest now records 9 complete portraits, 28 C3 portraits needing user review, and 23 blocked portraits. The five promoted C4 entries are:

| ID | Person | Source basis | Runtime registration |
| --- | --- | --- | --- |
| P-07 | William Norton | NLI Record vtls000544361; anonymous-author public-domain Commons record | `GFX_slopx_ireland_portrait_william_norton` |
| P-08 | Douglas Hyde | 1903 *The Cabinet of Irish Literature* scan; Commons No Known Copyright Restrictions record | `GFX_slopx_ireland_portrait_douglas_hyde` |
| P-10 | Seán Mac Eoin | RTÉ source; unknown-author circa-1922 Commons record with Irish/US public-domain basis | `GFX_slopx_ireland_portrait_sean_mac_eoin` |
| P-11 | Frank Aiken | British Pathé 1933 newsreel frame; Commons UK/US public-domain record | `GFX_slopx_ireland_portrait_frank_aiken` |
| P-12 | Seán MacEntee | British Pathé 1933 newsreel frame; Commons UK/US public-domain record | `GFX_slopx_ireland_portrait_sean_macentee` |

Each promoted row now records source URL(s), source hash, processed/final paths, final DDS hash, crop, target size, source tier, credit, and clearance state in `docs/plans/ireland_focus_tree/assets/source_manifest.json`. P-09 remains review-gated because the Harris & Ewing rights chain is jurisdiction-sensitive; P-13 remains review-gated because its NLI Flickr Commons record is a no-known-restrictions record rather than an explicit unrestricted grant.

The manifest currently records:

- 60 canonical portraits: 9 complete, 28 `needs_user_review`, and 23 `blocked`.
- 2 route-character portrait extensions: `RC-PORTRAIT-01` already `needs_user_review`; `RC-PORTRAIT-02` is blocked.
- The 16 packages from the 2026-07-19 handoff are now reconciled: five are C4 and eleven remain C3 `needs_user_review`; they were not replaced or reprocessed.

This pass researched the 34 blocked canonical rows without an existing package and the blocked `RC-PORTRAIT-02` extension. It produced 11 conditional packages, all at C3 (`cleared with conditions` / `needs_user_review`). No item was marked C4 (`cleared unrestricted`).

| disposition | count | IDs |
| --- | ---: | --- |
| New C3 source packages | 11 | `P-14`, `P-17`, `P-18`, `P-19`, `P-22`, `P-25`, `P-28`, `P-30`, `P-36`, `P-40`, `P-53` |
| Remaining canonical rows without a package | 23 | `P-15`, `P-16`, `P-20`, `P-24`, `P-26`, `P-31`, `P-32`, `P-33`, `P-35`, `P-37`, `P-38`, `P-39`, `P-41`, `P-42`, `P-45`, `P-48`, `P-50`, `P-51`, `P-54`, `P-55`, `P-57`, `P-59`, `P-60` |
| Remaining blocked route extension | 1 | `RC-PORTRAIT-02` — Father Edward Cahill |
| New C4 unrestricted packages | 5 | `P-07`, `P-08`, `P-10`, `P-11`, `P-12` |

The batch metadata is [portrait_clearance_metadata_2026-07-22.json](../../../../assets/ireland_focus_tree/sourced/metadata/portrait_clearance_metadata_2026-07-22.json). It contains source, archive, author, date, rights, crop, hash, output, sprite, and uncertainty fields for each of the 11 packaged records.

## Clearance and source-tier rules

The 11 packaged items are C3 only. They are usable as review-ready candidates, not as unrestricted release assets. Each requires source credit retention and a parent/user decision on derivative use and redistribution. A Commons public-domain or “no known restrictions” template is recorded as evidence, but it is not treated as an automatic C4 grant for this project.

Where Commons is the access layer, the table records the underlying source separately. The package uses the manifest’s source-tier vocabulary: NLI holdings are tier 3, university/library collections are tier 4, press archives are tier 8, published books are tier 9, open web sources are tier 11, and Commons is treated as the tier-7 digitised access layer rather than as a replacement for the underlying source.

All final portraits use the real source subject and the feature-assets `leader` processor at 156x210. No face, person, emblem, or institutional scene was generated. Low-resolution and halftone sources are explicitly flagged for visual review.

## New source-backed packages

Each row links the exact file record and the underlying holding or immediate source. Paths are relative to the repository root.

### P-14 — Joseph Walshe — C3

- Exact source: [Wikimedia Commons file](https://commons.wikimedia.org/wiki/File:Joseph_Walshe,_1922_(cropped).jpg); access copy [direct image](https://upload.wikimedia.org/wikipedia/commons/e/e9/Joseph_Walshe%2C_1922_%28cropped%29.jpg).
- Holding/source: [NLI Flickr Commons record](https://www.flickr.com/photos/nlireland/53209638691/), Kathleen McKenna-Napoli photographic collection, NLI ref. NPA MKN11; original photographer credited as Fotografia Felici; dated 1922.
- Rights note: Commons records “No restrictions”; retain NLI/source credit and keep C3 pending project review.
- Outputs: `source_originals/portrait_joseph_walshe_1922_nli.jpg`, `processed_png/leader_joseph_walshe.png`, `gfx/leaders/ireland/leader_joseph_walshe.dds`.
- Sprite: `ireland_portrait_p_14`; crop `[0, 0, 270, 360]`.
- Uncertainty: The file is already a crop from an NLI group/image record; verify NLI/Flickr Commons derivative-use treatment before distribution.

### P-17 — Thomas F. O'Higgins — C3

- Exact source: [Wikimedia Commons file](https://commons.wikimedia.org/wiki/File:Thomas_F._O%27Higgins,_circa_1933.jpg); access copy [direct image](https://upload.wikimedia.org/wikipedia/commons/0/05/Thomas_F._O%27Higgins%2C_circa_1933.jpg).
- Immediate source: Maurice Manning, *The Blueshirts*; original photographer/source not established; circa 1933.
- Rights note: Commons marks the file public domain, but the original author and first-publication chain are unknown.
- Outputs: `source_originals/portrait_thomas_f_ohiggins_1933.jpg`, `processed_png/leader_thomas_f_ohiggins.png`, `gfx/leaders/ireland/leader_thomas_f_ohiggins.dds`.
- Sprite: `ireland_portrait_p_17`; crop `[0, 0, 364, 396]`.
- Uncertainty: The centered subject is exact, but the image is a group photograph and the photographer is unknown; retain C3.

### P-18 — Patrick McGilligan — C3

- Exact source: [Wikimedia Commons file](https://commons.wikimedia.org/wiki/File:Patrick_McGilligan_1925.jpg); access copy [direct image](https://upload.wikimedia.org/wikipedia/commons/e/e4/Patrick_McGilligan_1925.jpg).
- Immediate source: Mark Tierney, *Ireland Since 1870*; original source/author not established; dated 1925.
- Rights note: Commons marks the file public domain, but the underlying publication and author chain remain incomplete.
- Outputs: `source_originals/portrait_patrick_mcgilligan_1925.jpg`, `processed_png/leader_patrick_mcgilligan.png`, `gfx/leaders/ireland/leader_patrick_mcgilligan.dds`.
- Sprite: `ireland_portrait_p_18`; crop `[0, 0, 650, 762]`.
- Uncertainty: Review the Commons public-domain basis and project redistribution treatment before use.

### P-19 — James Everett — C3

- Exact source: [Wikimedia Commons file](https://commons.wikimedia.org/wiki/File:James_Everett,_1949.jpg); access copy [direct image](https://upload.wikimedia.org/wikipedia/commons/a/a6/James_Everett%2C_1949.jpg).
- Holding/source: Irish Press, 22 December 1949, via the [Irish Newspaper Archive](https://archive-irishnewsarchive-com); author credited as unknown photographer, Irish Press.
- Rights note: Commons marks the file public domain; keep the Irish Press/archive credit and review press-source terms.
- Outputs: `source_originals/portrait_james_everett_1949.jpg`, `processed_png/leader_james_everett.png`, `gfx/leaders/ireland/leader_james_everett.dds`.
- Sprite: `ireland_portrait_p_19`; crop `[0, 0, 491, 973]`.
- Uncertainty: The 1949 newspaper halftone is coarse and the photographer is unknown. It is an intentional late-1940s source for this roster, not a WWII-era substitute.

### P-22 — James Hickey — C3

- Exact source: [Wikimedia Commons file](https://commons.wikimedia.org/wiki/File:James_Hickey,_1937.jpg); access copy [direct image](https://upload.wikimedia.org/wikipedia/commons/f/f8/James_Hickey%2C_1937.jpg).
- Immediate source: [Irish Election Literature](https://irishelectionliterature.com/2015/02/24/choose-hickey-for-cork-city-james-hickey-labour-1937-general-election-cork-borough/); unknown photographer; circa 1937.
- Rights note: Commons records public domain in the United States and under its unknown-author Irish-work treatment; this remains C3.
- Outputs: `source_originals/portrait_james_hickey_1937.jpg`, `processed_png/leader_james_hickey.png`, `gfx/leaders/ireland/leader_james_hickey.dds`.
- Sprite: `ireland_portrait_p_22`; crop `[0, 0, 251, 335]`.
- Uncertainty: Exact crop is usable but only 251x335 and sourced through a secondary web archive.

### P-25 — Michael Donnellan — C3

- Exact source: [Wikimedia Commons file](https://commons.wikimedia.org/wiki/File:Michael_Donnellan,_circa_1944.jpg); access copy [direct image](https://upload.wikimedia.org/wikipedia/commons/2/27/Michael_Donnellan%2C_circa_1944.jpg).
- Holding/source: Connacht Tribute, 20 May 1944, via the [Irish Newspaper Archive record](https://archive-irishnewsarchive-com.ezproxy.slv.vic.gov.au/Olive/APA/INA.Edu/Default.aspx#panel=document).
- Rights note: Commons marks the file public domain; original publication and author-lifespan evidence are incomplete.
- Outputs: `source_originals/portrait_michael_donnellan_1944.jpg`, `processed_png/leader_michael_donnellan.png`, `gfx/leaders/ireland/leader_michael_donnellan.dds`.
- Sprite: `ireland_portrait_p_25`; crop `[0, 0, 166, 280]`.
- Uncertainty: The exact source is only 166 pixels wide and the archive link is proxy-gated; visual and rights review are required.

### P-28 — Edward Joseph Byrne — C3

- Exact source: [Wikimedia Commons file](https://commons.wikimedia.org/wiki/File:Edward_Joseph_Byrne_archbishop_of_Dublin.jpg); access copy [direct image](https://upload.wikimedia.org/wikipedia/commons/f/fe/Edward_Joseph_Byrne_archbishop_of_Dublin.jpg).
- Immediate source: [CHOMI Irish charity letters project](http://www.chomi.org/irish-charity-letters-1922-1940/); unknown author; image caption identifies Byrne as Archbishop of Dublin in 1932.
- Rights note: Commons marks the anonymous work public domain; the web project is not an identified formal archive or rights grant.
- Outputs: `source_originals/portrait_edward_joseph_byrne_1932.jpg`, `processed_png/leader_edward_joseph_byrne.png`, `gfx/leaders/ireland/leader_edward_joseph_byrne.dds`.
- Sprite: `ireland_portrait_p_28`; crop `[0, 0, 420, 550]`.
- Uncertainty: Exact person/date are supported, but creator and source-project rights are not independently established.

### P-30 — Joseph MacRory — C3

- Exact source: [Wikimedia Commons NLI file](https://commons.wikimedia.org/wiki/File:Cardinal_MacRory_October_7,_1930.jpg); access copy [direct image](https://upload.wikimedia.org/wikipedia/commons/c/c8/Cardinal_MacRory_October_7%2C_1930.jpg).
- Holding/source: [NLI Flickr Commons record](https://www.flickr.com/photos/nlireland/6219229141/), NLI ref. IND_H_1411; photographed 7 October 1930; credited to National Library of Ireland on The Commons.
- Rights note: Commons records “No restrictions” / no known copyright restrictions; retain C3 because this is not a project-specific written grant.
- Outputs: `source_originals/portrait_joseph_macrory_1930_nli.jpg`, `processed_png/leader_joseph_macrory.png`, `gfx/leaders/ireland/leader_joseph_macrory.dds`.
- Sprite: `ireland_portrait_p_30`; crop `[145, 20, 491, 486]` from the 661x486 NLI landscape source.
- Uncertainty: The exact NLI source is low-contrast and landscape; parent visual approval is required.

### P-36 — Tom Barry — C3

- Exact source: [Wikimedia Commons cropped file](https://commons.wikimedia.org/wiki/File:Tom_Barry,_August_1921_(cropped)_(cropped).png); access copy [direct image](https://upload.wikimedia.org/wikipedia/commons/b/b7/Tom_Barry%2C_August_1921_%28cropped%29_%28cropped%29.png).
- Holding/source: [National Library of Ireland catalogue record](https://catalogue.nli.ie/Record/vtls000812410); Keogh Brothers Ltd; 21 August 1921.
- Rights note: Commons marks the extracted crop public domain; retain the NLI catalogue/creator credit and review derivative-use terms.
- Outputs: `source_originals/portrait_tom_barry_1921_nli.png`, `processed_png/leader_tom_barry.png`, `gfx/leaders/ireland/leader_tom_barry.dds`.
- Sprite: `ireland_portrait_p_36`; crop `[0, 0, 265, 353]`.
- Uncertainty: The source is a crop from a group wedding photograph; the subject is clear, but the project should verify the NLI reproduction terms.

### P-40 — Charles Kerins — C3

- Exact source: [Wikimedia Commons file](https://commons.wikimedia.org/wiki/File:Charlie_Kerins,_circa_1930s.jpg); access copy [direct image](https://upload.wikimedia.org/wikipedia/commons/c/cc/Charlie_Kerins%2C_circa_1930s.jpg).
- Immediate source: [Danny Morrison historical source](https://www.dannymorrison.com/1249/); unknown author; circa 1930s (Commons metadata gives 1938).
- Rights note: Commons marks the file public domain under its unknown-author Irish-work treatment; retain C3.
- Outputs: `source_originals/portrait_charlie_kerins_1930s.jpg`, `processed_png/leader_charlie_kerins.png`, `gfx/leaders/ireland/leader_charlie_kerins.dds`.
- Sprite: `ireland_portrait_p_40`; crop `[43, 0, 267, 300]`.
- Uncertainty: Exact identity is supported, but source is a low-resolution secondary web image with unknown author.

### P-53 — Patrick Belton — C3

- Exact source: [Wikimedia Commons file](https://commons.wikimedia.org/wiki/File:Patrick_Belton,_1933.jpg); access copy [direct image](https://upload.wikimedia.org/wikipedia/commons/3/3a/Patrick_Belton%2C_1933.jpg).
- Holding/source: [National Library of Ireland catalogue record](http://catalogue.nli.ie/Record/vtls000121648); creator credited as P. F. O'Reilly, 66 Dame Street, Dublin; 1933.
- Rights note: Commons marks the file public domain; retain the NLI catalogue/creator credit and review scan/derivative terms.
- Outputs: `source_originals/portrait_patrick_belton_1933.jpg`, `processed_png/leader_patrick_belton.png`, `gfx/leaders/ireland/leader_patrick_belton.dds`.
- Sprite: `ireland_portrait_p_53`; crop `[0, 0, 300, 400]`.
- Uncertainty: The NLI object and credited creator are identified, but project reproduction treatment still needs review.

## Still blocked or requiring a higher clearance state

### C2 review holds — no output files created

These are exact or near-exact source leads that cannot be packaged under the C3 workflow because the source terms are restrictive or materially unclear. They remain blocked in the canonical manifest, which was not edited.

- `P-20` William O'Brien — [Commons record](https://commons.wikimedia.org/wiki/File:William_O%27Brien_1922.jpg) points to the [Trinity College Dublin digital collection](https://digitalcollections.tcd.ie/concern/parent/zg64tn45h/works/sb397977q). The source metadata states that images are for single-use academic application and prohibits publication, transmission, or display without formal written approval. No source original, PNG, or DDS was created. Written TCD permission is required.
- `P-32` Alfred O'Rahilly — exact 1949 [UCC portrait object](https://www.ucc.ie/en/heritage/collections/portrait-james-sinton-sleator-prha-1885-1950-alfred-orahilly.html) by James Sinton Sleator, ref. `UCCHS.Portrait007`; the page is © University College Cork. No download or derivative was created. UCC permission is required. A different Constitution Committee group image was rejected because the source page says O'Rahilly and Kevin O'Shiel were absent from that session.
- `P-59` J. J. Walsh — the [Irish Times cabinet-group source](https://www.irishtimes.com/culture/books/what-drove-those-who-ruled-ireland-after-the-founding-of-the-free-state-1.1670817) identifies a Walshe/Topical Press Agency/Getty image. This is a commercial/press rights lead, not an unrestricted portrait object; no file was downloaded or processed.
- `P-60` Oliver J. Flanagan — [Irish Election Literature source](https://irishelectionliterature.com/2013/12/13/some-oliver-j-flanagan-pictures-newspaper-cuttings-and-leaflets/) exposes postwar newspaper pictures/cuttings but no clear exact image licence or unrestricted archival object. No file was downloaded or processed.

### C1 provenance leads still without an exact cleared image object

The following rows retain their manifest C1 (`provenance identified`) / blocked disposition. Identity or archive leads exist, but no exact period portrait with usable source object and rights evidence was found in this pass:

`P-15` John Leydon; `P-16` Thekla Beere; `P-24` Luke Duffy; `P-26` Patrick Cogan; `P-31` Michael Browne; `P-33` John Hayes; `P-35` Maurice Twomey; `P-37` Seán Russell; `P-38` Stephen Hayes; `P-39` Hugh McAteer; `P-41` Harry White; `P-42` Jim O'Donovan; `P-45` Mick Fitzpatrick; `P-48` Roddy Connolly; `P-50` Michael Price; `P-51` Seán Murray; `P-54` P. J. Coughlan; `P-55` Liam D. Walsh; and `P-57` Tomás Ó Dochartaigh.

Specific rejection notes:

- `P-37`: modern photographs of Seán Russell's statue were rejected; they are not a real-person portrait source.
- `P-38`: NLI finding-aid leads identify papers but did not expose a downloadable, rights-cleared portrait object.
- `P-42`: identity pages were found, but no exact archival portrait with reuse terms.
- `P-55`: an Irish Times historical article is a text lead, not a source image with clearance.

### Route extension — C1 blocked

- `RC-PORTRAIT-02` Father Edward Cahill remains blocked. The [Irish Jesuit Archives identity page](https://jesuitarchives.ie/cahill-edward-1868-1941-jesuit-priest) establishes the person and dates but does not expose an exact downloadable portrait or reuse terms. A located RTÉ Archives item was a letter scan, not a portrait, and was rejected as a likeness substitute. No source original, PNG, or DDS was created.

## Untouched prior packages and excluded rows

The following 16 existing source-backed candidate packages from the 2026-07-19 handoff were preserved untouched: `P-07`, `P-08`, `P-09`, `P-10`, `P-11`, `P-12`, `P-13`, `P-21`, `P-23`, `P-29`, `P-34`, `P-44`, `P-47`, `P-49`, `P-52`, `P-58`.

Excluded by the request because they were already complete or review-gated: complete `P-01`–`P-04`; review-gated `P-05`, `P-06`, `P-27`, `P-43`, `P-46`, `P-56`; and review-gated `RC-PORTRAIT-01` Daniel Morrissey. The clerical route is a collective Clerical-Lay Guardianship presentation and was not treated as an individual portrait.

## Asset and GFX handoff

Created under `assets/ireland_focus_tree/sourced/`:

- 11 source originals under `source_originals/`.
- 11 processed 156x210 PNGs and 11 processor metadata JSON files under `processed_png/`.
- 11 final DDS files under `gfx/`, generated with `convert_to_dds.py` at 156x210.
- 11 per-asset review sheets under `review/`.
- [portrait_clearance_contact_sheet_2026-07-22.png](../../../../assets/ireland_focus_tree/sourced/review/portrait_clearance_contact_sheet_2026-07-22.png).
- [portrait_clearance_metadata_2026-07-22.json](../../../../assets/ireland_focus_tree/sourced/metadata/portrait_clearance_metadata_2026-07-22.json).

Canonical sprite names and final files:

| sprite name | final DDS |
| --- | --- |
| `ireland_portrait_p_14` | `gfx/leaders/ireland/leader_joseph_walshe.dds` |
| `ireland_portrait_p_17` | `gfx/leaders/ireland/leader_thomas_f_ohiggins.dds` |
| `ireland_portrait_p_18` | `gfx/leaders/ireland/leader_patrick_mcgilligan.dds` |
| `ireland_portrait_p_19` | `gfx/leaders/ireland/leader_james_everett.dds` |
| `ireland_portrait_p_22` | `gfx/leaders/ireland/leader_james_hickey.dds` |
| `ireland_portrait_p_25` | `gfx/leaders/ireland/leader_michael_donnellan.dds` |
| `ireland_portrait_p_28` | `gfx/leaders/ireland/leader_edward_joseph_byrne.dds` |
| `ireland_portrait_p_30` | `gfx/leaders/ireland/leader_joseph_macrory.dds` |
| `ireland_portrait_p_36` | `gfx/leaders/ireland/leader_tom_barry.dds` |
| `ireland_portrait_p_40` | `gfx/leaders/ireland/leader_charlie_kerins.dds` |
| `ireland_portrait_p_53` | `gfx/leaders/ireland/leader_patrick_belton.dds` |

Suggested target for canonical wiring remains the existing project-selected `.gfx` file, per the manifest. No `.gfx` file was edited. Parent integration must keep every item at C3 until the source/credit review is complete; do not wire any C2/C1 item or imply that a missing manifest update means the row is complete.
