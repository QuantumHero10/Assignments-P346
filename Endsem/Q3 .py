import mylibrary.nr as nr
import math
def f(x):
    return 2.5-(x*math.exp(x))

def d(x):
    return -(math.exp(x)+x*math.exp(x))

def main():
    x0=1.0
    print("The spring can be strectched upto :",nr.main(f,d,x0),"m")

main()