def main(func,rangeA,rangeB):
    import math
    import matplotlib.pyplot as plt
    X=[]
    h=(rangeB-rangeA)/1000
    while rangeA <= rangeB :
        X.append(rangeA)
        rangeA+=h
    Y = [func(x) for x in X]
    plt.plot(X,Y)