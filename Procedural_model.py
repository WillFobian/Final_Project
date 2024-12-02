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

def create_random_sphere():
    x_pos = random.uniform(-10, 10)
    y_pos = random. uniform(0, 5)
    z_pos = random.uniform(-10, 10)
    radius = random.uniform(1,3)
    rotation = [random.uniform(0, 360) for _ in range(3)]
    sphere = cmds.polySphere(r=radius)[0]
    cmds.move(x_pos, y_pos, z_pos, sphere)
    cmds.rotate(rotation[0], rotation[1], rotation[2], sphere)
    apply_random_color(sphere)
    return sphere

def create_random_cylinder():
    x_pos = random.uniform(-10, 10)
    y_pos = random.uniform(0, 5)
    z_pos = random.uniform(-10, 10)
    radius = random.uniform(1, 3)
    height = random.uniform(2, 6)
    rotation = [random.uniform(0, 360) for _ in range(3)]
    cylinder = cmds.polyCylinder(r=radius, h=height)[0]
    cmds.move(x_pos, y_pos, z_pos, cylinder)
    cmds.rotate(rotation[0], rotation[1], rotation[2], cylinder)
    apply_random_color(cylinder)
    return cylinder



def apply_random_color(obj):
    shader = cmds.shadingNode('lambert', asShader=True)
    shading_group = cmds.setAttr(shader + ".color", random.random(), random.random(), random.random(), type="double3")
    cmds.select(obj)
    cmds.hyperShade(assign=shader)