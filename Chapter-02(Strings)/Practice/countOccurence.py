def occurance (s1):
    countDict=dict()
    for char in s1:
        count=s1.count(char)
        countDict[char]=count
    
    print(countDict)

occurance("Apple")