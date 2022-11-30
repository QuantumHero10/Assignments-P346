import mylibrary.nit as nit #Importing intergration library file
# nit.simp is for simpson method
import math
def f(x):
    return 1/(math.sqrt(1-(math.sin(math.pi/8)*math.sin(x))**2))
def main():
    a=0
    b=math.pi/2
    n=10 # N=10
    print("Value of T =",(4*math.sqrt(1/9.8)*(nit.simp(f,a,b,n))),"s")
main()