list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

for item in list1:
    if (item==""):
        list1.remove(item)
    
print(list1)

resList = list(filter(None, list1))
print(resList)