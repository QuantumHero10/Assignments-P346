import mylibrary.gas as gas #Importing the code for Gauss-Seidel method
import mylibrary.lud as lud #Importing the code for LU decomposition method
import mylibrary.jac as jac #Importing the code for Jacobi method
def main():
    path='C:\\Users\\manor\\Desktop\\P346 codes\\matrix3.csv' #Augmented matrix full path
    lud.main(path) #Solving linear equations using Gauss-Seidel method
    jac.main(path) #Solving linear equations using Jacobi method
    gas.main(path) #Solving linear equations using LU decomposition method

main()