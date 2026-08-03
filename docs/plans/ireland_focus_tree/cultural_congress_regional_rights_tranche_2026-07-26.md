# Cultural Congress Regional-Rights Tranche

Feature slug: `ireland_focus_tree`

Date: 2026-07-26

## Scope

This tranche makes the Five-Region Cultural Congress objective represent regional participation and rights-bearing representation instead of only a Dublin venue, three controlled states, and a transport stockpile. It does not claim live engine execution, event firing, AI behavior, asset clearance, or scenario completion.

## Canonical work preserved

`Hold a Provincial Cultural Congress` remains a P-level action for county, language, labour, Church, artistic, and historical delegates. It now requires the serious-culture/archive lane, a regional-participation record or component floor, and at least one rights-bearing constituency through Minority Confidence, Labour Organisation, or Church influence, while retaining its 5-Truck transport commitment and dynamic costs.

The `Hold a Five-Region Cultural Congress` map objective now rechecks the active action and mission, the three authored state/building platforms, the participation and rights authority, and more than one concealed-evidence region. Full, partial, boycott, central-capture, failure, and delegation cleanup remain owned by the existing mission lifecycle.

## Source changes

- `common/script_constants/slopx_ireland_constants.txt` adds regional and rights floors of 30 and 35.
- `common/scripted_triggers/slopx_ireland_triggers.txt` adds `slopx_ireland_cultural_congress_authority` and attaches it to the named map objective.
- `common/decisions/slopx_ireland_decisions.txt` gates the action on the authority proof; its existing truck charge and capped refund remain unchanged.
- `localisation/english/slopx_ireland_l_english.yml` exposes current regional, minority, and labour values alongside the named requirements.
- `docs/slopx_dynamic_effects.md` records the authority contract and side effects.

## Boundaries

The congress authority creates no delegates, Cultural Capacity, evidence, offices, territory, Northern control, cores, recognition, industry, units, or passive Political Power. It only admits the existing dated mission, which retains its material and result handling.

## Validation evidence

- Static source inspection confirms the helper and mission map objective are each defined once, and the action uses the helper in its own availability block.
- Existing inventory counts remain 216 focuses, 13 categories, 140 actions, and 54 missions.
- Localisation remains UTF-8 with BOM; touched Clausewitz source contains no unsupported comparison operators.
- HOI4 was not launched, so parser behavior, mission ticking, delegate outcomes, AI selection, and cleanup execution remain not-run.
