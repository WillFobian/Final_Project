import maya.cmds as cmds
import random

def create_random_cube():
    x_pos = random.uniform(-10, 10)
    y_pos = random.uniform(0, 5)
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
    y_pos = random.uniform(0, 5)
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

def create_random_cone():
    x_pos = random.uniform(-10, 10)
    y_pos = random.uniform(0, 5)
    z_pos = random.uniform(-10, 10)
    radius = random.uniform(1, 2)
    height = random.uniform(2, 6)
    rotation = [random.uniform(0, 360) for _ in range(3)]
    cone = cmds.polyCone(r=radius, h=height)[0]
    cmds.move(x_pos, y_pos, z_pos, cone)
    cmds.rotate(rotation[0], rotation[1], rotation[2], cone)
    apply_random_color(cone)
    return cone

def create_random_torus():
    x_pos = random.uniform(-10, 10)
    y_pos = random.uniform(0, 5)
    z_pos = random.uniform(-10, 10)
    radius = random.uniform(1, 2)
    height = random.uniform(2, 6)
    rotation = [random.uniform(0, 360) for _ in range(3)]
    torus = cmds.polyTorus(r=radius, h=height)[0]
    cmds.move(x_pos, y_pos, z_pos, torus)
    cmds.rotate(rotation[0], rotation[1], rotation[2], torus)
    apply_random_color(torus)
    return torus

def apply_random_color(obj):
    shader = cmds.shadingNode('lambert', asShader=True)
    shading_group = cmds.setAttr(shader + ".color", random.random(), random.random(), random.random(), type="double3")
    shading_group = cmds.setAttr(shader + "SG", 1)
    cmds.setAttr(shading_group + ".surfaceShader", shader, type="node")
    cmds.select(obj)
    cmds.hyperShade(assign=shading_group)

def generate_procedural_scene(num_objects=10):
    for _ in range(num_objects):
        shape_type = random.choice(['cube', 'sphere', 'cylinder', 'cone', 'torus'])
        if shape_type == 'cube':
            create_random_cube()
        elif shape_type == 'sphere':
            create_random_sphere()
        elif shape_type == 'torus':
            create_random_torus()
        elif shape_type == 'cylinder':
            create_random_cylinder()
        elif shape_type == 'cone':
            create_random_cone()
        

