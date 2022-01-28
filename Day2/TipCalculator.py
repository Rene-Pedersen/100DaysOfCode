# This is the final project of day 2, a tip calculator
print("Welcome to the tip calculator.")

bill = float(input("What was the toal bill? $"))
tip_percentage = (int(input("What percentage tip would you like to give? "
                             "10, 12 or 15? "))) / 100 + 1
num_people = int(input("How many people to split the bill? "))
each_to_pay = round((bill * tip_percentage) / num_people, 2)

print(f"Each person should pay: ${each_to_pay:.2f}")




