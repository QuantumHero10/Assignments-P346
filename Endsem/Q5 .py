import mylibrary.plotfunc as fplot
import mylibrary.rk4 as rk4

def f1(x,y,t):
    return (y)

def f2(x,y,t):
    return (-0.02*y)-10

print("Without air resistance maximum height reached is : 5m")
print("The time taken to reach maximum point is : 1s")
x0=0.0
y0=10.0
t0=0.0
tn=1.0 #As maximum height is reached at t=1s
dt=0.01
print("The maximum height reched including air resistance =",rk4.main(f1,f2,x0,y0,t0,tn,dt),"m")
