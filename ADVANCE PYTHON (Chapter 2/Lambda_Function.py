#SQUARE OF ANY NUMBER
print("*******************SQUARE A NUMBER*********************")
square = lambda a:a*a
a=int(input("Enter the NUmber You wnat to Square ="))
s=square(a)
print(f"Square of {a} is {s}")
print("")
#AREA OF RECTANGLE
print("****AREA OF RECTANGLE*********")
area = lambda l,b:l*b
l=int(input("Enter the Length of rectangle :"))
b=int(input("Enter breadth of rectangle :"))
a=area(l,b)
print("Area of rectangle = ",a)
print("")
#SUM OF 3 NUMBERS
print("*****************SUM OF THREE NUMBERS*******************")
sum=lambda a,b,c:a+b+c
a=int(input("Enter the 1st number ="))
b=int(input("Enter the 2nd number ="))
c=int(input("Enter the 3rd number ="))
s=sum(a,b,c)
print(f"Sum of {a} + {b} + {c} is {s}")