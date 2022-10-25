# Newton-Raphson method

def main(f,d,x):
    ct=0
    print("Initial guess =",x)
    while abs(f(x))>10**-6:
        ct+=1
        x= x - f(x)/d(x)
        print(x)
    print("The required root is:",x)
    print("No. of Iterations:",ct)
    return x

