"""PhotoCraft command-line entry point."""
import sys
from pathlib import Path

from PIL import Image

from .core import load_action, run_action


def main(argv=None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    if len(argv) < 3 or argv[0] != "run":
        print("Usage: python -m photocraft run <action.json> <input> <output>")
        return 1
    action = load_action(argv[1])
    img = Image.open(argv[2])
    out = run_action(img, action)
    Path(argv[3]).parent.mkdir(parents=True, exist_ok=True)
    out.save(argv[3])
    print(f"Saved -> {argv[3]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
