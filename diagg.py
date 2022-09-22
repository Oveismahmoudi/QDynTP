import numpy.linalg as la
import numpy as np
import TPmod

# 1. write the basis for N particles in L site
basis = TPmod.distribute(p=3, N=8)
for i in basis:
    print(i)
# 2. Express H on this basis (write H matrix)

# 3. Diagonalize H, find the eig.vec. and eig.val. find the ground state
# arr = np.array([[1, 2], [5, 6]])

# val, vec = la.eig(arr)

# gs_energy = np.min(val)
# gs_vector = vec[(np.where(gs_energy)[0][0])]

# print(gs_energy)
# print(gs_vector)

