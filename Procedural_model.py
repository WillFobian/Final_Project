import maya.cmds as cmds
import random
import math

def create_random_cube():
    x_pos = random.uniform(-10, 10)
    y_pos = random. uniform(0, 5)
    z_pos = random.uniform(-10, 10)
    size = random.uniform(1, 5)
    rotation = [random.uniform(0, 360) for _ in range(3)]
    cube = cmds.polyCube(w=size, h=size, d=size)[0]
    cmds.move(x_pos, y_pos, z_pos, cube)
    cmds.rotate(rotation[0], rotation[1], rotation[2], cube)
    apply_random_color(cube)

    return cube

