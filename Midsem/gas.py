
import numpy as np
import csv
def printmatrix(M):
  n=np.size(M,0)
  m=np.size(M,1)
  for i in range (n):
    for j in range (m):
      if M[i,j]==0:
        M[i,j]=abs(M[i,j])
      print(round(float(M[i,j]),2),end='          ')
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

def gauss(M): #Main algorithm function for Gauss-Seidel 
    M=swap(M)
    n=len(M)
    X1=[]
    X2=[]
    for i in range (0,n):
        X1.append(0.0)
    X1=np.matrix(X1)
    X2=np.matrix(X1)
    ep=0.0
    c=0
    for i in range (0,500):
        for j in range (0,n):
            sum2=0.0
            sum1=0.0
            for m in range(0,j):
                sum1=sum1+(M[j,m]*X2[0,m])
            for l in range(j+1,n):
                sum2=sum2+(M[j,l]*X1[0,l])
            X2[0,j]= (M[j,n]-sum1-sum2)/M[j,j]
        a=0
        if c > 0 :
            for k in range (0,n):
                ep = X2[0,k]-X1[0,k]
                if abs(ep) < 10**-6 :
                    a+=1
        if a==n:
            break
        x3=np.matrix(X2)
        X1=x3
    print("The solution of the given linear equations using Gauss-Seidel method is : \n")
    for i in range (0,n):
        print("x"+str(i+1)+" = "+str(X2[0,i]))

def input(path): #To read augmented matrix
  M=[]
  with open(path) as x:
    cr=csv.reader(x)
    for line in cr:
      row=[]
      for n in line:
        row.append(float(n))
      M.append(row)
  return (np.matrix(M))

def main(p): #main function
    p=str(p)
    A=np.matrix(input(p))
    print("The input matrix is : \n")
    printmatrix(A)
    gauss(A)
    return
