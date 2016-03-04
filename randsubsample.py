import numpy as np
import matplotlib.pyplot as plt

#Randomly generate 1000 points
np.random.seed(100) #Seed for repeatable results
NPoints = 1000
X = np.random.randn(2, NPoints)
#Randomly subsample 100 points
NSub = 100
Y = X[:, np.random.permutation(NPoints)[0:NSub]]
plt.plot(X[0, :], X[1, :], '.', color='b')
plt.hold(True) #Don't clear the plot when plotting the next thing
plt.scatter(Y[0, :], Y[1, :], 20, color='r')
plt.show()
