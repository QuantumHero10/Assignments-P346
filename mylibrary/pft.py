# Polynomial fit
import numpy as np
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