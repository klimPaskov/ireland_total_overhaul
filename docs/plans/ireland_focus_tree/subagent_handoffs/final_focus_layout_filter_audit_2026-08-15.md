# Final Focus Layout and Filter Audit — 2026-08-15

## Verdict

The Ireland national focus tree is structurally clean for the requested audit surface. One small semantic defect was found and patched: the Fianna branch's mutual exclusions were not reciprocal in source. No layout redesign or filter rewrite was needed.

## Changed files and identifiers

- `common/national_focus/ireland_focus_tree.txt`
  - `ireland_the_rights_of_local_guardians`: added `mutually_exclusive = { focus = ireland_the_hounds_are_heard_again }` (around line 4742).
  - `ireland_recognise_the_elder_claim`: added the same reciprocal mutual exclusion (around line 4797).
- This handoff file.
- `thumbnail.png` and unrelated files were not touched by this audit.

Before the patch, `ireland_the_hounds_are_heard_again` listed both alternatives (`ireland_the_rights_of_local_guardians` and `ireland_recognise_the_elder_claim`), while the alternatives only used `available` `NOT = { has_completed_focus = ... }` guards. After the patch, all three pairings are represented by reciprocal engine mutual-exclusion declarations; the existing availability guards remain as readable route gating. The intended Fianna/Tuatha/Compact route choices are unchanged.

## Route coverage

| Surface | Evidence | Result |
| --- | --- | --- |
| Opening trunks | `ireland_state_still_defined`, `ireland_economic_war_review`, `ireland_defence_estimates` (tree overview, lines 1–9; opening blocks lines 67–187) | Three authored trunks remain. Economic and defence cards use deliberate `available` gates rather than disconnected visible prerequisites. |
| Shared political/material/defence lanes | Opening blocks through `ireland_government_formation`, `ireland_development_authority`, and `ireland_maritime_protection` | Present and connected; no unknown prerequisite or relative-position references. |
| Political families | `ireland_republican_government`, `ireland_norton_parliamentary`, `ireland_clann_founding`, `ireland_vocational_constitution`, plus the bridge roots | Present; branch visibility is supplied by the 28 `allow_branch = { always = yes }` blocks. |
| Northern policy/reclamation | `ireland_northern_settlement_ledger` through `ireland_northern_policy_proof`, plus `ireland_northern_question_in_arms` (around lines 2880–3050) | Present; all nine Northern policy/reclamation focuses carry `FOCUS_FILTER_ANNEXATION`. Existing decision/flag hooks remain. |
| Five Provinces | `ireland_five_province_mandates` through `ireland_five_provinces_capstone` (around lines 4133–4510) | Complete. The capstone has six OR prerequisite leaves and the same six terminal focus leaves plus six one-to-one conclusion flags in availability. |
| Otherworld | `ireland_otherworld_investigation` through `ireland_otherworld_capstone` (around lines 4520–5145) | Complete. The capstone has six OR prerequisite leaves and exactly the matching six conclusion flags in availability; each flag is set by its terminal reward. |
| Territorial/Atlantic/postwar expansion | `ireland_unfinished_national_question` through `ireland_atlantic_settlement_concluded` (around lines 6034–6610) | Complete; all 36 territorial expansion/reclamation/postwar focuses carry Annexation. Claims and timed war-goal actions remain decision-mediated; no free-core shortcut was found. |
| Convergence | `ireland_high_king_of_two_irelands`, `ireland_crown_and_five_provinces`, `ireland_five_courts_of_the_otherworld`, `ireland_fivefold_high_kingdom_of_two_irelands` | Present and gated by route capstones/conclusion proof. |

No unintended orphan or isolated focus was found. The source has 256 unique focus nodes, zero unknown prerequisite references, and zero unknown `relative_position_id` references. There are additional no-prerequisite, `available`-gated family roots by design; they are not unconditionally available opening roots.

## Layout evidence

Fresh `hoi4.focus_inspect` revision after the patch:

- Revision: `638d0ab4e98afd31f5f4b3604991d1daae276ba639385e9a2c1748f6c74eb6a8`
- Artifact: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/0f9c6eaa50630511890205c6c21e52729f3fca2c7012ef274bf738ac7f9d407a/892766070ec309c1746fb02a3ec04ced7066e9645c94de1d62e2cca582f80d0b/focus-inspect.638d0ab4e98afd31f5f4b3604991d1daae276ba639385e9a2c1748f6c74eb6a8.json`
- 256 focuses; 262 connectors; crossing `0`; node intersection `0`; long connector `0`; too-close pair `0`; minimum same-row spacing `2`.
- Bounds `x -44..21`, `y 0..26`; layout hash unchanged at `18d96979a06ebd399625b00fcea76947b07d9e53bef997ca6426b4fc46c355f0`.

Fresh `hoi4.focus_render` artifacts:

- HTML: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/00e29a74fc94ff808077fb13b876b758f4ba941e9d30aefdaf05b9e3f8841be3/6c42b6970108c2d63ada5ca81824137e47000b5e4de08f172f4461897301787f/ireland_focus_tree.focus.html`
- SVG: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/a76f351b1892d1d1293ac79059fa3e26381ba9299f7986c6295a5f4c42b368a4/90a6fdc9c807747674e514f4a780d5cc04e5a1c94568afc99fab5174a00aead8/ireland_focus_tree.focus.svg`
- JSON: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/56e3bea2f3eeeedf28b899d644f3f3353229bc691244ea08dd3f32ae6fa784a3/1fede85e2748b2418265970d3576edb67f7dd45fc8073620e14547178727bb91/ireland_focus_tree.focus.json`
- Source map: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/30ab236cea439bc8591c942e44ffe7d67ea53af6e4891983964110ae39c097db/182927be28504043d27d15a489a47706a2e8e3e909013d73cfdb296d7d84b0f7/ireland_focus_tree.focus.source-map.json`
- Plan: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/f38c5342b632b65d6082ad5fa5574849de62685e06e7777ef0f379307283a9ee/c08489737ba458c29eaea996b51d3e97d2f5d941ef5e86a8c7b3b8d38b11a800/ireland_focus_tree.focus.plan.json`

The six remaining `FOCUS_LAYOUT_LINEAR_DETOUR` warnings are nonblocking and are the accepted pairs: `ireland_civilian_oversight -> ireland_interoperability`, `ireland_treaty_port_diplomacy -> ireland_british_leverage_management`, `ireland_pentarchy_guardians -> ireland_five_sovereign_orders`, `ireland_the_rights_of_local_guardians -> ireland_a_law_for_two_orders`, `ireland_the_courts_beneath_the_hills -> ireland_a_government_under_the_mounds`, and `ireland_the_emergency_must_end -> ireland_human_sovereignty_restored`. The other diagnostic is the unrelated vanilla `continuous_restrict_freedom_desc` localisation warning.

## Icon coverage

| Check | Result |
| --- | --- |
| Focus icon references | 256/256 focus IDs resolve to `GFX_focus_ireland_*` definitions in `interface/ireland_icons.gfx`; 332 total project focus definitions are registered. |
| Focus localisation | 256/256 titles and 256/256 descriptions exist in `localisation/english/ireland_l_english.yml`. |
| Reward/trigger tooltip keys | 235 unique Ireland focus tooltip keys found in source; 235/235 localisation keys resolve. Every focus has a completion reward block. |
| Shine overlays | 188/256 focus IDs currently have matching entries in `interface/ireland_focus_shine.gfx`; 68 late-route focuses lack a shine overlay. Base focus sprites are present, so this is a nonblocking UI polish/asset follow-up outside this focus/filter patch. |

## Filter and reward audit

- XP parity is exact in both directions: Army XP `15/15`, Navy XP `12/12`, Air XP `4/4`; no focus has a direct XP reward without its matching XP filter or a matching XP filter without a direct XP reward.
- Research parity is exact after including `add_tech_bonus`, `add_doctrine_cost_reduction`, and the two maritime research-speed variable rewards: Research filter `29`, semantic research rewards `29`, mismatch `0`.
- Direct building rewards all carry Industry (`21/21`). The additional Industry-tagged contract/material focuses are intentional route-intent cards, not missing building rewards.
- Annexation filter coverage is `36/36` for the complete Northern, reunification, Atlantic, and postwar expansion set. The 36 IDs are: `ireland_northern_settlement_ledger`, `ireland_northern_local_authorities`, `ireland_northern_trade_corridor`, `ireland_northern_labour_social_bridge`, `ireland_northern_federal_preparation`, `ireland_northern_unitary_preparation`, `ireland_northern_wartime_bargain`, `ireland_northern_policy_proof`, `ireland_northern_question_in_arms`; `ireland_unfinished_national_question`, `ireland_border_and_atlantic_dossier`, `ireland_test_the_state_instruments`, `ireland_define_the_national_question`, `ireland_authorise_reunification_instruments`, `ireland_northern_plebiscite_guarantees`, `ireland_workers_reunification_campaign`, `ireland_ulster_ultimatum`, `ireland_customs_union_leverage`, `ireland_crown_and_province_mandate`, `ireland_settlement_under_law`, `ireland_all_island_workers_republic`, `ireland_force_the_border_question`, `ireland_belfast_compact`, `ireland_restore_ulsters_place`; and `ireland_atlantic_ambition`, `ireland_atlantic_security_compacts`, `ireland_republics_across_the_channel`, `ireland_gaelic_marches`, `ireland_atlantic_concessions`, `ireland_dal_riata_claim`, `ireland_enforce_atlantic_claims`, `ireland_postwar_settlement_office`, `ireland_local_rights_charter`, `ireland_protectorate_statutes`, `ireland_integration_review_commission`, `ireland_atlantic_settlement_concluded`.
- Existing expansion hooks remain wired: the direct claim rewards are limited to `ireland_northern_settlement_ledger`, `ireland_gaelic_marches`, and `ireland_dal_riata_claim`; the other territorial cards use existing decision unlocks and route flags. No unrelated decision or event files were changed.

## AI, localisation, and reward mismatches

- `common/ai_strategy_plans/IRE_ireland_strategy_plans.txt` references all 256 focus IDs in its `ai_national_focuses`/`focus_factors` surfaces; unknown focus references `0`, source focus IDs without any plan reference `0`.
- No broken focus-level AI references or route filter gaps were found. Historical zero guards remain on the alternate/exceptional entry and escalation focuses as authored.
- No focus title, description, or reward-tooltip key mismatch was found in the requested target tree.
- No focus reward name/description contradiction was found during the targeted review of the Five Provinces, Otherworld, Fianna/Tuatha branch, Northern reclamation, and Atlantic/postwar cards.

## Validation and remaining risks

Meaningful validation run:

1. Offline Paradox wiki National focus modding guidance and required core wiki pages were consulted before the source audit.
2. Vanilla HOI4 documentation and vanilla national-focus examples were consulted for prerequisite OR semantics, availability, mutual exclusion, search filters, and AI focus plans.
3. Fresh `hoi4.focus_inspect` and `hoi4.focus_render` completed with `validation.passed = true` and no blockers.
4. Source checks confirmed unique IDs, known prerequisite/relative-position references, reciprocal mutual exclusions, focus icon/loc/reward coverage, AI references, XP/research parity, and Annexation coverage.

Skipped meaningful validation: no live HOI4 launch or save-game route playthrough was run; this was a source/MCP audit and the parent agent owns live-session verification. No `hoi4.focus_rewrite` was used because the tree did not need a route redesign.

Remaining risks are limited to the six nonblocking detour advisories, the unrelated vanilla continuous-focus localisation warning, and 68 optional focus-shine registrations. The source patch is ready for parent review and selective commit.
