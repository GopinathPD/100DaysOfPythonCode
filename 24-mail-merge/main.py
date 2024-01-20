#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# open the names and put it in a list
names = []
with open("Input/Names/invited_names.txt") as data:
    for name in data.readlines():
        names.append(name.replace("\n", ""))

# open the starting format letter
with open("Input/Letters/starting_letter.txt") as letter_format:
    letter = letter_format.read()

# save the invitation for everyone
for name in names:
    invite_letter = letter.replace("[name]", name)
    # save the invite as separate text file
    with open(f"Output/ReadyToSend/invite_{name}.txt", "w") as file:
        file.write(invite_letter)
