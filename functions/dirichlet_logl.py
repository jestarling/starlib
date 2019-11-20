"""
Dirichlet log-likelihood function.

INPUTS:
  data: a vector of data values (x).
  alpha: a vector of alpha values (k-1 long).

OUTPUT:

#data must be n*k matrix.  Each of the k cols contains n observations.
#alpha must be length k vector, summing to 1.  All values must be in (0,1).

"""
import sys
import numpy as np
import numpy.random as npr
import scipy.special as sps


def dirll(data,alpha):
  data = np.array(data) #Convert to numpy array for vectorized operations.
  alpha = np.array(alpha) 
  n = np.shape(data)[0] #Number of observations.  Each obs is length j.
  logxi = np.mean(np.log(data),axis=0) #logxi = (1/N) * sum(log(x_ij))
  logl = n * (sps.gammaln(np.sum(alpha)) - np.sum(sps.gammaln(alpha)) + np.sum(np.dot(alpha-1,logxi)))
  return logl

"""
Example code:
k = 4
n = 5
x = np.abs(npr.normal(loc=0,scale=1,size=n*k).reshape((n,k))) #Dirichlet values must be positive.
alpha = [.2,.3,.4,.1]

"""