import math
import mylibrary.nb as nb #Importing the code for Bisection method
import mylibrary.rf as rf #Importing the code for Regula-falsi method
import mylibrary.nr as nr #Importing the code for Newton-Raphson method

def f(x):  # Non linear equation
    return (-x - math.cos(x))

def d(x):  # First derivative of Non linear equation w.r.t x
    return (-1 + math.sin(x))

def main(f,d):
    a= -2.0 #Interval
    b= 0.0
    nb.main(f,a,b) #Solving linear equations using Bisection method
    rf.main(f,a,b) #Solving linear equations using Regula-falsi method
    x0= 1.0  #Initial guess for newton-raphson
    nr.main(f,d,x0) #Solving linear equations using Newton-Raphson method

main(f,d)