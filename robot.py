from pyrosim import pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import pybullet as p

from sensor import Sensor
from motor import Motor

import constants as c

class Robot:
    def __init__(self):
        self.id =  p.loadURDF('body.urdf')
        self.nn = NEURAL_NETWORK("brain.nndf")
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
        for neuron_name in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuron_name):
                desired_angle = self.nn.Get_Value_Of(neuron_name)
                joint_name = self.nn.Get_Motor_Neurons_Joint(neuron_name)
                self.motors[joint_name].get_value(desired_angle)

    def think(self, t):
        self.nn.Update()

        