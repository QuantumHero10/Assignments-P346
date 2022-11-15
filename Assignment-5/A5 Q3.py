import math
import mylibrary.lcg as lcg
import mylibrary.mac as mac
import mylibrary.nit as nit
def f(x):
    return x**2
def xf(x):
    return x*(f(x))

com = mac.mont(xf,0,2,1000,lcg)/mac.mont(f,0,2,1000,lcg)
print("Estimated centre of mass from the end given in question =",com,"m")
print("Actual value of centre of mass =",1.5,"m\n")