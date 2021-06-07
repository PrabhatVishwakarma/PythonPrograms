''' 2 +22 + 222 + 2222 +.....+(n-2n) +n'''
number_of_terms = int(input("enter the number of terms :"))
start = 2
sum = 0
for i in range(0, number_of_terms):
    print(start, end=" + ")
    sum += start
    start = (start * 10) + 2
print("\nSum of above series is:", sum)