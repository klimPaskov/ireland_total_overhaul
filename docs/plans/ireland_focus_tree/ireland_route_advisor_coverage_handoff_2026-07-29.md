# Ireland route advisor coverage handoff — 2026-07-29

> Historical handoff. The two-role baseline described here is superseded for
> current advisor coverage by
> `ireland_route_advisor_package_tranche_2026-08-01.md`. It remains as evidence
> for the earlier Lemass/Mulcahy repair; later country-package and Northern
> observations are not current blockers when the newer tranche is present.

## Result

Implemented the two advisor roles that are fully supported by the canonical office matrices, existing character roster, existing vanilla traits, and C4-cleared sourced portraits:

| Character / idea token | Slot | Trait | Cost | Route and office gate | AI weight | Lifecycle |
| --- | --- | --- | ---: | --- | --- | --- |
| `ireland_sean_lemass` | `political_advisor` | `captain_of_industry` | 150 PP | Visible before route commitment and on the three de Valera routes or Lemass route. Unavailable after route archive, government/cabinet vacancy, constitutional-government-law exit, or while Lemass is ruling leader. | Base `1`; factor `2` on the three de Valera routes. | Retained as a minister on de Valera routes; dismissed before promotion to Taoiseach; retired on incompatible committed routes; may return to minister status after a failed Lemass leadership outcome if the constitutional office remains valid. |
| `ireland_richard_mulcahy` | `army_chief` | `army_chief_defensive_2` | 100 PP | Visible before route commitment and on Cosgrave, Mulcahy, or Costello routes. Unavailable after route archive, government/Chief-of-Staff vacancy, military-command collapse, constitutional-government-law exit, or while Mulcahy is ruling leader. | Base `1`; factor `2` on Cosgrave or Costello routes. | Retained as defence figure under Cosgrave and as separate party/defence authority under Costello; dismissed before promotion to Taoiseach; retired on incompatible committed routes; may return to command after a failed Mulcahy leadership outcome if civilian command remains valid. |

Both roles remain ordinary paid appointments. Nothing calls `activate_advisor`, and neither route commitment nor political victory grants an advisor for free.

The 1936 history now recruits the sourced custom Lemass and Mulcahy tokens instead of the two vanilla duplicate-person tokens `IRE_sean_lemass` and `IRE_richard_james_mulcahy`. The static advisor definitions use the same established vanilla traits and costs as those vanilla Ireland roles.

No new advisor trait or localisation key was required. Character names are existing literal names and both traits use vanilla localisation. General route-spirit localisation was not touched.

## Files changed

- `common/characters/ireland_route_characters.txt`
  - Added the two static advisor roles and small-portrait consumers using their already registered sourced sprites.
- `history/countries/IRE - Ireland.txt`
  - Replaced the two recruited vanilla duplicate-person tokens with the custom sourced tokens.
- `common/scripted_effects/ireland_runtime.txt`
  - Added `ireland_sync_route_advisor_lifecycle`.
  - Preserved Lemass on the three de Valera routes and Mulcahy on Cosgrave/Mulcahy/Costello routes.
  - Dismissed each advisor before an incompatible ruling office and after invalid office, law, command, route, or archive state.
- `docs/plans/ireland_focus_tree/ireland_route_advisor_coverage_handoff_2026-07-29.md`

## Validation

- Advisor coverage added: exactly `2` roles, with exactly `2` unique idea tokens.
- The 1936 history has one recruitment line for each custom token and no longer recruits either vanilla duplicate-person token; existing route activation calls remain idempotent.
- No `activate_advisor` call exists for either token.
- `captain_of_industry` and `army_chief_defensive_2` exist in vanilla trait definitions; no new trait idea was added.
- P-02 Seán Lemass and P-04 Richard Mulcahy are both `complete`, C4-cleared manifest records. Their source originals and processed PNGs remain preserved under `docs/portraits/`.
- Source-manifest baseline remains `47 complete / 55 needs_user_review / 67 blocked`.
- The three persistent route-spirit families remain unchanged: governing, society, and security, with 21 registered states in each family when the opening state is included.
- No source, DDS, GFX, decision, focus, event, achievement, GUI, specification, or route-spirit/localisation file was changed.
- Static validation only; live Hearts of Iron IV testing was excluded by the user.

## Canonical items not safe to implement in this tranche

- No final researched named-advisor ledger exists in Part 6. The broader office lists identify portfolio families, but do not supply a complete, implementation-safe named roster with exact route, law, date, failure, and office gates.
- The exact live `needs_user_review` portrait consumers remain P-05 John A. Costello, P-06 James Dillon, P-27 Joseph Blowick, P-43 Frank Ryan, P-46 Peadar O'Donnell, P-56 Gearóid Ó Cuinneagáin, and RC-PORTRAIT-01 Daniel Morrissey. None was promoted to an additional advisor consumer.
- Costello is a legal/parliamentary figure and compromise Taoiseach, not automatically a generic legal advisor.
- Dillon's intervention and agricultural roles require distinct dated/failure states and no existing trait exactly represents both.
- Blowick requires the post-1944 Clann leadership conference, which has no safe advisor gate in the current route lifecycle.
- Frank Ryan requires survival, return, and a break from Axis tutelage. The current IRA route still recruits him without those canonical proofs; correcting that requires the out-of-scope event/focus lifecycle, so no Ryan advisor was added.
- Peadar O'Donnell and Gearóid Ó Cuinneagáin retain movement/council offices distinct from cabinet appointment.
- William Norton and the wider Labour/cabinet portfolio roster are outside the owned route-character definition. Adding dynamic scripted advisor roles or duplicate custom characters would lose static gates or create duplicate identities.
- Institutional and collective characters remain non-advisors. No canonical matrix row requires a collective council advisor role with a safe engine precedent.

No commit was created.
