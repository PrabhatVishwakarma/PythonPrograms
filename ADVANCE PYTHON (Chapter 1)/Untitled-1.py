while (True):
    print("enter q to exit")
    a=int(input("Enter the Number :"))
    if a=="q" or a=="Q":
        break
    try:
        if a>6:
            print(f"{a} is greater then 6")
    except Exception as e:
        print(e)