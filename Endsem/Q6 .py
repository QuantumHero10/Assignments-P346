import mylibrary.egv as egv
import math
import numpy as np # Used Only for defining matrices
def main():
    A=np.matrix([[1,-2,0,5],[0,7,1,5],[0,4,4,0],[0,0,0,2]])
    x0=np.matrix([1.0,1.0,1.0])
    xk=np.matrix([0.0,0.0,0.0])
    ep=10**-3 #precision
    lambda1,xk,ct=(egv.main(A,x0,xk,ep))
    print("No. of iterations:",ct)
    print("Dominant eigenvalue : ",lambda1)
    #print(xk)
    sum=0
    for i in range (0,3):
        sum+=abs(xk[0,i]*xk[0,i])
    sum1=math.sqrt(sum)
    for i in range (0,3):
        xk[0,i]=float(xk[0,i]/sum1)
    print("Corresponding normalized eigenvector : \n",xk ,"\nIt is column matrix just printed in row form")

main()