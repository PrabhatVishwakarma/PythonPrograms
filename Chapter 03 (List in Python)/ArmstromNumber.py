n=int(input("Enter 3 Digit NUmber :"))
f=(n//100)
m=(n//10)-f*10
l=n%10
sum=n
if (f**3+m**3+l**3==sum):
    print(f"{n} is an ArmStrom Number")
else:
    print(f"{n} is not an Aramstrom number")