# Final compact Cabinet Briefing localisation audit — 2026-08-15

Status: **COMPLETE** for the requested localisation/player-facing audit. No source localisation or scripted-localisation patch was required. No GUI, focus, gameplay, or thumbnail files were changed by this audit.

## Scope

Audited the active compact Cabinet Briefing surfaces:

- `interface/ireland_national_situation.gui`
- `interface/ireland_national_situation_inlay.gui`
- `common/focus_inlay_windows/ireland_national_situation_inlay.txt`
- `common/scripted_guis/ireland_scripted_guis.txt`
- `common/scripted_localisation/ireland_localisation.txt`
- Cabinet category wiring in `common/decisions/categories/ireland_categories.txt`
- Ireland focus reward text and the exceptional-route refresh wrapper

The active surfaces consistently present Government, National Supply, Defence, and National Question as four cards. The full decision view has only the guarded `Advance Programme` action; the focus inlay has no action button. Supply and Defence alone expose aggregate numeric values.

## Required audit results

### Missing keys

None in the active compact surface. The Cabinet GUI’s labels, tooltips, button text, and five scripted-localisation calls resolve. The repository-wide scripted-localisation check found 450 `localization_key` references (389 unique) with no missing localisation keys.

The focus reward scan found one apparent non-mod key, `available_mio_tt`; this is a vanilla/base-game localisation key used by an availability tooltip, not an Ireland localisation defect. The 58 focus completions that call `ireland_refresh_exceptional_route_state` each have their own Ireland `*_reward_tt` text.

### Duplicate keys

None. All three localisation YAML files were checked for exact duplicate keys, and the 64 defined-text names were also unique.

### Scripted localisation

`GetIrelandCabinetGovernmentStatus`, `GetIrelandCabinetSupplyStatus`, `GetIrelandCabinetDefenceStatus`, `GetIrelandCabinetNorthernStatus`, and `GetIrelandCabinetAssessment` are present and have ordered fallback branches. The active GUI and inlay use the same status functions and assessment function. No broken scripted-localisation reference was found.

The old six-tab/row compatibility definitions remain in the localisation/scripted-localisation sources, but no active compact `interface/*.gui` file references them. The dedicated Northern Settlement and Evidence ledgers still use their own row/selector wording; that is separate from the Cabinet Briefing and is not a compact-surface defect.

### Dynamic text opportunities

The required dynamic opportunities are covered:

- Government and Northern Question are qualitative status text.
- National Supply and Defence use their existing aggregate display variables (`ireland_provision_display`, `ireland_readiness_display`); no extra per-row diagnostic values are exposed.
- Northern status uses the existing integration-stage value when its authored route is open.
- The assessment is contextual and changes priority with the current cabinet condition.
- `Advance Programme` is guarded by `ireland_briefing_context_action_available`, and its tooltip resolves the current dynamic requirements through `GetIrelandMechanicsHubStateActionRequirements`.

No static value was found that needs a new dynamic localisation helper.

### Wording and colour

The active wording is natural policy-facing language. The three-line card tooltips explain the matter, its consequence, and the current status. State colours are consistently restrained: grey for settled/closed/pending, green for ready/steady, yellow for warning/contested, and red for critical/recovery. No active compact text contains the forbidden diagnostic/debug phrases “what this value does”, “what does this value do”, “selected row”, “refresh projection”, “binding gate”, “internal value”, or “mechanic family”.

`Provision focuses` and `Northern Settlement Ledger` are intentional names for existing gameplay surfaces, not implementation commentary.

### Obsolete six-tab text

No active compact GUI reference was found for the retired tab, row, detail-header, selection, or refresh strings. Legacy keys such as `ireland_mechanics_hub_detail_header`, `ireland_mechanics_hub_selection_none`, `ireland_mechanics_hub_context_action`, and `ireland_mechanics_hub_refresh_action` remain in localisation for compatibility/history and were not deleted because they are outside this localisation-only correction. Their presence does not expose obsolete text on the active four-card surfaces.

### Focus reward wrapper

`common/scripted_effects/ireland_exceptional_routes.txt` exposes `ireland_refresh_exceptional_route_state` as a public wrapper whose body calls `ireland_refresh_exceptional_route_state_internal` inside `hidden_effect`. The large route-state effect list is therefore hidden from focus completion tooltips. A source scan found 58 focus completion rewards using the public wrapper, each paired with a focus-specific `custom_effect_tooltip = <focus_id>_reward_tt`; no direct `_internal` calls occur outside the wrapper definition. All of those Ireland reward keys are present.

## Encoding

All three localisation YAML files are UTF-8 with BOM:

- `localisation/english/ireland_l_english.yml`
- `localisation/english/ireland_exceptional_routes_l_english.yml`
- `localisation/english/ireland_game_rules_l_english.yml`

No localisation encoding concern was found. Scripted localisation is Clausewitz `.txt` source rather than YAML localisation and had no malformed reference in the active path.

## Cross-surface uncertainty for parent review

The accepted compact contract describes authored records as locked until their route opens. The current scripted trigger `ireland_mechanics_hub_state_visible` is true for an initialized IRE country, so Government can fall through to its qualitative `Contested`/`Steady`/`Strained`/`Settled` branches rather than an explicit locked branch. This is a trigger/gameplay contract question, not a localisation defect, so it was not changed here. If the intended lock applies to Government, the owning scripted-trigger agent should resolve that condition and retain the existing status keys.

## Recommended fixes

No active localisation fix is recommended. The compact wording, dynamic status calls, tooltips, colours, and focus reward masking are complete. Optional future cleanup may remove or quarantine the now-unreferenced six-tab compatibility strings after the parent confirms that no legacy ledger surface needs them; that cleanup is not necessary for the current compact correction.

## Validation and handoff

- Active Cabinet GUI extraction: all localisation keys and all five scripted-localisation functions resolved; no old tab/row/refresh/detail references.
- Localisation duplicate/BOM audit: three YAML files, all BOM-present, no duplicate keys.
- Scripted-localisation coverage: 450 references, no missing keys; 64 defined-text names, no duplicates.
- Focus wrapper audit: 58 public-wrapper calls, all paired with Ireland reward tooltips; no direct internal calls outside the hidden wrapper.
- No in-game render or runtime scenario execution was performed; this was a source-level localisation audit against the frozen GUI/focus wiring.

Changed files: none. Changed keys: none. Dynamic localisation added or fixed: none. No commit was created; the parent agent can include this handoff with the larger plan commit.
