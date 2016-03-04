import numpy as np
import matplotlib.pyplot as plt
#Make a sinusoid point cloud
t = np.linspace(0, 2*np.pi, 100)
X = np.zeros((2, len(t)))
X[0, :] = t
X[1, :] = np.sin(t)
#Mean-center
X = X-np.mean(X, 1)[:, None]
#Do PCA
D = X.dot(X.T) #X*X Transpose
[eigs, V] = np.linalg.eig(D) #Eigenvectors in columns
eigs = np.sqrt(eigs/X.shape[1]) #Make average dot product length
#Scale columns by eigenvectors
V = V*eigs[None, :]
plt.plot(X[0, :], X[1, :], '.'); plt.hold(True)
#First eigvec is in first column, second in second
plt.arrow(0, 0, V[0, 0], V[1, 0], ec = 'r')
plt.arrow(0, 0, V[0, 1], V[1, 1], ec = 'g')
plt.axes().set_aspect('equal', 'datalim'); plt.show()
