
"""
Function:  
Euclidean norm of a vector.

INPUTS:
    x: vector of observations
    
OUTPUTS:
    vn: the euclidean norm
    
"""

import numpy as np

def vec_norm(x):
    
    vn = np.sqrt(np.sum(np.square(x)))
    return vn

