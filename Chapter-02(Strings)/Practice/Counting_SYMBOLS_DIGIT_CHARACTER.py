def counting(s1):
    lowercharCount=0
    uppercharCount=0
    digitCount=0
    symbolCount=0
    print("Orignal String is = ",s1)
    for char in s1:
        if char.islower():
            lowercharCount+=1
        elif char.isupper():
            uppercharCount+=1
        elif char.isnumeric():
            digitCount+=1
        else:
            symbolCount+=1
    print("LOWER CHARACTER =",lowercharCount)
    print("UPPER CHARACTER =",uppercharCount)
    print("DIGIT CHARACTER =",digitCount)
    print("SYMBOL CHARACTER =",symbolCount)
    




counting("Hey Prabhat 1233 #$I*($(@ yo332&$*#ur ve$$#$#Ry S23#@marT")