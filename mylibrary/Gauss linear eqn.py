import numpy as np
def gauss(M,n):
    x1=np.matrix([[0.0],[0.0],[0.0]])
    x2=np.matrix([[0.0],[0.0],[0.0]])
    ep=0.0
    c=0
    for i in range (0,50):
        for j in range (0,n):
            sum=0.0
            for l in range(0,n):
                if j != l:
                    sum=sum+(M[j,l]*x1[l,0])
            x2[j,0]= (M[j,3]-sum)/M[j,j]
        a=0
        if c > 0 :
            for k in range (0,n):
                ep = ((x2[k,0]-x1[k,0])*100)/x1[k,0]
                if abs(ep) < 10**-4 :
                    a+=1
        if a==3:
            break
        x3=np.matrix(x2)
        x1=x3
        c+=1
    print("The solution of the given linear equations is :\n")
    print("X = ",x2)
    print("No. of iterations =",c)
    return

A = np.matrix([[4.0, -1.0, 1.0,7.0],[4.0, -8.0, 1.0,-21.0],[-2.0, 1.0, 5.0,15.0]])
gauss(A,3)