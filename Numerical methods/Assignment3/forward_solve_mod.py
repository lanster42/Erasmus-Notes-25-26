import numpy as np

def forward_solve_mod(A,b):
    """
    Routine to compute solution to linear system with lower triangular matrix

    INPUTS:
        A = numpy array with matrix of linear system (should be lower triangular)
        b = numpy array with right-hand side

    OUTPUTS:
        v = solution to the linear system
    """
    
    # Initializations
    m = len(A)
    v = np.zeros(m)
    
    # Checks on the inputs
    if len(b) != m:
        raise Exception("Size mismatch between matrix and right-hand side")
    

    # Proceed from first to last row with forward substitution
    for i in range(0,m):
        v[i] = b[i]-np.dot(A[[i],:i],v[:i])
        
    return v