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

## Per-part printability gate

Before accepting a printable assembly, evaluate every exported part separately
in its declared print orientation. Record the bed-contact faces, unsupported
overhangs/bridges, the largest unsupported span, support policy, and any
surface that must remain cosmetic or dimensionally accurate. A part fails this
gate if its intended orientation leaves a large plate or roof bridging between
narrow rails/tongues, even when the CAD solid and assembly sweep are valid.
Do not hide that failure by calling the part "printable"; either redesign its
cross-section, deliberately choose/remove support, or choose and document a
different orientation.

For a flush sliding lid, include a section normal to the slide direction and
measure the actual, post-boolean geometry: panel thickness over its unsupported
span; tongue and groove envelopes; clearance at every limiting face; and the
remaining wall web/cap after a groove is cut. Named values are not sufficient
when later booleans, fillets, or overlap used to unite a solid change them.
Flag a thin, wide panel as a flex/warp risk and require a stiffness decision or
coupon; do not infer stiffness from a valid mesh. When no calibrated printer
profile is available, use a coupon containing the full tongue/groove section
and enough panel width to expose bridging or flex, not only a tiny rail strip.

The digital report must state pass/fail for: assembly motion, each part's print
orientation/support check, interface fit envelope, remaining structural web,
and the physical coupon needed. A failed per-part gate blocks final production
STL acceptance, though diagnostic exports may still be saved.

Use this loop: valid CAD solid and mesh -> process/orientation check -> export
-> small fit coupon -> print and measure -> update named calibration parameters
-> revalidate -> full-part acceptance. Physical acceptance requires real slicer,
printer, and measurement feedback; digital checks cannot prove it.
