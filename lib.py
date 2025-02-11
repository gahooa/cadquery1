import cadquery as cq
import subprocess

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


def dove_box(text, x=0, y=0, d=180):
    angle = 0

    wp = cq.Workplane("XY").moveTo(x, y)

    for char in text:
        if char == ' ':
            continue
        elif char == "F":
            wp = wp.polarLine(10, angle).polarLine(2, angle+135).polarLine(4, angle).polarLine(2, angle-135).polarLine(10, angle)
            wp = wp.polarLine(10, angle).polarLine(2, angle-135).polarLine(4, angle).polarLine(2, angle+135).polarLine(10, angle)
        elif char == "L":
            angle += 90
        elif char == "R":
            angle -= 90
        else:
            raise Exception(f"Invalid character: {char}")

    wp = wp.close()

    wp = wp.extrude(d)

    return wp