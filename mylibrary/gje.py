#Library function for Gauss-Jordon elimination method
import numpy as np
import csv
def printmatrix(M): #Function to print a matrix
  n=len(M)
  for i in range (n):
    for j in range (n+1):
      if M[i,j]==0:
        M[i,j]=abs(M[i,j])
      print(float(M[i,j]),end='           ')
    print("\n")
  print("\n") 

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

def input(path): #To read augmented matrix
  i=0
  j=0
  M=[]
  with open(path) as x:
    cr=csv.reader(x)
    next(cr)
    for line in cr:
      row=[]
      for n in line:
        row.append(float(n))
      M.append(row)
  return (np.matrix(M))


def main(p): #main function
  p=str(p)
  A = input(p)
  print("The input matrix is : \n")
  printmatrix(A)
  B=gje(A)
  n=len(B)
  print("The solution of the given linear equations using Gauss-Jordon elimination mathod is : \n")
  for i in range (0,n):
    print("x"+str(i+1)+" = "+str(B[i,n]))
  return


