import pandas


# TODO 1. Create a dictionary in this format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
wrong_input = True
while wrong_input:
    user_input = input("Enter a word: ").upper()
    try:
        phonetics_list = [data_dict[char] for char in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(phonetics_list)
        wrong_input = False
