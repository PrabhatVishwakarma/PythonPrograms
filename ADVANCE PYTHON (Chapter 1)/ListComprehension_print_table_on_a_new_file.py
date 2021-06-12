while(True):
    num=int(input("enter the Number whose Table To want to print in a file ="))

    print("If You Want save the file enter S or s")
    if num =="s" or num=="S":
        break

    Table=[num*i for i in range(1,11)]

    with open ("table.txt","a") as f:
        f.write(f"table of {num} -:")
        f.write(str(Table))
        f.write("\n")