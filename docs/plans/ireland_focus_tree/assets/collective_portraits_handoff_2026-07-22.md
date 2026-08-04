# Ireland Focus Tree — Collective Portrait Asset Handoff

Date: `2026-07-22`

Feature slug: `ireland_focus_tree`

Asset worker scope: `assets/ireland_focus_tree/generated/collective_portraits/` and `gfx/leaders/ireland/collective_*.dds`, plus this handoff.

Package result: `handed_off`

Main integration (2026-07-22): all fourteen sprite definitions are registered in `interface/ireland_route_assets.gfx`, and all fourteen institutional offices are represented in `common/characters/ireland_route_characters.txt`. Route activation recruits the relevant office portrait while retaining sourced historical characters where the route has a real founder or organiser; route-leader cleanup retires unused institutional candidates with the rest of the route transition.

Exactly 14 distinct fictional institutional/collective leader-style portraits were generated, processed, and converted. No real-person likenesses, historical documents, historical symbols, fallbacks, reused stills, `.gfx` edits, or gameplay edits were used.

## Wiring handoff

- Source mode for every portrait: `$imagegen` built-in generation.
- Final portrait size: `156x210`.
- Proposed sprite names: `GFX_IRE_<concept_id>`.
- Suggested target registry: `interface/_leader_portraits.gfx`; preserve the repository’s existing leader-portrait registration convention when wiring.
- Exact texture path for each sprite is the final DDS path listed below.
- These are institutional/collective portraits. Use institutional leader names; do not assign a random personal name pool or gender metadata from these images.
- All item statuses: `handed_off`.
- Blockers: none.

## Per-item file inventory

Hashes are SHA-256. `source_png` is the generated source; `processed_png` is the deterministic 156x210 preview; `dds` is the final runtime texture.

### `collective_army_council`

- Sprite: `GFX_IRE_collective_army_council`
- `assets/ireland_focus_tree/generated/collective_portraits/source_png/collective_army_council.png` — `1086x1448`, 2041835 bytes, `fbcafcec0d38c8c9eb54e59c4a6c6262da2a56cbc621e8f01e655c19af18266f`, `handed_off`.
- `assets/ireland_focus_tree/generated/collective_portraits/processed_png/collective_army_council.png` — `156x210`, 48281 bytes, `1bb7bae59a54858187c7580e73cdd5703c05f6cffd816ce3e2d5b37d37b7ed83`, `handed_off`.
- `gfx/leaders/ireland/collective_army_council.dds` — `156x210`, 131168 bytes, `d06f9be2c5bb0d81d5034a14b8f2cf627ef66b2cb5f36fb67bd2bc71d9c471ae`, `handed_off`.

### `collective_civil_republican_directorate`

- Sprite: `GFX_IRE_collective_civil_republican_directorate`
- `assets/ireland_focus_tree/generated/collective_portraits/source_png/collective_civil_republican_directorate.png` — `1086x1448`, 2286857 bytes, `120330d7417de74cdb0af2d29461cdf745afe067b10f46fc8aca3850657c72ae`, `handed_off`.
- `assets/ireland_focus_tree/generated/collective_portraits/processed_png/collective_civil_republican_directorate.png` — `156x210`, 52430 bytes, `5f1e4ba1cbcfe4c45d2968f6dc06d55f38dcfe4909d5c61bf05e9f820deea3a9`, `handed_off`.
- `gfx/leaders/ireland/collective_civil_republican_directorate.dds` — `156x210`, 131168 bytes, `6f6a09ded2153c99875030ee44317ada5ab434b462421c82f29ff9fbdf331a09`, `handed_off`.

### `collective_workers_party`

- Sprite: `GFX_IRE_collective_workers_party`
- `assets/ireland_focus_tree/generated/collective_portraits/source_png/collective_workers_party.png` — `1086x1448`, 2272991 bytes, `e0c53fb0ba2c66e7084f843e3b19cf0578f9ef3e8f066f482db390557c9ee5ed`, `handed_off`.
- `assets/ireland_focus_tree/generated/collective_portraits/processed_png/collective_workers_party.png` — `156x210`, 52529 bytes, `23846f7cf0072c7e8dd191ed4b6ab650f8ba84d49d90bddf500f054953c3731b`, `handed_off`.
- `gfx/leaders/ireland/collective_workers_party.dds` — `156x210`, 131168 bytes, `556850bf5f242fa0b25a9d5a46a965e1f2e97877c88026dbdf9a7a9ea4a2e945`, `handed_off`.

### `collective_workers_smallholders`

- Sprite: `GFX_IRE_collective_workers_smallholders`
- `assets/ireland_focus_tree/generated/collective_portraits/source_png/collective_workers_smallholders.png` — `1086x1448`, 2289643 bytes, `fdd173b1721c4067b1777adf35ef5643ceb17b346d1c70ca8d875a1cc59c826e`, `handed_off`.
- `assets/ireland_focus_tree/generated/collective_portraits/processed_png/collective_workers_smallholders.png` — `156x210`, 52210 bytes, `43ab77ad966b7f6f28591a93101da2bb52134243537091c8e91bf0f669f92014`, `handed_off`.
- `gfx/leaders/ireland/collective_workers_smallholders.dds` — `156x210`, 131168 bytes, `ead8c51ee54597a27870cb44f45819fa135cefae33877baacea7eb4a6e73eabc`, `handed_off`.

### `collective_corporate_estate`

- Sprite: `GFX_IRE_collective_corporate_estate`
- `assets/ireland_focus_tree/generated/collective_portraits/source_png/collective_corporate_estate.png` — `1086x1448`, 2125431 bytes, `a0543ce92051fe9af2c3f06c3cfce329782b0ea9b2eda2f3fed566ea91b78ef2`, `handed_off`.
- `assets/ireland_focus_tree/generated/collective_portraits/processed_png/collective_corporate_estate.png` — `156x210`, 51906 bytes, `229069536e2c872eed4f3c63a03e1cea952553901c3b40c8bda38410c7b07a37`, `handed_off`.
- `gfx/leaders/ireland/collective_corporate_estate.dds` — `156x210`, 131168 bytes, `68acc3a43ce1e6792a3eefea6371e67f5942c85bc2de905876c10aaba9c2e1d8`, `handed_off`.

### `collective_oduffy_command`

- Sprite: `GFX_IRE_collective_oduffy_command`
- `assets/ireland_focus_tree/generated/collective_portraits/source_png/collective_oduffy_command.png` — `1086x1448`, 2113742 bytes, `2d7d55443b7b0e2c354ae8e813015904f997fe952b6e03ca136cc01e4a0f9d01`, `handed_off`.
- `assets/ireland_focus_tree/generated/collective_portraits/processed_png/collective_oduffy_command.png` — `156x210`, 57132 bytes, `23b7b0a3b56ed3de99d44e65deaf7b5d300b8ee95b43a111c5153e0c785666e1`, `handed_off`.
- `gfx/leaders/ireland/collective_oduffy_command.dds` — `156x210`, 131168 bytes, `1d9ec2ea7b24f2bd6221062571d8a2ad22242f29dc5123964cfe4225cb1ae6af`, `handed_off`.

### `collective_clerical_guardianship`

- Sprite: `GFX_IRE_collective_clerical_guardianship`
- `assets/ireland_focus_tree/generated/collective_portraits/source_png/collective_clerical_guardianship.png` — `1086x1448`, 2261618 bytes, `ab3e48db7295e33a673d46ba4f3f42eedcccf3b3c6d7b18bfd53e03dc3f5ec30`, `handed_off`.
- `assets/ireland_focus_tree/generated/collective_portraits/processed_png/collective_clerical_guardianship.png` — `156x210`, 57327 bytes, `8b436c50eff64335dc47302f86386a0d733d25082d7f5e34f3b178ef736ebc10`, `handed_off`.
- `gfx/leaders/ireland/collective_clerical_guardianship.dds` — `156x210`, 131168 bytes, `ffdc966263943f699c454c884410d00ecb1a724a46915a43b35e0e6f1f97773d`, `handed_off`.

### `collective_gaelic_corporate`

- Sprite: `GFX_IRE_collective_gaelic_corporate`
- `assets/ireland_focus_tree/generated/collective_portraits/source_png/collective_gaelic_corporate.png` — `1086x1448`, 2280520 bytes, `43ecd4a2e5b60bef95bcca782483a393f9158e24fb0d6bdc20dc0361e3819c2c`, `handed_off`.
- `assets/ireland_focus_tree/generated/collective_portraits/processed_png/collective_gaelic_corporate.png` — `156x210`, 53462 bytes, `66cd9858c7595a3182599b81494bfbd57772dfcf5a1ff1d25c7c03b736adf43d`, `handed_off`.
- `gfx/leaders/ireland/collective_gaelic_corporate.dds` — `156x210`, 131168 bytes, `759d4ddec461ad2ce08fb3f02f0e6d2888eb2da2d0fe34bbffbf89fcbf85822b`, `handed_off`.

### `collective_christian_national`

- Sprite: `GFX_IRE_collective_christian_national`
- `assets/ireland_focus_tree/generated/collective_portraits/source_png/collective_christian_national.png` — `1086x1448`, 2276241 bytes, `7c5c186d8685f30b9d3cbfc6ef4c8beddf5b4c2102e3284e3f49e29b9a3eeef2`, `handed_off`.
- `assets/ireland_focus_tree/generated/collective_portraits/processed_png/collective_christian_national.png` — `156x210`, 52210 bytes, `439960421fbbd7643540cce010f67f35a0fbfa50dc050d3fcd61370eabbc7623`, `handed_off`.
- `gfx/leaders/ireland/collective_christian_national.dds` — `156x210`, 131168 bytes, `d5afe938c671c3ed68a36a8cb85235c6060f807e50df343d6cea01846794f59f`, `handed_off`.

### `collective_regional_ailtiri`

- Sprite: `GFX_IRE_collective_regional_ailtiri`
- `assets/ireland_focus_tree/generated/collective_portraits/source_png/collective_regional_ailtiri.png` — `1086x1448`, 2370946 bytes, `8cdb3287497b3a517349ca25e3459cc2a1007df569a78feab06d0833009fb1a7`, `handed_off`.
- `assets/ireland_focus_tree/generated/collective_portraits/processed_png/collective_regional_ailtiri.png` — `156x210`, 58835 bytes, `97aa2f81ac7bc37e414d2afee07ccfdf525b4c2db8e35807f6638cb619d481d0`, `handed_off`.
- `gfx/leaders/ireland/collective_regional_ailtiri.dds` — `156x210`, 131168 bytes, `236fe720dda522593f45a3be2dd412fe713a0cef382a0bc118d3130ed4658506`, `handed_off`.

### `collective_ailtiri_state`

- Sprite: `GFX_IRE_collective_ailtiri_state`
- `assets/ireland_focus_tree/generated/collective_portraits/source_png/collective_ailtiri_state.png` — `1086x1448`, 2006952 bytes, `338e4703f6e7f669be4d5df0a4e9d727ded0773f13712466b2dcde4cbf0762bf`, `handed_off`.
- `assets/ireland_focus_tree/generated/collective_portraits/processed_png/collective_ailtiri_state.png` — `156x210`, 53175 bytes, `f95a797218c637f3951a5082566af8fc6f56ca42e78eab04ade8293cf4967ef5`, `handed_off`.
- `gfx/leaders/ireland/collective_ailtiri_state.dds` — `156x210`, 131168 bytes, `2249ce433209930f0751420d2dbace9dccd16dddc30a4775caa6c8e37b7f510f`, `handed_off`.

### `collective_high_king_sacral`

- Sprite: `GFX_IRE_collective_high_king_sacral`
- `assets/ireland_focus_tree/generated/collective_portraits/source_png/collective_high_king_sacral.png` — `1086x1448`, 2363472 bytes, `3f2f0de2d8526760c0a2a73d8c88401e3c511f5d582eec4647b3ea22712b61bb`, `handed_off`.
- `assets/ireland_focus_tree/generated/collective_portraits/processed_png/collective_high_king_sacral.png` — `156x210`, 54550 bytes, `368533130973eed980424c00de1adaaed240e6252b43ddbcf99c8adf63ac481c`, `handed_off`.
- `gfx/leaders/ireland/collective_high_king_sacral.dds` — `156x210`, 131168 bytes, `89a20c3521efe785b634053d61a6cb38c8c45cd228543ff5fe91b89530eac458`, `handed_off`.

### `collective_five_provinces`

- Sprite: `GFX_IRE_collective_five_provinces`
- `assets/ireland_focus_tree/generated/collective_portraits/source_png/collective_five_provinces.png` — `1085x1450`, 2207093 bytes, `d5d49db6fab148e7b5ec3bb7ef7bd5431d4aeb6c929ec0b02b7749e76ca3dfbb`, `handed_off`.
- `assets/ireland_focus_tree/generated/collective_portraits/processed_png/collective_five_provinces.png` — `156x210`, 49653 bytes, `f96f0c77e98cf7a379adb207072b0d968abff346aec9799d5727efb6d5b06d62`, `handed_off`.
- `gfx/leaders/ireland/collective_five_provinces.dds` — `156x210`, 131168 bytes, `fbcce9bb2715da4285f3ec2c4f2bd4b59a5c50d252ca687acffa21e7d87dfa37`, `handed_off`.

### `collective_otherworld_compact`

- Sprite: `GFX_IRE_collective_otherworld_compact`
- `assets/ireland_focus_tree/generated/collective_portraits/source_png/collective_otherworld_compact.png` — `1086x1448`, 1988456 bytes, `0fe486776b0160cb3612cbdfdb9675aafddc4e1c7660277c8ba58b0d4e8b52c5`, `handed_off`.
- `assets/ireland_focus_tree/generated/collective_portraits/processed_png/collective_otherworld_compact.png` — `156x210`, 57384 bytes, `a46e0fa2faee32c58400805b9ed0aa8ec9f90aeda201d9e9ef470e4627cdd9f4`, `handed_off`.
- `gfx/leaders/ireland/collective_otherworld_compact.dds` — `156x210`, 131168 bytes, `8066098883b2e2750013fdc57fa0f6d21029d3f499e2b215dcf7c2958a16efb3`, `handed_off`.

## Package-control files

- `assets/ireland_focus_tree/generated/collective_portraits/contact_sheet.png` — `1360x1200`, 811450 bytes, SHA-256 `7c16d2e61a17f4f8b7f5146e6dc4bb1c313abfa0627ab99f2d33f19372c89a21`, `handed_off`.
- `assets/ireland_focus_tree/generated/collective_portraits/manifest.md` — documentation file, 18372 bytes, SHA-256 `bd27112a25983e0b3edc03d521ef740dce9db0663039e4dc922f85bcceb492b5`, `handed_off`.
- `docs/plans/ireland_focus_tree/assets/collective_portraits_handoff_2026-07-22.md` — this handoff; its final SHA-256 is reported separately because including a file’s own hash would be self-referential.

## Validation evidence

- `14` source PNGs present; all generated through the built-in imagegen path.
- `14` processed PNGs present at exactly `156x210`.
- `14` DDS files present under `gfx/leaders/ireland/` with exact canonical `collective_*.dds` names and `131168` bytes each, matching the repository’s 32-bit uncompressed portrait output size.
- Contact sheet reviewed at processed scale; all 14 concepts are visually distinct and readable.
- DDS conversion used only the repository-standard `convert_to_dds.py` workflow.
- No blockers, no omitted concepts, no substitutions, and no unrelated files were changed.
