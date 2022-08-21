#Function for calculating the sum of AP
def ap(a,d,n):
    s=0.0
    c=0.0
    for i in range (0,n):
        c=a+(i*d)
        s=s+c
    return s

#Function for calculating the sum of GP
def gp(a,r,n):
    s=0.0
    c=0.0
    for i in range (0,n):
        c= a*(r**i)
        s=s+c
    return s

#Function for calculating the sum of HP
def hp(a,d,n):
    s=0.0
    c=0.0
    for i in range (0,n):
        c=1/(a+(i*d))
        s=s+c
    return s

#Function to write output to a file
def output(s):
    with open("Assignment-1\\Output(Q2).txt",'a') as file:
        file.write(s)
        file.write('\n')
        file.close()
    return

#Function to create a output file
with open("Assignment-1\\Output(Q2).txt",'w') as file:
    file.write("OUTPUT : \n")
    file.close()
cd=1.5
cr=0.5
b=float(input('\nEnter the 1st term of the series:'))
m=int(input('\nEnter the number of terms:'))
s1="The sum of "+str(m)+" terms of the AP series is : "+str(ap(b,cd,m))
s2="The sum of "+str(m)+" terms of the GP series is : "+str(gp(b,cr,m))
s3="The sum of "+str(m)+" terms of the HP series is : "+str(hp(b,cd,m))
output(s1)
output(s2)
output(s3)