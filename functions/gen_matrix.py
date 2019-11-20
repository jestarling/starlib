"""
Generates various types of square matrices:

INPUTS:
	types:  zero, identity, diagonal,uTriangular,lTriangular,
	        uuTriangular,luTriangular,usTriangular,lsTriangular
  n: dimension of square matrices.  Default n = 5.

"""

import sys
import numpy as np
import numpy.random as npr
import numpy.linearalg as npl

def gen_matrix(type='identity',n=5):
  
  mat = np.zeros((n,n))
  
  #Print shape (dimensions) and size (total # entries) of matrix.
  print(np.shape(mat))
  print(np.size(mat))
  
  #Zero matrix.
  if type == 'zero':
    mat = np.zeros((n,n))
  
  #Identity matrix.
  if type == 'identity':
    mat = np.identity(n)
    
    #Identical function:
    #mat = np.eye(n)  

  #Diagonal matrix (random normal diagonal).
  if type == 'diagonal':
    d = npr.normal(loc=0,scale=1,size=n)
    mat = np.diag(d)

	#Upper triangular.
  if type == 'ut':
    mat = npr.normal(loc=0,scale=1,size=n*n).reshape((n,n))
    mat = np.triu(mat)
   
	#Upper unit triangular.  (Upper, with diagonal = 1)
  if type == 'uut':
    mat = npr.normal(loc=0,scale=1,size=n*n).reshape((n,n))
    mat = np.triu(mat)
    np.fill_diagonal(mat,1)
    
	#Upper strictly triangular.  (Upper, with diagonal = 0)
  if type == 'uut':
    mat = npr.normal(loc=0,scale=1,size=n*n).reshape((n,n))
    mat = np.triu(mat,k=1)    
    
	#Lower triangular.
  if type == 'lt':
    mat = npr.normal(loc=0,scale=1,size=n*n).reshape((n,n))
    mat = np.tril(mat)
   
	#Upper unit triangular.  (Lower, with diagonal = 1)
  if type == 'lut':
    mat = npr.normal(loc=0,scale=1,size=n*n).reshape((n,n))
    mat = np.tril(mat)
    np.fill_diagonal(mat,1)
    
	#Upper strictly triangular.  (Lower, with diagonal = 0)
  if type == 'ust':
    mat = npr.normal(loc=0,scale=1,size=n*n).reshape((n,n))
    mat = np.tril(mat,k=1)
	
	#Symmetric matrix.
  if type == 'sym':
      mat = npr.normal(loc=0,scale=1,size=n*n).reshape((n,n))
      mat = mat + mat.T - np.diag(mat.diagonal())
  
  return mat


	
