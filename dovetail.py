
import cadquery as cq
from lib import show, dove_box




wp1 = dove_box("F F F L F L F R F L F L F R F L F")
wp2 = dove_box("F L F R F R F L F L F F L F F F L F F", 0, 100)

wp = wp1.union(wp2)


show(wp)

