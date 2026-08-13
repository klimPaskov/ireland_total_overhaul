# Industrial company MIO completion handoff — 2026-08-13

## Scope and outcome

This tranche implements the accepted capability gaps for Ford Cork, Harland & Wolff Belfast, and the Irish Shipping founding gate. The parent agent owns the final integrated review and commit; this handoff records the source surfaces and validation evidence.

- Ford Cork is now `ireland_ford_cork_works_organization`, a selectable motorized/mechanized MIO inheriting `generic_motorized_mechanized_organization`.
- Harland & Wolff Belfast is now `ireland_harland_wolff_belfast_organization`, a selectable naval MIO inheriting `generic_task_force_ship_organization`.
- The ordinary `industrial_concern` fallback blocks for Ford Cork and Harland & Wolff were removed. The remaining public/civil institutions remain ordinary concerns.
- Irish Shipping remains an ordinary maritime concern as specified, but its focus is now gated by its historical founding window or the existing project emergency state.

## Changed files and identifiers

### MIO definitions

`common/military_industrial_organization/organizations/ireland_organizations.txt`

- `ireland_ford_cork_works_organization`
  - `allowed = { original_tag = IRE }` creates the organization for original-tag Ireland.
  - `visible` and `available` require `ireland_company_ford_cork_unlocked`.
  - Inherits the vanilla motorized/mechanized equipment and research categories.
  - Initial trait `ireland_ford_cork_works_initial_trait` covers motorized and mechanized equipment; `ireland_ford_cork_works_local_assembly` is a production trait rooted at `generic_mio_trait_all_wheel_drive`.
  - AI weighting follows the existing `ireland_ai_priority_provision` and `ireland_ai_supporting_provision` flags.
- `ireland_harland_wolff_belfast_organization`
  - `allowed = { original_tag = IRE }` creates the organization for original-tag Ireland.
  - `visible` and `available` require `ireland_company_harland_wolff_unlocked`.
  - Inherits the vanilla task-force ship categories for carriers, cruisers, and destroyers and their corresponding research categories.
  - Initial trait `ireland_harland_wolff_belfast_initial_trait` provides shipyard capacity; `ireland_harland_wolff_belfast_yards` and `ireland_harland_wolff_belfast_refit_discipline` add the Belfast yard/refit path.
  - AI weighting follows the existing `ireland_ai_priority_readiness` and `ireland_ai_supporting_readiness` flags.

### Focus wiring and gates

`common/national_focus/ireland_focus_tree.txt`

- `ireland_ford_cork_works_agreement` keeps its existing domestic-manufacturing and 1938-trade-settlement availability. Completion sets `ireland_company_ford_cork_unlocked`, shows `ireland_ford_cork_works_organization`, grants two MIO size points, and retains the bounded major truck delivery.
- `ireland_harland_and_wolff_access` keeps its existing lawful gate: `ireland_northern_policy_proof`, state `119` owned and controlled by Ireland, and `ireland_northern_final_review_passed`. Completion sets `ireland_company_harland_wolff_unlocked`, shows `ireland_harland_wolff_belfast_organization`, grants two MIO size points, and retains the Belfast dockyard/refit reward.
- `ireland_irish_shipping_registry` retains its `ireland_maritime_reserve` and `ireland_atlantic_convoy_office` prerequisites and now requires:

  ```text
  OR = {
      date > 1941.3.31
      has_country_flag = ireland_national_emergency_active
  }
  ```

  This means the focus is available from 1 April 1941 onward, or earlier while the existing project-maintained `ireland_national_emergency_active` flag is set. Completion still unlocks the ordinary Irish Shipping concern, sets `ireland_company_shipping_unlocked`, and grants the bounded convoy delivery.

### Concerns, localisation, and contracts

- `common/ideas/ireland_industrial_concerns.txt`: removed the Ford Cork and Harland & Wolff ordinary-concern blocks; no duplicate concern remains for either equipment producer.
- `localisation/english/ireland_l_english.yml`: added direct MIO and trait keys (`ireland_ford_cork_works_organization`, `ireland_ford_cork_works_initial_trait`, `ireland_ford_cork_works_local_assembly`, `ireland_harland_wolff_belfast_organization`, `ireland_harland_wolff_belfast_initial_trait`, `ireland_harland_wolff_belfast_yards`, and `ireland_harland_wolff_belfast_refit_discipline`); updated company descriptions and Ford/Shipping/Harland reward text to say organization/MIO where appropriate; removed orphaned Ford/Harland concern localization pairs.
- Existing company-specific decisions were preserved unchanged: `ireland_contract_ford_motor_works`, `ireland_contract_belfast_refit`, and `ireland_contract_merchant_tonnage`. Their material outputs remain gated by the corresponding company flags.
- Existing `interface/ireland_industrial_concerns.gfx` registrations and company DDS files were reused; no placeholder or fallback icon was introduced.

## Before and after behavior

Before this tranche, Ford Cork and Harland & Wolff were ordinary selectable ideas with no MIO organization tree, while the Irish Shipping focus could be taken as soon as its two focus prerequisites were complete. After this tranche, Ford and Harland are unlocked through the normal MIO tooltip/effect path and gain their inherited vanilla equipment specializations plus company-specific traits. Irish Shipping cannot be founded before April 1941 unless the existing project emergency flag is active. The existing procurement decisions and bounded material contracts remain available through their original company flags.

## Validation evidence

- Read the vanilla MIO organization documentation and the offline MIO modding wiki page. Cross-checked `generic_motorized_mechanized_organization`, `generic_task_force_ship_organization`, vanilla Ford and Harland precedents, `show_mio_tooltip`, and `mio:<organization> = { add_mio_size = ... }` focus effects.
- Confirmed inherited equipment/research categories and custom equipment-stat/production-stat keys against vanilla organization definitions. Confirmed `GFX_generic_mio_trait_icon_efficiency_gain`, `GFX_generic_mio_trait_icon_production_capacity`, and `GFX_generic_mio_trait_icon_reliability` exist in vanilla interface definitions; confirmed both Ireland company icon DDS files and existing mod GFX registrations exist.
- Source search found no live gameplay references to the removed ordinary keys `ireland_company_ford_cork_works` or `ireland_company_harland_and_wolff_access` outside localisation/docs before cleanup; the new MIO IDs and unlock flags are unique in the mod source.
- Read-only `hoi4_focus_inspect` for `ireland_focus_tree` returned `FOCUS_INSPECTED` with validation passed and no blocking diagnostics. Its only warnings were an unrelated clerical connector layout warning and a vanilla continuous-focus localisation warning.
- Localisation remains UTF-8 with BOM after the key cleanup.
- A full game launch was not run in this subagent tranche because the parent owns the shared integrated validation and concurrent focus/doc edits were present.

## Remaining risks and simplifications

- No requested simplification or fallback was used. Ford and Harland intentionally rely on the MIO system rather than retaining ordinary concern substitutes.
- The MIO UI/equipment assignment should be exercised during the parent’s integrated live validation, especially after the accepted focus-tree and documentation edits are combined.
- No territorial event/postwar logic, public-family depth, advisor assets, or thumbnail surface was changed.
