# Ireland source-asset handoff: blocked symbol/document rows S-09, S-10, S-12, S-15, S-17, S-18, S-20, S-23, S-26, S-28, S-30, S-33

Date: 2026-08-02  
Scope: bounded sourced-asset research only  
Runtime/GFX edits: none

Supersession note (2026-08-02): this handoff records the bounded research
snapshot before parent-owned promotions. S-15, S-20, S-23 and S-26 were later
promoted under the conditional approval ledger, and S-33 was separately
cleared from the exact NLI IND_H_3281 photograph and promoted under
`assets/source_research_handoffs/source_clearance_final_pass_2026-08-02.md`.

## Result

All twelve assigned rows now have a concrete historical source, a source tier, an explicit clearance state, a provenance/rights note, a repo-local source file, a processed PNG preview, a converter-produced staged DDS, and a manifest record. The package is:

`assets/ireland_focus_tree/sourced/research_2026-08-02/symbol_clearance_s09_s33/`

The machine-readable package manifest is `manifest.json`; the proposed sprite/runtime handoff is `gfx_handoff.md`; the twelve-image contact sheet is under `contact_sheet/`. The central Ireland source manifest is updated for the same twelve IDs, but runtime final-DDS paths remain unset for the C2/C3 review state. No file was copied to `gfx/interface/ireland/sourced/`.

## Clearance disposition

| ID | Concrete source | State | Main remaining gate |
| --- | --- | --- | --- |
| S-09 | 1948 National Labour leaflet for Sean O'Moore and Frank Robbins, Irish Election Literature | C2 / blocked | 1948 is a later alternate to the preferred scenario window; sender and reproduction permission are unknown |
| S-10 | 1943 Clann na Talmhan / National Agricultural Party leaflet, Irish Election Literature | C2 / blocked | original sender and reproduction permission are unknown |
| S-12 | NLI EPH F27 Easter Lily poster, reproduced on page 59 of the Cumann na mBan heritage booklet | C2 / blocked | NLI object is identified and credited, but reproduction permission is not granted |
| S-15 | circa-1934 Republican Congress masthead record on Wikimedia Commons | C3 / needs user review | Commons PD-text statement applies to the masthead treatment; underlying publication/image chain is not a primary NLI scan |
| S-17 | 7 July 1935 National Corporate Party event advertisement, Irish Election Literature | C2 / blocked | rights and original sender are unknown |
| S-18 | 1944 *Aiséirge Says... The New Order in the New Ireland* cover, Irish Election Literature | C2 / blocked | period object is exact, but image permission is not stated |
| S-20 | 20 March 1918 A.H. Poole/NLI portrait of Éamon de Valera with visible Fáinne | C3 / needs user review | contextual badge crop, not a standalone badge; retain NLI/Poole credit and confirm conditions |
| S-23 | 7 August 1945 NLI Poole photograph from Muintir na Tíre's National Rural Week | C3 / needs user review | exact organization/event context, but not a standalone Muintir mark; retain NLI/Poole credit |
| S-26 | circa-1942 NLI “Yours for the keeping” LSF/LDF recruiting poster | C2 / blocked | Irish Defence Forces owns reproduction rights and Flickr record is All Rights Reserved |
| S-28 | 1941 LOP 17 Coast Watching Service logbook entry reproduced in official An Cosantóir | C2 / blocked | official publication/archive provenance is strong, but image reuse terms are not stated |
| S-30 | 1940 Marine Service officer Lt. Billy Richardson photograph, History Ireland | C2 / blocked | photographer/archive and reuse permission are not stated |
| S-33 | November 1939 DFArchives photograph of the Spike Island map, tied to the 1938 Treaty-Port handover | C2 / blocked | source is CC BY-NC-ND 2.0; the processed crop is a derivative and cannot be cleared under ND terms |

## Source and processing notes

- S-09 and S-10 use period election leaflets from the named Irish Election Literature pages. Their pages explicitly provide historical identity/date context but do not provide an image licence; both remain C2.
- S-12 uses the exact Easter Lily poster identified in the booklet caption as NLI EPH F27 / `vtls000511268`; the rendered page 59 is retained beside the original PDF so the crop does not become an invented replacement.
- S-15 uses a documented circa-1934 Republican Congress masthead, not the rejected modern Starry Plough SVG or a generic flag photograph.
- S-20 and S-23 use NLI on The Commons period photographs. The NLI/Commons records provide the named photographer/archive context and no-known-restrictions/CC0 record, but both remain conditional review items because the intended crops are contextual rather than standalone object scans.
- S-26 uses the exact NLI recruiting poster; its stated rights owner and All Rights Reserved status are preserved rather than inferred away.
- S-28 uses the logbook image reproduced on official Defence Forces magazine page 44, with the older Michael Kennedy/M&N Coastwatching paper retained as research context. It is a documentary crop, not a modern lookout-post photograph.
- S-30 uses the exact 1940 Marine Service context described in the History Ireland caption; no current Naval Service badge was substituted.
- S-33 uses the period Spike Island map photograph. The explicit CC BY-NC-ND 2.0 licence is the reason it remains blocked despite the strong historical fit; the modern Commons Treaty-Port redraw remains rejected.

The staged DDS files were produced with `.agents/skills/hoi4-feature-assets/tools/convert_to_dds.py` at the recorded target sizes. They are review artifacts only and must not be wired or promoted without the clearance state changing.

## Main-agent handoff

1. Review `manifest.json` for source URLs, hashes, credits, crop semantics, and conditions.
2. Use the contact sheet and processed PNGs for visual review.
3. Do not copy the staged DDS files into the runtime `gfx` tree while a row is C2 or while a C3 condition is unaccepted.
4. If a row is approved, copy/rename only that row's staged DDS to the proposed runtime path and wire the proposed sprite name in the existing `.gfx` surface. This subagent intentionally did not perform those edits.

No gameplay, event, focus, localisation, GUI, `.gfx`, or unrelated asset files were changed by this handoff.
