import pickle

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from mpl_toolkits import mplot3d


import cv2
# import mediapipe as mp
import urllib.request
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import animation
import PyQt5
from PIL import Image
# from IPython.display import Video
import nb_helpers




fn = 'tracking_points_test_ex.pickle'

with open(fn, 'rb') as ftr:
  vertexes = pickle.load(ftr)

fig = plt.figure()
fig.set_size_inches(5, 5, True)
ag = fig.add_subplot(projection='3d')

nb_helpers.plot_data(vertexes[0], ax)
nb_helpers.scale_axes(ax)
plt.show()
exit()







fig = plt.figure()
ax = plt.axes(projection='3d')
data = vertexes[0]

z = data[:, 0]
x = data[:, 1:2].flatten()
y = data[:, 2:].flatten()



# z = np.linspace(0, 1, 100)
# print(z)
# exit()

print(len(data))
exit()

ax.plot3D(data, 'maroon')
ax.set_title('fefe')
ax.set_xlabel('X')
ax.set_ylabel('Y')
plt.show()



exit()


for i in vertexes:
  data = i

  zdata = data[:, 0]
  ydata = data[:, 1:2]
  xdata = data[:, 2:]
  print(zdata)
  print('\n\n')
  print(xdata)
  print('\n\n')
  print(ydata)
  # exit()

  fig = plt.figure()
  ax = plt.axes(projection='3d')
  ax.scatter3D(xdata, ydata, zdata, c=data, cmap='Greens');
  plt.pause(0.05)
  break

plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# 
# for ver in vertexes[:5]:
#   for (x, y, z) in ver:
#     plt.scatter(x, y)
#     plt.title("Real Time plot")
#     plt.xlabel("x")
#     plt.ylabel("sinx")
#     plt.pause(0.05)
# 
# plt.show()

# loc = 1
# def update_graph():
#   global loc
#   data = vertexes[loc]
# 
#   xdata = data[:, 0]
#   ydata = data[:, 1:2]
#   zdata = data[:, 2:]
# 
# 
#   graph._offsets3d = (xdata, ydata, zdata)
#   title.set_text('3D Test, time={}'.format(loc))
#   loc += 1
# 
# 
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# title = ax.set_title('3D Test')
# 
# data = vertexes[0]
# xdata = data[:, 0]
# ydata = data[:, 1:2]
# zdata = data[:, 2:]
# 
# graph = ax.scatter(xdata, ydata, zdata)
# 
# plt.show()
