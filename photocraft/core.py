"""PhotoCraft core: action runner and plugin base."""
from __future__ import annotations

import abc
from pathlib import Path
from typing import Any

try:
    from PIL import Image
except ImportError:  # pragma: no cover
    Image = None  # type: ignore


class Plugin(abc.ABC):
    """Base class for all PhotoCraft plugins/operators."""

    name: str = "base"

    @abc.abstractmethod
    def apply(self, image, **params):
        """Apply the operation to an image and return a new image."""
        raise NotImplementedError


REGISTRY: dict[str, type[Plugin]] = {}


def register(cls: type[Plugin]) -> type[Plugin]:
    """Class decorator that registers a plugin by its ``name``."""
    REGISTRY[cls.name] = cls
    return cls


@register
class Grayscale(Plugin):
    name = "grayscale"

    def apply(self, image, **params):
        return image.convert("L")


@register
class Resize(Plugin):
    name = "resize"

    def apply(self, image, width=None, height=None, **params):
        if width and height:
            return image.resize((int(width), int(height)))
        return image


@register
class Watermark(Plugin):
    name = "watermark"

    def apply(self, image, text="PhotoCraft", position=(10, 10),
              color=(255, 255, 255), **params):
        from PIL import ImageDraw
        draw = ImageDraw.Draw(image)
        draw.text((int(position[0]), int(position[1])), text, fill=color)
        return image


def load_action(path: str | Path) -> dict:
    """Load an action definition (JSON) from disk."""
    import json
    return json.loads(Path(path).read_text(encoding="utf-8"))


def run_action(image, action: dict):
    """Run every step in an action against the image."""
    for step in action.get("steps", []):
        plugin_cls = REGISTRY[step["plugin"]]
        image = plugin_cls().apply(image, **step.get("params", {}))
    return image
