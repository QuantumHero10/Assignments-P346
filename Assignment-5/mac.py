# Library code for Monte-Carlo integration 
import math
import matplotlib.pyplot as plt
def mont(f,a,b,n,lcg):
    F=[]
    S=[]
    Y1=[]
    ct=0
    for i in range(10,n,10):
        ct+=1
        Y0,X0=lcg.main(i)
        Y1.append(i)
        X=[]
        for j in range(0,i):
            X.append(a+((b-a)*X0[j]))
        sum0=0.0
        sum1=0.0
        for k in range(0,i):
            sum0+= f(X[k])
            sum1+= f(X[k])**2
        F.append((b-a)*(sum0/i))
        S.append((sum1/i)-((sum0**2)/i))
    #plt.plot(Y1,F)
    #plt.show()
    return (F[ct-1])
    
