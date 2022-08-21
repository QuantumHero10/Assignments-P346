import numpy as np
#Function to print a matrix
def printmatrix(M):
  n=np.size(M,0)
  m=np.size(M,1)
  for i in range (n):
    for j in range (m):
      if M[i,j]==0:
        M[i,j]=abs(M[i,j])
      output(str(round(float(M[i,j]),3))+'       ')
    output("\n")
  output("\n")

#Function to multiply 2 matrices
def multi(M,N):
    m1=np.size(M,0)
    m2=np.size(M,1)
    n1=np.size(N,0)
    n2=np.size(N,1)
    P=[]
    output('The input matrices are:\n\n\n')
    printmatrix(M)
    printmatrix(N)
    #if statement to check if 2 matrices can be multiplied or not
    if m2 != n1:
        output('The two input matrices cannot be multiplied.\n')
        return
    for i in range (0,m1):
        row=[]
        for j in range (0,n2):
            c=0.0
            s=0.0
            for k in range (0,m2):
                c=M[i,k]*N[k,j]
                s=s+c
            row.append(s)
        P.append(row)
    Q=np.matrix(P)
    output('The product of the above two matrices is:\n' )
    printmatrix(Q)

#Function to write output to a file
def output(s):
    with open("C:\\Users\\manor\\Desktop\\P346 codes\\Assignment-1\\Output(Q4).txt",'a') as file:
        file.write(s)
        file.close()
    return

#Function to create a output file
with open("C:\\Users\\manor\\Desktop\\P346 codes\\Assignment-1\\Output(Q4).txt",'w') as file:
    file.write("OUTPUT : \n")
    file.close()

A = np.matrix([[2.0,-3.0,1.4],[2.5,1.0,-2.0],[-0.8,0.0,3.1]])
B = np.matrix([[0.0,-1.0,1.0],[1.5,0.5,-2.0],[3.0,0.0,-2.0]])
C = np.matrix([[-2.0],[0.5],[1.5]])
D = np.matrix([[1.0],[0.0],[-1.0]])
AB= multi(A,B)
DC= multi(D,C)
BC= multi(B,C)