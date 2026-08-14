# Focus inlay background generation prompt

- Feature: `ireland_mechanics_hub`
- Asset: Ireland National Situation focus-tree inlay background
- Source mode: `$imagegen` (generated UI panel art)
- Generation date: 2026-08-14
- Intended canvas: 460x248

```text
Use case: ui-mockup
Asset type: Hearts of Iron IV focus-tree inlay background panel
Primary request: Create one final static, game-ready illustrated background for a compact Ireland National Situation focus-tree inlay. It should read as a restrained 1930s Irish civil-service ledger and pinned summary panel, with deep green leather or painted wood, aged cream paper, restrained brass rules and fasteners, and subtle archival material texture.
Scene/backdrop: A compact horizontal dossier panel seen straight-on, designed to sit beside focus branches and support live UI content.
Subject: The panel frame and surface only; no people, no flags, no portraits, no status icons, no buttons, no labels.
Style/medium: Hand-painted HOI4-style interface background, subdued period-authentic materials, realistic but restrained, clear at small UI size.
Composition/framing: Exact wide 460:248 composition. Strong outer frame with modest leather edge and thin brass rule accents. Keep the central interior and upper title band as clean, low-contrast negative space for a title and six status rows. Leave the bottom edge quiet and evenly toned for two separately rendered buttons. Any decoration must stay in the outer margin and away from likely click regions; no visual noise in the title, row, or button areas.
Lighting/mood: Soft diffuse office light, calm administrative gravity, low contrast across the usable interior, slightly deeper values at edges to separate overlaid text.
Color palette: Deep forest green, near-black green, aged cream, muted parchment, restrained antique brass; no vivid green, amber, red, or grey state signalling.
Materials/textures: Fine worn leather grain, paper fibers, lightly scuffed painted wood, thin brass rules, very subtle pinned-paper impression; polished enough for a final game asset, not grungy.
Text (verbatim): ""
Constraints: No baked text, no readable marks, no labels, no numbers, no flags, no portraits, no icons, no status colours, no button shapes, no ornament inside click regions, no UI widgets, no watermarks, no modern props, no cinematic color grading. Static only. Keep the negative space broad and legible at the final 460x248 size.
Avoid: illegible pseudo-writing, fake typography, decorative seals, heraldic symbols, national emblems, busy paperwork, high-contrast patterns, glowing edges, bevel-heavy fantasy UI, modern interface styling.
```

The generated source was resized locally to the exact runtime canvas and converted to RGBA before DDS conversion. The existing `gfx/interface/ireland/gui/conditions/background.dds` was used as the adjacent-style presentation reference; it was not edited or copied into the final asset.
