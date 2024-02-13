import numpy as np
cimport numpy as cnp
cimport cython

@cython.boundscheck(False)
@cython.wraparound(False)
def gauss_seidel(double[:,:] f):
    cdef unsigned int i, j
    cdef double[:,:] newf
    cdef double scalar
    
    newf = f.copy()
    scalar = 0.25
    
    for i in range(1,newf.shape[0]-1):
        for j in range(1,newf.shape[1]-1):
            newf[i,j] = scalar * (newf[i,j+1] + newf[i,j-1] +
                                   newf[i+1,j] + newf[i-1,j])
    
    return newf