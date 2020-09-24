# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 13:20:03 2020

@author: areyes
"""

import csv
import numpy as np
import matplotlib.pyplot as plt

data_path = 'C:/Users/areyes/Dropbox/ineel/11090/pronostico/datasets/arenal/datosValidadosArenal.csv'
with open(data_path, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    headers = next(reader)
    data = np.array(list(reader)).astype(float)
    
print(headers)
print(data.shape)
print(data[1:4])

# Plot the data
#plt.plot(data[:, 1], data[:, 0])
plt.plot(data[:, 0],'g-')
#plt.axis('equal')
plt.xlabel('Indice de la tabla')
plt.ylabel(headers[0])
plt.show()

plt.plot(data[:, 1])
plt.xlabel('Indice de la tabla')
plt.ylabel(headers[1])
plt.show()

from windrose import WindroseAxes
import matplotlib.pyplot as plt

# theta = [0, 60, 120, 180, 240, 300]
# speed = [10, 0, 10, 40, 50, 40]

# ax = WindroseAxes.from_ax()
# ax.bar(theta, speed)
# ax.set_legend()
# plt.show()

# from windrose import WindroseAxes
# from matplotlib import pyplot as plt
# import matplotlib.cm as cm
# import numpy as np

# Create wind speed and direction variables

ws = np.random.random(500) * 6
wd = np.random.random(500) * 360

ax = WindroseAxes.from_ax()
ax.bar(data[:, 1], data[:, 0], normed=True, opening=0.8, edgecolor='white')

# ax.bar(wd, ws, normed=True, opening=0.8, edgecolor='white')
# ax.bar()
#plt.show()

ax.set_legend()
