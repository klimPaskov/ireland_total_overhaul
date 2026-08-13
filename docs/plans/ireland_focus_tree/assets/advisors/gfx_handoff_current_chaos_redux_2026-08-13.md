# Ireland advisor cards - current Chaos Redux workflow handoff

This handoff supersedes `advisor_icon_handoff_2026-08-03.md` and the copied Ireland workflow. It records the current Chaos Redux `create_advisor_icon.py` run for all 45 stable runtime cards. Independent visual approval is complete and recorded in `../../subagent_handoffs/advisor_card_independent_approval_2026-08-13.md`.

## Current contract

- Tool: `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/tools/create_advisor_icon.py`
- Canonical template: `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/advisors/advisor_template.png` (SHA-256 `8f594ef62afba6fdec58de66a80609350dcfe884320b11e6cb6220f1a0e19f58`).
- Native card: `65x67`; measured opening `30.477406015014285x45.09450833210553`, center `24.76151027919129,30.645146882359736`, rotation `-4.76 degrees`, offset `0 0`.
- Current tool defaults: under-frame bleed `2 px`, resampling edge guard `1 px`, `source_pre_crop=false`, `frame_clip=true`, `stretch=false`; no zero-rotation exception.
- Required evidence per card: native preview, nearest-neighbour 4x review, placement study, 8x red/green/yellow alignment overlay, metadata JSON, and runtime DDS.

## Runtime wiring

- Runtime DDS folder remains `gfx/interface/ideas/ireland/advisors/`.
- Stable runtime basenames and `interface/ireland_advisors.gfx` sprite names are unchanged.
- Main agent owns `.gfx`/gameplay/localisation; this handoff only documents asset outputs.

## Coverage and QA

- 45/45 cards have all required outputs.
- 45/45 native previews are `65x67`; 4x reviews are `260x268`; placement studies are `284x314`; alignment overlays are `520x536`.
- 45/45 runtime DDS outputs are one-level uncompressed BGRA, `65x67`, exact length `17548` bytes, and pixel-identical to native previews after decode.
- Every card reports `opening_alpha_gap_pixels=0`, `inner_edge_alpha_gap_pixels=0`, `exterior_alpha_leak_pixels=0`.
- Contact sheets: `contact_sheet_current_2026-08-13.png`, `contact_sheet_native_2026-08-13.png`, `contact_sheet_alignment_8x_2026-08-13.png`.
- Parent/auditor independent visual approval: **approved** by `docs/plans/ireland_focus_tree/subagent_handoffs/advisor_card_independent_approval_2026-08-13.md`.
- The current contact-sheet header records that completed approval state; it is a review artifact, not a runtime texture.

## Corrected source inputs

- **Sean Lemass**: `source_inputs/sean_lemass_fianna_fail_members_1932_crop.png`, an opaque crop of the labeled 1932 Fianna Fail group photograph. Source URL: `https://commons.wikimedia.org/wiki/File:1932_Fianna_F%C3%A1il_members.jpg`; NLI catalogue `vtls000293270`; public-domain unknown-author Irish work. The old runtime source DDS had transparent canvas alpha and failed current opening coverage; no identity substitution or alpha flattening was used.
- **Nora Connolly O'Brien**: `source_inputs/nora_connolly_commons_original_20201121.png`, the archived 2020-11-21 pre-background-removal revision of the opaque Commons file. Source URL: `https://commons.wikimedia.org/wiki/File:Nora_Connolly_O%27Brien,_circa_1910s-1920s.png`; exact revision: `https://upload.wikimedia.org/wikipedia/commons/archive/4/40/20201121033158%21Nora_Connolly_O%27Brien%2C_circa_1910s-1920s.png`; source page `http://www.weneverforget.org/tag/nora-connolly/`; unknown photographer; circa 1910s-1920s; Commons records PD-US/PD-Ireland. The old runtime source DDS had transparent canvas alpha and failed current opening coverage; no identity substitution or alpha flattening was used.

## Sprite table

| Sprite | Runtime DDS | Native preview | Metadata |
| --- | --- | --- | --- |
| `GFX_ireland_advisor_richard_mulcahy` | `gfx/interface/ideas/ireland/advisors/advisor_richard_mulcahy.dds` | `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_richard_mulcahy.png` | `docs/plans/ireland_focus_tree/assets/advisors/metadata/advisor_richard_mulcahy.json` |
| `GFX_ireland_advisor_sean_lemass` | `gfx/interface/ideas/ireland/advisors/advisor_sean_lemass.dds` | `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_sean_lemass.png` | `docs/plans/ireland_focus_tree/assets/advisors/metadata/advisor_sean_lemass.json` |
| `GFX_ireland_advisor_oscar_traynor` | `gfx/interface/ideas/ireland/advisors/advisor_oscar_traynor.dds` | `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_oscar_traynor.png` | `docs/plans/ireland_focus_tree/assets/advisors/metadata/advisor_oscar_traynor.json` |
| `GFX_ireland_advisor_douglas_hyde` | `gfx/interface/ideas/ireland/advisors/advisor_douglas_hyde.dds` | `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_douglas_hyde.png` | `docs/plans/ireland_focus_tree/assets/advisors/metadata/advisor_douglas_hyde.json` |
| `GFX_ireland_advisor_sean_t_okelly` | `gfx/interface/ideas/ireland/advisors/advisor_sean_t_okelly.dds` | `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_sean_t_okelly.png` | `docs/plans/ireland_focus_tree/assets/advisors/metadata/advisor_sean_t_okelly.json` |
| `GFX_ireland_advisor_frank_aiken` | `gfx/interface/ideas/ireland/advisors/advisor_frank_aiken.dds` | `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_frank_aiken.png` | `docs/plans/ireland_focus_tree/assets/advisors/metadata/advisor_frank_aiken.json` |
| `GFX_ireland_advisor_sean_macentee` | `gfx/interface/ideas/ireland/advisors/advisor_sean_macentee.dds` | `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_sean_macentee.png` | `docs/plans/ireland_focus_tree/assets/advisors/metadata/advisor_sean_macentee.json` |
| `GFX_ireland_advisor_joseph_walshe` | `gfx/interface/ideas/ireland/advisors/advisor_joseph_walshe.dds` | `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_joseph_walshe.png` | `docs/plans/ireland_focus_tree/assets/advisors/metadata/advisor_joseph_walshe.json` |
| `GFX_ireland_advisor_sean_mac_eoin` | `gfx/interface/ideas/ireland/advisors/advisor_sean_mac_eoin.dds` | `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_sean_mac_eoin.png` | `docs/plans/ireland_focus_tree/assets/advisors/metadata/advisor_sean_mac_eoin.json` |
| `GFX_ireland_advisor_thomas_f_ohiggins` | `gfx/interface/ideas/ireland/advisors/advisor_thomas_f_ohiggins.dds` | `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_thomas_f_ohiggins.png` | `docs/plans/ireland_focus_tree/assets/advisors/metadata/advisor_thomas_f_ohiggins.json` |
| `GFX_ireland_advisor_patrick_mcgilligan` | `gfx/interface/ideas/ireland/advisors/advisor_patrick_mcgilligan.dds` | `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_patrick_mcgilligan.png` | `docs/plans/ireland_focus_tree/assets/advisors/metadata/advisor_patrick_mcgilligan.json` |
| `GFX_ireland_advisor_james_everett` | `gfx/interface/ideas/ireland/advisors/advisor_james_everett.dds` | `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_james_everett.png` | `docs/plans/ireland_focus_tree/assets/advisors/metadata/advisor_james_everett.json` |
| `GFX_ireland_advisor_p_20` | `gfx/interface/ideas/ireland/advisors/advisor_p_20.dds` | `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_p_20.png` | `docs/plans/ireland_focus_tree/assets/advisors/metadata/advisor_p_20.json` |
| `GFX_ireland_advisor_james_hickey` | `gfx/interface/ideas/ireland/advisors/advisor_james_hickey.dds` | `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_james_hickey.png` | `docs/plans/ireland_focus_tree/assets/advisors/metadata/advisor_james_hickey.json` |
| `GFX_ireland_advisor_william_davin` | `gfx/interface/ideas/ireland/advisors/advisor_william_davin.dds` | `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_william_davin.png` | `docs/plans/ireland_focus_tree/assets/advisors/metadata/advisor_william_davin.json` |
| `GFX_ireland_advisor_michael_donnellan` | `gfx/interface/ideas/ireland/advisors/advisor_michael_donnellan.dds` | `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_michael_donnellan.png` | `docs/plans/ireland_focus_tree/assets/advisors/metadata/advisor_michael_donnellan.json` |
| `GFX_ireland_advisor_edward_joseph_byrne` | `gfx/interface/ideas/ireland/advisors/advisor_edward_joseph_byrne.dds` | `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_edward_joseph_byrne.png` | `docs/plans/ireland_focus_tree/assets/advisors/metadata/advisor_edward_joseph_byrne.json` |
| `GFX_ireland_advisor_ireland_p_31` | `gfx/interface/ideas/ireland/advisors/advisor_ireland_p_31.dds` | `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_ireland_p_31.png` | `docs/plans/ireland_focus_tree/assets/advisors/metadata/advisor_ireland_p_31.json` |
| `GFX_ireland_advisor_john_charles_mcquaid` | `gfx/interface/ideas/ireland/advisors/advisor_john_charles_mcquaid.dds` | `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_john_charles_mcquaid.png` | `docs/plans/ireland_focus_tree/assets/advisors/metadata/advisor_john_charles_mcquaid.json` |
| `GFX_ireland_advisor_joseph_macrory` | `gfx/interface/ideas/ireland/advisors/advisor_joseph_macrory.dds` | `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_joseph_macrory.png` | `docs/plans/ireland_focus_tree/assets/advisors/metadata/advisor_joseph_macrory.json` |
| `GFX_ireland_advisor_frank_duff` | `gfx/interface/ideas/ireland/advisors/advisor_frank_duff.dds` | `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_frank_duff.png` | `docs/plans/ireland_focus_tree/assets/advisors/metadata/advisor_frank_duff.json` |
| `GFX_ireland_advisor_p_33` | `gfx/interface/ideas/ireland/advisors/advisor_p_33.dds` | `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_p_33.png` | `docs/plans/ireland_focus_tree/assets/advisors/metadata/advisor_p_33.json` |
| `GFX_ireland_advisor_maurice_twomey` | `gfx/interface/ideas/ireland/advisors/advisor_maurice_twomey.dds` | `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_maurice_twomey.png` | `docs/plans/ireland_focus_tree/assets/advisors/metadata/advisor_maurice_twomey.json` |
| `GFX_ireland_advisor_tom_barry` | `gfx/interface/ideas/ireland/advisors/advisor_tom_barry.dds` | `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_tom_barry.png` | `docs/plans/ireland_focus_tree/assets/advisors/metadata/advisor_tom_barry.json` |
| `GFX_ireland_advisor_p_37` | `gfx/interface/ideas/ireland/advisors/advisor_p_37.dds` | `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_p_37.png` | `docs/plans/ireland_focus_tree/assets/advisors/metadata/advisor_p_37.json` |
| `GFX_ireland_advisor_p_42` | `gfx/interface/ideas/ireland/advisors/advisor_p_42.dds` | `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_p_42.png` | `docs/plans/ireland_focus_tree/assets/advisors/metadata/advisor_p_42.json` |
| `GFX_ireland_advisor_sean_macbride` | `gfx/interface/ideas/ireland/advisors/advisor_sean_macbride.dds` | `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_sean_macbride.png` | `docs/plans/ireland_focus_tree/assets/advisors/metadata/advisor_sean_macbride.json` |
| `GFX_ireland_advisor_george_gilmore` | `gfx/interface/ideas/ireland/advisors/advisor_george_gilmore.dds` | `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_george_gilmore.png` | `docs/plans/ireland_focus_tree/assets/advisors/metadata/advisor_george_gilmore.json` |
| `GFX_ireland_advisor_nora_connolly_obrien` | `gfx/interface/ideas/ireland/advisors/advisor_nora_connolly_obrien.dds` | `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_nora_connolly_obrien.png` | `docs/plans/ireland_focus_tree/assets/advisors/metadata/advisor_nora_connolly_obrien.json` |
| `GFX_ireland_advisor_p_51` | `gfx/interface/ideas/ireland/advisors/advisor_p_51.dds` | `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_p_51.png` | `docs/plans/ireland_focus_tree/assets/advisors/metadata/advisor_p_51.json` |
| `GFX_ireland_advisor_patrick_belton` | `gfx/interface/ideas/ireland/advisors/advisor_patrick_belton.dds` | `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_patrick_belton.png` | `docs/plans/ireland_focus_tree/assets/advisors/metadata/advisor_patrick_belton.json` |
| `GFX_ireland_advisor_ernest_blythe` | `gfx/interface/ideas/ireland/advisors/advisor_ernest_blythe.dds` | `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_ernest_blythe.png` | `docs/plans/ireland_focus_tree/assets/advisors/metadata/advisor_ernest_blythe.json` |
| `GFX_ireland_advisor_ireland_p_59` | `gfx/interface/ideas/ireland/advisors/advisor_ireland_p_59.dds` | `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_ireland_p_59.png` | `docs/plans/ireland_focus_tree/assets/advisors/metadata/advisor_ireland_p_59.json` |
| `GFX_ireland_advisor_p_60` | `gfx/interface/ideas/ireland/advisors/advisor_p_60.dds` | `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_p_60.png` | `docs/plans/ireland_focus_tree/assets/advisors/metadata/advisor_p_60.json` |
| `GFX_ireland_advisor_charlie_kerins` | `gfx/interface/ideas/ireland/advisors/advisor_charlie_kerins.dds` | `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_charlie_kerins.png` | `docs/plans/ireland_focus_tree/assets/advisors/metadata/advisor_charlie_kerins.json` |
| `GFX_ireland_advisor_ireland_p_16` | `gfx/interface/ideas/ireland/advisors/advisor_ireland_p_16.dds` | `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_ireland_p_16.png` | `docs/plans/ireland_focus_tree/assets/advisors/metadata/advisor_ireland_p_16.json` |
| `GFX_ireland_advisor_ireland_p_24` | `gfx/interface/ideas/ireland/advisors/advisor_ireland_p_24.dds` | `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_ireland_p_24.png` | `docs/plans/ireland_focus_tree/assets/advisors/metadata/advisor_ireland_p_24.json` |
| `GFX_ireland_advisor_ireland_p_32` | `gfx/interface/ideas/ireland/advisors/advisor_ireland_p_32.dds` | `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_ireland_p_32.png` | `docs/plans/ireland_focus_tree/assets/advisors/metadata/advisor_ireland_p_32.json` |
| `GFX_ireland_advisor_ireland_p_38` | `gfx/interface/ideas/ireland/advisors/advisor_ireland_p_38.dds` | `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_ireland_p_38.png` | `docs/plans/ireland_focus_tree/assets/advisors/metadata/advisor_ireland_p_38.json` |
| `GFX_ireland_advisor_ireland_p_39` | `gfx/interface/ideas/ireland/advisors/advisor_ireland_p_39.dds` | `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_ireland_p_39.png` | `docs/plans/ireland_focus_tree/assets/advisors/metadata/advisor_ireland_p_39.json` |
| `GFX_ireland_advisor_ireland_p_41` | `gfx/interface/ideas/ireland/advisors/advisor_ireland_p_41.dds` | `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_ireland_p_41.png` | `docs/plans/ireland_focus_tree/assets/advisors/metadata/advisor_ireland_p_41.json` |
| `GFX_ireland_advisor_ireland_p_48` | `gfx/interface/ideas/ireland/advisors/advisor_ireland_p_48.dds` | `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_ireland_p_48.png` | `docs/plans/ireland_focus_tree/assets/advisors/metadata/advisor_ireland_p_48.json` |
| `GFX_ireland_advisor_ireland_p_50` | `gfx/interface/ideas/ireland/advisors/advisor_ireland_p_50.dds` | `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_ireland_p_50.png` | `docs/plans/ireland_focus_tree/assets/advisors/metadata/advisor_ireland_p_50.json` |
| `GFX_ireland_advisor_ireland_p_54` | `gfx/interface/ideas/ireland/advisors/advisor_ireland_p_54.dds` | `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_ireland_p_54.png` | `docs/plans/ireland_focus_tree/assets/advisors/metadata/advisor_ireland_p_54.json` |
| `GFX_ireland_advisor_ireland_p_57` | `gfx/interface/ideas/ireland/advisors/advisor_ireland_p_57.dds` | `docs/plans/ireland_focus_tree/assets/advisors/previews/advisor_ireland_p_57.png` | `docs/plans/ireland_focus_tree/assets/advisors/metadata/advisor_ireland_p_57.json` |
