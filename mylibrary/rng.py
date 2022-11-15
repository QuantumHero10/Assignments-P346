#function for RNG
def main(n):
    x = 0.1
    c = 3.98
    X=[]
    for i in range (n):
        X.append(x)
        x=c*x*(1-x)
    return X

