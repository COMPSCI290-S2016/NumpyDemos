import numpy as np

np.random.seed(15) #For repeatable results
X = np.round(5*np.random.randn(4, 3)) #Make a random 4x3 matrix
print X.shape #Tuple that stores dimensions of array
print X, "\n\n"
#Now do some "array slicing"
print X[:, 0], "\n\n" #Access first column
print X[1, :], "\n\n" #Access, second row
print X[3, 2], "\n\n" #Access fourth row, third column
#Unroll into a 1D array row by row
Y = X.flatten()
print Y.shape
print Y, "\n\n"
Y = Y[:, None]
print Y.shape
print Y
