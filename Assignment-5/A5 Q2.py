import math
import mylibrary.lcg as lcg
import mylibrary.mac as mac
def f(x):
    return (math.sin(x))**2

a=-1
b=1
n=900
print("Estimated value of integral using monte carlo integration =",mac.mont(f,a,b,n,lcg))
print("Actual value of integral =",0.5453512865871592)