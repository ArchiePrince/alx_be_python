print("************************************************************************************")
print("This solution calculates user's monthly savings based on monthly income and expenses")
print("************************************************************************************")


#Receive user's monthly_income and monthly_expenses
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your montly expenses: "))

#calculated monthly savings
monthly_savings = monthly_income - monthly_expenses

#Projected savings achieved within the year with interest (monthly savings x time x rate)
time = 12
rate = 0.05
projected_savings = int(monthly_savings * 12 + (monthly_savings * time * rate))

#Display results of monthly savings and projected savings with interest.
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")