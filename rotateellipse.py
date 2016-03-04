import numpy as np
import matplotlib.pyplot as plt
np.random.seed(404)
X = np.random.randn(2, 300)
#Scale X by "broadcasting"
X = np.array([[5], [1]])*X
#Setup a rotation matrix
[C, S] = [np.cos(np.pi/4), np.sin(np.pi/4)]
R = np.array([[C, -S], [S, C]])
#Multiply points on the left by the rotation matrix
Y = R.dot(X)
#Set axes equal scale
plt.axes().set_aspect('equal', 'datalim')
plt.plot(Y[0, :], Y[1, :], '.')
plt.show()
