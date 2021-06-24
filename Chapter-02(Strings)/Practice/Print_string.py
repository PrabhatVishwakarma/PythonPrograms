def centerValue(s1,s2):
    string1=int(len(s1)/2)
    string2=int(len(s2)/2)
    print("Orignal String : ",s1,s2)
    print(string1)
    output=s1[0]+s2[0]+s1[string1]+s2[string2:]
    print(output)

centerValue("America","Japan")