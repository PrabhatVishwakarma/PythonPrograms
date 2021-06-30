list1=[5, 20, 15, 20, 25, 50, 20]
n=int(input("Removal number :"))
for x in list1:
    if x==n:
        list1.remove(n)
print(list1)