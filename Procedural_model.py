import maya.cmds as cmds
import random

# Create a random cube
def create_random_cube():
    x_pos = random.uniform(-10, 10)
    y_pos = random.uniform(0, 5)  # Y-axis position fixed to be above the ground
    z_pos = random.uniform(-10, 10)
    size = random.uniform(1, 5)  # Random size for the cube
    rotation = [random.uniform(0, 360) for _ in range(3)]  # Random rotation
    cube = cmds.polyCube(w=size, h=size, d=size)[0]  # Create cube
    cmds.move(x_pos, y_pos, z_pos, cube)  # Position the cube
    cmds.rotate(rotation[0], rotation[1], rotation[2], cube, relative=True)  # Rotate the cube
    apply_random_color(cube)  # Apply random color to the cube
    return cube

# Create a random sphere
def create_random_sphere():
    x_pos = random.uniform(-10, 10)
    y_pos = random.uniform(0, 5)
    z_pos = random.uniform(-10, 10)
    radius = random.uniform(1, 3)
    rotation = [random.uniform(0, 360) for _ in range(3)]  # Random rotation
    sphere = cmds.polySphere(r=radius)[0]  # Create sphere (only radius, no height)
    cmds.move(x_pos, y_pos, z_pos, sphere)  # Position the sphere
    cmds.rotate(rotation[0], rotation[1], rotation[2], sphere, relative=True)  # Rotate the sphere
    apply_random_color(sphere)  # Apply random color to the sphere
    return sphere

# Create a random cylinder
def create_random_cylinder():
    x_pos = random.uniform(-10, 10)
    y_pos = random.uniform(0, 5)
    z_pos = random.uniform(-10, 10)
    radius = random.uniform(1, 3)
    height = random.uniform(2, 6)
    rotation = [random.uniform(0, 360) for _ in range(3)]  # Random rotation
    cylinder = cmds.polyCylinder(r=radius, h=height)[0]  # Create cylinder (correct flags for radius and height)
    cmds.move(x_pos, y_pos, z_pos, cylinder)  # Position the cylinder
    cmds.rotate(rotation[0], rotation[1], rotation[2], cylinder, relative=True)  # Rotate the cylinder
    apply_random_color(cylinder)  # Apply random color to the cylinder
    return cylinder

# Create a random cone
def create_random_cone():
    x_pos = random.uniform(-10, 10)
    y_pos = random.uniform(0, 5)
    z_pos = random.uniform(-10, 10)
    radius = random.uniform(1, 2)
    height = random.uniform(2, 6)
    rotation = [random.uniform(0, 360) for _ in range(3)]  # Random rotation
    cone = cmds.polyCone(r=radius, h=height)[0]  # Create cone (correct flags for radius and height)
    cmds.move(x_pos, y_pos, z_pos, cone)  # Position the cone
    cmds.rotate(rotation[0], rotation[1], rotation[2], cone, relative=True)  # Rotate the cone
    apply_random_color(cone)  # Apply random color to the cone
    return cone

# Create a random torus
def create_random_torus():
    x_pos = random.uniform(-10, 10)
    y_pos = random.uniform(0, 5)
    z_pos = random.uniform(-10, 10)
    radius = random.uniform(1, 2)
    height = random.uniform(2, 6)
    rotation = [random.uniform(0, 360) for _ in range(3)]  # Random rotation
    torus = cmds.polyTorus(r=radius, h=height)[0]  # Create torus (correct flags for radius and height)
    cmds.move(x_pos, y_pos, z_pos, torus)  # Position the torus
    cmds.rotate(rotation[0], rotation[1], rotation[2], torus, relative=True)  # Rotate the torus
    apply_random_color(torus)  # Apply random color to the torus
    return torus

# Apply a random color to a new Lambert shader for each object
def apply_random_color(obj):
    # Create a new Lambert shader
    shader_name = cmds.shadingNode('lambert', asShader=True)  # Create Lambert shader
    shading_group = cmds.setAttr(shader_name + ".color", random.random(), random.random(), random.random(), type="double3")  # Set random color
    shading_group = cmds.setAttr(shader_name + ".color", random.random(), random.random(), random.random(), type="double3")  # Random color value
    # Assign the shader to the object
    cmds.select(obj)
    cmds.hyperShade(assign=shader_name)

# Generate a procedural scene with random objects
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

# Run the function to generate the scene
generate_procedural_scene(10)  # Generate 10 random objects
