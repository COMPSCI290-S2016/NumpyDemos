import numpy as np
import matplotlib.pyplot as plt

#Randomly generate 1000 points
np.random.seed(100) #Seed for repeatable results
NPoints = 1000
X = np.random.randn(2, NPoints)
#Compute distances of points to origin
R = np.sqrt(np.sum(X**2, 0))
#Select points in X with distance greater than 1
#from origin
Y = X[:, R > 1]
#Plot result
plt.plot(Y[0, :], Y[1, :], '.', color='b')
plt.show()
