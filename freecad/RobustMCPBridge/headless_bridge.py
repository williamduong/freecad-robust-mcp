"""Start Robust MCP Bridge reliably with FreeCADCmd on Windows.

``startup_bridge.py`` waits for a GUI QApplication. FreeCAD 1.1's Windows
console mode exposes QtCore but no QCoreApplication, which can make that GUI
wait path hang. This dedicated entry point starts the bridge directly and lets
``FreecadMCPPlugin.run_forever`` use its headless queue processor.
"""

from freecad_mcp_bridge.server import FreecadMCPPlugin


if __name__ == "__main__":
    FreecadMCPPlugin().run_forever()
