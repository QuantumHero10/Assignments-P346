import matplotlib.pyplot as plt
import numpy as np
#Function to plot the sum of the terms of a series vs n. 
def f(m):
    s=0.0
    c=0.0
    S=[]
    N=[]
    #for loop to calulate sum for all values upto n 
    for i in range (1,m+1):
        c=(-1)*((-0.5)**i)
        s=s+c
        S.append(s)
        N.append(i)
    plt.plot(N,S)
    plt.show()
n=int(input('\nEnter the number of terms in the series:'))
f(n)