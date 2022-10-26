# Laguerre method
import math
def f(A,x):
    y=0.0
    n=len(A)
    for i in range (0,n):
        y+=(A[i]*(x**(n-i-1)))
    return y

def d(A):
    n=len(A)
    R=[0]*n
    for i in range (0,n-1):
        R[i+1] = A[i]*(n-i-1)
    return R

def lag(M,b,n):
    g= f(d(M),b)/f(M,b)
    h= (g*g) - (f(d(d(M)),b)/f(M,b))
    p = math.sqrt((n-1)*(n*h - g*g))
    if g==0 and p==0:
        return "terminate"
    if abs(g + p) >= abs(g - p):
        a = n/(g+p)
    else:
        a = n/(g-p)
    b=b-a
    return b

def df(A,x):
    n=len(A)
    R=[0]*n
    for i in range (1,n):
        j=A[i-1]
        R[i] = j
        A[i-1] = 0
        A[i] = A[i] + (j*x)
    return R

def main(A):
    b0=1.5
    b=float(b0)
    n1=1
    print("The roots of the given polynomial equation are:\n")
    for i in range (1,1000):
        if abs(f(A,b)) < 10**-6:
            n1+=1
            print("Root",(n1-1),"=",b)
            A=df(A,b)
            if f(A,b)==0:
                return
            b=lag(A,b0,n1)
            if b=="terminate":
                return
            continue
        else:
            b=lag(A,b,n1)