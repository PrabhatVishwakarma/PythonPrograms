with open("test.txt") as my_file:
    file = my_file.readlines()
    n = int(input("Enter the line number you want to read :"))
    print(file[n-1])