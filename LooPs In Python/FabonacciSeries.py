N=int(input("Enter the number :"))
fab=0
N1=0
N2=1


for x in range(0,N+1):
        fab=N1+N2
        N1 = N2
        N2 = fab
        print(fab)


