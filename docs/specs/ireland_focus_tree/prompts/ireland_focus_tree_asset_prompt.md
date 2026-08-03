# Ireland Focus Tree Asset Production Prompt

Feature slug: `ireland_focus_tree`

Read the canonical Part 6 asset ledger and the repository asset, animation and subagent skills before production. This prompt creates asset packages. It does not edit gameplay, localisation, GUI or GFX files unless the parent explicitly grants that narrow scope.

## Source routing

Use `hoi4_asset_source_researcher` for every real person, historical flag, attested symbol, document, site and real photographed event. Use `hoi4_icon_artist` for focus, idea, decision, category, mission, achievement, law and mechanic icons. Use `hoi4_generated_feature_art` for alternate flags, fictional councils, generated event scenes, hidden interfaces and impossible actors. Use `hoi4-frame-animation` for the seven approved animations.

Never generate a real leader portrait. Never present generated art as archival. Record source, date, archive, author, licence confidence, era fit and uncertainty for sourced assets.


## Source clearance workflow

Every sourced item uses one of exactly five clearance states from the canonical asset ledger: `C0 discovered only`, `C1 provenance identified`, `C2 restricted or review pending`, `C3 cleared with conditions`, or `C4 cleared for unrestricted project use`. Catalogue discovery never counts as permission. No final DDS may be produced from `C0`, `C1`, or `C2` material. `C3` material must carry every attribution and distribution condition into the package.

Search in the ledger's exact eleven-tier source hierarchy. Prefer the highest-confidence holding source that has usable rights. An open-web mirror can identify an item but cannot establish provenance, date, authenticity, ownership, or licence. Trace it to the holding archive before selection.

Every per-item source manifest must record the holding source, catalogue or object identifier, creator, date or date range, source URL, rights holder, licence or permission, clearance state, required credit, intended crop and use, uncertainty, rejected alternatives, source path, processed path, final DDS path, intended sprite name, and whether controlled reuse is approved.

## Exact budget

- 60 sourced real-person portraits
- 14 institutional or collective portraits
- 1 historical base flag set
- 18 alternate flag sets
- 8 faction or regional-order emblems
- at least 216 focus icons
- 13 category icons
- 70 decision icons
- 54 mission icons
- 63 persistent spirit state icons
- 27 temporary state icons
- 51 law icons
- 45 mechanic and value icons
- 32 achievement concepts with normal, grey and not-eligible states
- 120 unique event and news images, 69 sourced and 51 generated
- 3 scripted GUI asset families
- 7 animated assets with static fallbacks

## Reference folders

Inspect the matching repositories under `.agents/skills/hoi4-feature-assets/assets/` for ideas, focuses, decisions, achievements, flags, report images and news images. Match framing, scale, contrast, texture and readability. Do not use a uniform recolour batch as a complete icon family.

## Placement

Use feature-scoped folders under the correct category where engine conventions allow. Keep achievement DDS files in `gfx/achievements/` with filenames matching full achievement IDs. Keep flags in the large, medium and small flag roots with valid tag or cosmetic-tag filenames.

## Animation briefs

Produce independent source frames for the hidden evidence seal, Ailtirí takeover seal, High Kingship crown selection, Five Provinces compact, verified Otherworld entry, compact breach warning and convergence conclusion seal. Local scripts may align, crop, resize, sheet and convert frames. They may not create final motion from transforms or filters. Produce source frames, processed frames, horizontal sheet PNG, final DDS, static fallback, contact sheet, GIF preview and GFX handoff.

## Manifests and QA

Every asset records source mode, intended use, dimensions, final path, sprite name, related route or event, licence or generation prompt, uncertainty, and controlled-reuse status. Every sourced asset also records the complete clearance and per-item source manifest fields above. Reject modern reenactments, film stills, wrong-era material, fake historical documents, white-halo transparency and unreadable icons. Placeholder art does not satisfy the ledger.
