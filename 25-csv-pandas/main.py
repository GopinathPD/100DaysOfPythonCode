# with open("weather_data.csv") as file:
#     weather_data = file.readlines()

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

# import pandas

# data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
# # avg_temp = sum(temp_list) / len(temp_list)
# # print(avg_temp)
#
# avg_temp = data["temp"].mean()
# max_temp = data["temp"].max()
# print(max_temp)
#
# # Get the data in columns
# print(data["temp"])
#
# # Get the data in row
# print(data[data.day == "Monday"])
#
# # Get the row with max temperature
# max_temp = data["temp"].max()
# print(data[data.temp == max_temp])
#
# # Get the Monday's temperature in Fahrenheit
# monday_temp = int(data[data.day == "Monday"]["temp"][0])
# monday_temp_fahrenheit = (monday_temp * (9/5)) + 32
# print(monday_temp_fahrenheit)
#
# # Create a dataframe from scratch
# data_dact = {
#     "students": ["Gopi", "Mohan", "Raja"],
#     "scores": [75, 85, 95]
# }
# data = pandas.DataFrame(data_dact)
# data.to_csv("new_data.csv")

import pandas as pd
raw_data = pd.read_csv("squirrel-data.csv")
fur_color = raw_data["Primary Fur Color"]
unique_color = fur_color.unique()[1:].tolist()
fur_count = []
for color in unique_color:
    count = 0
    for row in fur_color:
        if row == color:
            count += 1
    fur_count.append(count)

# Create new data frame
new_data = {
    "Fur Color": unique_color,
    "Count": fur_count
}

# Save as csv file
new_data_csv = pd.DataFrame(new_data)
new_data_csv.to_csv("fur_count.csv")
