list =[]
n = int(input("Enter the NUmber Of Items In a List :"))

for SerialNumber in range(1,n+1):
    print("Item Number ", SerialNumber , ":", end=" ")
    item = float(input())
    list.append(item)
    
print("User List :", list)


