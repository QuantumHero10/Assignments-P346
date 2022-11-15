import math 
import numpy as np
import mylibrary.nit as nit
def f(x):
    return math.sqrt(1+(1/x))

a=1
b=4
A=[]
for n in range (10,31,10):
    r=[]
    r.append(nit.mid(f,a,b,n))
    r.append(nit.trp(f,a,b,n))
    r.append(nit.simp(f,a,b,n))
    A.append(r)
A=np.matrix(A)


print("                  Midpoint                  Trapezoid               Simpson\n")
for i in range (0,3):
    print("N =",(i+1)*10,end="    ")
    for j in range (0,3):
        print("  ",A[i,j],end="    ")
    print("\n")

print("Actual value of the integral =",3.620184280785752,"\n")