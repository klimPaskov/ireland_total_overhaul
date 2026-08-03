# Ireland focus tree: bounded six-portrait source audit

> Historical bounded research snapshot. These six rows remain blocked in the
> authoritative 2026-07-29 manifest. The package-wide counts recorded below
> were correct on 2026-07-22 but are superseded by the current 47 complete,
> 31 review-gated, and 91 blocked source entries. P-15, P-24, and P-31 now
> carry C2 documentary provenance, but still have no usable portrait object.

Date: 2026-07-22
Scope: P-15, P-16, P-24, P-26, P-31, and P-33 only.

## Result

No exact real-person portrait met the required identity and rights bar. All six manifest rows remain unchanged at `status: blocked` and `clearance_state: C1 provenance identified`; no source original, processed PNG, or DDS was created for this batch. No substitute, statue, reenactment, generated likeness, or modern wrong-person image was retained.

The canonical vanilla leader reference was checked at `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/` and its contact sheet; the target presentation remains 156x210 with an identity-preserving upper-torso/face crop.

## Evidence by canonical row

| ID | Current status | Evidence checked | Blocking reason |
| --- | --- | --- | --- |
| P-15 John Leydon | `blocked / C1` unchanged | Catholic Archives identifies an Irish delegation group photograph containing John Leydon and credits Keystone Press: [catalogue browse](https://catholicarchives.co.uk/index.php/informationobject/browse?onlyMedia=1&page=295&repos=55727&sf_culture=en&showAdvanced=1&sort=relevance&sortDir=asc&topLod=0). | Exact individual portrait/crop, photographer object, and reuse permission were not established. The archival/photo lead is not a rights-cleared source asset. |
| P-16 Thekla Beere | `blocked / C1` unchanged | The Irish Times identifies a photograph of Thekla Beere with Patrick Hillery and credits Jimmy McCormack: [article](https://www.irishtimes.com/business/economy/2022/09/23/john-fitzgerald-taliban-like-marriage-bar-held-back-the-nations-economy/). TARA provides an identity biography but not a reusable portrait object: [Biographical Portraits](https://www.tara.tcd.ie/bitstreams/8bd2acbd-80ce-48a4-a68a-02fad6fff382/download). | The exact press photograph is commercially held; no compatible reuse permission was found. The TARA and National Archives records are identity/text leads only. |
| P-24 Luke Duffy | `blocked / C1` unchanged | Ballymote Heritage Group reproduces a 1912 IDAA group and a c.1920s Luke Duffy photograph, both credited “courtesy of Drapers Assistant Mandate Archive”: [The Corran Herald issue 53](https://ballymoteheritage.com/wp-content/uploads/2022/04/The-Corran-Herald-issue-53-2020-2021.pdf). | The exact image is a courtesy reproduction in a secondary PDF, without an identified reusable licence or direct archive permission. It was not extracted or packaged. |
| P-26 Patrick Cogan | `blocked / C1` unchanged | The official [Oireachtas member record](https://www.oireachtas.ie/en/members/member/Patrick-Cogan.D.1938-06-30/) exposes an image endpoint, but the retrieved object was only a generic 80x80 avatar placeholder, not Patrick Cogan. Oireachtas reuse terms also exclude third-party image rights: [copyright and reuse](https://www.oireachtas.ie/en/copyright-and-reuse/) and [open-data licence](https://www.oireachtas.ie/en/open-data/license/). | No exact portrait object was obtained. The placeholder download was deleted and is not a source candidate. |
| P-31 Michael Browne | `blocked / C1` unchanged | The name is identity-ambiguous between Michael Browne, Bishop of Galway (1895–1980) ([NLI correspondence record](https://catalogue.nli.ie/Collection/vtls000823240/HierarchyTree?recordID=vtls000823240)), and Michael Browne, Dominican cardinal (1887–1971) ([biographical lead](https://en.wikipedia.org/wiki/Michael_Browne_%28cardinal%29)). A Commons image lead titled “Bishop Browne Consecrating St. Colman's Cathedral 1919” depicts Robert Browne, not Michael Browne. | No exact person disambiguation plus rights-cleared portrait was established. No image was retained. |
| P-33 John Hayes | `blocked / C1` unchanged | The tempting public-domain [Commons crop](https://commons.wikimedia.org/wiki/File:Sean_Hayes,_1927_(cropped).jpg) is identified through its page usage as Seán Hayes, the Tipperary politician (1890–1968), not the canonical Cork figure. The canonical person’s birth name is John Hayes in the [Cork biography](https://en.wikipedia.org/wiki/Se%C3%A1n_Hayes_%28Cork_politician%29); the NLI’s [First Dáil group-photo record](https://catalogue.nli.ie/Record/vtls000532931) identifies John Hayes (West Cork), but does not provide a compatible reuse grant. | The public-domain crop is the wrong person and was deleted. The exact NLI object remains rights-uncleared, so no package was made. |

## Package and count audit

- No files were added under `assets/ireland_focus_tree/sourced/`.
- The two temporary review downloads (the Patrick Cogan avatar placeholder and the wrong-person Seán Hayes crop) were deleted.
- This subagent did not modify `docs/plans/ireland_focus_tree/assets/source_manifest.json`; all six rows still have `source_path`, `processed_png_path`, and `final_dds_path` set to `not_created`.
- Manifest totals remain 169 entries: 34 complete, 28 needs-user-review, 107 blocked; clearance counts remain C1 107, C3 42, C4 20. All five clearance-state definitions remain present.

## Remaining risks / next evidence needed

The rows can move only after an archive or rights holder supplies an exact object and a written or clearly documented reuse basis: an individual John Leydon image, a licensed Thekla Beere photograph, permission for the Luke Duffy archive reproduction, a real Patrick Cogan portrait rather than the Oireachtas placeholder, disambiguated Michael Browne identity plus rights, or the NLI John Hayes object with a usable licence/permission. The Tipperary Seán Hayes Commons file must not be reused for P-33.
