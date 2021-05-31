'''count=0
with open("test.txt", 'r') as f:
    lines = f.readlines()
    count = len(lines)

with open("NewFile.txt","w") as f:
    for line in lines:
        if count==3:
            count -= 1
            continue
        else:
            f.write(line)
        count -= 1'''

#OR

f1 = open("test.txt", "r")

f2 = open("NewFile.txt", "w")
count = 0
for i in f1:
    if count==5:
        pass
    else:
        f2.write(i)
    count+=1
