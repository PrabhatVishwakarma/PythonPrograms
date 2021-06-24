import string
def removeCharacter(s1):
    special_chars = string.punctuation
    for special_chars in s1:
        new=s1.remove(special_chars)
    print(new)

s1=input("Enter String With Unique Character :")
removeCharacter(s1)