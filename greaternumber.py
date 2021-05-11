a =int(input("Enter first Number :"))
b=int(input("Enter second Number :"))
c =int(input("Enter Third Number :"))
if a<b and c<b:
    print(b, "is Greater")
elif a<c and b<c:
    print(c," is Greater")
else:
    print(a," is Greater")