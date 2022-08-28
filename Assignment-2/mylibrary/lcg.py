import matplotlib.pyplot as plt
#function for LCG
def main(x,n):
    c=12345.0
    a=1103515245.0
    m=32768.0
    xlist=[]
    y=[]
    for i in range (n):
        x=((a*x)+c)%(m)
        xlist.append(x/m)
        y.append(i+1)
    return xlist
