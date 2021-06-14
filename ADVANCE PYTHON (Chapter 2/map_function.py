def square(num):
    return num*num

list1=[1,7,2,6]

#**********METHOD 1***********

l2=[]
for x in list1:
    l2.append(square(x))
print(l2)


#*********METHOD 2*************
print(list(map(square,list1)))