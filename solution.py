import os
import re
import subprocess
import numpy as np
from pyrosim import pyrosim

class Solution:
    def __init__(self):
        self.weights = np.random.rand(3,2) * 2 - 1
        self.num_sensors = 3
        self.num_motors = 2

    def create_world(self):
        pyrosim.Start_SDF('world.sdf')

        length, width, height = 1, 1, 1
        x,y,z = -2, -2, 0.5
        pyrosim.Send_Cube(name=f"Box", pos=[x,y,z] , size=[length,width,height])

        pyrosim.End()

    def generate_body(self):
        pyrosim.Start_URDF("body.urdf")

        length, width, height = 1, 1, 1
        x,y,z = 0, 0, 1.5
        pyrosim.Send_Cube(name=f"Torso", pos=[x,y,z] , size=[length,width,height])
        pyrosim.Send_Cube(name=f"BackLeg", pos=[0.5, 0, -0.5] , size=[length,width,height])
        pyrosim.Send_Cube(name=f"FrontLeg", pos=[-0.5, 0, -0.5] , size=[length,width,height])

        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [x+0.5,y,z-0.5])
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [x-0.5,y,z-0.5])
        
        pyrosim.End()

    def generate_brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")

        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")

        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")

        for i in range(self.num_sensors):
            for j in range(self.num_motors):
                pyrosim.Send_Synapse( sourceNeuronName = i , targetNeuronName = self.num_motors+j , weight = self.weights[i, j])

        pyrosim.End()

    def evaluate(self, gen):
        self.create_world()
        self.generate_body()
        self.generate_brain()
        sim_type = 'GUI' if gen == 0 else 'DIRECT'
        subprocess_run_string = ['python3', 'simulate.py', sim_type]

        sp = subprocess.Popen(subprocess_run_string, stdout=subprocess.PIPE)

        # Parse standard output from subprocess
        stdout, stderr = sp.communicate()
        out_str = stdout.decode()
        fitness_str = re.search('\(.+\)', out_str)[0].strip('()').split(' ')

        self.fitness = float(fitness_str[0])

    def mutate(self):
        # Mutate a random synapse
        rand_i = np.random.randint(0, self.num_sensors)
        rand_j = np.random.randint(0, self.num_motors)
        self.weights[rand_i, rand_j] = np.random.rand() * 2 - 1