# CAD strategy

Choose a backend first. FreeCAD plus the connected `freecad-print3d` MCP is the
default execution path. Use AutoCAD only when its automation is actually
available and its 2D/documentation workflow is requested; use STEP or DXF for
an honest interchange otherwise.

| Design form | Default construction |
| --- | --- |
| One contiguous parametric mechanical part | A PartDesign Body with constrained sketches, origin/datum references, then additive/subtractive features. |
| Multiple moving or bought-in parts | Separate bodies/components, a shared master-parameter scheme, and an explicit clearance/envelope check. |
| Early CSG, imported solids, utilities | Part workbench or scripted shapes; retain parameters when future edits are expected. |
| 2D drawing, laser/CNC layout | Draft or Sketcher; export a dimension-controlled DXF. |
| Organic/surface form | Use the appropriate surface/mesh workflow, then explicitly validate the printable/manufacturable shell. |

Anchor primary sketches to origin planes, datum planes, or named master geometry.
Do not make generated faces and edges the only reference for a later critical
sketch: topology can change after edits. Group parameters as requirements,
manufacturing, and calibration. Build in this order: primary envelope;
cavities and retained-component interfaces; repeated/symmetric features;
strength features; edge treatments; cosmetic detail.

Before choosing a construction for sliders, snap fits, hinges, threads,
heat-set inserts, seals, bearings, shafts, or sheet metal, research the exact
mechanism and manufacturing process first.
