print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# Calculate percentage multiplier (e.g., 12% becomes 1.12)
tip_as_percent = 1 + (tip / 100)
per_person_bill = round((bill / people) * tip_as_percent, 2)

print(f"Each person should pay: ${per_person_bill}")