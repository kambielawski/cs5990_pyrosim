import time
import numpy as np

import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim

from world import World
from robot import Robot

import constants as c

class Simulation:
    def __init__(self):
        # Create physics sim client
        self.physics_client = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        # Set gravity
        p.setGravity(0,0,-9.8)

        self.world = World()
        self.robot = Robot()

    def __del__(self):
        p.disconnect()

    def run(self):
        # Run simulation for 1000 steps
        for t in range(c.N_TIMESTEPS):
            p.stepSimulation()
            self.robot.sense(t)
            self.robot.act(t)
            time.sleep(0.0003)
