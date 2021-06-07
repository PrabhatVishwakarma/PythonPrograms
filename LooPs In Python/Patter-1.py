'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
'''

lines=int(input("Enter the numbers of line :"))
 
for row in range(1,lines+1):   # 1
    for column in range(1,row+1):     #
        print(column, end="")     #
    print('')