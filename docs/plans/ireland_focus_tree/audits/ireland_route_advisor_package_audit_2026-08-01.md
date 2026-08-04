# Ireland route advisor package audit — 2026-08-01

## Scope

This audit covers the current route-specific advisor package. It supersedes the
earlier two-role coverage finding for the current implementation, while
preserving that handoff as historical evidence. It does not claim completion of
the full Ireland country-package audit or the full feature goal.

## Current package

`common/characters/ireland_route_characters.txt` contains exactly 32
advisor blocks and 32 unique `idea_token` values:

| Portfolio family | Advisor tokens |
| --- | --- |
| Starting constitutional roster | `ireland_oscar_traynor`, `ireland_douglas_hyde`, `ireland_sean_t_okelly` |
| Existing constitutional package | `ireland_sean_lemass`, `ireland_richard_mulcahy` |
| Fianna Fáil / development | `ireland_frank_aiken_advisor`, `ireland_sean_macentee_advisor` |
| Fine Gael / coalition / intervention | `ireland_joseph_walshe_advisor`, `ireland_sean_mac_eoin_advisor`, `ireland_thomas_f_ohiggins_advisor`, `ireland_patrick_mcgilligan_advisor` |
| Labour / unions | `ireland_james_everett_advisor`, `ireland_william_obrien_advisor`, `ireland_james_hickey_advisor`, `ireland_william_davin_advisor` |
| Clann na Talmhan | `ireland_michael_donnellan_advisor` |
| Church / service / vocational | `ireland_edward_joseph_byrne_advisor`, `ireland_john_charles_mcquaid_advisor`, `ireland_joseph_macrory_advisor`, `ireland_frank_duff_advisor`, `ireland_john_hayes_advisor` |
| IRA civil / command | `ireland_maurice_twomey_advisor`, `ireland_tom_barry_advisor`, `ireland_jim_odonovan_advisor`, `ireland_sean_macbride_advisor`, `ireland_charles_kerins_advisor` |
| Republican Congress | `ireland_george_gilmore_advisor`, `ireland_nora_connolly_obrien_advisor`, `ireland_sean_murray_advisor` |
| O'Duffy / Ailtirí | `ireland_patrick_belton_advisor`, `ireland_ernest_blythe_advisor`, `ireland_oliver_flanagan_advisor` |

The historical roster is used for sourced real people only. Ryan, Peadar
O'Donnell, Gearóid Ó Cuinneagáin, O'Duffy, and collective councils remain
movement or country-leader offices, not ordinary advisor duplicates.

## Route and lifecycle wiring

- `common/scripted_triggers/ireland_triggers.txt` defines the route
  helper gates for constitutional, de Valera/Lemass, Fine Gael/Dillon, Norton,
  Clann, vocational, clerical, IRA civil, IRA command, Congress plural,
  Congress vanguard, O'Duffy, and Ailtirí portfolios.
- `ireland_recruit_route_advisors` is called from route-leader activation
  and recruits only the roster permitted by the selected route and date.
- Hiring remains an ordinary advisor appointment: route activation does not
  call `activate_advisor` and does not grant political power or bypass the
  normal appointment cost.
- `ireland_sync_route_advisor_lifecycle` dismisses invalid hired roles
  when route, office, archive, command, closure, or date conditions fail, then
  retires invalid route characters so a later valid recovery can recruit them
  without stacking duplicate identities.
- The 1936 country history uses custom sourced Traynor, Hyde, and O'Kelly
  tokens rather than the three vanilla duplicate-person tokens.

## Source and asset crosswalk

The portrait source IDs used by this package are all present in
`docs/plans/ireland_focus_tree/assets/source_manifest.json` with complete
clearance (C3 or C4 as recorded in the manifest):

| Source IDs | Runtime use |
| --- | --- |
| P-08, P-09, P-10, P-11, P-12, P-13, P-14, P-17, P-18, P-19, P-20, P-22, P-23, P-25 | Starting roster, Fianna Fáil, Fine Gael, Labour, and Clann advisors |
| P-28, P-29, P-30, P-33, P-34, P-35, P-36, P-40, P-42, P-44 | Church/service and IRA advisors |
| P-47, P-49, P-51, P-53, P-58, P-60 | Republican Congress, O'Duffy, and Ailtirí advisors |

Runtime DDS files remain in the standard mod `gfx/` tree and GFX definitions
remain in `interface/ireland_sourced_assets.gfx`. Source masters remain
preserved under `docs/portraits/`; the temporary `assets/` tree is not a
runtime destination. No real-person portrait was generated or used as a
substitute for a missing source.

## Static evidence

The scoped audit was rerun after the lifecycle changes:

- Character-file braces: `539/539`.
- Runtime-effect braces: `10227/10227`.
- Trigger-file braces: `1786/1786`.
- Country-history braces: `8/8`.
- Advisor blocks and tokens: `32/32`, unique.
- Top-level custom character IDs: `54`, unique.
- Every custom route recruit resolves to a character definition.
- Every portrait reference resolves to a registered GFX sprite.
- No touched script uses unsupported `<=` or `>=` operators.
- Live HOI4 execution was intentionally excluded by the task boundary.

## Remaining boundaries

This audit closes the earlier narrow advisor-coverage finding, not the full
Ireland completion goal. Full completion still requires the remaining canonical
route, asset-clearance, UI, animation/audio, AI, achievement, static-engine,
and audit evidence to be satisfied. No fallback or shortened route was used in
this tranche.
