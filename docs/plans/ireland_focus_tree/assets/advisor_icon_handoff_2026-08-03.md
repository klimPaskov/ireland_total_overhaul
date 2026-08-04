# Ireland advisor icon handoff

Generated 2026-08-03 for the Ireland Total Overhaul advisor roster.

## Imported Chaos Redux workflow

- Source script: `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/tools/create_advisor_icon.py`
- Source template: `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/advisors/advisor_template.png`
- Ireland script copy: `assets/ireland_focus_tree/advisor_workflow/create_advisor_icon.py`
- Ireland template copy: `assets/ireland_focus_tree/advisor_workflow/advisor_template.png`
- Template SHA-256: `8F594EF62AFBA6FDEC58DE66A80609350DCFE884320B11E6CB6220F1A0E19F58`
- Native advisor card size: `65x67`
- Generation parameters: `--portrait-size 50 65 --portrait-offset 0 0 --rotation 0 --sepia-strength 0.18`
- The Ireland script retains the template compositing and DDS verification workflow; its Pillow pixel iteration uses `getdata()` for compatibility with the bundled Pillow runtime.

## Runtime wiring

- Character `small` portrait slots are updated in `common/characters/ireland_route_characters.txt`.
- The original `large` portrait slots remain source-side full portraits.
- Card sprites are registered in `interface/ireland_advisors.gfx`.
- Generated DDS cards live in `gfx/interface/ideas/ireland/advisors/`.
- Preview PNGs live in `docs/plans/ireland_focus_tree/assets/advisors/previews/`.
- The unprefixed `sean_lemass.png` file is a smoke-test preview only; it is not referenced by the game.

## Complete source map

| Advisor card sprite | Source portrait | Generated card |
|---|---|---|
| `GFX_ireland_advisor_richard_mulcahy` | `gfx/leaders/ireland/leader_richard_mulcahy.dds` | `advisor_richard_mulcahy.dds` |
| `GFX_ireland_advisor_sean_lemass` | `gfx/leaders/ireland/leader_sean_lemass.dds` | `advisor_sean_lemass.dds` |
| `GFX_ireland_advisor_oscar_traynor` | `gfx/leaders/ireland/leader_oscar_traynor.dds` | `advisor_oscar_traynor.dds` |
| `GFX_ireland_advisor_douglas_hyde` | `gfx/leaders/ireland/leader_douglas_hyde.dds` | `advisor_douglas_hyde.dds` |
| `GFX_ireland_advisor_sean_t_okelly` | `gfx/leaders/ireland/leader_sean_t_okelly.dds` | `advisor_sean_t_okelly.dds` |
| `GFX_ireland_advisor_frank_aiken` | `gfx/leaders/ireland/leader_frank_aiken.dds` | `advisor_frank_aiken.dds` |
| `GFX_ireland_advisor_sean_macentee` | `gfx/leaders/ireland/leader_sean_macentee.dds` | `advisor_sean_macentee.dds` |
| `GFX_ireland_advisor_joseph_walshe` | `gfx/leaders/ireland/leader_joseph_walshe.dds` | `advisor_joseph_walshe.dds` |
| `GFX_ireland_advisor_sean_mac_eoin` | `gfx/leaders/ireland/leader_sean_mac_eoin.dds` | `advisor_sean_mac_eoin.dds` |
| `GFX_ireland_advisor_thomas_f_ohiggins` | `gfx/leaders/ireland/leader_thomas_f_ohiggins.dds` | `advisor_thomas_f_ohiggins.dds` |
| `GFX_ireland_advisor_patrick_mcgilligan` | `gfx/leaders/ireland/leader_patrick_mcgilligan.dds` | `advisor_patrick_mcgilligan.dds` |
| `GFX_ireland_advisor_james_everett` | `gfx/leaders/ireland/leader_james_everett.dds` | `advisor_james_everett.dds` |
| `GFX_ireland_advisor_p_20` | `gfx/leaders/ireland/leader_p_20.dds` | `advisor_p_20.dds` |
| `GFX_ireland_advisor_james_hickey` | `gfx/leaders/ireland/leader_james_hickey.dds` | `advisor_james_hickey.dds` |
| `GFX_ireland_advisor_william_davin` | `gfx/leaders/ireland/leader_william_davin.dds` | `advisor_william_davin.dds` |
| `GFX_ireland_advisor_michael_donnellan` | `gfx/leaders/ireland/leader_michael_donnellan.dds` | `advisor_michael_donnellan.dds` |
| `GFX_ireland_advisor_edward_joseph_byrne` | `gfx/leaders/ireland/leader_edward_joseph_byrne.dds` | `advisor_edward_joseph_byrne.dds` |
| `GFX_ireland_advisor_ireland_p_31` | `gfx/leaders/ireland/leader_p_31.dds` | `advisor_ireland_p_31.dds` |
| `GFX_ireland_advisor_john_charles_mcquaid` | `gfx/leaders/ireland/leader_john_charles_mcquaid.dds` | `advisor_john_charles_mcquaid.dds` |
| `GFX_ireland_advisor_joseph_macrory` | `gfx/leaders/ireland/leader_joseph_macrory.dds` | `advisor_joseph_macrory.dds` |
| `GFX_ireland_advisor_frank_duff` | `gfx/leaders/ireland/leader_frank_duff.dds` | `advisor_frank_duff.dds` |
| `GFX_ireland_advisor_p_33` | `gfx/leaders/ireland/leader_p_33.dds` | `advisor_p_33.dds` |
| `GFX_ireland_advisor_maurice_twomey` | `gfx/leaders/ireland/leader_maurice_twomey.dds` | `advisor_maurice_twomey.dds` |
| `GFX_ireland_advisor_tom_barry` | `gfx/leaders/ireland/leader_tom_barry.dds` | `advisor_tom_barry.dds` |
| `GFX_ireland_advisor_p_37` | `gfx/leaders/ireland/leader_p_37.dds` | `advisor_p_37.dds` |
| `GFX_ireland_advisor_p_42` | `gfx/leaders/ireland/leader_p_42.dds` | `advisor_p_42.dds` |
| `GFX_ireland_advisor_sean_macbride` | `gfx/leaders/ireland/leader_sean_macbride.dds` | `advisor_sean_macbride.dds` |
| `GFX_ireland_advisor_george_gilmore` | `gfx/leaders/ireland/leader_george_gilmore.dds` | `advisor_george_gilmore.dds` |
| `GFX_ireland_advisor_nora_connolly_obrien` | `gfx/leaders/ireland/leader_nora_connolly_obrien.dds` | `advisor_nora_connolly_obrien.dds` |
| `GFX_ireland_advisor_p_51` | `gfx/leaders/ireland/leader_p_51.dds` | `advisor_p_51.dds` |
| `GFX_ireland_advisor_patrick_belton` | `gfx/leaders/ireland/leader_patrick_belton.dds` | `advisor_patrick_belton.dds` |
| `GFX_ireland_advisor_ernest_blythe` | `gfx/leaders/ireland/leader_ernest_blythe.dds` | `advisor_ernest_blythe.dds` |
| `GFX_ireland_advisor_ireland_p_59` | `gfx/leaders/ireland/leader_j_j_walsh.dds` | `advisor_ireland_p_59.dds` |
| `GFX_ireland_advisor_p_60` | `gfx/leaders/ireland/leader_p_60.dds` | `advisor_p_60.dds` |
| `GFX_ireland_advisor_charlie_kerins` | `gfx/leaders/ireland/leader_charlie_kerins.dds` | `advisor_charlie_kerins.dds` |
| `GFX_ireland_advisor_ireland_p_16` | `gfx/leaders/ireland/leader_p_16.dds` | `advisor_ireland_p_16.dds` |
| `GFX_ireland_advisor_ireland_p_24` | `gfx/leaders/ireland/leader_p_24.dds` | `advisor_ireland_p_24.dds` |
| `GFX_ireland_advisor_ireland_p_32` | `gfx/leaders/ireland/leader_p_32.dds` | `advisor_ireland_p_32.dds` |
| `GFX_ireland_advisor_ireland_p_38` | `gfx/leaders/ireland/leader_p_38.dds` | `advisor_ireland_p_38.dds` |
| `GFX_ireland_advisor_ireland_p_39` | `gfx/leaders/ireland/leader_p_39.dds` | `advisor_ireland_p_39.dds` |
| `GFX_ireland_advisor_ireland_p_41` | `gfx/leaders/ireland/leader_p_41.dds` | `advisor_ireland_p_41.dds` |
| `GFX_ireland_advisor_ireland_p_48` | `gfx/leaders/ireland/leader_p_48.dds` | `advisor_ireland_p_48.dds` |
| `GFX_ireland_advisor_ireland_p_50` | `gfx/leaders/ireland/leader_p_50.dds` | `advisor_ireland_p_50.dds` |
| `GFX_ireland_advisor_ireland_p_54` | `gfx/leaders/ireland/leader_p_54.dds` | `advisor_ireland_p_54.dds` |
| `GFX_ireland_advisor_ireland_p_57` | `gfx/leaders/ireland/leader_p_57.dds` | `advisor_ireland_p_57.dds` |

## Validation record

- 45 generated DDS cards are present.
- Every generated DDS reopens as `65x67` and uses the expected one-level BGRA payload size.
- 45 prefixed preview PNGs are present for handoff review.
- Sample previews reviewed: Seán Lemass, Douglas Hyde, and the P-31 source portrait.
