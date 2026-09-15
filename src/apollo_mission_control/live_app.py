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
    """Serve guided PC+2 contingency-chain validation controls."""
    return FileResponse(WEB_ROOT / "contingency.html")


@app.get("/model-tests", include_in_schema=False)
def model_tests_console() -> FileResponse:
    """Shareable numerical validation against the protected model API."""
    return FileResponse(WEB_ROOT / "model_tests.html")
