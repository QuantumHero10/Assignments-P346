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
  return N

def input(path):
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

def identity(n):
  s=0.0
  P=[]
  for i in range (0,n):
    row=[]
    for j in range (0,n):
      if i==j:
        s=float(1)
      else:
        s=float(0)
      row.append(s)
    P.append(row)
  return P

def multi(M,N):
    m1=np.size(M,0)
    m2=np.size(M,1)
    n1=np.size(N,0)
    n2=np.size(N,1)
    P=[]
    #if statement to check if 2 matrices can be multiplied or not
    if m2 != n1:
        print('The two input matrices cannot be multiplied.\n')
        return
    for i in range (0,m1):
        row=[]
        for j in range (0,n2):
            c=0.0
            s=0.0
            for k in range (0,m2):
                c=M[i,k]*N[k,j]
                s=s+c
            row.append(s)
        P.append(row)
    Q=np.matrix(P)
    print('The input matrices are:\n')
    printmatrix(M)
    printmatrix(N)
    print('The product of the above two matrices is:\n' )
    printmatrix(Q)


def main():
  p='C:\\Users\\manor\\Desktop\\P346 codes\\matrix2.csv'
  A=input(p)
  C=np.matrix(A)
  m=len(A)
  I = np.matrix(identity(m))
  print("The input matrix is : \n")
  printmatrix(A)
  print("The inverse matrix is : \n")
  B=gje(A,I)
  multi(C,B)
