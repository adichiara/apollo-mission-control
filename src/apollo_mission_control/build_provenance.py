"""Runtime build provenance for physical playtest evidence.

This is modern validation infrastructure, not Apollo-era simulation state.
"""

from __future__ import annotations

import os
from typing import Any


def build_provenance() -> dict[str, Any]:
    """Return stable build identity without exposing secrets or hidden sim state."""
    commit = (
        os.getenv("RENDER_GIT_COMMIT")
        or os.getenv("APOLLO_BUILD_COMMIT")
        or "unknown"
    )
    return {
        "commit": commit,
        "environment": "render" if os.getenv("RENDER", "").lower() == "true" else "local",
        "service_id": os.getenv("RENDER_SERVICE_ID"),
        "service_name": os.getenv("RENDER_SERVICE_NAME"),
    }
