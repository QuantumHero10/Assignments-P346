#Library function for Gauss-Jordon Inverter
import numpy as np
import csv
def swap(M,n): #To swap pivot elements of value zero
  x=n
  y=M[n,n]
  m=len(M)
  for i in range (m):
    for j in range (n,(n+1)):
      k=M[i,j]
      if k**2 >= y**2:
        y=k
        x=i
  if x<n:
    return
  s=np.matrix(M[x])
  M[x]=M[n]
  M[n]=s

def gje(M): #Main algorithm function for LU decomposition
  n=len(M)-1
  c=0.0
  for i in range (0,n+1):
    if M[i,i]==0:
      swap(M,i)
    M[i]=M[i]/M[i,i]
    for j in range (i+1,n+1):
      c=(M[j,i])/(M[i,i])
      M[j]=M[j]-(c*M[i])

  for i in range (0,n):
    k=n-i
    for j in range (0,k):
      l=k-j-1
      c=(M[l,k])/(M[k,k])
      M[l]=M[l]-(c*M[k])
  return (M)

def main(A): #main function
  B=gje(A)
  n=len(B)
  return B


