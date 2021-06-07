lines=int(input("Enter The Number Of Line :"))
for row in range(1,lines+1):
    for column in range(0,row):
        print("*", end=" ")
    print("")



for row in range(lines, 0, -1):
    for column in range(0, row - 1):
        print("*", end=' ')
    print("")