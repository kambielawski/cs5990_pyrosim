import time

import pybullet as p
import pybullet_data

# Create physics sim client
physics_client = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Set gravity
p.setGravity(0,0,-9.8)

# Set plane
plane_id = p.loadURDF('plane.urdf')

# Bring link in
p.loadSDF('boxes.sdf')

# Run simulation for 1000 steps
n_timesteps = 1000
for i in range(n_timesteps):
    p.stepSimulation()
    time.sleep(0.001)

# Disconnect from physics client
p.disconnect()