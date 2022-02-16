# TIP CALCULATOR PROJECT

print("Welcome to the Tip Calculator!")
total_bill = float(input("What was the total bill? $"))
percentage_chosen = float(input("What Percentage would you like to give? 10, 12 or 15 percent? "))
total_people = float(input("How many people will split the bill? "))
formula = (total_bill / total_people) * (1 + percentage_chosen/100)
rounded_formula = round(formula, 2)

print(f"Each person should pay:  ${rounded_formula}")