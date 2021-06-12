import random
randomNumber= random.randint(1,100)
userNumber = None
gusses = 0

while (userNumber != randomNumber):
    userNumber=int(input("Enter The Number :"))
    if userNumber>randomNumber:
        print("Smaller Number, Please!")
    elif userNumber<randomNumber:
        print("Bigger Number Please")
    gusses+=1
        
print(f"You reached to the correct answer in {gusses} attemts.")
print(f"congratulation ! You got the right choice = {randomNumber} ")
