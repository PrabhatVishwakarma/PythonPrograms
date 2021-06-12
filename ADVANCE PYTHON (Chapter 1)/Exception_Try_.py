while(True):
    print("Press Q or q to quit")
    a=int(input("Enter Number :"))
    if a=='q' or a=='Q':
        break
    try:
        if a%2==0 and a%3==0:
           print(f"{a} is Divisible by both 2 and 3")
        elif a%2==0:
            print(f"{a} is Divisble by 2")
        elif a%3==0:
            print(f"{a} is Divided by 3")
        else:
            print("HEY Please return right number")
    except Exception as e:
        print(f'Your Error is - {e}')
    
    

