def capLetterFirst(s1):
    print("Orignal String Is -",s1)
    lower = []
    upper = []
    for char in s1:
        if char.islower():
            lower.append(char)
        else:
            upper.append(char)
    sorting="".join(lower+upper)
    print("Shorted character is - ",sorting)

capLetterFirst("TreeWasVeryBeautiFul")