def middleAppend(s1,s2):
    middleIndex= int(len(s1)/2)
    print(middleIndex)
    print("Orignal String Are - ",s1,s2)
    middleThree= s1[:middleIndex]+s2+s1[middleIndex:]
    print("After appending : ",middleThree)

middleAppend("Prabhat","Khushi")