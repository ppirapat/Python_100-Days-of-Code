# Import Built-in "random" Package for random number generator 
import random

# Create list of string
RPS = ['Rock', 'Paper', 'Scissors']

# Input of your choice and computer choice.
User_RPS = int(input("What do you choose? Type 0 for Rock, Type 1 for Paper, Type 2 for Scissors. \n"))
PC_RPS = random.randint(0,2)

# Output computer choice using List index RPS[int]
print(f"Computer chose:\n{RPS[PC_RPS]}")

# Rock Paper Scissors Game Logic
if User_RPS >= 3 or User_RPS < 0:
    print("You typed an invalid number, you lose!")
else:
    if User_RPS == PC_RPS:
        print("It's a draw.")
    elif User_RPS == 0 and PC_RPS == 1:
        print("You lose!")
    elif User_RPS == 0 and PC_RPS == 2:
        print("You win!")
    elif User_RPS == 1 and PC_RPS == 0:
        print("You win!")
    elif User_RPS == 1 and PC_RPS == 2:
        print("You lose!")
    elif User_RPS == 2 and PC_RPS == 0:
        print("You lose!")
    elif User_RPS == 2 and PC_RPS == 1:
        print("You win!")
