from __future__ import annotations

import importlib
from typing import Any


class MissingDependencyError(RuntimeError):
    """Raised when a runtime dependency is not installed."""


def require_module(module_name: str, install_name: str | None = None) -> Any:
    try:
        return importlib.import_module(module_name)
    except ModuleNotFoundError as exc:
        pip_name = install_name or module_name
        raise MissingDependencyError(
            f"Missing dependency '{module_name}'. Install with: pip install {pip_name}"
        ) from exc
