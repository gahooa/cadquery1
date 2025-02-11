import subprocess
import cadquery as cq
from lib import show

width = 43.55
depth = 175
height = 20.03
wall = 2.5
inner_fillet = 5


result = (
    cq.Workplane("XZ")
    .sketch()
    .trapezoid(4, 8, 90)
    .vertices()
    .circle(0.5, mode="s")
    .reset()
    .vertices()
    .fillet(0.25)
    .reset()
    .rarray(0.6,2, 5, 2)
    .slot(1.5, 0.4, mode="s", angle=122)
    .reset()
    .finalize()
    .extrude(1)
)


foo = cq.Workplane("XY").box(width, depth, height, centered=(True, False, False))

handle = cq.Workplane("XY").circle(width/3).extrude(wall)

foo = foo.union(handle)

# select the top plane of the box
foo = foo.faces(">Z").sketch().rect(width-wall-wall, depth-wall-wall).vertices().fillet(inner_fillet).finalize().cutBlind(-(height-wall))

# select the next to bottom plane of the box
foo = foo.faces(">Z[1]").faces(">Y").edges().fillet(inner_fillet)


# Make the label slot
foo = foo.faces("<X").workplane().moveTo(0, 5).lineTo(-.5, 5.5).lineTo(-.5, 18).lineTo(0, 18.5).close().cutThruAll()

show(foo)





