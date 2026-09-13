# FDM design and validation

Establish the material, nozzle, layer height, extrusion/XY calibration,
orientation, loads, mating part, and required feel before setting a clearance.
Make fit and compensation named parameters, never unexplained offsets. If no
printer profile exists, state the missing data and choose a conservative coupon
instead of inventing a universal tolerance.

For enclosures with sliding lids, verify the retained item envelope, wall and
floor thickness, lid travel, positive stop, rail engagement, finger access, and
the open/closed clearance. Evaluate print orientation, bridging/overhangs,
support removal, anisotropic strength, and likely wear surfaces.

Use this loop: valid CAD solid and mesh -> process/orientation check -> export
-> small fit coupon -> print and measure -> update named calibration parameters
-> revalidate -> full-part acceptance. Physical acceptance requires real slicer,
printer, and measurement feedback; digital checks cannot prove it.
