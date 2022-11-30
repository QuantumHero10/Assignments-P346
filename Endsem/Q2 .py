import mylibrary.lcg as lcg
import matplotlib.pyplot as plt
def main():
    n=nl=5000
    T, ls, rs = [], [], []
    for t in range(50000):
        T.append(t)
        
        for i in range(n):
            y,X=lcg.main(nl)
            if float(X[i]) < nl/n :# determine the particle is in which side
                l=-1
                p=nl/n
            else:
                l=1
                p=1-nl/n
            if X[i] < p:# determine if the particle is going to travel or not
                nl += l
                break
        ls.append(nl)
        rs.append(n-nl)

    plt.plot(T, ls, label="number of particles on the left side")
    plt.plot(T, rs, label="number of particles on the right side")
    plt.xlabel("t")
    plt.ylabel("number of particles")
    plt.legend()
    plt.show()

main()