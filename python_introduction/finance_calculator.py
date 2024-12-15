# finance_calculator.py

# Prompting the user for input
monthly_income = float(input("Enter your monthly income: "))  # User input for monthly income
monthly_expenses = float(input("Enter your total monthly expenses: "))  # User input for monthly expenses

# Calculating monthly savings
monthly_savings = monthly_income - monthly_expenses

# Calculating projected savings after one year with 5% interest
projected_annual_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)

# Displaying the results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings:.2f}.")

