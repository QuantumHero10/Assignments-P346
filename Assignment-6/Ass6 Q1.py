import matplotlib.pyplot as plt
import math
def f1(x,y,t):
    return (y)

def f2(x,y,t):
    return (-(0.1*y) - x + math.cos(1.2*t))

def couple(x0,y0,t,tn,dt):# RK4 for coupled differential equations
    X=[]
    Y=[]
    T=[]
    T1=[]
    ct=1
    while t < tn :
        X.append(x0)
        Y.append(y0)
        T.append(t)
        k1x=dt*f1(x0,y0,t)
        k1y=dt*f2(x0,y0,t)
        k2x=dt*f1(x0+k1x/2,y0+k1y/2,t+dt/2)
        k2y=dt*f2(x0+k1x/2,y0+k1y/2,t+dt/2)
        k3x=dt*f1(x0+k2x/2,y0+k2y/2,t+dt/2)
        k3y=dt*f2(x0+k2x/2,y0+k2y/2,t+dt/2)
        k4x=dt*f1(x0+k3x,y0+k3y,t+dt)
        k4y=dt*f2(x0+k3x,y0+k3y,t+dt)
        x0+= (k1x + 2*k2x + 2*k3x + k4x)/6
        y0+= (k1y + 2*k2y + 2*k3y + k4y)/6
        t+=dt
        ct+=1
    plt.plot(T,Y)
    plt.title(str(" t vs y plot "+"( The value of y at t ="+str(tn)+":-"+str(y0)+")"))
    plt.xlabel("t")
    plt.ylabel("y")
    plt.show()



x0=2.0
y0=-1.0
t0=0.0
tn=100
dt=0.01
couple(x0,y0,t0,tn,dt)