# Guessing Game Python by Rabeel Maroof
# First Project for BS Artificial Intelligence - CSC 2027

import random

print("Welcome to Guessing Game!")
print("AI has selected a number from 1 to 100")
print("You have 7 chances!\n")

secret = random.randint(1, 100)
chances = 7

while chances > 0:
    try:
        guess = int(input(f"Guess the number (Chances left {chances}): "))
        
        if guess == secret:
            print("\nWOW! You Won!")
            print(f"The secret number was: {secret}")
            break
        elif guess < secret:
            print("Too Low! Try a higher number.")
        else:
            print("Too High! Try a lower number.")
        
        chances -= 1
        print(f"Chances left: {chances}\n")

    except:
        print("Oops! Please enter only a number!")

if chances == 0:
    print(f"\nGame Over! The number was {secret}")
    
print("\nThanks for playing! Made by Rabeel Maroof")
