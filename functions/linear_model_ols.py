"""
Orinary Least Squares linear regression.

INPUTS:
X is design matrix (n*p) with no intercept vector of 1's.
y is vector of responses (length n)

OUTPUT:
beta_hat: vector of coefficient estimates. b[0] = intercept.
RSS: residual sum of squares.
sigma_hat: sqrt of variance estimate.
beta_hat_se: standard error vector for beta_hat coefficients.
ci: vector of confidence intervals for beta_hat coefficients.
n: number of observations
p: number of predictors

"""

import sys
import numpy as np
from scipy import linalg as la
import numpy.linalg as npl
import pandas as pd

def lm(X,y):
  #Set X and y as numpy arrays.
  #X = np.array(X)
  #y = np.array(y)
  
  n, p = X.shape #Set dimensions
  
  #Error checking.
  if len(y) != n:
    print('Number of obs must equal length of response vector y.')
    return None
  
  #Add intercept column of 1's at front of X matrix.
  X = pd.concat([np.ones(n), X], axis=1)
  concatenate((a,b), axis=1)

linear.regression <- function(X,y){

	n = length(y)
	X = as.matrix(cbind(rep(1,n),X))
	beta_hat <- solve(t(X) %*% X) %*% t(X) %*% y

	#Calculate y_hat and RSS.
	y_hat <- X %*% beta_hat
	RSS <- t(y - X %*% beta_hat) %*% (y - X %*% beta_hat)

	n <- nrow(X)	#Number of obs.
	p <- 4			#Number of predictors.
	sigma2_hat <- RSS / (n-p-1)		#Estimate of sigma^2.
	sigma_hat <- sqrt(sigma2_hat)	#Estimate of sigma.

	#Estimated standard error and CI for each coefficient:
	beta_hat_se <- sqrt( sigma2_hat * diag(solve(t(X) %*% X)) ) #Standard errors.

	#95% CI for beta_hat's.
	lb <- beta_hat -  1.96 * beta_hat_se
	ub <- beta_hat + 1.96 * beta_hat_se
	sig <- ifelse( (lb < 0) & (ub > 0), 0,1)

	#Display CI, including star for betas not equal to zero based on the CI.
	ci = data.frame(lower.bound=lb,upper.bound=ub,sig.coefs=sig)
	
	return(list(beta_hat = beta_hat, 
				RSS = RSS, 
				sigma_hat = sigma_hat, 
				beta_hat_se = beta_hat_se, 
				ci = ci,
				n=n,
				p = ncol(X)-1))
} #End myLinearReg function.
