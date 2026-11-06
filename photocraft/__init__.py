"""PhotoCraft - photo processing plugin & action library."""
from .core import Plugin, register, REGISTRY, load_action, run_action

__all__ = ["Plugin", "register", "REGISTRY", "load_action", "run_action"]
__version__ = "0.1.0"
