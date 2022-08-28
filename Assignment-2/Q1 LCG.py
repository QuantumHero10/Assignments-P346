import matplotlib.pyplot as plt
#function for LCG
def LCG(c,a,n):
  x=10.0
  m=32768.0
  xlist=[]
  ylist=[]
  for i in range (n):
    x=((a*x)+c)%(m)
    xlist.append(x/m)
    ylist.append(i+1)
  plt.plot(ylist,xlist,'.',color='purple')
  plt.show()
x1=LCG(12345,1103515245,1000)
