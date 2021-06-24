def countWord(s1):
    print(s1)
    f=input("Enter the word you want to count : ")
    r=s1.lower()
    count=r.count(f.lower())
    print(f"{f} is {count} times in a {s1}")

countWord("Prabhat is a good boy. Prabhat know python. Prabhat have 100 Girlfriend")