#Library function for Cholesky decomposition method
import numpy as np
import csv
def printmatrix(M): #Function to print a matrix
  n=np.size(M,0)
  m=np.size(M,1)
  for i in range (n):
    for j in range (m):
      if M[i,j]==0:
        M[i,j]=abs(M[i,j])
      print(round(float(M[i,j]),2),end='          ')
    print("\n")
  print("\n")

def cholesky(M): #Main algorithm function for cholesky
    print("The input matrix is : \n")
    printmatrix(M)
    n=len(M)
    for i in range (0,n): #To check symmetric matrix or not
        for j in range (0,n):
            if M[i,j]!=M[j,i]:
                print('The given matrix is not symmetric so it cannot be solved by cholesky decomposition method.\n')
                return 
    L=np.matrix(M)
    T=[]
    X=[]
    Y=[]
    for i in range (0,n): 
        X.append(0.0)
    X=np.matrix(X)
    Y=np.matrix(X)
    for i in range (0,n):
        for j in range (0,n):
            if j>i:
                L[i,j]=0.0
    for i in range (0,n): #Finding lower triangular matrix
        s=0.0
        for k in range (0,i):
            s=s+(L[i,k]*L[i,k])
        L[i,i]=np.sqrt(M[i,i]-s)
        for j in range (i+1,n):
            s1=0.0
            for x in range (0,i):
                s1=s1+(L[j,x]*L[i,x])
            L[j,i]=(M[j,i]-s1)/(L[i,i])
    for i in range (0,n): #Finding upper triangular matrix
        row=[]
        for j in range (0,n):
            row.append(L[j,i])
        T.append(row)
    T=np.matrix(T)
    for i in range (0,n): # Backward substitution
        s2=0.0
        for j in range (0,i):
            s2=s2+(L[i,j]*Y[0,j])
        Y[0,i]=((M[i,n]-s2)/L[i,i])
    for i in range (n,0,-1): # Forward substitution
        s3=0.0
        k=i-1
        for j in range (k+1,n):
            s3= s3+ (T[k,j]*X[0,j])
        X[0,k]=((Y[0,k]-s3)/T[k,k])
    print("The solution of the given linear equations using Cholesky decomposition method is : \n")
    for i in range (0,n):
        print("x"+str(i+1)+" = "+str(X[0,i]))
    return X

def input(path): #To read input matrix
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
    A=np.matrix(input(p))
    cholesky(A)
    return


