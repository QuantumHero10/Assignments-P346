def mid(f,a,b,n):
    h=(b-a)/n
    x=a+(h/2)
    sum=0.0
    while x<=b :
        sum+=h*f(x)
        x+=h
    return sum

def trp(f,a,b,n):
    h=(b-a)/n
    x=a+(h/2)
    sum=0.0
    while x<b :
        sum+=h*((f(x-h/2)+f(x+h/2))/2)
        x+=h
    return sum

def simp(f,a,b,n):
    h=(b-a)/n
    sum=f(a)+f(b)
    for i in range (1,n) :
        if i % 2 == 0:
            sum+=2*f(a+i*h)
        elif i % 2 == 1:
            sum+=4*f(a+i*h)
    return sum*h/3


