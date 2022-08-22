class myComplex():
    def comp_op(self):

        #SUM
        s=c1+c2
        cx.output("The sum of the given two complex numbers is: "+str(s)+"\n")
        #PRODUCT
        p=c1*c2
        cx.output("The product of the given two complex numbers is: "+str(p)+"\n")
        #modulus
        mc1=((c1.real)**2 + (c1.imag)**2)**0.5
        mc2=((c2.real)**2 + (c2.imag)**2)**0.5
        cx.output("The modulus of the complex number "+str(c1)+" is "+str(mc1)+"\nThe modulus of the complex number "+str(c2)+" is "+str(mc2))

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
c1=complex(3,-2)
c2=complex(1,2)
cx.comp_op()