def greaterNumber(num):
    if num>111111:
        return True
    else:
        return False

l=[1876543,135678,2476543,2887,90987,2343,3,2,34,3,45,434,566543,456543,454,4567,43,876,4,3,34543,45,43,4,5,43,45,54,3,456,54,5,6]
s=l.sort()
print(s)
print(list(filter(greaterNumber,l)))