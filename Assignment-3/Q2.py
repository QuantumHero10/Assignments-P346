import mylibrary.chy as chy #Importing the code for Cholesky decomposition method
import mylibrary.gas as gas #Importing the code for Gauss-Seidel method
def main():
    path='C:\\Users\\manor\\Desktop\\P346 codes\\matrix2.csv' #Augmented matrix full path
    chy.main(path) #Solving linear equations using Cholesky decomposition method
    gas.main(path) #Solving linear equations using Gauss-Seidel method

main()