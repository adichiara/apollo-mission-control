"""Deployment entrypoint with live-play validation metadata.

The underlying simulator/API remains ``web_app.app``. This module only adds
modern deployment provenance needed by physical playtest reports.
"""

from __future__ import annotations

from typing import Any

from .build_provenance import build_provenance
from .web_app import app


@app.get("/api/build", tags=["validation"])
def build_info() -> dict[str, Any]:
    """Return the server build identity used to correlate playtest evidence."""
    return build_provenance()
