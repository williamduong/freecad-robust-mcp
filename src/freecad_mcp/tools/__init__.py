"""MCP tool implementations for FreeCAD.

This package contains all MCP tool definitions for interacting with FreeCAD.
Tools are organized by category:

- execution: Python code execution tools
- documents: Document management tools
- objects: Object creation and manipulation tools
- partdesign: PartDesign workbench tools
- spreadsheet: Spreadsheet workbench tools for parametric design
- draft: Draft workbench tools (ShapeString for 3D text)
- export: Export functionality tools
- macros: Macro management tools
- view: View and screenshot tools
- validation: Object and document validation tools
"""

import os
from collections.abc import Awaitable, Callable
from typing import Any

from freecad_mcp.tools.documents import register_document_tools
from freecad_mcp.tools.draft import register_draft_tools
from freecad_mcp.tools.execution import register_execution_tools
from freecad_mcp.tools.export import register_export_tools
from freecad_mcp.tools.macros import register_macro_tools
from freecad_mcp.tools.objects import register_object_tools
from freecad_mcp.tools.partdesign import register_partdesign_tools
from freecad_mcp.tools.spreadsheet import register_spreadsheet_tools
from freecad_mcp.tools.validation import register_validation_tools
from freecad_mcp.tools.view import register_view_tools

__all__ = [
    "register_all_tools",
    "register_document_tools",
    "register_draft_tools",
    "register_execution_tools",
    "register_export_tools",
    "register_macro_tools",
    "register_object_tools",
    "register_partdesign_tools",
    "register_spreadsheet_tools",
    "register_validation_tools",
    "register_view_tools",
]


PRINT3D_TOOLS = frozenset(
    {
        # One flexible mutation tool is cheaper in context than exposing every
        # PartDesign primitive while retaining the full FreeCAD Python API.
        "execute_python",
        "get_freecad_version",
        "get_connection_status",
        "get_console_output",
        "list_documents",
        "create_document",
        "open_document",
        "save_document",
        "recompute_document",
        "list_objects",
        "inspect_object",
        "export_step",
        "export_stl",
        "export_3mf",
        "validate_object",
        "validate_document",
        "safe_execute",
        "undo_if_invalid",
        "get_screenshot",
        "set_view_angle",
        "fit_all",
    }
)


class _ToolProfileProxy:
    """Pass only profile-allowed ``@mcp.tool`` decorators to FastMCP."""

    def __init__(self, mcp: Any, allowed_tools: frozenset[str]) -> None:
        self._mcp = mcp
        self._allowed_tools = allowed_tools

    def tool(self, *args: Any, **kwargs: Any) -> Callable[[Any], Any]:
        decorator = self._mcp.tool(*args, **kwargs)

        def register(func: Any) -> Any:
            if func.__name__ in self._allowed_tools:
                return decorator(func)
            return func

        return register

    def __getattr__(self, name: str) -> Any:
        return getattr(self._mcp, name)


def register_all_tools(
    mcp: Any,
    get_bridge_func: Callable[[], Awaitable[Any]],
    profile: str | None = None,
) -> None:
    """Register FreeCAD tools with a full or token-efficient profile.

    Args:
        mcp: The FastMCP (Robust MCP Server) instance (Any due to lack of stubs).
        get_bridge_func: Async function returning the active bridge connection.
        profile: ``full`` (default) registers upstream's complete toolset.
            ``print3d`` exposes only the 21 tools needed for parametric
            modeling, validation, export, and optional preview.
    """
    selected_profile = profile or os.environ.get("FREECAD_TOOL_PROFILE", "full")
    if selected_profile not in {"full", "print3d"}:
        raise ValueError(
            "FREECAD_TOOL_PROFILE must be 'full' or 'print3d', "
            f"got {selected_profile!r}"
        )

    profile_mcp = (
        mcp
        if selected_profile == "full"
        else _ToolProfileProxy(mcp, PRINT3D_TOOLS)
    )
    register_execution_tools(profile_mcp, get_bridge_func)
    register_document_tools(profile_mcp, get_bridge_func)
    register_object_tools(profile_mcp, get_bridge_func)
    register_partdesign_tools(profile_mcp, get_bridge_func)
    register_spreadsheet_tools(profile_mcp, get_bridge_func)
    register_draft_tools(profile_mcp, get_bridge_func)
    register_export_tools(profile_mcp, get_bridge_func)
    register_macro_tools(profile_mcp, get_bridge_func)
    register_view_tools(profile_mcp, get_bridge_func)
    register_validation_tools(profile_mcp, get_bridge_func)
