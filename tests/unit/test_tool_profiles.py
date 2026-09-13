"""Tests for token-efficient MCP tool profiles."""

from collections.abc import Callable
from typing import Any

from freecad_mcp.tools import PRINT3D_TOOLS, register_all_tools


class MockMCP:
    """Minimal FastMCP stand-in that records decorated tools."""

    def __init__(self) -> None:
        self.registered: dict[str, Any] = {}

    def tool(self, *args: Any, **kwargs: Any) -> Callable[[Any], Any]:
        def decorator(func: Any) -> Any:
            self.registered[func.__name__] = func
            return func

        return decorator


async def _get_bridge() -> Any:
    return None


def test_print3d_profile_registers_only_curated_tools() -> None:
    mcp = MockMCP()
    register_all_tools(mcp, _get_bridge, profile="print3d")

    assert set(mcp.registered) == PRINT3D_TOOLS
    assert "create_sketch" not in mcp.registered
    assert "spreadsheet_create" not in mcp.registered


def test_unknown_profile_is_rejected() -> None:
    mcp = MockMCP()

    try:
        register_all_tools(mcp, _get_bridge, profile="small")
    except ValueError as error:
        assert "FREECAD_TOOL_PROFILE" in str(error)
    else:
        raise AssertionError("An unknown profile must fail clearly")
