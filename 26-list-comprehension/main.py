# Standard way
import pandas

list = [1, 2, 3]
new_list = []
for n in list:
    add_1 = n + 1
    new_list.append(add_1)

print(new_list)

# list comprehension way
new_list2 = [n + 2 for n in list]
print(new_list2)

name = "Gopinath"
name_list = [char for char in name]
print(name_list)

# conditional list comprehension
# new_list = [new_item for item in list if test]


# Dictionary comprehension
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key, value) in dict.items()}

# Loop through rows of a data frame
student_data = {
    'student': ['Gopi', 'Raja', 'Mohan'],
    'score': [95, 89, 92]
}

student_dataframe = pandas.DataFrame(student_data)
print(student_dataframe)

for (index, row) in student_dataframe.iterrows():
    print(row)