import numpy as np

def backward_solve(A,b):
    """
    Routine to compute solution to linear system with upper triangular matrix

    INPUTS:
        A = numpy array with matrix of linear system (should be upper triangular)
        b = numpy array with right-hand side

    OUTPUTS:
        v = solution to the linear system
    """
    
    # Initializations
    m = len(A)
    v = np.zeros(m)
    
    # Checks on the inputs - were not required but good to have
    if len(b) != m:
        raise Exception("Size mismatch between matrix and right-hand side")

    # Proceed from last to first row with forward substitution
    for i in range(m-1,-1,-1):
        v[i] = (b[i]-np.dot(A[[i],i+1:],v[i+1:]))/A[[i],[i]]
        
    return v