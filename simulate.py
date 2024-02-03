import time

import numpy as np
import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data

# Create physics sim client
physics_client = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Set gravity
p.setGravity(0,0,-9.8)

# Set plane
plane_id = p.loadURDF('plane.urdf')
robot_id = p.loadURDF('body.urdf')

# Bring link in
p.loadSDF('world.sdf')

pyrosim.Prepare_To_Simulate(robot_id)

# Run simulation for 1000 steps
n_timesteps = 1000
backleg_sensor_values = np.zeros(n_timesteps)
frontleg_sensor_values = np.zeros(n_timesteps)
for i in range(n_timesteps):
    p.stepSimulation()
    back_leg_sensor = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    front_leg_sensor = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    backleg_sensor_values[i] = back_leg_sensor
    frontleg_sensor_values[i] = front_leg_sensor
    time.sleep(0.001)

np.save('./data/sensor_vals.npy', np.array([backleg_sensor_values, frontleg_sensor_values]))

# Disconnect from physics client
p.disconnect()