# Regula-falsi method

def main(f,a,b):
    c=0.0
    ct=0
    c= b - ((b-a)*f(b))/(f(b)-f(a))
    while abs(f(c))>10**-6:
        c= b - ((b-a)*f(b))/(f(b)-f(a))
        if f(a)*f(c)<0:
            b=c
        elif f(b)*f(c)<0:
            a=c
        ct+=1
        if ct==100:
            break
        print(c)
    print(c)
    print("No. of Iterations:",ct)
    print("The required root is:",c)
