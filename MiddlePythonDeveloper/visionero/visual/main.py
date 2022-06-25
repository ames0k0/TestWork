#!/usr/bin/env python

# from PyQt5.Qt import QtCore, QtGui
import numpy as np
import itertools

import pickle


from PyQt5.QtWidgets import QApplication, QLabel

# app = QApplication()

# w = gl.GLViewWidget()
# w.opts['distance'] = 20
# w.show()
# w.setWindowTitle('A cube')

fn = 'tracking_points_test_ex.pickle'

with open(fn, 'rb') as ftr:
  vertexes = pickle.load(ftr)

faces = []

for i in range(2):
    temp = np.where(vertexes==i)
    for j in range(3):
        temp2 = temp[0][np.where(temp[1]==j)]
        for k in range(2):
            faces.append([temp2[0],temp2[1+k],temp2[3]])

faces = np.array(faces)

colors = np.array([[1,0,0,1] for i in range(12)])


cube = gl.GLMeshItem(vertexes=vertexes, faces=faces, faceColors=colors,
                     drawEdges=True, edgeColor=(0, 0, 0, 1))

w.addItem(cube)

if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()

