# Ireland review-row and route-portrait re-audit

Date: 2026-08-01

Status: baseline source-clearance evidence. EV-SRC-041 was subsequently
promoted by the exact FRUS handoff recorded below. The S-24/S-27 dispositions
in this baseline were superseded by the explicit user-approved conditional
promotion recorded in
`assets/source_research_handoffs/event_news_user_approved_conditional_2026-08-01.md`;
the machine manifest and crosswalk are the current status authority.

## Scope and authority

This pass rechecked the five then-remaining `needs_user_review` rows in
`docs/plans/ireland_focus_tree/assets/source_manifest.json` and both entries in
`route_character_portrait_extensions`. The machine manifest remains the source
of truth. The audit does not treat a source page, a processed preview, or an
existing DDS as permission to promote an item. No generated likeness, generic
replacement, period-inaccurate substitute, or fallback was introduced.

At the time of this baseline pass, the canonical manifest totals were 110
`complete`, 2 `needs_user_review`, and 57 `blocked` rows. The two then-remaining
review rows were S-24 and S-27. The separate route-extension review row is
RC-PORTRAIT-01; RC-PORTRAIT-02 remains blocked. EV-SRC-041 is complete under
`assets/source_research_handoffs/EV041_FRUS_clearance_2026-08-01.md`, and
EV-SRC-055 is complete under
`assets/source_research_handoffs/EV055_Oireachtas_clearance_2026-08-01.md`.
EV-SRC-059 is complete under
`assets/source_research_handoffs/EV059_UKHO_chart_clearance_2026-08-01.md`.

## Review dispositions

| ID | Current disposition | Evidence checked | Disposition reason |
| --- | --- | --- | --- |
| S-24 | Baseline C2 / `needs_user_review`; superseded by conditional C3 promotion | Wikimedia Commons file record for *Vexillum Legionis.jpg*; local original and 128x128 processed preview | The record confirms PercioNeto, 11 August 2012, and CC BY-SA 3.0. The physical holding, object date and separate insignia-use boundary remain recorded in the current manifest; the user-approved package is not C4. |
| S-27 | Baseline C2 / `needs_user_review`; superseded by conditional C3 promotion | Wikimedia Commons file record for *Two volunteers for the Irish Local Defence Force aka LDF 02.jpg*; local original and 397x153 processed preview | The record identifies Roe McMahon, circa 1940, the photo album source, and a public-domain/PDM assertion. The image-level accession, photographer lifespan, U.S. status and visible armband evidence remain unresolved; the user-approved package is not C4. |
| EV-SRC-041 | C4 / `complete` (follow-up promotion) | Office of the Historian FRUS 1940 Vol. III, Document 161; official source page, ebook preservation, 1400x900 capture, processed 397x153 crop, runtime DDS | The exact 9 November 1940 record discusses British use of southern Irish ports and Ireland's neutrality. It is explicitly labelled as the 1940 antecedent to the later 1941 claims record. The older RMG chart remains research-only and was not promoted. See `assets/source_research_handoffs/EV041_FRUS_clearance_2026-08-01.md`. |
| EV-SRC-055 | C3 / `complete` (follow-up promotion) | Houses of the Oireachtas scan of the Constitution (Consequential Provisions) Bill 1937, Bill No. 41a, as passed by Dáil Éireann; 210x176 processed crop, runtime DDS, and H01 consumer | The exact-period constitutional-law document is a canonical visual equivalent for flavour family 12. Oireachtas attribution, licence, disclaimer, and third-party exclusions remain attached to the manifest and `assets/source_research_handoffs/EV055_Oireachtas_clearance_2026-08-01.md`; the modern eISB HTML remains supporting legal text, not the runtime image. |
| EV-SRC-059 | C3 / `complete` (follow-up promotion) | UWM/AGSL ContentDM item `agdm/8818`, exact JP2 source, processed 210x176 crop, runtime DDS, and F17 Cork ports consumer | The chart title records Admiralty publication on 23 January 1891 after an 1888 survey; UWM retains its 1898 catalogue record. The underlying UK government chart is recorded as public domain, and UWM’s public-domain guidance supplies the credit/no-permission condition. The chart remains a pre-war geographic context object rather than a 1941 claim facsimile. See `assets/source_research_handoffs/EV059_UKHO_chart_clearance_2026-08-01.md`. |
| RC-PORTRAIT-01 | C3 / `complete` (local-mod scope) | NLI EPH D163 / Wikimedia Commons *Daniel Morrissey 1927.png*, preserved source, processed PNG, and runtime DDS | The Commons record identifies the 1927 image and records a public-domain claim, while the NLI catalogue retains a reproduction-rights notice. The package is complete under the user-approved local-mod scope; retain both NLI/Wikimedia credits and do not present it as unrestricted redistribution. |
| RC-PORTRAIT-02 | C1 / `blocked` | Irish Jesuit Archives identity record; no exact portrait object or cleared image | The identity is historically attested, but no exact portrait source, image licence, or usable period object was found. The clerical route continues to use its collective office portrait; no individual likeness is substituted. |

## External record observations

The Wikimedia record for S-24 identifies the uploader, date, and CC BY-SA 3.0
terms, while the S-27 record identifies the circa-1940 scene, Roe McMahon, the
photo-album source, and a public-domain/PDM assertion. Those facts strengthen
provenance but do not resolve the remaining item-level questions recorded in
the manifest. The Daniel Morrissey record similarly identifies the 1927 NLI
source and a public-domain assertion; it does not remove the NLI reproduction
notice from the clearance decision.

## Runtime and cleanup result

- The follow-up promotions copied only cleared source packages into the
  standard `gfx/` root: EV-SRC-041 under C4 FRUS clearance, EV-SRC-055 under
  conditional C3 Oireachtas clearance, and EV-SRC-059 under conditional C3
  UWM/AGSL chart clearance.
- EV-SRC-055 and EV-SRC-059 each have an Ireland-owned GFX registration and a
  semantically matched event consumer; no unrelated event was rewired.
- Daniel Morrissey's existing source, processed preview, and runtime DDS remain
  preserved; the route lifecycle remains explicit and auditable.
- Father Edward Cahill has no runtime consumer and no invented portrait.
- The two canonical review rows and the two route-extension dispositions
  remain visible in the manifest rather than being hidden behind a false
  completion count.

This audit closes the recheck itself. It does not close source clearance: the
feature remains incomplete until the listed review and blocked decisions are
resolved with compatible source authority or explicit user-approved conditions.
