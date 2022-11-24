import matplotlib.pyplot as plt
import math

def pde():
    lx=2
    nx=20
    lt=20
    nt=100000

    hx=lx/nx
    ht=lt/nt
    a=ht/(hx*hx)
    V0=[0.0]*(nx+1)
    V1=[0.0]*(nx+1)
    T0=[]
    print('alpha = ',a)

    for i in range (0,nx+1):
        V0[i]=0.0
        T0.append(hx*i)
    V0[int(nx/2)]=300
    plt.plot(T0,V0)
    for i in range (1,1001):
        for j in range (0,nx+1):
            if j==0:
                V1[j]=(1-2*a)*V0[j]  +  a*V0[j+1]
            elif (j==nx):
                V1[j]=a*V0[j-1]  +  (1-2*a)*V0[j]
            else:
                V1[j]=a*V0[j-1]  +  (1-2*a)*V0[j]  +  a*V0[j+1]
        
        for k in range (0,nx+1):
            V0[k]=V1[k]
        if i==100 or i==200 or i==500 or i==1000 or i==2000 or i==5000 or i==10000 or i==20000 :
            plt.plot(T0,V0)
    plt.title((" α = "+str(a)))
        
pde()
plt.show()
    

