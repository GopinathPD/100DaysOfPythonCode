import random
from art import logo, vs
from game_data import data
from replit import clear

print(logo)

# Generate a random account from the game data.
def random_account(game_data):
    return random.choice(game_data)

# Format account data into printable format.
def format_account(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

# Ask user for a guess.
def ask_user():
    return input("Who has more followers? Type 'A' or 'B': ").lower()

# Check if user is correct.
def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

# Higher Lower Game Logic
def game():
    print("Welcome to the Higher Lower Game!")
    score = 0
    game_over = False
    account_a = random_account(data)
    account_b = random_account(data)
    
    while not game_over:
        account_a = account_b
        account_b = random_account(data)
        while account_a == account_b:
            account_b = random_account(data)

        print(f"Compare A: {format_account(account_a)}")
        print(vs)
        print(f"Against B: {format_account(account_b)}")
        
        guess = ask_user()
        a_followers = account_a["follower_count"]
        b_followers = account_b["follower_count"]
        is_correct = check_answer(guess, a_followers, b_followers)

        clear()
        print(logo)
        
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            game_over = True
            print(f"Sorry, that's wrong. Final score: {score}")
        
# Initiate the Game
game()
