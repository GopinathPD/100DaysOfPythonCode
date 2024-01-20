# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# mode will be read by default, w for write (replaces the existing text), a for append
with open("../../../../../new_file.txt", mode="w") as file:
    file.write("New text3.")
