#Guess the Number Game

import random

print("Welcome to Bulles and Cows Game")
print("It is Two digit Guessing Game")
secret_number = str(random.randint(10,99))

changes = 7

while changes > 0:
    player_guess = input("Enter the GuessNumber:")
    if(secret_number == player_guess):
        print("Congrats!!! You won the Game")
        break
    else:
        cows = 0
        bulls = 0
        if(secret_number[0] == player_guess[0]):
            bulls +=1
        if(secret_number[1] == player_guess[1]):
            bulls +=1
        if(secret_number[0] == player_guess[1]):
            cows +=1
        if(secret_number[1] == player_guess[0]):
            cows +=1
        print("Bulls :" ,bulls)
        print("Cows :" ,cows)

        changes -=1

        if(changes < 1):
            print("You loss the game")
            print("The Secret Number is:",secret_number)
            break
