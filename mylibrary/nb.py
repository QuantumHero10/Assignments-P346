# Bisection method

def main(f,a,b):
    ct=0
    c=0.0
    t=0.7
    while f(a)*f(b)>0:
        if abs(f(a))>abs(f(b)):
            b=b+(t*(b-a))
        elif abs(f(a))<abs(f(b)):
            a=a-(t*(b-a))
    c=(a+b)/2
    while abs(f(c))>10**-6:
        ct+=1
        c=(a+b)/2
        if f(a)*f(c) < 0:
            b=c
        elif f(c)*f(b) < 0:
            a=c
        print(c)
    print("The required root is:",c)
    print("No. of Iterations:",ct)
