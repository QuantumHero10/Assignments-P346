import mylibrary.gas as gas #Importing the code for Gauss-Seidel method
import mylibrary.lud as lud #Importing the code for LU decomposition method
def main():
    path='C:\\Users\\manor\\Desktop\\P346 codes\\matrix3.csv' #Augmented matrix full path
    lud.main(path) #Solving linear equations using Gauss-Seidel method
    gas.main(path) #Solving linear equations using LU decomposition method

main()