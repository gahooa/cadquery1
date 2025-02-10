import subprocess
import cadquery as cq


def show(o):
    cq.exporters.export(o, 'o.step')
    subprocess.run((
        'f3d', 
        '--camera-orthographic=0',
        '--grid-color', '0.8,0.8,0.8', 
        '--grid-absolute',
        '--grid-unit', '10',
        '--grid-subdivisions', '10',
        '--background-color', '1,1,1', 
        '--position', '100,1400', 
        '--resolution', '2000,1600', 
        '--point-size', '4',
        '--line-width', '2',
        'o.step',
    ))

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





