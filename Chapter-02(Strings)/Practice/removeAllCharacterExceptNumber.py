def removeAlphabets(s1):
    for i in s1:
        if i.isnumeric():
            print(i, end="")
    
    # Also

    a = "".join([items for items in s1 if items.isdigit()])
    print(a)


removeAlphabets("ygyuyg8764gdyg1233prfe4321bht")
