# GFX handoff — Ireland sourced report tranche

The source worker did not edit `.gfx`; the main integration pass registered these five C3-cleared report sprites in `interface/ireland_sourced_assets.gfx`. Their final runtime DDS paths are under `gfx/event_pictures/ireland/`.

```text
GFX_report_event_ireland_report_historical_chain_report_02 -> gfx/event_pictures/ireland/event_ev_src_002_report.dds
GFX_report_event_ireland_report_historical_chain_report_03 -> gfx/event_pictures/ireland/event_ev_src_003_report.dds
GFX_report_event_ireland_report_historical_chain_report_05 -> gfx/event_pictures/ireland/event_ev_src_005_report.dds
GFX_report_event_ireland_report_historical_chain_report_14 -> gfx/event_pictures/ireland/event_ev_src_014_report.dds
GFX_report_event_ireland_report_constitutional_crisis_report_01 -> gfx/event_pictures/ireland/event_ev_src_019_report.dds
```

Ready-to-copy sprite shape, subject to the project's existing event-picture sprite conventions:

```text
spriteType = {
    name = GFX_report_event_ireland_report_historical_chain_report_02
    texturefile = "gfx/event_pictures/ireland/event_ev_src_002_report.dds"
}
```

Repeat the same shape for the other four mappings above. Do not register EV-SRC-004, EV-SRC-006, EV-SRC-007, EV-SRC-008, EV-SRC-009, EV-SRC-010 or EV-SRC-016: their manifest rows are blocked and their final DDS paths are `not_created`.

The complete source, rights, crop and hash record is in [source_research_EV_SRC_002_019_2026-07-22.md](source_research_EV_SRC_002_019_2026-07-22.md).
