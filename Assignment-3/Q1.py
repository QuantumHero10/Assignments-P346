import mylibrary.gje as gje #Importing the code for Gauss-Jordon elimination method
import mylibrary.lud as lud #Importing the code for LU decomposition method
def main():
    path='Assignment-3\\matrix1.csv' #Augmented matrix full path
    gje.main(path) #Solving linear equations using Gauss-Jordon elimination method
    lud.main(path) #Solving linear equations using LU decomposition method

main()
