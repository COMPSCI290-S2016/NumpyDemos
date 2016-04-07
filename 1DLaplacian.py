#Programmer: Chris Tralie
#Purpose: To show the laplacian eigenvectors on the discrete graph of a circle
import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse.linalg import lsqr, cg, eigsh
from scipy import sparse

if __name__ == '__main__':
    N = 20
    NBasis = 15
    M = N-1
    #Setup the rows and columns
    I = np.zeros(M*2+2)
    J = np.zeros(M*2+2)
    V = np.ones(M*2+2)
    #Left neighbors
    I[0:M] = np.arange(0, N-1)
    J[0:M] = np.arange(1, N)
    #Right neighbors
    I[M:2*M] = np.arange(1, N)
    J[M:2*M] = np.arange(0, N-1)
    #Connect beginning to end
    I[2*M:] = np.array([0, M])
    J[2*M:] = np.array([M, 0])
    #Make the adjacency matrix
    A = sparse.coo_matrix((V, (I, J)), shape=(N, N)).tocsr()
    #Compute the degree of each vertex by summing the rows of the adjacency matrix
    D = np.array(A.sum(1)).flatten()
    #Make the laplacian matrix: D - A  (need to put the degree along the diagonals)
    L = sparse.dia_matrix((D, 0), A.shape) - A
    #Display the laplacian
    plt.imshow(L.todense(), aspect = 'auto', interpolation = 'none')
    plt.title('Circle Graph Laplacian Matrix')
    plt.savefig("CircleLaplacian.png", bbox_inches = 'tight')
    #Display the eigenvalues one at a time
    (eigvalues, eigvectors) = eigsh(L, NBasis, which='SM')
    for i in range(eigvectors.shape[1]):
        plt.subplot(eigvectors.shape[1], 1, i+1)
        plt.plot(eigvectors[:, i])
        plt.axis('off')
    plt.title('Circle Graph Eigenvectors')
    plt.savefig('CircleEigvecs.svg', bbox_inches = 'tight')
