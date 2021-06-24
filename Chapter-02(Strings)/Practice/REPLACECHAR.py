from string import punctuation
def replaceSymbol1(s1):
    replaceSymbol="#"
    for i in punctuation:
        s1=s1.replace(i,replaceSymbol)
    print(s1)

s1=input("Enter the String :")
replaceSymbol1(s1)

