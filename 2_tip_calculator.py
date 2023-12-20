#Welcome Message
print("Welcome to the tip calculator.")

#Get the input of total bill
total_bill = float(input("What was the total bill? $"))

#Get the input of tip percentage
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

#Get the input of number of people
people_split = int(input("How many people to split the bill? "))

#Calculate the tip amount
people_share = (total_bill / people_split) * (1 + tip_percentage / 100)
people_share_rounded = round(people_share, 2)

#Print the result
print("Each person should pay: $" + str(people_share_rounded))
