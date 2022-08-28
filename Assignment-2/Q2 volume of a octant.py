import mylibrary.lcg as lcg
#Function to find volume of an octant of a sphere
def vol_octant():
    n=1000
    c=0
    x0=10
    x=lcg.main(x0,n)
    y=lcg.main(x0,n)
    z=lcg.main(x0,n)
    #Loop to count the number of points inside the octant
    for i,j,k in zip(x,y,z):
      if (i**2 + j**2 + k**2) <= 1:
        c+=1
    vol = c/n
    output('The volume of one octant of the sphere is : '+str(vol))

#Function to write output to a file
def output(s):
    with open("Assignment-2\\Output(Q2).txt",'a') as file:
        file.write(s)
        file.close()
    return

#Function to create a output file
with open("Assignment-2\\Output(Q2).txt",'w') as file:
    file.write("OUTPUT : \n")
    file.close()

vol_octant()
