#Function for finding sum of first n odd numbers and factorial of n
def f(m):
    s=0
    f=1
    for i in range (0,m):
        s+=((2*i)+1)
    for j in range (1,m+1):
        f*=j
    print('The sum of first',m,'odd numbers is : ',s)
    print('The factorial of',m,'is : ',f)

n=int(input('\nEnter a number:'))
f(n)
