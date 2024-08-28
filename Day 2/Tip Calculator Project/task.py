print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))


total_with_tip = bill + (bill * tip*.01)

per_person = round(total_with_tip / people, 2)

print("Each person owes $" + str(per_person))