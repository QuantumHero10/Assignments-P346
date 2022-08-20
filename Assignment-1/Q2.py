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

cd=1.5
cr=0.5
b=float(input('\nEnter the 1st term of the series:'))
m=int(input('\nEnter the number of terms:'))
print(ap(b,cd,m))
print(gp(b,cr,m))
print(hp(b,cd,m))