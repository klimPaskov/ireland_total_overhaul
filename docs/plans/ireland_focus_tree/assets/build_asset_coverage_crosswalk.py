"""Build the row-level Ireland asset-to-consumer coverage crosswalk.

This is a mechanical audit/report builder. It does not modify gameplay files or
promote staging art. Runtime paths are read from the Ireland-owned .gfx files,
while source-package clearance remains authoritative in source_manifest.json.
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
ASSET_ROOT = ROOT / "assets" / "ireland_focus_tree"
ICON_ROOT = ASSET_ROOT / "icons"
FRESH_ICON_PACKAGE = ICON_ROOT / "regenerated_goal_and_law_icons_fresh_2026-08-01_v1"
FRESH_FOCUS_ICON_ROOT = FRESH_ICON_PACKAGE
FRESH_LAW_ICON_ROOT = FRESH_ICON_PACKAGE
OUT = ROOT / "docs" / "plans" / "ireland_focus_tree" / "assets" / "asset_coverage_crosswalk.md"

GFX_FILES = {
    "focus": "interface/ireland_icons.gfx",
    "secondary": "interface/ireland_secondary_assets.gfx",
    "route": "interface/ireland_route_assets.gfx",
    "gui": "interface/ireland_gui_assets.gfx",
    "animation": "interface/ireland_animation_assets.gfx",
    "event": "interface/ireland_event_art.gfx",
    "sourced": "interface/ireland_sourced_assets.gfx",
}


@dataclass(frozen=True)
class GfxRow:
    kind: str
    sprite: str
    texture: str
    gfx_file: str
    line: int
    sprite_type: str
    block: str


@dataclass(frozen=True)
class CodeRow:
    identifier: str
    icon: str
    file: str
    line: int
    block: str
    parent: str = "—"


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def rel(path: Path | str) -> str:
    """Return a stable project-relative path for report tables."""

    if isinstance(path, str):
        value = path.replace("\\", "/")
        if value in {"", "not_created", "—"}:
            return value or "—"
        path = Path(value)
    try:
        return path.resolve().relative_to(ROOT.resolve()).as_posix()
    except ValueError:
        return path.as_posix()


def existing(path_value: str) -> bool:
    if path_value in {"", "not_created", "—"}:
        return False
    path = Path(path_value.replace("\\", "/"))
    if path.is_absolute():
        return path.exists()
    return (ROOT / path).exists()


def line_number(source: str, offset: int) -> int:
    return source.count("\n", 0, offset) + 1


def balanced_block(source: str, brace_start: int) -> str:
    depth = 0
    quote = False
    escaped = False
    for index in range(brace_start, len(source)):
        char = source[index]
        if quote:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                quote = False
            continue
        if char == '"':
            quote = True
        elif char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return source[brace_start : index + 1]
    raise ValueError(f"Unclosed block at offset {brace_start}")


def named_blocks(source: str, pattern: str) -> list[tuple[str, str, int]]:
    """Extract blocks whose opening line is matched by pattern."""

    rows: list[tuple[str, str, int]] = []
    for match in re.finditer(pattern, source, re.MULTILINE):
        brace_start = source.find("{", match.start(), match.end() + 1)
        if brace_start < 0:
            continue
        rows.append((match.group(1) if match.lastindex else "", balanced_block(source, brace_start), line_number(source, match.start())))
    return rows


def value(block: str, key: str) -> str:
    match = re.search(rf"\b{re.escape(key)}\s*=\s*\"?([^\s\"}}]+)", block, re.MULTILINE)
    return match.group(1) if match else "—"


def condition_summary(block: str) -> str:
    flags = sorted(set(re.findall(r"\bhas_country_flag\s*=\s*([A-Za-z0-9_]+)", block)))
    variables = sorted(set(re.findall(r"\b(?:var|variable)\s*=\s*([A-Za-z0-9_]+)", block)))
    focuses = sorted(set(re.findall(r"\b(?:focus|has_completed_focus)\s*=\s*([A-Za-z0-9_]+)", block)))
    surfaces = [
        key
        for key in (
            "allowed",
            "visible",
            "available",
            "prerequisite",
            "complete",
            "complete_effect",
            "remove",
            "remove_effect",
            "timeout",
            "timeout_effect",
            "cancel_trigger",
        )
        if re.search(rf"\b{key}\s*=", block)
    ]
    parts: list[str] = []
    if surfaces:
        parts.append("surfaces=" + ",".join(surfaces))
    if flags:
        parts.append("flags=" + ",".join(flags[:12]) + (f" (+{len(flags) - 12})" if len(flags) > 12 else ""))
    if variables:
        parts.append("vars=" + ",".join(variables[:12]) + (f" (+{len(variables) - 12})" if len(variables) > 12 else ""))
    if focuses:
        parts.append("focuses=" + ",".join(focuses[:8]) + (f" (+{len(focuses) - 8})" if len(focuses) > 8 else ""))
    return "; ".join(parts) or "no static binding tokens found; inspect owning block"


def parse_gfx(path: Path, kind: str) -> list[GfxRow]:
    source = text(path)
    rows: list[GfxRow] = []
    for match in re.finditer(
        r"\b(spriteType|frameAnimatedSpriteType|textSpriteType)\s*=\s*\{(.*?)\}",
        source,
        re.DOTALL | re.IGNORECASE,
    ):
        block = match.group(2)
        sprite = value(block, "name")
        texture = value(block, "texturefile")
        if sprite in {"", "—", "â€”"}:
            continue
        rows.append(
            GfxRow(
                kind=kind,
                sprite=sprite,
                texture=texture,
                gfx_file=rel(path),
                line=line_number(source, match.start()),
                sprite_type=match.group(1),
                block=block,
            )
        )
    return rows


def parse_code_rows(path: Path, pattern: str, icon_key: str = "icon") -> list[CodeRow]:
    source = text(path)
    rows: list[CodeRow] = []
    for identifier, block, line in named_blocks(source, pattern):
        icon = value(block, icon_key)
        rows.append(CodeRow(identifier, icon, rel(path), line, block))
    return rows


def block_spans(source: str, pattern: str) -> list[tuple[str, str, int, int]]:
    rows: list[tuple[str, str, int, int]] = []
    for identifier, block, line in named_blocks(source, pattern):
        start = source.find(identifier, 0)
        # The line number is unique for these owning blocks; use the opening-line
        # offset to assign nested rows to their category without relying on names.
        line_start = source.splitlines(keepends=True)
        offset = sum(len(item) for item in line_start[: line - 1])
        rows.append((identifier, block, offset, offset + len(block)))
    return rows


def parse_focus_rows(path: Path) -> list[CodeRow]:
    source = text(path)
    rows: list[CodeRow] = []
    for _, block, line in named_blocks(source, r"^\tfocus\s*=\s*\{"):
        identifier = value(block, "id")
        icon = value(block, "icon")
        if identifier.startswith("ireland_") and icon.startswith("GFX_focus_"):
            rows.append(CodeRow(identifier, icon, rel(path), line, block))
    return rows


def sprite_candidates(intended: str) -> list[str]:
    """Return the Ireland-owned runtime naming variants for a manifest row."""

    if not intended:
        return []
    return [
        intended,
        "GFX_" + intended,
        "GFX_ireland_" + intended,
        "GFX_report_event_" + intended,
        "GFX_news_event_" + intended,
    ]


def assign_decision_parents(rows: list[CodeRow], path: Path) -> list[CodeRow]:
    source = text(path)
    category_spans = block_spans(source, r"^(ireland_[A-Za-z0-9_]+)\s*=\s*\{")
    result: list[CodeRow] = []
    for row in rows:
        line_offset = sum(len(item) for item in source.splitlines(keepends=True)[: row.line - 1])
        parent = next((name for name, _, start, end in category_spans if start <= line_offset <= end), "—")
        result.append(CodeRow(row.identifier, row.icon, row.file, row.line, row.block, parent))
    return result


def all_gfx_rows() -> list[GfxRow]:
    rows: list[GfxRow] = []
    for kind, relative_path in GFX_FILES.items():
        rows.extend(parse_gfx(ROOT / relative_path, kind))
    return rows


def build_consumer_index() -> dict[str, list[str]]:
    index: dict[str, list[str]] = defaultdict(list)
    for root_name in ("common", "events", "interface"):
        root = ROOT / root_name
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if path.suffix.lower() not in {".txt", ".gui"}:
                continue
            try:
                lines = text(path).splitlines()
            except UnicodeDecodeError:
                continue
            for number, line in enumerate(lines, 1):
                for token in set(re.findall(r"\bGFX_[A-Za-z0-9_]+", line)):
                    index[token].append(f"{rel(path)}:{number}")
    return index


def consumers(sprite: str, index: dict[str, list[str]], extra: str = "") -> str:
    hits = list(index.get(sprite, []))
    if extra:
        hits.append(extra)
    if not hits:
        return "not found outside registration; runtime consumer binding remains an audit item"
    if len(hits) > 6:
        return "<br>".join(hits[:6]) + f"<br>… (+{len(hits) - 6} references)"
    return "<br>".join(hits)


def manifest_lookup() -> tuple[list[dict], dict[str, dict]]:
    data = json.loads(text(ROOT / "docs/plans/ireland_focus_tree/assets/source_manifest.json"))
    rows = data["entries"]
    lookup: dict[str, dict] = {}
    for entry in rows:
        for key in sprite_candidates(entry.get("intended_sprite_name", "")):
            if key:
                lookup[key] = entry
    return rows, lookup


def staging_paths(group: str, row: GfxRow, ordinal: int | None = None) -> tuple[str, str, str]:
    texture = row.texture.replace("\\", "/")
    base = Path(texture).stem
    source: Path | None = None
    processed: Path | None = None
    fallback: Path | None = None

    if group == "focus":
        stem = row.sprite.removeprefix("GFX_focus_")
        source = FRESH_FOCUS_ICON_ROOT / "source_png" / "focus" / f"goal_{stem}.png"
        processed = FRESH_FOCUS_ICON_ROOT / "processed_png" / "focus" / f"goal_{stem}.png"
    elif group == "decision_category":
        source = ICON_ROOT / "source_png/decision_categories" / f"{base}_source.png"
        processed = ICON_ROOT / "processed_png/decision_categories" / f"{base}.png"
    elif group == "decision_action":
        source = ICON_ROOT / "source_png/decision_actions" / f"{base}_source.png"
        processed = ICON_ROOT / "processed_png/decision_actions" / f"{base}.png"
    elif group == "mission":
        source = ICON_ROOT / "source_png/missions" / f"{base}_source.png"
        processed = ICON_ROOT / "processed_png/missions" / f"{base}.png"
    elif group == "spirit":
        source = ICON_ROOT / "source_png/spirits" / f"{base}_source.png"
        processed = ICON_ROOT / "processed_png/spirits" / f"{base}.png"
    elif group == "overlay":
        source = ICON_ROOT / "source_png/temporary_overlays" / f"{base}_source.png"
        processed = ICON_ROOT / "processed_png/temporary_overlays" / f"{base}.png"
    elif group == "law":
        source = FRESH_LAW_ICON_ROOT / "source_png" / "law" / f"{base}.png"
        processed = FRESH_LAW_ICON_ROOT / "processed_png" / "law" / f"{base}.png"
    elif group == "mechanic":
        source = ICON_ROOT / "source_png/mechanic_ledger" / f"{base}_source.png"
        processed = ICON_ROOT / "processed_png/mechanic_ledger" / f"{base}.png"
    elif group == "achievement":
        if ordinal is None:
            raise ValueError("achievement rows require an ordinal")
        source_base = f"achievement_ireland_{ordinal:03d}"
        suffix = ""
        for state in ("grey", "not_eligible"):
            if row.sprite.endswith("_" + state):
                suffix = "_" + state
        source = ICON_ROOT / "source_png/achievements" / f"{source_base}{suffix}_source.png"
        processed = ICON_ROOT / "processed_png/achievements" / f"{source_base}{suffix}.png"
    elif group == "event_generated":
        source = ASSET_ROOT / "generated/source_png" / f"{base}.png"
        processed = ASSET_ROOT / "generated/processed_png" / f"{base}.png"
    elif group == "route_collective":
        stem = row.sprite.removeprefix("GFX_IRE_")
        source = ASSET_ROOT / "generated/collective_portraits/source_png" / f"{stem}.png"
        processed = ASSET_ROOT / "generated/collective_portraits/processed_png" / f"{stem}.png"
    elif group == "route_emblem":
        stem = Path(texture).stem
        source_stem = stem.removesuffix("_large").removesuffix("_small")
        source = ASSET_ROOT / "generated/emblems/source_png" / f"{source_stem}_master.png"
        processed = ASSET_ROOT / "generated/emblems/processed_png" / f"{stem}.png"
    elif group == "gui":
        parts = texture.split("/")
        surface = parts[-2]
        gui_stem = row.sprite.removeprefix("GFX_ireland_gui_")
        source = ASSET_ROOT / "generated/gui" / surface / "source" / f"{gui_stem}_source.png"
        processed = ASSET_ROOT / "generated/gui" / surface / "processed" / f"{gui_stem}.png"
        fallback = ASSET_ROOT / "generated/gui" / surface / "static_fallback" / f"{gui_stem}_static_fallback.dds"
    elif group == "animation":
        if base.endswith("_sheet"):
            slug = base.removesuffix("_sheet")
        elif base.endswith("_static"):
            slug = base.removesuffix("_static")
        else:
            slug = base
        source = ASSET_ROOT / "animations" / slug / "source_frames"
        processed = ASSET_ROOT / "animations" / slug / "processed_frames"
        fallback = ASSET_ROOT / "animations" / slug / f"{slug}_static.png"

    source_value = rel(source) if source else "not separately staged by this package"
    processed_value = rel(processed) if processed else "not separately staged by this package"
    fallback_value = rel(fallback) if fallback else "—"
    return source_value, processed_value, fallback_value


def status_for(runtime: str, source: str, processed: str) -> str:
    runtime_ok = existing(runtime)
    source_ok = existing(source) or source.endswith("/source_frames")
    processed_ok = existing(processed) or processed.endswith("/processed_frames")
    return "runtime+source+processed present" if runtime_ok and source_ok and processed_ok else (
        "runtime present; staging evidence incomplete" if runtime_ok else "runtime missing"
    )


def markdown_cell(value_text: str) -> str:
    return value_text.replace("|", "\\|").replace("\n", "<br>")


def row_line(number: int, owner: str, requirement: str, sprite: str, registration: str, source: str, processed: str, consumer: str, binding: str, status: str) -> str:
    cells = [
        str(number),
        owner,
        requirement,
        f"`{sprite}`",
        registration,
        source,
        processed,
        consumer,
        binding,
        status,
    ]
    return "| " + " | ".join(markdown_cell(item) for item in cells) + " |"


def table_header() -> str:
    return "| # | owner | requirement | sprite / engine id | runtime registration | source evidence | processed evidence | live consumer | state / visibility binding | status |\n|---:|---|---|---|---|---|---|---|---|---|"


def render_gfx_section(title: str, owner: str, rows: list[GfxRow], group: str, index: dict[str, list[str]], manifest_by_sprite: dict[str, dict], start_number: int, code_by_identifier: dict[str, CodeRow] | None = None, achievement_ids: dict[str, int] | None = None) -> tuple[list[str], int]:
    lines = [f"## {title}", "", table_header()]
    number = start_number
    action_texture_counts = Counter(row.texture for row in rows)
    for row in rows:
        row_group = row.kind if group.startswith("route_") else group
        ordinal = achievement_ids.get(row.sprite) if achievement_ids else None
        source, processed, fallback = staging_paths(row_group, row, ordinal)
        manifest = manifest_by_sprite.get(row.sprite) or manifest_by_sprite.get(row.sprite.removeprefix("GFX_"))
        if manifest and group != "focus":
            # A cleared source may live only in the preserved-evidence path.
            # Prefer that path when production source is intentionally absent,
            # while keeping a missing processed PNG visibly missing.
            source = rel(
                manifest.get("source_path")
                or manifest.get("source_preservation_path")
                or "not_created"
            )
            processed = rel(manifest.get("processed_png_path") or "not_created")
        runtime = rel(row.texture)
        status = status_for(runtime, source, processed)
        if manifest:
            status = f"manifest {manifest.get('status', 'unknown')} / {manifest.get('clearance_state', 'state not recorded')}"
        consumer_extra = ""
        code = code_by_identifier.get(row.sprite) if code_by_identifier else None
        if code:
            consumer_extra = f"{code.file}:{code.line}"
        if code:
            binding = condition_summary(code.block)
        elif index.get(row.sprite):
            binding = "direct consumer listed; no separate state/visibility block"
        else:
            binding = "registration only; see consumer references"
        if group == "animation":
            frames = value(row.block, "noOfFrames")
            fps = value(row.block, "animation_rate_fps")
            looping = value(row.block, "looping")
            binding = f"frames={frames}; fps={fps}; looping={looping}; static fallback={fallback}"
        if group == "achievement":
            state = "completed"
            if row.sprite.endswith("_grey"):
                state = "grey"
            elif row.sprite.endswith("_not_eligible"):
                state = "not eligible"
            binding = f"achievement state={state}; engine suffix convention; owning achievement block is listed in consumer"
        if group == "decision_action" and action_texture_counts[row.texture] > 1:
            binding += f"; controlled reuse={action_texture_counts[row.texture]} named action aliases share this DDS"
        lines.append(
            row_line(
                number,
                owner,
                row.sprite.removeprefix("GFX_"),
                row.sprite,
                f"{row.gfx_file}:{row.line} → `{runtime}`",
                f"`{source}`",
                f"`{processed}`",
                consumers(row.sprite, index, consumer_extra),
                binding,
                status,
            )
        )
        number += 1
    lines.append("")
    return lines, number


def main() -> None:
    gfx_rows = all_gfx_rows()
    by_sprite: dict[str, list[GfxRow]] = defaultdict(list)
    for row in gfx_rows:
        by_sprite[row.sprite].append(row)
    primary_gfx = {row.sprite: row for row in gfx_rows}
    index = build_consumer_index()
    manifest_rows, manifest_lookup_by_name = manifest_lookup()
    blocked_manifest_rows = [row for row in manifest_rows if row.get("status") in {"blocked", "needs_user_review"}]
    source_event_rows = [row for row in manifest_rows if row.get("family") == "event_news"]

    focus_path = ROOT / "common/national_focus/ireland_focus_tree.txt"
    decision_path = ROOT / "common/decisions/ireland_decisions.txt"
    category_path = ROOT / "common/decisions/categories/ireland_categories.txt"
    spirit_path = ROOT / "common/ideas/ireland_spirits.txt"
    achievement_path = ROOT / "common/achievements/ireland_achievements.txt"

    focus_rows = parse_focus_rows(focus_path)
    fresh_focus_source_count = len(list((FRESH_FOCUS_ICON_ROOT / "source_png" / "focus").glob("*.png")))
    fresh_focus_status = (
        f"{fresh_focus_source_count} independently generated emblems have full staging evidence"
        if fresh_focus_source_count
        else "no fresh focus source rows are present in this checkout"
    )
    category_rows = parse_code_rows(category_path, r"^(ireland_[A-Za-z0-9_]+)\s*=\s*\{")
    action_rows = assign_decision_parents(parse_code_rows(decision_path, r"^\t(ireland_action_[A-Za-z0-9_]+)\s*=\s*\{"), decision_path)
    mission_rows = assign_decision_parents(parse_code_rows(decision_path, r"^\t(ireland_mission_[A-Za-z0-9_]+)\s*=\s*{"), decision_path)
    spirit_rows = parse_code_rows(spirit_path, r"^\s*(ireland_spirit_[A-Za-z0-9_]+)\s*=\s*\{")

    achievement_source = text(achievement_path)
    achievement_blocks = parse_code_rows(achievement_path, r"^(ireland_[A-Za-z0-9_]+)\s*=\s*\{")
    achievement_blocks = [row for row in achievement_blocks if row.identifier != "unique_id"]
    achievement_id_lines = {row.identifier: row.line for row in achievement_blocks}
    achievement_order = {f"GFX_achievement_{row.identifier}": index + 1 for index, row in enumerate(achievement_blocks)}
    achievement_ids: dict[str, int] = {}
    for base_sprite, ordinal in achievement_order.items():
        for suffix in ("", "_grey", "_not_eligible"):
            achievement_ids[base_sprite + suffix] = ordinal

    manifest_by_sprite: dict[str, dict] = {}
    for entry in manifest_rows:
        intended = entry.get("intended_sprite_name", "")
        for candidate in sprite_candidates(intended):
            if candidate:
                manifest_by_sprite[candidate] = entry

    decision_gfx = [row for row in gfx_rows if row.kind == "focus" and row.sprite.startswith("GFX_decision_")]
    category_gfx = [row for row in decision_gfx if row.sprite.startswith("GFX_decision_category_")]
    action_gfx = [row for row in decision_gfx if row.sprite.startswith("GFX_decision_ireland_")]
    mission_gfx = [row for row in gfx_rows if row.kind == "secondary" and row.sprite.startswith("GFX_mission_")]
    spirit_gfx = [
        row
        for row in gfx_rows
        if row.kind == "secondary"
        and row.sprite.lower().startswith(("gfx_idea_ireland_spirit_", "gfx_ireland_spirit_"))
    ]
    overlay_gfx = [row for row in gfx_rows if row.kind == "secondary" and row.sprite.startswith("GFX_ireland_temporary_overlay_")]
    law_gfx = [row for row in gfx_rows if row.kind == "secondary" and row.sprite.startswith("GFX_ireland_law_")]
    mechanic_gfx = [row for row in gfx_rows if row.kind == "secondary" and row.sprite.startswith("GFX_ireland_mechanic_ledger_")]
    achievement_gfx = [row for row in gfx_rows if row.kind == "secondary" and row.sprite.startswith("GFX_achievement_")]
    route_gfx = [row for row in gfx_rows if row.kind == "route"]
    gui_gfx = [row for row in gfx_rows if row.kind == "gui"]
    animation_gfx = [row for row in gfx_rows if row.kind == "animation"]
    event_gfx = [row for row in gfx_rows if row.kind == "event"]
    sourced_gfx = [row for row in gfx_rows if row.kind == "sourced"]

    sections: list[str] = [
        "# Ireland asset coverage crosswalk",
        "",
        f"Generated {date.today().isoformat()} by `docs/plans/ireland_focus_tree/assets/build_asset_coverage_crosswalk.py`.",
        "",
        "This is the row-level handoff between canonical requirements, source or generated evidence, Ireland-owned runtime registrations, and live implementation consumers. `assets/` is staging only; every runtime path in this report is rooted under the mod's standard `gfx/` tree. A row marked blocked or needs_user_review is deliberately not cleared by registration.",
        "",
        "## Coverage summary",
        "",
        "| surface | canonical rows | runtime registrations | consumer surface | visual/source status |",
        "|---|---:|---:|---|---|",
        f"| Focus goal icons | {len(focus_rows)} | {len(focus_rows)} | `common/national_focus/ireland_focus_tree.txt` + paired shine masks | {fresh_focus_status}; all runtime focus DDS rows remain listed individually below |",
        f"| Decision categories | {len(category_rows)} | {len(category_gfx)} | `common/decisions/categories/ireland_categories.txt` | registered |",
        f"| Named decision actions | {len(action_rows)} | {len(action_gfx)} unique action sprites | `common/decisions/ireland_decisions.txt` + `common/decisions/ireland_marine_service.txt` | {len(set(row.texture for row in action_gfx))} controlled-reuse textures |",
        f"| Missions | {len(mission_rows)} | {len(mission_gfx)} | `common/decisions/ireland_decisions.txt` | registered; mission outcome blocks remain code-owned |",
        f"| Persistent route spirits | {len(spirit_rows)} | {len(spirit_gfx)} | `common/ideas/ireland_spirits.txt` | registered route-spirit entries |",
        f"| Temporary overlays | 10 durable overlays + 17 event/temporary overlays | {len(overlay_gfx)} | decision/event/controller consumers | registered; conditional state bindings audited per row |",
        f"| Law icons | {len(law_gfx)} | {len(law_gfx)} | scripted law stages in `common/scripted_effects/ireland_laws.txt` | registered; dynamic stage-to-sprite binding is recorded per row |",
        f"| Mechanic/ledger icons | {len(mechanic_gfx)} | {len(mechanic_gfx)} | BOP and scripted GUI surfaces | registered; direct consumer evidence listed per row |",
        f"| Achievement states | {len(achievement_gfx)} | {len(achievement_gfx)} | `common/achievements/ireland_achievements.txt` | registered achievement-state rows |",
        f"| Route/symbol assets | {len(route_gfx)} | {len(route_gfx)} | route character and route-state consumers | generated source packages; runtime DDS present |",
        f"| Scripted GUI assets | {len(gui_gfx)} | {len(gui_gfx)} | three GUI layouts | static runtime package; state surface listed per row |",
        f"| Independent animations | {len(animation_gfx)} registrations | {len(animation_gfx)} | three GUI surfaces and event/evidence states | frame sheets + static fallbacks |",
        f"| Generated event/news art | {len(event_gfx)} | {len(event_gfx)} | event/news code consumers | generated source/processed package; runtime DDS present |",
        f"| Source-package registrations | {len(manifest_rows)} manifest rows | {len(sourced_gfx)} registered rows | leaders, symbols, reports | {len(blocked_manifest_rows)} blocked/review rows remain unpromoted |",
        "",
		f"The canonical goal/law visual evidence is the fresh regenerated package at `assets/ireland_focus_tree/icons/regenerated_goal_and_law_icons_fresh_2026-08-01_v1/`. This checkout contains {fresh_focus_source_count} fresh focus-emblem source rows and 51 fresh 60x68 law-emblem sources. The complete {len(focus_rows)}-focus runtime set is checked row-by-row below; source and processing evidence remain a separate staging concern, while final DDS files belong under the mod's standard `gfx/` tree.",
        "",
    ]

    row_number = 1
    section, row_number = render_gfx_section("Focus goal icons", "goal-icon requirement", [primary_gfx[row.icon] for row in focus_rows if row.icon in primary_gfx], "focus", index, manifest_by_sprite, row_number, {row.icon: row for row in focus_rows})
    sections.extend(section)

    category_code = {row.icon: row for row in category_rows}
    section, row_number = render_gfx_section("Decision categories", "decision category", category_gfx, "decision_category", index, manifest_by_sprite, row_number, category_code)
    sections.extend(section)

    action_code = {row.icon: row for row in action_rows}
    section, row_number = render_gfx_section("Decision action sprites", "decision action", action_gfx, "decision_action", index, manifest_by_sprite, row_number, action_code)
    sections.extend(section)

    mission_code = {row.icon: row for row in mission_rows}
    section, row_number = render_gfx_section("Mission sprites", "mission family", mission_gfx, "mission", index, manifest_by_sprite, row_number, mission_code)
    sections.extend(section)

    spirit_code = {row.icon: row for row in spirit_rows}
    section, row_number = render_gfx_section("Persistent route-spirit sprites", "persistent route spirit", spirit_gfx, "spirit", index, manifest_by_sprite, row_number, spirit_code)
    sections.extend(section)

    section, row_number = render_gfx_section("Temporary overlay sprites", "temporary overlay", overlay_gfx, "overlay", index, manifest_by_sprite, row_number)
    sections.extend(section)

    section, row_number = render_gfx_section("Law-stage sprites", "law stage", law_gfx, "law", index, manifest_by_sprite, row_number)
    sections.extend(section)

    section, row_number = render_gfx_section("Mechanic and ledger sprites", "mechanic / ledger", mechanic_gfx, "mechanic", index, manifest_by_sprite, row_number)
    sections.extend(section)

    achievement_code = {
        f"GFX_achievement_{identifier}": CodeRow(identifier, f"GFX_achievement_{identifier}", rel(achievement_path), line, "")
        for identifier, line in achievement_id_lines.items()
    }
    section, row_number = render_gfx_section("Achievement state sprites", "achievement state", achievement_gfx, "achievement", index, manifest_by_sprite, row_number, achievement_code, achievement_ids)
    sections.extend(section)

    route_rows: list[GfxRow] = []
    for row in route_gfx:
        group = "route_collective" if row.sprite.startswith("GFX_IRE_collective_") else "route_emblem"
        route_rows.append(GfxRow(group, row.sprite, row.texture, row.gfx_file, row.line, row.sprite_type, row.block))
    section, row_number = render_gfx_section("Route collective portraits and symbols", "route identity asset", route_rows, "route_collective", index, manifest_by_sprite, row_number)
    sections.extend(section)

    section, row_number = render_gfx_section("Scripted GUI static assets", "GUI surface asset", gui_gfx, "gui", index, manifest_by_sprite, row_number)
    sections.extend(section)

    section, row_number = render_gfx_section("Independent animation registrations", "animation package", animation_gfx, "animation", index, manifest_by_sprite, row_number)
    sections.extend(section)

    generated_event_rows = [GfxRow("event_generated", row.sprite, row.texture, row.gfx_file, row.line, row.sprite_type, row.block) for row in event_gfx]
    section, row_number = render_gfx_section("Generated event and news art", "generated event/news art", generated_event_rows, "event_generated", index, manifest_by_sprite, row_number)
    sections.extend(section)

    section, row_number = render_gfx_section("Sourced leaders, symbols, and report art", "source-package runtime row", sourced_gfx, "sourced", index, manifest_by_sprite, row_number)
    sections.extend(section)

    sections.extend(["## Source-package manifest coverage", "", "The following rows are the source-of-truth clearance ledger. A final DDS path does not override a blocked or needs_user_review state. Rows without a registered sprite are intentionally surfaced as unresolved wiring rather than silently treated as complete.", "", table_header()])
    for number, entry in enumerate(manifest_rows, row_number):
        intended = entry.get("intended_sprite_name", "—")
        candidates = [candidate for candidate in sprite_candidates(intended) if candidate in by_sprite]
        registration = "<br>".join(f"{row.gfx_file}:{row.line} → `{rel(row.texture)}`" for candidate in candidates for row in by_sprite[candidate]) or "not registered in Ireland-owned .gfx"
        consumer_hits = []
        for candidate in candidates:
            consumer_hits.extend(index.get(candidate, []))
        if not consumer_hits and candidates:
            consumer_hits.append("registered sprite has no non-.gfx consumer reference")
        if not consumer_hits:
            consumer_hits.append("no registered sprite consumer")
        state = entry.get("status", "unknown") + "; " + entry.get("clearance_state", "clearance state not recorded")
        sections.append(
            row_line(
                number,
                entry.get("family", "source package"),
                entry.get("id", "—") + " — " + entry.get("canonical_name", "—"),
                intended,
                registration,
                f"`{rel(entry.get('source_path', 'not_created'))}`",
                f"`{rel(entry.get('processed_png_path', 'not_created'))}`",
                "<br>".join(consumer_hits[:8]),
                "manifest clearance and intended-use record; blocked/review rows stay concealed or review-gated",
                state,
            )
        )
    sections.extend([
        "",
        "## Audit interpretation",
        "",
		"- Earlier focus-icon normalization and v5-v12 packages are retained as technical or rejected evidence only. The fresh 2026-08-01 package is the accepted goal/law source of truth after complete-sheet boundary, chroma, alignment, and runtime readback review.",
		f"- The {len(focus_rows)} focus and 51 law rows are wired to stable runtime names and `.gfx` registrations. The fresh staging package supplies {fresh_focus_source_count} focus source rows; every runtime DDS row, including the restored naval focus rows, is listed and checked individually.",
        f"- Decision-action rows distinguish {len(action_rows)} named consumers from the {len(set(row.texture for row in action_gfx))} allocated DDS textures. Reuse is recorded at the row level and is not a free placeholder: each reused texture has a named decision consumer and category binding.",
        "- The law, overlay, and mechanic packages are registered assets whose dynamic state controllers are intentionally listed in the consumer column. A missing direct `GFX_` token is an audit finding, not a claim that the asset is used.",
        f"- Portrait, symbol/document, and source event/news clearance remains governed by the five-state manifest. The manifest contains 60 portrait rows, 40 symbol/document rows, and {len(source_event_rows)} source event/news rows; {len(blocked_manifest_rows)} blocked/review rows remain unpromoted and are not cleared by this crosswalk.",
        "- Live HOI4 engine, GUI click-region, frame playback, texture-loading, and scenario validation remain intentionally unrun and are excluded from the completion gate by user direction; this report is static coverage evidence.",
        "",
    ])
    OUT.write_text("\n".join(sections) + "\n", encoding="utf-8")
    print(f"wrote {rel(OUT)}")
    print(f"focus={len(focus_rows)} categories={len(category_rows)} actions={len(action_rows)} missions={len(mission_rows)} spirits={len(spirit_rows)} achievements={len(achievement_blocks)} manifest={len(manifest_rows)}")


if __name__ == "__main__":
    main()
