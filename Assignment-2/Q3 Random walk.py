import math
import matplotlib.pyplot as plt
import mylibrary.lcg as lcg
#Function for generating a random walk
def randomwalk(s1,s2,n):
    x=lcg.main(s1,n)                #Different seeds for different axes
    y=lcg.main(s2,n)
    xc=[0.0]
    yc=[0.0]
    rms=0.0
    d=0.0
    dsp=0.0
    x2=0.0
    y2=0.0
    #Loop to find the points in a random walk
    for i in range (0,n) :
        x1=((x[i]*2)-1)+x2
        y1=((y[i]*2)-1)+y2
        xc.append(x1)
        yc.append(y1)
        d+=((x1-x2)**2 +(y1-y2)**2)
        x2=x1
        y2=y1
    rms=math.sqrt(d/n)
    dsp=math.sqrt((x1**2)+(y1**2))
    output("The rms distance for random walk of "+str(n)+" steps is : \n")
    output(str(rms)+'\n')
    output("The net displacement for random walk of "+str(n)+" steps is : \n")
    output(str(dsp)+'\n')
    plt.title("\nRandom walk of "+str(n)+" steps")
    plt.plot(xc,yc,color='orange')
    plt.show()

    #Function to write output to a file
def output(s):
    with open("Assignment-2\\Output(Q3).txt",'a') as file:
        file.write(s)
        file.close()
    return

#Function to create a output file
with open("Assignment-2\\Output(Q3).txt",'w') as file:
    file.write("OUTPUT : \n")
    file.close()

randomwalk(10,5,300)
randomwalk(14,9,600)
randomwalk(19,13,900)
