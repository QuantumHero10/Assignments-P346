#Function for finding sum of first n odd numbers and factorial of n
def f(m):
    s=0
    f=1
    for i in range (0,m):
        s+=((2*i)+1)
    for j in range (1,m+1):
        f*=j
    s1=('The sum of first '+str(m)+' odd numbers is : '+str(s))
    if m<0:
        s2=('The factorial of '+str(m)+' cannot be calculated.')
    else:
        s2=('The factorial of '+str(m)+' is : '+str(f))
    output(s1)
    output(s2)
    return

#Function to write output to a file
def output(s):
    with open("Assignment-1\\Output(Q1).txt",'a') as file:
        file.write(s)
        file.write('\n')
        file.close()
    return

#Function to create a output file
with open("Assignment-1\\Output(Q1).txt",'w') as file:
    file.write("OUTPUT : \n")
    file.close()
n=int(input('\nEnter a number:'))
f(n)
