import constants as c
import pyrosim.pyrosim as pyrosim
import pybullet as p
import numpy as np

class Motor:
    def __init__(self, jointName, robot_id):
        self.robot_id = robot_id
        self.jointName = jointName
        self.amplitude = c.amplitude
        self.freq = c.freq
        self.phase_offset = c.phase_offset

        self.init_values()

    def init_values(self):
        t = np.arange(c.N_TIMESTEPS)
        self.values = self.amplitude * np.sin(self.freq * t + self.phase_offset)

    def get_value(self, t):
        pyrosim.Set_Motor_For_Joint(
                bodyIndex = self.robot_id,
                jointName = self.jointName,
                controlMode = p.POSITION_CONTROL,
                targetPosition = self.values[t],
                maxForce = 50)
        return self.values[t]

