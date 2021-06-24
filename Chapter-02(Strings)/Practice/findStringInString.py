def findString (s1,st2):
    f=s1.rfind(st2)
    print(f)

s1=input("Enter the orignal string :")
s2=input("Enter the word you want to find index : ")
findString(s1,s2)