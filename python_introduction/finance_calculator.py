monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
montly_savings = monthly_income - monthly_expenses
string_monthly_savings = str(montly_savings)
projected_savings = str(int(montly_savings * 12 + (montly_savings * 12 * 0.05)))
print("Your monthly savings are $"+string_monthly_savings+".")
print("Projected savings after one year, with interest, is: $"+projected_savings+".")


#Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05))