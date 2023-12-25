alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 
'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):

    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
        
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)            
            new_position = (position + shift_amount) % 26
            end_text += alphabet[new_position]
        else:
            end_text += letter

    print(f"Here's the {cipher_direction}d result: {end_text}")

#Import and print the logo from art.py when the program starts.
from art import logo
print(logo)

#Can you figure out a way to ask the user if they want to restart the 
cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and 
call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if 
the user types 'yes'. 

game_continue = True
while game_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to 
decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))  #If the user enters a 
shift number with multiples of 26, the program will return the same result 
for encoded and decoded texts.
    caesar(start_text=text, shift_amount=shift, 
cipher_direction=direction)

    #Ask the user for the game continution
    game_continue_input = input("Do you want to continue? Type 'yes' or 
'no':\n")
    if game_continue_input.lower() != "yes":
        game_continue = False
        print("Goodbye")



    
