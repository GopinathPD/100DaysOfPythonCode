# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo

# Introduction messages
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts_left = 0
random_number = random.randint(1, 100)
if difficulty_level.lower() == 'easy':
    attempts_left = 10
elif difficulty_level.lower() == 'hard':
    attempts_left = 5
else:
    print("That's not a valid option..!!/n Please try again..!!")

while attempts_left > 0:
    print(f"You have {attempts_left} attempts remaining to guess")
    guess = int(input("Make a guess: "))
    if guess == random_number:
        print(f"You got it! The answer was {random_number}")
        break
    elif guess > random_number:
        print("Too high.")
    elif guess < random_number:
        print("Too low.")

    attempts_left -= 1
    if attempts_left == 0:
        print("You've run out of guesses, you lose.")
    else:
        print("Guess again.")
