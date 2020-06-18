from random import randint
computer_choice = randint(1, 3)

rock = 1
paper = 2
scissors = 3

print("Enter player 1's choice: 1 = rock, 2 = paper, 3 = scissors")
player_one = int(input())
print(computer_choice)

if player_one == rock:
    if computer_choice == scissors:
        print("player 1 wins")
    elif computer_choice == paper:
        print("computer wins with paper")
    else:
        print("tie!")
elif player_one == paper:
    if computer_choice == rock:
        print("player 1 wins")
    elif computer_choice == scissors:
        print("computer wins with scissors")
    else:
        print("tie!")
else:
    if computer_choice == paper:
        print("player 1 wins")
    elif computer_choice == rock:
        print("computer wins with rock")
    else:
        print("tie!")
