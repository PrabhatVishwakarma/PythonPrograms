from functools import reduce

sum = lambda a,b: a+b

l=[1,2,9,8]
val=reduce(sum,l)
print(val)