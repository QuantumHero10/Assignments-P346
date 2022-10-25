import math
import mylibrary.nb as nb #Importing the code for Bisection method
import mylibrary.rf as rf #Importing the code for Regula-falsi method

def f(x):  # Non linear equation
    return (math.log10(0.5*x) - math.sin(2.5*x))

def main(f):
    a= 1.5 #Interval
    b= 2.5
    nb.main(f,a,b) #Solving linear equations using Bisection method
    rf.main(f,a,b) #Solving linear equations using Regula-falsi method

main(f)