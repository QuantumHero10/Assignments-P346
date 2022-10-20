import math
import mylibrary.nr as nr
def f(x):
    return ((x-5)*math.exp(x)) + 5 

def d(x):
    return math.exp(x)*(x-4)

def wein(f,d):
    h=6.626*(10**-34)
    c=3*(10**8)
    k=1.381*(10**-23)
    x0=10
    x=nr.main(f,d,x0)
    b=(h*c)/(x*k)
    print("Value of Wein's constant = ",b,"m K")

wein(f,d)
