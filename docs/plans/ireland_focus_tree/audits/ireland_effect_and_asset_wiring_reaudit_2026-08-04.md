# Ireland effect and asset-wiring reaudit

## Focus effects

- Focus inventory: 226 focus blocks.
- Bespoke material rewards: 10 maritime focuses.
- Shared serious reward profiles: 216 focuses.
- Focuses without a material reward after helper expansion: 0.
- Focuses with duplicate standard reward profiles: 0.

The standard calls preserve every existing route flag, proof record, event,
decision unlock, route commitment, ledger update, and cleanup effect. Profiles
add immediate visible resources and do not infer route state.

## Visual reference chain

The audit walks gameplay and GUI consumers through sprite definitions to their
texture files in both the mod and vanilla registries.

- Explicit GFX consumers checked: 861 references / 806 unique sprite names.
- Missing sprite definitions: 0.
- Missing implicit idea-picture sprites: 0.
- Missing mod texture files: 0.
- Duplicate project sprite names: 0 across 1,290 definitions.
- Descriptor `replace_path` entries capable of hiding vanilla assets: 0.
- Images fully decoded through Pillow: 1,088 RGBA assets; failures: 0.

## Player-facing surface inventory

- Focus icon consumers: 227.
- Character large portraits: 67, all 156x210.
- Advisor small cards: 45, all 65x67; this matches the imported Chaos Redux
  workflow and the dominant current vanilla advisor-small contract.
- Idea pictures: 106.
- Decision icons: 212.
- Report-event pictures: 106, using the vanilla 210x176 report surface.
- News-event pictures: 20, using their separately registered news sprites.

No visual source change was warranted: every referenced asset is defined,
present, dimensionally valid for its surface, and decodable. Replacing or
resizing these files would damage valid wiring rather than repair it.

## Tooling limitation

The HOI4 MCP in this desktop session remains bound to the deleted retired-mod
workspace and returns `FOCUS_SOURCE_NOT_FOUND` for the Ireland path. The checks
above therefore use the repository, current vanilla source, official dimensions,
and full binary decode rather than an MCP raster.
