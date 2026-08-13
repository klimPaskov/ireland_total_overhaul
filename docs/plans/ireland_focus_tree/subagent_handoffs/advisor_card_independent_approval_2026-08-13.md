# Ireland advisor-card independent approval — 2026-08-13

## Scope and verdict

This is a read-only independent approval audit of the current Chaos Redux
advisor dossier-card package. It covers the 45 runtime DDS files under
`gfx/interface/ideas/ireland/advisors/`, the current manifest and review
evidence under `docs/plans/ireland_focus_tree/assets/advisors/`, and the
advisor sprite consumers in `interface/ireland_advisors.gfx` and
`common/characters/ireland_route_characters.txt`.

**Verdict: APPROVED for the current runtime-card asset package and independent
visual gate.** No card has a compositing, dimension, alpha-coverage, alignment,
identity, or GFX-coverage blocker. This approval is for the asset package; an
in-game UI load/screenshot was not available to this audit.

No gameplay or asset source was edited. The worktree contains concurrent
parent changes; they were preserved.

## Guidance and evidence consulted

- `AGENTS.md` and `.agents/skills/hoi4-subagents/SKILL.md`.
- `.agents/skills/hoi4-feature-assets/SKILL.md`, including the native
  `65x67` advisor-card and provenance requirements.
- Current Chaos Redux workflow named by the handoff:
  `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/SKILL.md`,
  section 21.1, and its `tools/README.md` advisor/high-command dossier
  section. The inspected compositor is
  `create_advisor_icon.py`; its canonical template hash is retained in the
  current manifest.
- The required offline Paradox wiki core pages and graphical/interface,
  portrait, and idea pages under `paradox_wiki/`, plus the available vanilla
  documentation markdown files.
- Chaos Redux canonical advisor/high-command reference contact sheet:
  `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/advisors/contact_sheet.png`.
- Current package authority:
  `docs/plans/ireland_focus_tree/assets/advisors/manifest_current_chaos_redux_2026-08-13.json`
  and `gfx_handoff_current_chaos_redux_2026-08-13.md`. The older
  `docs/plans/ireland_focus_tree/assets/advisor_icon_handoff_2026-08-03.md`
  is superseded and was not treated as current workflow authority.

## Runtime inventory and DDS/header checks

The current manifest contains 45 cards. The runtime folder contains exactly 45
`.dds` files, with no extra advisor runtime files. Every file independently
checked as follows:

| Check | Result |
| --- | --- |
| DDS magic | `DDS ` for 45/45 |
| Header size | `124` for 45/45 |
| Native dimensions | `65x67` for 45/45 |
| Payload length | `17,548` bytes for 45/45 (`128 + 65*67*4`) |
| Row pitch | `260` bytes for 45/45 |
| Pixel format | 32-bit uncompressed BGRA masks `00FF0000/0000FF00/000000FF/FF000000` for 45/45 |
| Mipmap/caps state | one-level `caps = 0x1000`; no mipmap chain for 45/45 |
| DDS decode | Pillow reopens every file as RGBA `65x67` |
| Preview identity | decoded DDS pixels equal the paired processed preview PNG for 45/45 |
| Manifest hashes | runtime and processed-preview hashes match the current manifest for 45/45 |

All 45 metadata, native previews, nearest-neighbour 4x reviews, placement
studies, and 8x alignment overlays exist. Their observed dimensions are:

- native preview: `65x67` (45/45);
- 4x review: `260x268` (45/45);
- placement study: `284x314` (45/45);
- alignment overlay: `520x536` (45/45).

## Opening geometry, transform, and alpha coverage

The current Chaos Redux template hash is
`8f594ef62afba6fdec58de66a80609350dcfe884320b11e6cb6220f1a0e19f58`.
Independent measurement of that exact template reproduces the manifest values:

- opening center: `(24.76151027919129, 30.645146882359736)`;
- opening size: `(30.477406015014285, 45.09450833210553)`;
- opening rotation: `-4.76` degrees.

All 45 metadata records use the same canonical transform:

- portrait opening-fill size exactly `30.477406015014285 x 45.09450833210553`;
- center offset `(0, 0)` and alignment error `0.0` degrees;
- rotation `-4.76` degrees, with no zero-rotation exception;
- sepia strength `0.18`;
- under-frame bleed `2` px and resampling edge guard `1` px;
- `source_pre_crop = false`, `frame_clip = true`, `stretch = false`;
- exactly one placement-study candidate, matching the selected transform.

I independently re-ran the compositor's read-only alpha-coverage audit against
all decoded runtime cards and the canonical template. Every card reports:

```text
opening_alpha_gap_pixels = 0
inner_edge_alpha_gap_pixels = 0
exterior_alpha_leak_pixels = 0
```

This confirms that the visible opening and translucent inner edge have portrait
coverage, while no portrait pixels escape the verified bleed mask.

## Visual and alignment review

The retained review sheets were inspected at native and nearest-neighbour 4x
scale, with the canonical Chaos Redux reference contact sheet used as the
frame/style comparison:

- `docs/plans/ireland_focus_tree/assets/advisors/contact_sheet_current_2026-08-13.png`
  (`1548x3037`, all 45 labeled cards);
- `contact_sheet_native_2026-08-13.png` (`898x1773`, all 45 native cards);
- `contact_sheet_alignment_8x_2026-08-13.png` (`2848x5373`, all 45 overlays);
- individual files under `review_4x/`, `placement_studies/`, and
  `alignment_8x/`.

The dossier frame, paper plate, irregular silhouette, palette, shadow, and
transparent outer corners are coherent across the set. At 4x, faces and
head-and-shoulders remain readable, the paper does not expose frame holes, and
there is no visible exterior matte/fringe. The alignment sheets show the
measured opening in red, canonical fill plane in green, and uniform covering
portrait in yellow; the lines are consistently coincident with the frame and
the yellow bounds remain within the safe under-frame region. Some inherited
source DDS portraits are visibly low-resolution at 4x, but that is source
quality rather than a current compositor or frame-integrity defect.

The corrected Lemass and Nora overlays were also inspected individually:

- `alignment_8x/advisor_sean_lemass_alignment_8x.png`;
- `alignment_8x/advisor_nora_connolly_obrien_alignment_8x.png`.

Both preserve the expected face/head-and-shoulders composition and the same
canonical frame geometry.

## Identity and provenance

All 45 current manifest cards declare
`grounded_source_only / sourced real person`, and every approved source path
exists. The 43 unchanged DDS sources match a `complete` row in
`docs/plans/ireland_focus_tree/assets/source_manifest.json`; those rows retain
their source URL and rights/license record (43/43 matched, 43/43 with URL and
rights/license evidence).

### Seán Lemass correction

- Current source: `docs/plans/ireland_focus_tree/assets/advisors/source_inputs/sean_lemass_fianna_fail_members_1932_crop.png`;
  opaque RGB `760x1023`, manifest hash
  `5f68f3f4690d286ee91861b5d3697a06013dfb56caea53ef20abd1d799fc324d`.
- Parent image: `sean_lemass_fianna_fail_members_1932.jpg`, `6709x5138`,
  hash `9472b5cdb28a6194cce77ff297657311080564f6cf3527b0b6563edd4f036333`;
  crop box `[3700, 320, 4460, 1343]` reproduces the selected crop dimensions.
- Provenance: Wikimedia Commons file
  `https://commons.wikimedia.org/wiki/File:1932_Fianna_F%C3%A1il_members.jpg`,
  National Library of Ireland catalogue object `vtls000293270`, public-domain
  unknown-author Irish work, dated 1932. The crop is the labeled Lemass sitter.
- The current runtime card visibly retains that sitter's facial geometry and
  clothing. The previous leader DDS
  `gfx/leaders/ireland/leader_sean_lemass.dds` has transparent source-canvas
  pixels (2,941 fully transparent and 980 partial-alpha pixels), which is why
  it was not reused as the card source. No `leader_sean_lemass_opaque.png`
  fallback remains; the selected archival crop is the direct source.

### Nora Connolly O'Brien correction

- Current source: `docs/plans/ireland_focus_tree/assets/advisors/source_inputs/nora_connolly_commons_original_20201121.png`;
  opaque RGBA `346x489`, all alpha values `255`, manifest hash
  `1f319635c37aff7ba4a955660731f9c4cb20ebbdec2a2c64013dbc812e3fa07e`.
- Provenance: Wikimedia Commons file
  `https://commons.wikimedia.org/wiki/File:Nora_Connolly_O%27Brien,_circa_1910s-1920s.png`,
  exact archived revision
  `https://upload.wikimedia.org/wikipedia/commons/archive/4/40/20201121033158%21Nora_Connolly_O%27Brien%2C_circa_1910s-1920s.png`,
  revision timestamp `2020-11-21T03:31:58Z`, source page
  `http://www.weneverforget.org/tag/nora-connolly/`, unknown photographer,
  public-domain PD-US/PD-Ireland basis, circa 1910s–1920s.
- The runtime card visibly preserves the same period portrait and identity. The
  previous leader DDS
  `gfx/leaders/ireland/leader_nora_connolly_obrien.dds` has transparent source-
  canvas pixels (5,495 fully transparent and 1,521 partial-alpha pixels), so it
  was not used as the card source. No generic, generated, or alpha-flattened
  fallback was introduced.

The selected-source decision and the absence of the removed Lemass fallback are
also recorded in `source_inputs/README.md` and the current Chaos Redux GFX
handoff.

## Sprite and consumer coverage

`interface/ireland_advisors.gfx` contains exactly 45 unique
`GFX_ireland_advisor_*` sprite names and 45 unique texture paths. The independent
cross-check found:

- no duplicate sprite names or texture paths;
- every texture path points to an existing DDS in
  `gfx/interface/ideas/ireland/advisors/`;
- no manifest-only or GFX-only card;
- all 45 `small = GFX_ireland_advisor_*` consumers in
  `common/characters/ireland_route_characters.txt` resolve to the same 45
  manifest/GFX entries;
- no stale advisor DDS outside the intended runtime folder.

The corrected consumers remain the stable identifiers
`GFX_ireland_advisor_sean_lemass` and
`GFX_ireland_advisor_nora_connolly_obrien`; no gameplay identifier or portrait
slot was changed by this audit.

## Validation record

Read-only validation used a Python verifier that loaded the current Chaos Redux
`create_advisor_icon.py` measurement and alpha routines without invoking its
writers. It checked manifest/source/runtime/preview hashes, decoded DDS pixels,
headers, dimensions, metadata geometry and flags, alpha coverage, artifact
presence, GFX pairing, and character small-slot references. It returned zero
failures for all 45 cards. `view_image` review covered the three aggregate
contact sheets, canonical reference sheet, and the individual Lemass/Nora 4x
and alignment evidence.

Skipped meaningful validation: a live HOI4 render or save-load test of the
advisor UI was not available through this read-only audit. The parent should
perform the normal live UI check when integrating the concurrent asset changes;
no static evidence indicates a runtime path or DDS-load defect.

## Remaining risks and simplifications

- No implementation simplification or fallback was made in this audit.
- The 43 unchanged sources rely on the prior `complete` source-manifest records
  rather than repeating URL/license fields in the current card manifest; the
  source-manifest cross-check confirms those records are present. Keep that
  source-manifest authority with the package if cards are moved or renamed.
- Visual approval does not certify a live-game UI screenshot; that is the only
  meaningful validation intentionally left to the parent.

## Parent handoff

No asset regeneration or gameplay repair is required from this audit. The
current package can proceed as the approved Chaos Redux advisor-card set, with
the two corrected sourced inputs retained exactly as documented above.
