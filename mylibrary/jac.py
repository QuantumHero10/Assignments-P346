#Jacobi Iterative method
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

def swap(M): # To find diagonally dominant matrix
  n=len(M)
  for i in range (0,n):
    y=M[i,i]
    x=i
    s=0
    for j in range (0,n):
      k=M[j,i]
      if k**2 > y**2:
        y=k
        x=j
    for k in range (0,n+1):
      s=float(M[x,k])
      M[x,k]=float(M[i,k])
      M[i,k]=float(s)
  print("The diagonally dominant matrix is:-\n")
  printmatrix(M)
  return M

def jac(M,n):
    M=swap(M)
    x1=[0.0]*n
    x2=[0.0]*n
    x1=np.matrix(x1)
    x2=np.matrix(x2)
    ep=0.0
    for i in range (0,500):
        for j in range (0,n):
            sum=0.0
            for l in range(0,n):
                if j != l:
                    sum=sum+(M[j,l]*x1[0,l])
            x2[0,j]= (M[j,n]-sum)/M[j,j]
        a=0
        for k in range (0,n):
            ep = (x2[0,k]-x1[0,k])
            if abs(ep) < 10**-6 :
                a+=1
        if a==n:
            break
        x3=np.matrix(x2)
        x1=x3
    return x2

def input(path):
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

def main(p):
  A = input(p)
  n=len(A)
  print("The input matrix is : \n")
  printmatrix(A)
  B=jac(A,n)
  print("The solution of the given linear equations using Jacobi method is : \n")
  for i in range (0,n):
    print("x"+str(i+1)+" = "+str(B[0,i]))
  return
