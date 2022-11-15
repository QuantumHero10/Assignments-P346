# Library code for Midpoint, Trapezoid and Simpson integration

def mid(f,a,b,n):#Midpoint
    h=(b-a)/n
    x=a+(h/2)
    sum=0.0
    while x<=b :
        sum+=h*f(x)
        #print(sum)
        x+=h
    return sum

def trp(f,a,b,n):#Trapezoid
    h=(b-a)/n
    x=a+(h/2)
    sum=0.0
    while x<b :
        sum+=h*((f(x-h/2)+f(x+h/2))/2)
        #print(sum)
        x+=h
    return sum

def simp(f,a,b,n):#Simpson
    h=(b-a)/n
    x=a
    sum=0.0
    w=0.0
    ct=0
    while x<=b :
        if ct==0 or ct== n:
            w=1/3
        elif ct % 2 == 0:
            w=2/3
        elif ct % 2 == 1:
            w=4/3
        sum+=w*h*f(x)
        #print(sum)
        x+=h
        ct+=1
    return sum


