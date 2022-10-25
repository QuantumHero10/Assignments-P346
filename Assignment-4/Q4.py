import mylibrary.pft as pft #Importing the code for Polynomial fitting
import mylibrary.gji as gji #Importing the code for Gauss jordan inverter
def main():
    n = 4 # No. of terms in the fitting equation 
    path = 'C:\\Users\\manor\\Desktop\\P346 codes\\fitmatrix.csv' # File path of the data
    pft.main(gji,path,n) #Fitting the given data using Polynomial fitting

main()