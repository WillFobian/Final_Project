import maya.cmds as cmds
import random
import math

def create_random_cube():
    x_pos = random.uniform(-10, 10)
    y_pos = random. uniform(0, 5)
    z_pos = random.uniform(-10, 10)
    size = random.uniform(1, 5)
    rotation = [random.uniform(0, 360) for _ in range(3)]
    
