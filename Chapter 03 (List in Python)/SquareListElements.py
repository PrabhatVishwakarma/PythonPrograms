aList = [1, 2, 3, 4, 5, 6, 7]
list2=[]
for i in aList:
    list2.append(i*i)
print(list2)

aList=[x*x for x in aList]
print(aList)

