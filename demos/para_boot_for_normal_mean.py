""""

SDS 383C - Stats Mod 1 - Fall 2016 - PROBLEM 2-c-ii:  

Parametric bootstrap and confidence interval for exp of normal mean, theta.          

I.e. bootstrap estimate and CI for exp(theta).
"""

import sys
import numpy as np
import numpy.random as npr

B = 1000  #Number of bootstrap iterations.
mu_boot = np.zeros(B)
theta_boot = np.zeros(B) #Initialize vector to hold bootstrap theta estimates.

#Set up parameters for true normal distribution.
mu = 5
sigma = 1
n = 100

#MLE estimate of exp(theta)
th_hat = np.exp(np.mean(npr.normal(loc=mu, scale=sigma, size=n)))

for i in range(0,B):
  #Draw a sample from the distribution, since parametric.
  y_boot = npr.normal(loc=mu, scale=sigma, size=n)
  
  #Calculate statistics from the bootstrap draw.
  mu_boot[i] = np.mean(y_boot)
  theta_boot[i] = np.exp(mu_boot[i])

#Display bootstrapped variance.
var_theta_boot = np.var(theta_boot)
print(var_theta_boot)

#Display 95% CI: (Using percentile interval)
lb = np.percentile(theta_boot,.025)
ub = np.percentile(theta_boot,.975)
ci = [lb,ub]
print(ci)

#Display 95% CI: (Using normal interval, for fun.  This interval is wider.)
lb = th_hat - 1.96 * np.sqrt(var_theta_boot)
ub = th_hat + 1.96 * np.sqrt(var_theta_boot)
ci_norm = [lb,ub]
print(ci_norm)

