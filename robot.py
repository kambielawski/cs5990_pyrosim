import pyrosim.pyrosim as pyrosim
import pybullet as p

from sensor import Sensor
from motor import Motor

import constants as c

class Robot:
    def __init__(self):
        self.id =  p.loadURDF('body.urdf')
        pyrosim.Prepare_To_Simulate(self.id)

        self.prepare_to_sense()
        self.prepare_to_act()

    def prepare_to_sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = Sensor(linkName)

    def prepare_to_act(self):
        self.motors = {}
        for i, jointName in enumerate(pyrosim.jointNamesToIndices):
            if i == 0:
                self.motors[jointName] = Motor(jointName, self.id)
            else:
                self.motors[jointName] = Motor(jointName, self.id)
                self.motors[jointName].freq /= 2
                self.motors[jointName].init_values()

    def sense(self, t):
        for _, sensor in self.sensors.items():
            sensor.get_value(t)

    def act(self, t):
        for _, motor in self.motors.items():
            motor.get_value(t)

        