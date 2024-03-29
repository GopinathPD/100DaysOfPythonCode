from tkinter import *
from tkinter import messagebox
import random
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = 8
    nr_symbols = 2
    nr_numbers = 2

    # Eazy Level - Order not randomised:
    # e.g. 4 letter, 2 symbol, 2 number = JduE&!91
    pass_letters = []
    pass_letters += [random.choice(letters) for _ in range(0, nr_letters)]
    pass_letters += [random.choice(symbols) for _ in range(0, nr_symbols)]
    pass_letters += [random.choice(numbers) for _ in range(0, nr_numbers)]
    shuffled_pass = ''.join(random.sample(pass_letters, len(pass_letters)))
    password_entry.insert(0, shuffled_pass)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    # Confirm the fields are not empty
    if website == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        # Show the message box and ask for confirmation
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n"
                                                              f"Email: {email} \n Password: {password} \n"
                                                              f"Is it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                # Delete the contents
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- Find Password ------------------------------- #
def find_password():
    try:
        with open("data.json", "r") as data_file:
            # Reading old data
            data = json.load(data_file)
            try:
                website = data[website_entry.get()]
                email = website["email"]
                password = website["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\n Password: {password}")
            except KeyError:
                messagebox.showinfo(title="Oops", message="No details for the website exists.")
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No Data File Found.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(120, 100, image=lock_image)
canvas.grid(row=0, column=1)

# Generate Static Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entry Textbox
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)

email_entry = Entry(width=38)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "abc@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Button controls
search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(row=1, column=2)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
