import math
import numpy as np

def eval(A,x0,xk):
    k=1000
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
        #print(xky)
        ct+=1
        if i==0:
            lambda0=float(sum)
        if i>0 :
            if xky==0:
                break
            lambdak=xk1y/xky
            if abs(lambdak-lambda0)<10**-3:
                break
            lambda0=float(lambdak)
    print("No. of iterations :-",ct)
    return lambdak,xk


A=np.matrix([[2,1,2],[2,2,-2],[3,1,1]])
x0=np.matrix([1.0,0.0,1.0])
xk=np.matrix([0.0,0.0,0.0])
lambda1,xk=(eval(A,x0,xk))
print("Dominant eigenvalue =",lambda1)
sum=0
for i in range (0,3):
    sum+=abs(xk[0,i]**2)
sum1=math.sqrt(sum)
print("The corresponding Eigenvector :-")
for i in range (0,3):
    xk[0,i]=float(xk[0,i]/sum1)

print("     ",float(xk[0,0]))
print("E1 =       ",float(xk[0,1]))
print("     ",float(xk[0,2]))