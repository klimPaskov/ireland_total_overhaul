# Ireland runtime integration audit — 2026-07-28

Feature slug: `ireland_focus_tree`  
Namespace: `ireland`  
Runtime root: `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/ireland_total_overhaul`

## Disposition

This audit separates final runtime implementation from temporary asset staging. Final
DDS/TGA files belong under `gfx/`; `assets/ireland_focus_tree/` remains the source,
generation, contact-sheet, provenance, and audit workspace.

The integration tranche promotes the Ireland runtime files that are present and
structurally registered:

| Surface | Promoted files |
| --- | ---: |
| Gameplay/runtime source (`common/`, `history/`, `localisation/`) | 14 |
| Interface/GFX registrations | 6 |
| Event/news art | 78 DDS |
| Route flags | 57 TGA |
| Animated packages | 14 DDS |
| Decision categories/actions/missions | 137 DDS |
| Spirits | 63 DDS |
| Ireland emblems, route flags, GUI surfaces, and mechanic ledger | 162 DDS |
| Cleared real-person portraits | 38 DDS |
| Shared 216-focus shine overlay | 1 DDS |

The 68 source-manifest outputs present in the runtime tree are all C3
(`cleared with conditions`) or C4 (`cleared for unrestricted project use`). The
runtime references were checked against the local `gfx/` tree: the nine Ireland
`.gfx` files contain 1,528 texture references and none resolve to a missing local
file.

## Clearance boundary

The machine-readable source manifest remains authoritative:
`docs/plans/ireland_focus_tree/assets/source_manifest.json`.

- 48 C3 outputs are retained only with the attribution or source conditions recorded
  in the per-item manifest.
- 20 C4 outputs are unrestricted within the project clearance record.
- The 101 C1/C2 rows without a final output remain excluded. No review-blocked image
  was substituted with a generated likeness.
- `gfx/leaders/ireland/leader_daniel_morrissey.dds` remains staging-only because its
  route extension is explicitly `needs_user_review`.
- Source originals, review candidates, rejected crops, and blocked research leads
  remain under `assets/` and are not runtime references.

Generated art in the promoted set is limited to alternate, fictional, symbolic,
supernatural, or otherwise impossible material. The icon-specific regeneration and
all-family inspection are recorded in
`docs/plans/ireland_focus_tree/assets/icon_surface_audit_2026-07-28.md`.

## Non-live verification

This audit does not launch HOI4 and does not treat live in-game testing as a goal
completion gate, per the user instruction. It records the static checks that can be
performed without the game executable: local texture-reference resolution, source
clearance disposition, runtime/staging separation, and the registered asset counts.
Local Clausewitz parsing, MCP GUI diagnostics, source clearance, AI behavior, and
scenario execution remain separate completion gates recorded in the project status
ledger.
