import time

import pybullet as p

# Create physics sim client
physics_client = p.connect(p.GUI)

# Run simulation for 1000 steps
n_timesteps = 1000
for i in range(n_timesteps):
    p.stepSimulation()
    time.sleep(0.1)

# Disconnect from physics client
p.disconnect()