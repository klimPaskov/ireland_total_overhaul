# Ireland promoted event-source consumer repair audit

Feature slug: `ireland_focus_tree`
Namespace: `ireland`
Audit date: 2026-08-01
Scope: non-live source, GFX, manifest, and crosswalk review

## Result

The ten C3 event/news packages approved by the project owner have concrete
event consumers. The later EV-SRC-055 and EV-SRC-059 conditional C3 promotions
add two more cleared event/news packages with their own H01 and F17 consumers.
The four newly promoted C4 FRUS neutrality packages are registered with their
own exact sprites, but the current catalogue has no dedicated canonical
consumer references for those four slots; no unrelated consumer was invented.
Each registered consumer uses an Ireland-owned sprite, and each runtime DDS
remains under the standard `gfx/` tree. The staging `assets/` tree is used only
for source and processed evidence.

| Source | Registered sprite | Consumer | Runtime DDS |
|---|---|---|---|
| EV-SRC-020 | `GFX_report_event_ireland_report_constitutional_crisis_report_02` | `events/ireland_events.txt:20130` | `gfx/event_pictures/ireland/event_ev_src_020_report.dds` |
| EV-SRC-023 | `GFX_report_event_ireland_report_constitutional_crisis_report_05` | `events/ireland_events.txt:20221` | `gfx/event_pictures/ireland/ireland_report_constitutional_crisis_report_05.dds` |
| EV-SRC-032 | `GFX_news_event_ireland_news_historical_news_02` | `events/ireland_events.txt:2386` | `gfx/event_pictures/ireland/event_ev_src_032_news.dds` |
| EV-SRC-036 | `GFX_news_event_ireland_news_historical_news_06` | `events/ireland_flavour_events.txt:9680` | `gfx/event_pictures/ireland/event_ev_src_036_news.dds` |
| EV-SRC-037 | `GFX_news_event_ireland_news_historical_news_07` | `events/ireland_events.txt:99` | `gfx/event_pictures/ireland/event_ev_src_037_news.dds` |
| EV-SRC-038 | `GFX_news_event_ireland_news_historical_news_08` | `events/ireland_events.txt:5566` | `gfx/event_pictures/ireland/event_ev_src_038_news.dds` |
| EV-SRC-050 | `GFX_report_event_ireland_report_flavour_family_07` | `events/ireland_flavour_events.txt:13259` | `gfx/event_pictures/ireland/event_ev_src_050_report.dds` |
| EV-SRC-054 | `GFX_report_event_ireland_report_flavour_family_11` | `events/ireland_flavour_events.txt:10019` | `gfx/event_pictures/ireland/event_ev_src_054_report.dds` |
| EV-SRC-056 | `GFX_report_event_ireland_report_flavour_family_13` | `events/ireland_flavour_events.txt:19540` | `gfx/event_pictures/ireland/event_ev_src_056_report.dds` |
| EV-SRC-068 | `GFX_report_event_ireland_report_flavour_family_25` | `events/ireland_flavour_events.txt:18951` | `gfx/event_pictures/ireland/event_ev_src_068_report.dds` |
| EV-SRC-055 | `GFX_report_event_ireland_report_flavour_family_12` | `events/ireland_events.txt` H01 event `ireland_events.102` | `gfx/event_pictures/ireland/ireland_report_flavour_family_12.dds` |
| EV-SRC-059 | `GFX_report_event_ireland_report_flavour_family_16` | `events/ireland_flavour_events.txt` F17 event `ireland_flavour_events.683` (`cork_ports`) | `gfx/event_pictures/ireland/ireland_report_flavour_family_16.dds` |
| EV-SRC-004 | `GFX_report_event_ireland_report_historical_chain_report_04` | no dedicated canonical consumer reference; registration-only until an exact slot is mapped | `gfx/event_pictures/ireland/ireland_report_historical_chain_report_04.dds` |
| EV-SRC-022 | `GFX_report_event_ireland_report_constitutional_crisis_report_04` | no dedicated canonical consumer reference; registration-only until an exact slot is mapped | `gfx/event_pictures/ireland/ireland_report_constitutional_crisis_report_04.dds` |
| EV-SRC-040 | `GFX_news_event_ireland_news_historical_news_10` | no dedicated canonical consumer reference; registration-only until an exact slot is mapped | `gfx/event_pictures/ireland/ireland_news_historical_news_10.dds` |
| EV-SRC-058 | `GFX_report_event_ireland_report_flavour_family_15` | no dedicated canonical consumer reference; registration-only until an exact slot is mapped | `gfx/event_pictures/ireland/ireland_report_flavour_family_15.dds` |

## Crosswalk correction

`docs/plans/ireland_focus_tree/assets/build_asset_coverage_crosswalk.py` now
matches the four Ireland event-sprite naming forms used by the manifest:
the intended name, `GFX_` form, `GFX_report_event_` form, and
`GFX_news_event_` form. The regenerated
`docs/plans/ireland_focus_tree/assets/asset_coverage_crosswalk.md` records the
current consumer line for all ten rows rather than reporting registration-only
coverage.

EV-SRC-055 is now promoted under conditional C3 clearance. Its exact-period
Houses of the Oireachtas Constitution (Consequential Provisions) Bill scan is
registered as `GFX_report_event_ireland_report_flavour_family_12` and consumed
by the H01 constitutional plebiscite/election event. The modern eISB HTML is
retained as supporting legal text; the runtime visual is the source-derived
bill scan and not a placeholder or fallback.

EV-SRC-059 is promoted under conditional C3 clearance from the exact UWM/AGSL
Admiralty Chart 1765 source. The title, survey, UWM rights guidance, public-
domain record, attribution, date ambiguity, and non-navigation disclaimer are
preserved in the manifest and `EV059_UKHO_chart_clearance_2026-08-01.md`; the
runtime image is consumed by the semantically matched F17 Cork ports event.

EV-SRC-004, EV-SRC-022, EV-SRC-040, and EV-SRC-058 are promoted under C4
clearance from four distinct Office of the Historian FRUS records. Their exact
source pages, captures, hashes, processing records, and no-invented-consumer
boundary are preserved in
`assets/source_research_handoffs/EV004_022_040_058_FRUS_neutrality_clearance_2026-08-01.md`.

No live HOI4 launch, in-game test, or save test was run.

## Current consumer reconciliation — 2026-08-02

The five previously registration-only rows are now bound to existing,
semantically matched event records. The four numbered H04 slots are the four
neutrality-chain nodes; the flavour-family row is the existing F15 maritime
neutral-markings node. No event was added, duplicated, or rewired away from an
existing source package.

| Source | Consumer | Binding rationale |
|---|---|---|
| EV-SRC-004 | `events/ireland_events.txt:1090` — `ireland_events.112` | H04 node 1, Emergency War News; official neutrality record anchors the public emergency declaration. |
| EV-SRC-022 | `events/ireland_events.txt:1176` — `ireland_events.113` | H04 node 2, Emergency First Amendment; the official record is a wartime political/neutrality constitutional anchor. |
| EV-SRC-040 | `events/ireland_events.txt:1267` — `ireland_events.114` | H04 node 3, Emergency Powers Act; the record documents neutrality and refusal of territorial access while powers are defined. |
| EV-SRC-041 | `events/ireland_events.txt:1358` — `ireland_events.115` | H04 node 4, Emergency Six Month Review; the 1940 British-port demand is the review's concrete external-pressure record. |
| EV-SRC-058 | `events/ireland_flavour_events.txt:13090` — `ireland_flavour_events.655` | F15 node 6, Neutral Markings; the 1941 friendly-neutral statement is the exact maritime-neutrality flavour anchor. |

The regenerated crosswalk now reports these five source-to-consumer lines,
and the source manifest remains 132 complete / 37 blocked. This addendum
supersedes the registration-only wording above; the dated source handoffs and
clearance states remain unchanged.
