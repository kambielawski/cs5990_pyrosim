import time
import numpy as np

import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim

from world import World
from robot import Robot

import constants as c

class Simulation:
    def __init__(self, sim_type='GUI'):
        # Create physics sim client
        self.sim_type = sim_type
        if sim_type == 'GUI':
            self.physics_client = p.connect(p.GUI)
        else:
            self.physics_client = p.connect(p.DIRECT)
        
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
            self.robot.think(t)
            self.robot.act(t)
            if self.sim_type == 'GUI':
                time.sleep(0.0001)

        fitness = self.robot.get_fitness()
        print(f'({fitness})')
