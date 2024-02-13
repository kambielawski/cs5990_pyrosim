import pyrosim.pyrosim as pyrosim
import numpy as np

import constants as c

class Sensor:
    def __init__(self, name):
        self.name = name
        self.values = np.zeros(c.N_TIMESTEPS)

    def get_value(self, t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.name)
        return self.values