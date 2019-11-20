
"""
Function:  
Soft thresholding operator, ie proximal operator of the L1 scaled norm.

INPUTS:
    x: vector of observations
    lambda: penalization parameter (threshold)
    
OUTPUTS:
    theta: the soft thresholding estimator
    
"""

import sys
import numpy as np

def soft_thresh(y, lam):
    try:
        n = y.shape[0]
    except:
        n=1
    return np.sign(y) * np.maximum((np.abs(y) - lam), np.zeros(n))    