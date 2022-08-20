import numpy as np
class myComplex:
    #Function to print complex numbers
    def pcn(self,M):
        x=str(M[0])
        y=str(M[1])
        if M[1]<0:
            s=x+y+'i'
        elif M[1]>0:
            s=x+'+'+y+'i'
        else:
            s=x
        return s
    
    #function to calculate sum of 2 complex numbers
    def sum(self,M,N):
        S=[]
        S.append(int(M[0]+N[0]))
        S.append(int(M[1]+N[1]))
        print('The sum of',cx.pcn(M),'and',cx.pcn(N),'is',cx.pcn(S))
    
    #function to calculate product of 2 complex numbers
    def prod(self,M,N):
        P=[]
        P.append((M[0]*N[0])-(M[1]*N[1]))
        P.append((M[0]*N[1])+(M[1]*N[0]))
        print('The product of',cx.pcn(M),'and',cx.pcn(N),'is',cx.pcn(P))
    
    #function to calculate modulus of a complex number
    def mod(self,M):
        m=0.0
        m=np.sqrt((M[0]**2)+(M[1]**2))
        print('The modulus of',cx.pcn(M),'is',m)

cx=myComplex()
A=[3,-2]
B=[1,2]
cx.sum(A,B)
cx.prod(A,B)
cx.mod(A)
cx.mod(B)