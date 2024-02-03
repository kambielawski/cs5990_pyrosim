import numpy as np
import matplotlib.pyplot as plt

sensor_data = np.load('./data/sensor_vals.npy')
backleg_sensor_data, frontleg_sensor_data = sensor_data

plt.plot(backleg_sensor_data, label='back leg')
plt.plot(frontleg_sensor_data, label='front leg')
plt.legend()
plt.xlabel('timesteps')
plt.show()