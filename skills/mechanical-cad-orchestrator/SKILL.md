---
name: mechanical-cad-orchestrator
description: Turn mechanical-product intent into a researched, parametric CAD plan and verified FreeCAD outputs, especially for functional 3D-printable parts and assemblies.
---

# Mechanical CAD Orchestrator

Use this skill for functional mechanical parts, enclosures, moving interfaces,
assemblies, and 3D-printable components. Act as a design engineer: understand
the job to be done before selecting a CAD operation. Do not use it for purely
artistic meshes, certification claims, or unverified CAM/FEA conclusions.

## Mandatory artifact location

Unless the user explicitly chooses another location, create a descriptive
project directory below `D:\3D` before generating any model. Save the source
CAD file, scripts, exports, validation report, and preview there; do not leave
3D deliverables in Documents, Desktop, or a repository.

## Workflow

1. **Turn the request into a design brief.** Identify the object, user goal,
   retained components, loads, motion, assembly/disassembly, material and
   process, critical dimensions/standards, and requested deliverables. Ask one
   focused question only when a fit, safety, or compliance decision depends on
   it; otherwise state reasonable assumptions.
2. **Select a construction strategy.** Read [CAD strategy](references/cad-strategy.md).
   Decide the parameter groups, reference scheme, workbench, feature order, and
   validation points before building. Use FreeCAD as the default executable CAD
   backend. Use AutoCAD only when the user specifically needs it and a connected
   automation path exists; otherwise hand off neutral STEP/DXF geometry rather
   than claiming an AutoCAD action occurred.
3. **Research only what is needed.** Read [research routing](references/research-routing.md).
   Browse for unfamiliar mechanisms, materials, standards, process constraints,
   or likely failure modes. Start specific, then widen to analogous designs.
   Record the design decision and source, not a bulk copy of web pages or books.
4. **Build with the narrow CAD interface.** Use the `freecad-print3d` MCP
   server backed by the user's `williamduong/freecad-robust-mcp` fork. It is the
   `print3d` profile, deliberately limited to creation, inspection, validation,
   export, and recovery tools. Prefer one parameterized FreeCAD Python payload
   per coherent part; recompute after each meaningful feature. Escalate to the
   full profile only when a specialized tool materially reduces risk or work.
5. **Verify the design, not just command success.** Confirm recompute succeeds,
   the result is a valid positive-volume solid, critical dimensions and
   clearances are represented, and requested STEP/STL/3MF files export. Use
   `safe_execute` and `undo_if_invalid` around risky edits.
6. **For FDM / 3D printing, run the manufacturing loop.** Read
   [FDM design and validation](references/fdm-design-and-validation.md). Use
   named fit parameters, check orientation/support/overhang implications, then
   propose a small coupon before committing to a costly full print. Update only
   from actual printer/slicer/measurement feedback; never claim a physical fit
   was proven without it.

## Delegation and context discipline

For a complex request, delegate one bounded task at a time: a mechanism
researcher, CAD-strategy reviewer, or final manufacturability reviewer. Give a
subagent the brief plus only the relevant reference card and return a compact
decision report. Keep one owner for editing CAD files. Do not delegate routine
operations or load every reference preemptively.

## Deliverable report

State: interpreted intent and assumptions; selected construction approach;
research findings that changed a decision; named parameters and interfaces;
validation results and output paths; remaining manufacturing caveats; and the
next physical test when applicable.
