from __future__ import annotations

import argparse
from pathlib import Path


IMPORT_NEEDLE = "import math\n"
IMPORT_REPLACEMENT = "import math\nimport os\n"
SCALE_NEEDLE = '                            "guidance_scale": 0.5,\n'
SCALE_REPLACEMENT = (
    '                            "guidance_scale": float(os.environ.get("DP_GUIDANCE_SCALE", "0.5")),\n'
)
COLLISION_WEIGHT_NEEDLE = "return 3.0 * reward"
COLLISION_WEIGHT_REPLACEMENT = (
    'return float(os.environ.get("DP_COLLISION_GUIDANCE_WEIGHT", "3.0")) * reward'
)


def patch_decoder(repo_root: Path) -> bool:
    decoder_path = repo_root / "diffusion_planner" / "model" / "module" / "decoder.py"
    if not decoder_path.exists():
        raise FileNotFoundError(f"decoder.py not found: {decoder_path}")

    text = decoder_path.read_text(encoding="utf-8")
    updated = text
    if "import os\n" not in updated:
        updated = updated.replace(IMPORT_NEEDLE, IMPORT_REPLACEMENT, 1)
    if SCALE_REPLACEMENT not in updated:
        if SCALE_NEEDLE not in updated:
            raise RuntimeError(
                "Could not find the hardcoded guidance_scale line. "
                "The upstream decoder may have changed."
            )
        updated = updated.replace(SCALE_NEEDLE, SCALE_REPLACEMENT, 1)

    if updated != text:
        decoder_path.write_text(updated, encoding="utf-8")
        return True
    return False


def patch_collision_guidance(repo_root: Path) -> bool:
    collision_path = repo_root / "diffusion_planner" / "model" / "guidance" / "collision.py"
    if not collision_path.exists():
        raise FileNotFoundError(f"collision.py not found: {collision_path}")

    text = collision_path.read_text(encoding="utf-8")
    updated = text
    if "import os\n" not in updated:
        updated = updated.replace("import torch\n", "import os\nimport torch\n", 1)
    if COLLISION_WEIGHT_REPLACEMENT not in updated:
        if COLLISION_WEIGHT_NEEDLE not in updated:
            raise RuntimeError(
                "Could not find the hardcoded collision guidance weight line. "
                "The upstream collision guidance code may have changed."
            )
        updated = updated.replace(COLLISION_WEIGHT_NEEDLE, COLLISION_WEIGHT_REPLACEMENT, 1)

    if updated != text:
        collision_path.write_text(updated, encoding="utf-8")
        return True
    return False


def main() -> None:
    parser = argparse.ArgumentParser(description="Patch upstream Diffusion-Planner guidance overrides.")
    parser.add_argument("--repo-root", required=True, type=Path)
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    decoder_changed = patch_decoder(repo_root)
    collision_changed = patch_collision_guidance(repo_root)
    print(f"guidance_scale_override={'patched' if decoder_changed else 'already_enabled'}")
    print(f"collision_guidance_weight_override={'patched' if collision_changed else 'already_enabled'}")


if __name__ == "__main__":
    main()
