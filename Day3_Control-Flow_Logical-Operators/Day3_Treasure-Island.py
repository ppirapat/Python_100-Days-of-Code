# Output welcome message
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
 
 # Separate input choices to keep the code organised and less error-prone
 ## Note: to use special characters in print statement 
choice1 = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"?\n").lower()
choice2 = input("You've come to a lake. There is an island in the middle of the lake. Type \"swim\" or \"wait\"?\n").lower()
choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()

# Treasure Island Game - Logic
if choice1 == "left":
    choice2
    if choice2 == "wait":
        choice3
        if choice3 == "red": 
            print("It's a room full of fire. Game over.")        
        elif choice3 == "yellow":
            print("You found a treasure! You win!")
        elif choice3 == "blue":
            print("You enter a room full of beasts. Game over.")
        else: 
            print("You chose a door that doesn't exist. Game over.")
    else:
        print("You're attacked by trout. Game over.")
else:
    print("You fell into a hole. Game over.")