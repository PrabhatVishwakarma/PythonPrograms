def balancedString(s1,s2):
    a=True
    for char in s1:
        if char in s2:
            continue
        else:
            a=False 
    print (a)


balancedString("i","Khushi")