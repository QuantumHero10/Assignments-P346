import math
import numpy as np
import csv
def fit(M):
    n=len(M)
    sum=0.0
    sumx=0.0
    sumy=0.0
    sumxx=0.0
    sumxy=0.0
    sumyy=0.0
    for i in range (0,n):
      sum+=(1/(M[i,2]**2))
      sumx+=(M[i,0]/(M[i,2]**2))
      sumy+=(M[i,1]/(M[i,2]**2))
      sumxx+=((M[i,0]**2)/(M[i,2]**2))
      sumyy+=((M[i,1]**2)/(M[i,2]**2))
      sumxy+=((M[i,0]*M[i,1])/(M[i,2]**2))
    d = (sum*sumxx) - (sumx**2)
    a1 = ((sumxx*sumy) - (sumx*sumxy))/d
    a2 = ((sumxy*sum) - (sumx*sumy))/d
    s1 = math.sqrt(sumxx/d)
    s2 = math.sqrt(sum/d)
    print("r = ",(sumxy/(sumxx*sumyy)))
    r=[]
    N=[]
    r.append(a1)
    r.append(a2)
    N.append(r)
    r=[]
    r.append(s1)
    r.append(s2)
    N.append(r)
    N=np.matrix(N)
    return N

def input(path):
  M=[]
  with open(path) as x:
    cr=csv.reader(x)
    for line in cr:
      row=[]
      for n in line:
        row.append(float(n))
      M.append(row)
  return (np.matrix(M))
  
def main(p):
  A = input(p)
  B=fit(A)
  print("\nThe least square fit equation of the given data is : \n")
  a1=B[0,0]
  a2=B[0,1]
  s1=B[1,0]
  s2=B[1,1]
  print("y = ",a1," + ",a2,"x \n")
  print("Error in intercept = ",s1)
  print("Error in slope = ",s2)
  print("\n")
  
