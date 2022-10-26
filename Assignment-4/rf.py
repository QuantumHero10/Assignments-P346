# Regula-falsi method

def main(f,a,b):
    c=0.0
    ct=0
    c= b - ((b-a)*f(b))/(f(b)-f(a))
    e=10**-6
    while abs(f(c))>e and (b-a)>e and abs(f(a))>e and abs(f(b))>e:
        c= b - ((b-a)*f(b))/(f(b)-f(a))
        if f(a)*f(c)<0:
            b=c
        elif f(b)*f(c)<0:
            a=c
        else:
            a=a+0.1
        ct+=1
        print(c)
    print("No. of Iterations:",ct)
    print("The required root is:",c)
