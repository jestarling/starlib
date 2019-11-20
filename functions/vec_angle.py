"""
vecAngle(x,y)

This function calculates the angle in degrees between two vectors.

INPUTS:
  x A vector.  Defaults to NULL.
  y A vector.  Defaults to NULL.

OUTPUT:
  A scalar, the angle between the two vectors.

Example:
x <- c(1,3,5,7,9)
y <- c(2,4,6,8,10)
vecAngle(x,y)

author Jennifer Starling
"""

import sys
import numpy as np
import numpy.random as npr
import numpy.linearalg as npl

def vec_angle(x,y):
  a = np.sum(np.dot(x,y))
  b = np.sqrt(np.sum(np.power(x,2))) * np.sqrt(np.sum(np.power(y,2)))
  angle = np.arccos(a/b)
  return angle

