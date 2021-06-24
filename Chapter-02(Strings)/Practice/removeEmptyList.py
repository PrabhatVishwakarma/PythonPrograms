def remove(n):
    l1 = []
    for i in range(0, n):
        i = input("enter value :")
        print(i)
        l1.append(i)
    print("Orignal String is : ",)
    print(l1)
    new_s1=set(filter(None, l1))
    print("")
    print("After Removing Empty Elements : ")
    print(new_s1)

n=int(input("Enter The Number Of Elements :"))
remove(n)
