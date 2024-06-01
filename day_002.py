print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
tip = float(input("What percentage tip would you like to give? (10%, 12%, 15%)"))
people = int(input("How many people to split the bill? "))
tip_percent = tip / 100
total_tip_amount = bill * tip_percent
total_bill = round((bill + total_tip_amount) / people, 2)
print(f"Each person should pay {total_bill:.2f}€")
