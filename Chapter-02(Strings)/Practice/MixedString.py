def mixString(s1,s2):
    s2 = s2[::-1]
    print(s2)
    lS1 = len(s1)
    lS2 = len(s2)
    print(lS1)
    print(lS2)
    length  = lS1 if lS1 > lS2 else lS2
    print(length)
    resultString=""
    for i in range(length):
        if(i < lS1):
            resultString = resultString + s1[i]
        if(i < lS2):
            resultString = resultString + s2[i]
    print(resultString)

mixString("abcd","wxyz")