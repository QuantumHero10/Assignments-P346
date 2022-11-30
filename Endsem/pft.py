# Polynomial fit
import numpy as np
import matplotlib.pyplot as plt
import csv
def polyfit(M,p):
    n=len(M)
    N=[]
    for i in range (0,p):
        r=[]
        for j in range (0,p):
            sum2=0.0
            for k in range(0,n):
                sum2+= (M[k,0]**(i+j))
            r.append(sum2)
        sum1=0.0
        for l in range (0,n):
            sum1+=((M[l,0]**i)*M[l,1])
        r.append(sum1)
        N.append(r)
    N=np.matrix(N)
    return N

def d(A):
    n=len(A)
    R=[0]*n
    for i in range (0,n-1):
        R[i] = A[i+1]*(i+1)
    return R

def f(A,x):
    y=0.0
    n=len(A)
    for i in range (0,n):
        y+=(A[i]*(x**i))
    return y

def plotf(A):
  n=len(A)
  x=[]
  y=[]
  i=-2
  while i<=2:
    x.append(i)
    y.append(f(A,i))
    i+=0.01
  plt.plot(x,y,color='red',label='fit curve')
  plt.xlabel("x")
  plt.ylabel("y")
  plt.legend()
  plt.show()

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

def main(gji,p,n):
  A = input(p)
  X1=[]
  Y1=[]
  for i in range(0,len(A)):
      X1.append(float(A[i,0]))
      Y1.append(float(A[i,1]))
  plt.scatter(X1,Y1,label="Datapoints")
  B=polyfit(A,n)
  C=gji.main(B)
  for i in range(0,n):
    print("a"+str(i)+" = ",str(C[i,n]))
  print("The least square fit equation of the given data is : \n")
  print("y = ",C[0,n], end=' ')
  F=[C[0,n]]
  for i in range (1,n):
    print((" + "+str(C[i,n])+" x^"+str(i)), end=' ')
    F.append(C[i,n])
  print("\n")
  plotf(F)