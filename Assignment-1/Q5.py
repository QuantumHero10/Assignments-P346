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
        cx.output('The sum of '+str(cx.pcn(M))+' and '+str(cx.pcn(N))+' is '+str(cx.pcn(S)))
        cx.output('\n')
    
    #function to calculate product of 2 complex numbers
    def prod(self,M,N):
        P=[]
        P.append((M[0]*N[0])-(M[1]*N[1]))
        P.append((M[0]*N[1])+(M[1]*N[0]))
        cx.output('The product of '+str(cx.pcn(M))+' and '+str(cx.pcn(N))+' is '+str(cx.pcn(P)))
        cx.output('\n')
    
    #function to calculate modulus of a complex number
    def mod(self,M):
        m=0.0
        m=np.sqrt((M[0]**2)+(M[1]**2))
        cx.output('The modulus of '+str(cx.pcn(M))+' is '+str(m))
        cx.output('\n')

    #Function to write output to a file
    def output(self,s):
        with open("Assignment-1\\Output(Q5).txt",'a') as file:
            file.write(s)
            file.close()
        return

#Function to create a output file
with open("Assignment-1\\Output(Q5).txt",'w') as file:
    file.write("OUTPUT : \n")
    file.close()

cx=myComplex()
A=[3,-2]
B=[1,2]
cx.sum(A,B)
cx.prod(A,B)
cx.mod(A)
cx.mod(B)