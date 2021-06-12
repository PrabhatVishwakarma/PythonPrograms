while(True):

    a = int(input("Enter the number in a ="))
    b = int(input("Enter the number in b ="))
    if a=="X" or a=="x" or b=="X" or b=="x":
        break
    try:
        if b!=0:
            print(a/b)
    except ZeroDivisionError:
        print("infinite2")