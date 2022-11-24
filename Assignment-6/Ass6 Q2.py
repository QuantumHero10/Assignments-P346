import matplotlib.pyplot as plt
import math
def dzdx(z,y,x):
    return 0.01*(y-293.15)

def dydx(z,y,x):
    return (z)

def couple(z0,y0,x0,xn,dx):#Coupled RK4 with plot
    X=[]
    Y=[]
    Z=[]
    ct=1
    while x0 < xn :
        Z.append(z0)
        Y.append(y0)
        X.append(x0)
        k1z=dx*dzdx(z0,y0,x0)
        k1y=dx*dydx(z0,y0,x0)
        k2z=dx*dzdx(z0+k1z/2,y0+k1y/2,x0+dx/2)
        k2y=dx*dydx(z0+k1z/2,y0+k1y/2,x0+dx/2)
        k3z=dx*dzdx(z0+k2z/2,y0+k2y/2,x0+dx/2)
        k3y=dx*dydx(z0+k2z/2,y0+k2y/2,x0+dx/2)
        k4z=dx*dzdx(z0+k3z,y0+k3y,x0+dx)
        k4y=dx*dydx(z0+k3z,y0+k3y,x0+dx)
        z0+= (k1z + 2*k2z + 2*k3z + k4z)/6
        y0+= (k1y + 2*k2y + 2*k3y + k4y)/6
        x0+=dx
        ct+=1
    plt.plot(X,Y,'.',markersize=2.0)
    return y0

def couple2(z0,y0,yn,x0,xn,dx):#Coupled RK4 without plot for later use in code
    X=[]
    Y=[]
    Z=[]
    ct=1
    while x0 < xn :
        Z.append(z0)
        Y.append(y0)
        X.append(x0)
        k1z=dx*dzdx(z0,y0,x0)
        k1y=dx*dydx(z0,y0,x0)
        k2z=dx*dzdx(z0+k1z/2,y0+k1y/2,x0+dx/2)
        k2y=dx*dydx(z0+k1z/2,y0+k1y/2,x0+dx/2)
        k3z=dx*dzdx(z0+k2z/2,y0+k2y/2,x0+dx/2)
        k3y=dx*dydx(z0+k2z/2,y0+k2y/2,x0+dx/2)
        k4z=dx*dzdx(z0+k3z,y0+k3y,x0+dx)
        k4y=dx*dydx(z0+k3z,y0+k3y,x0+dx)
        z0+= (k1z + 2*k2z + 2*k3z + k4z)/6
        y0+= (k1y + 2*k2y + 2*k3y + k4y)/6
        x0+=dx
        ct+=1
        if abs(y0-yn)<=10**-3:
            print("T=100 C is at x =",x0-dx)
            return

x0=0.0
y0=40.0+273.15 #In Kelvin scale
xn=10.0
dx=0.1
a=40.0+273.15 #In Kelvin scale
b=200.0+273.15 #In Kelvin scale
ci=10
ch=ci
print("Initial guess slope:-",ci)
couple(ci,y0,x0,xn,dx)
y=float(couple(ci,y0,x0,xn,dx)-b)
while abs(y)>10**-4:
    if (y)<b:
        ch=ch+5.0
    else:
        ch=ch-5.0
    c = ci + ((ch-ci)*(b-float(couple(ci,y0,x0,xn,dx))))/(float(couple(ch,y0,x0,xn,dx))-float(couple(ci,y0,x0,xn,dx)))
    y=float(couple(c,y0,x0,xn,dx)-b)
couple(ch,y0,x0,xn,dx)
couple(c,y0,x0,xn,dx)
print("Final value of slope:-",c)
yn=100+273.15
(couple2(c,a,yn,x0,xn,dx*0.001))
plt.title("x vs T for different guess values")
plt.axhline(y = a, color = 'black')
plt.axhline(y = b, color = 'black')
plt.show()