"""Read back Ireland-owned DDS icon surfaces without launching HOI4.

The audit treats low-alpha BC3 edge noise as non-visible compression residue;
visible chroma-key pixels, opaque border contact, and wrong dimensions remain
failures. Animated frames are listed separately because their green/teal
subject palette is intentional and must not be mistaken for a matte.
"""

from __future__ import annotations

import json
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / "docs/plans/ireland_focus_tree/audits/ireland_runtime_icon_surface_readback_2026-08-02.json"


SURFACES = [
    ("focus_goals", ROOT / "gfx/interface/goals/ireland", (100, 88), 226, True),
    ("law_stages", ROOT / "gfx/interface/ideas/ireland/laws", (60, 68), 51, True),
    ("route_spirits", ROOT / "gfx/interface/ideas/ireland/spirits", (60, 68), 93, True),
    ("decision_categories", ROOT / "gfx/interface/decisions/categories/ireland", (52, 40), 14, True),
    ("decision_actions", ROOT / "gfx/interface/decisions/ireland/actions", (32, 32), 144, True),
    ("missions", ROOT / "gfx/interface/decisions/ireland/missions", (33, 32), 54, True),
    ("mechanic_ledger", ROOT / "gfx/interface/ireland/mechanic_ledger", (64, 64), 45, True),
    ("temporary_overlays", ROOT / "gfx/interface/ireland/temporary_overlays", (32, 32), 27, True),
    ("emblems", ROOT / "gfx/interface/ireland/emblems", None, 16, False),
    ("flags", ROOT / "gfx/interface/ireland/flags", None, 54, False),
]


def inspect(path: Path, expected_size: tuple[int, int] | None, strict_chroma: bool) -> dict:
    image = Image.open(path).convert("RGBA")
    pixels = list(image.getdata())
    visible_key = sum(1 for r, g, b, a in pixels if a >= 8 and r > 220 and g < 45 and b > 170)
    visible_green = sum(1 for r, g, b, a in pixels if a >= 8 and r < 30 and g > 220 and b < 30)
    edge_visible = 0
    for x in range(image.width):
        edge_visible += image.getpixel((x, 0))[3] >= 8
        edge_visible += image.getpixel((x, image.height - 1))[3] >= 8
    for y in range(image.height):
        edge_visible += image.getpixel((0, y))[3] >= 8
        edge_visible += image.getpixel((image.width - 1, y))[3] >= 8
    result = {
        "path": path.relative_to(ROOT).as_posix(),
        "dimensions": list(image.size),
        "expected_dimensions": list(expected_size) if expected_size else None,
        "dimension_ok": expected_size is None or image.size == expected_size,
        "visible_key_pixels": visible_key,
        "visible_green_pixels": visible_green,
        "visible_edge_pixels": edge_visible,
        "strict_chroma": strict_chroma,
    }
    transparent_surface = expected_size is not None
    result["complete"] = result["dimension_ok"] and (not transparent_surface or edge_visible == 0) and visible_key == 0 and (not strict_chroma or visible_green == 0)
    return result


def main() -> int:
    surfaces = []
    all_complete = True
    for name, directory, expected_size, expected_count, strict_chroma in SURFACES:
        files = sorted(directory.glob("*.dds"))
        rows = [inspect(path, expected_size, strict_chroma) for path in files]
        surface = {
            "name": name,
            "directory": directory.relative_to(ROOT).as_posix(),
            "expected_count": expected_count,
            "actual_count": len(files),
            "count_ok": len(files) == expected_count,
            "rows": rows,
            "complete": len(files) == expected_count and all(row["complete"] for row in rows),
        }
        surfaces.append(surface)
        all_complete = all_complete and surface["complete"]

    result = {"scope": "Ireland-owned runtime icon surfaces", "surfaces": surfaces, "all_complete": all_complete}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"all_complete": all_complete, "surfaces": {s["name"]: s["complete"] for s in surfaces}}))
    return 0 if all_complete else 2


if __name__ == "__main__":
    raise SystemExit(main())
