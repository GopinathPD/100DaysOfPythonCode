from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

# Add static Labels
label1 = Label(text="Miles")
label1.grid(row=0, column=2)

label2 = Label(text="is equal to")
label2.grid(row=1, column=0)

label3 = Label(text="Km")
label3.grid(row=1, column=2)

# Converted value Label
converted_value = Label(text="0")
converted_value.grid(row=1, column=1)

# Mile Input
mile_input = Entry(width=10)
mile_input.grid(row=0, column=1)


def convert_value():
    km_convert = round(int(mile_input.get()) * 1.60934, 2)
    converted_value.config(text=km_convert)


# Calculate Button
calculate_button = Button(text="Calculate", command=convert_value)
calculate_button.grid(row=2, column=1)

window.mainloop()
