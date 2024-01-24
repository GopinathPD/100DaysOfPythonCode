from tkinter import Tk, Label, Button, Entry
import turtle

# Window, Label, Button, Entry, Text, Spinbox, Scale, Checkbutton, Radiobutton, Listbox
window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
FONT = ("Arial", 24, "bold")
my_label = Label(text="Label", font=FONT)
my_label.grid(row=0, column=0)
my_label.config(padx=50, pady=50)

# Button
def button_clicked():
    new_text = text_input.get()
    my_label.config(text=new_text)


button1 = Button(text="Button", command=button_clicked)
button1.grid(row=1, column=1)

button2 = Button(text="New Button")
button2.grid(row=0, column=2)

# Entry
text_input = Entry(width=10)
text_input.grid(row=2, column=3)


# tim = turtle.Turtle()
# tim.write("Some Text", font=FONT)

window.mainloop()
