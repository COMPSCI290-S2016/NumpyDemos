import numpy as np
import matplotlib.pyplot as plt
np.random.seed(404)
X = np.random.randn(2, 300)
#Normalize each column
XNorm = np.sqrt(np.sum(X**2, 0))
#Broadcast 1/XNorm to each row
Y = X/XNorm
plt.plot(Y[0, :], Y[1, :], '.')
plt.show()
