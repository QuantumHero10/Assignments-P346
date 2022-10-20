import math
import mylibrary.lcg as lcg
def area_ellipse():
    x1=[]
    y1=[]
    n=226
    ct=0
    a=1 #semi-minor axis
    b=2 #semi-major axis
    x1,y1 = lcg.main(10,n)
    for i in range (0,n):
        dx = (x1[i])/(n)
        dy = y1[i]
        if ((dx**2) + dy**2) <= 1:
            ct+=1
    pi = (4*ct)/n #Value of pi 
    #Area of ellipse = PI*semi-minor axis*semi-major axis
    print("No. of random points = ",n)
    print("Area of the ellipse = ",pi*a*b) 
    print("Actual value = ",(math.pi*a*b)) 
    print("5% error = ",(0.05*math.pi*a*b)) 

area_ellipse()