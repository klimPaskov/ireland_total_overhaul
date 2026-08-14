# Ireland political-family lane reflow completion — 2026-08-14

## Result

The five substantive public-family programme islands were compacted from the detached far-left area into five straight, parallel lanes beneath the established political tree. The change is coordinate-only: focus IDs, rewards, availability, family locks, prerequisites, AI, icons, localisation, and the three opening trunks are unchanged.

The five lane roots are:

- democratic: `ireland_republican_ministries` at `(-24,18)`;
- communist: `ireland_vanguard_organisers` at `(-18,18)`;
- fascist: `ireland_veterans_command_council` at `(-12,18)`;
- oligarchic: `ireland_creditor_cabinet` at `(-6,18)`; and
- restoration: `ireland_claimants_convention` at `(0,18)`.

Their 26 descendants and advisor-capstone focuses occupy rows 19–22 in the same ordered lanes. Each family is revealed by its existing `allow_branch` family flag, so the tree still exposes only three opening trunks. The family lanes are horizontally centered on the political tree and no longer expand the layout to x = -42.

## Layout evidence

Fresh focus inspection reports:

- 218 focuses and 226 connectors;
- bounds x = -26..21 and y = 0..22, reduced from x = -42..21;
- zero connector crossings;
- zero connector-through-node intersections;
- zero long connectors;
- zero duplicate coordinates or visible overlaps;
- zero same-row spacing defects, with minimum spacing 2;
- maximum horizontal connector span 8 and maximum vertical span 2.

Inspection artifact:

`hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/85dbe6e42347983c81724e69887fc612cc2c93f8e6a99d996e2a56a0a7a41e30/c3be345607e9046da94518ce45eaaf230c3be8dc4d72ad05de771273e55f7056/focus-inspect.ea067e4f28da98eb.json`

Rendered review artifacts:

- HTML: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/decedccec4134d0192ed347c95a6b0b8ad3aa44428bee7db06a46e1dbc9a0f78/e36096dde6eade870059eb88753099cf40d449d7a3666b3f360afe3ffb1f5df6/ireland_focus_tree.focus.html`
- SVG: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/06e8fd612e2f9ab92f266a2a9ea8fc00b76daf9791c5e64be3aed8e36036cca1/a29cb0ac31ceaf8f8da10e9421eefe8105c6ea734b1b8d05e6f03f9ecf56e74f/ireland_focus_tree.focus.svg`

The inspector retains one nonblocking two-column linear detour from `ireland_clerical_failure_bridge` to `ireland_clerical_guardianship`. Straightening that pair forces a crossing with the adjacent Congress corridor; the zero-crossing authored geometry is retained. The other reported localisation warning belongs to vanilla `continuous_restrict_freedom`.

## Files changed

- `common/national_focus/ireland_focus_tree.txt` — 31 coordinate pairs only.
- This handoff and the supersession marker in the rejected experiment handoff.

No fallback focus, missing route, reward simplification, gameplay prerequisite change, or asset substitution was used.
