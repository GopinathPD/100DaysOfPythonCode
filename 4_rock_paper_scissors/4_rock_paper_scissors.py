rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Rock wins against scissors.  0 > 2
#Scissors win against paper.  2 > 1
#Paper wins against rock.  1 > 0

#Import Random module
import random
options = [rock, paper, scissors]

#Get the user input and validate
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if user_choice >= 3 or user_choice < 0:
  print("This is not a valid choice..!!")

#Generate Computer input randomly
comp_choice = random.randint(0,2)

#Print static messages
print(options[user_choice])
print("Computer chose:")
print(options[comp_choice])

#Game Logic
if user_choice == comp_choice:
  print("It's a draw")
elif (user_choice == 0 and comp_choice == 2) or (user_choice == 1 and comp_choice == 0) or (user_choice == 2 and comp_choice == 1):
  print("You win!")
elif (user_choice == 0 and comp_choice == 1) or (user_choice == 1 and comp_choice == 2) or (user_choice == 2 and comp_choice == 0):
  print("You Lose")

