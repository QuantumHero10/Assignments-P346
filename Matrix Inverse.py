import numpy as np
import csv
def printmatrix(M):
  n=len(M)
  for i in range (n):
    for j in range (n):
      if M[i,j]==0:
        M[i,j]=abs(M[i,j])
      print(round(float(M[i,j]),3),end='           ')
    print("\n")
  print("\n") 

def swap(M,N,n):
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
  r=np.matrix(N[x])
  N[x]=N[n]
  N[n]=r

def gje(M,N):
  n=len(M)-1
  c=0.0
  c1=0.0
  for i in range (0,n+1):
    if M[i,i]==0:
      swap(M,N,i)
    c1=float(M[i,i])
    M[i]=M[i]/c1
    N[i]=N[i]/c1
    for j in range (i+1,n+1):
      c=float((M[j,i])/(M[i,i]))
      M[j]=M[j]-(c*M[i])
      N[j]=N[j]-(c*N[i])

  for i in range (0,n):
    k=n-i
    for j in range (0,k):
      l=k-j-1
      c=float((M[l,k])/(M[k,k]))
      M[l]=M[l]-(c*M[k])
      N[l]=N[l]-(c*N[k])
  printmatrix(N)

def input():
  i=0
  j=0
  M=[]
  x = open(r"Assignments-P346\matrix2.csv")
  cr=csv.reader(x)
  next(cr)
  for line in cr:
    row=[]
    for n in line:
      row.append(float(n))
    M.append(row)
  return (np.matrix(M))

A=input()
I = np.matrix([[1.0,0.0,0.0,0.0],[0.0,1.0,0.0,0.0],[0.0,0.0,1.0,0.0],[0.0,0.0,0.0,1.0]])
print("The input matrix is : \n")
printmatrix(A)
print("The output matrix is : \n")
gje(A,I)
