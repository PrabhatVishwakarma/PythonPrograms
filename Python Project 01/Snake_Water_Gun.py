import random


def game( computer, player):
    
    if computer==player:
        print('TIE !')
    elif computer=='s' and player=='w':
        print('YOU LOSE !')
    elif computer=='s' and player=='g':
        print('YOU WIN !')
    elif computer=='w' and player=='s':
        print('YOU WIN !')
    elif computer=="w" and player=='g':
        print("YOU LOSE !")
    elif computer=="g" and player=='s':
        print('YOU LOSE !')
    elif computer=="g" and player=='w':
        print('YOU WIN !')


print("Snake Water Gun is a simple game that is played . The rules require that competing players use one hand to form one of three shapes at an agreed-upon time. The person that plays the strongest “object” is the winner of the game. ... Water will win from gun , gun will win from snake, snake will win from water.\n If You wana play ?")
name=input("Enter Your Name : ")
print("computer Turn : Snake(s) Water(w) or Gun(g)?")
randNo = random.randint(1, 3)
if randNo == 1:
    computer = 's'
elif randNo == 2:
    computer = 'w'
elif randNo == 3:
    computer = 'g'

print(name,"your turn")
player = input("Snake(s) Water(w) or Gun(g)?\n")

print("")
print(f"Computer Choose :{computer}")
print("")
print(f"You Choose :{player}")
game(computer, player)
