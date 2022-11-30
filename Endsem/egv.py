import math
import numpy as np

def main(A,x0,xk,ep):
    k=10000
    y=np.matrix(x0)
    ct=0
    for i in range (0,k):
        sum=0
        for j in range (0,3):
            sum+=y[0,j]*x0[0,j]
        xky=float(sum)
        for l in range (0,3):
            sum=0
            for j in range (0,3):
                sum+=A[l,j]*x0[0,j]
            xk[0,l]=float(sum)
        x0=np.matrix(xk)
        sum=0
        for j in range (0,3):
            sum+=y[0,j]*xk[0,j]
        xk1y=float(sum)
        ct+=1
        if i==0:
            l0=float(sum)
        if i>0 :
            if xky==0:
                break
            lk=xk1y/xky
            if abs(lk-l0)<ep:
                break
            l0=float(lk)
    return lk,xk,ct





