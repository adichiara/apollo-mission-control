"""Deployment entrypoint with live-play validation metadata.

The underlying simulator/API remains ``web_app.app``. This module only adds
modern deployment provenance needed by physical playtest reports plus small
validation-only pages used on the live deployment.
"""

from __future__ import annotations

from typing import Any

from fastapi.responses import FileResponse

from .build_provenance import build_provenance
from .web_app import WEB_ROOT, app


@app.get("/api/build", tags=["validation"])
def build_info() -> dict[str, Any]:
    """Return the server build identity used to correlate playtest evidence."""
    return build_provenance()


@app.get("/contingency", include_in_schema=False)
def contingency_console() -> FileResponse:
    """Serve the guided PC+2 delta-P contingency validation console."""
    return FileResponse(WEB_ROOT / "contingency.html")


@app.get("/dynamics-test", include_in_schema=False)
def dynamics_test_console() -> FileResponse:
    """Serve the Level-1 causal propulsion/dynamics validation console."""
    return FileResponse(WEB_ROOT / "dynamics.html")
