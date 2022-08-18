import numpy as np
import csv
def printmatrix(M):
  n=len(M)
  for i in range (n):
    for j in range (n+1):
      if M[i,j]==0:
        M[i,j]=abs(M[i,j])
      print(float(M[i,j]),end='           ')
    print("\n")
  print("\n") 

def swap(M,n):
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

def gje(M):
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

def input():
  i=0
  j=0
  M=[]
  x = open(r"C:\Users\manor\Desktop\matrix1.csv")
  cr=csv.reader(x)
  next(cr)
  for line in cr:
    row=[]
    for n in line:
      row.append(float(n))
    M.append(row)
  return (np.matrix(M))


A = input()
print("The input matrix is : \n")
printmatrix(A)
B=gje(A)
print("The output matrix is : \n")
printmatrix(B)