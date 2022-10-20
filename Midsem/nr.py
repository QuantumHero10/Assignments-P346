def main(f,d,x):
    while abs(f(x))>10**-4:
        x= x - f(x)/d(x)
    return x

