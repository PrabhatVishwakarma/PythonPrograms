from functools import reduce

sum = lambda a,c,b:a*b*c

l=[1,2,9,8]
val=reduce(sum,l)
print(val)