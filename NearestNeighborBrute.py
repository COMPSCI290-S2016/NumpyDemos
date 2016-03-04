import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 2*np.pi, 100)
X = np.zeros((2, len(t)))
X[0, :] = t
X[1, :] = np.cos(t)
Y = np.zeros((2, len(t)))
Y[0, :] = t
Y[1, :] = np.sin(t**1.2)
##FILL THIS IN TO COMPUTE DISTANCE MATRIX D
idx = np.argmin(D, 1) #Find index of closest point in Y to point in X
plt.plot(X[0, :], X[1, :], '.')
plt.hold(True)
plt.plot(Y[0, :], Y[1, :], '.', color = 'red')
for i in range(len(idx)):
    plt.plot([X[0, i], Y[0, idx[i]]], [X[1, i], Y[1, idx[i]]], 'b')
plt.axes().set_aspect('equal', 'datalim'); plt.show()
