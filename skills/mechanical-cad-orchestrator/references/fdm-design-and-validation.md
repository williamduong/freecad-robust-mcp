# FDM design and validation

Establish the material, nozzle, layer height, extrusion/XY calibration,
orientation, loads, mating part, and required feel before setting a clearance.
Make fit and compensation named parameters, never unexplained offsets. If no
printer profile exists, state the missing data and choose a conservative coupon
instead of inventing a universal tolerance.

For enclosures with sliding lids, model an explicit assembly/insertion path and
at least closed, working-open, and endpoint poses. For each pose and sampled
travel positions, check that the lid and rail/body do not intersect except at
declared stop faces; record usable travel, minimum rail engagement, open/closed
clearance, and finger access to the actual pull feature. A lid must have either
a positive stop that is compatible with its assembly path or a documented,
intentional removable endpoint. Do not accept a design where end walls block
the only path needed to insert the lid, or where the pull feature is hidden
behind a wall in the closed pose.

Before accepting a digital slider, record a compact motion-evidence table with
the named insertion, closed, working-open, and endpoint poses. For each pose,
record lid position, body/lid interference volume (or an equivalent clearance
test), rearward rail engagement, and whether the pull surface is reachable.
Check the entire interval with enough samples to catch a feature crossing an
end wall, not merely the two endpoints. Geometry/export QA fails if this table
is absent, any undeclared collision is nonzero, or the chosen stop/removal
policy contradicts the assembly path. Render at least one view from the
operating side that exposes this relationship.

Also verify the retained item envelope, wall and floor thickness, print
orientation, bridging/overhangs, support removal, anisotropic strength, and
likely wear surfaces.

Use this loop: valid CAD solid and mesh -> process/orientation check -> export
-> small fit coupon -> print and measure -> update named calibration parameters
-> revalidate -> full-part acceptance. Physical acceptance requires real slicer,
printer, and measurement feedback; digital checks cannot prove it.
