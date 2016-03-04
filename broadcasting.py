import numpy as np
import matplotlib.pyplot as plt
X = np.arange(4)
Y = np.arange(6)
Z = X[:, None] + Y[None, :]
print Z
