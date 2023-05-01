# User to input the name, number of hours worked and the hourly rate
user_name = input("Please enter your name: ")
hours_worked = float(input("Please enter the number of hours worked: "))
hourly_rate = float(input("Please enter the hourly rate: "))

# Calculate the income without taxation deductions
gross_income = hours_worked * hourly_rate

# Define Tax Rate
tax_rate = 0.2  # tax rate for all employees is 20%. In decimal format, 20% is equivalent to 0.20, which is
# simplified to 0.2

# Calculate the income tax deduction
tax_deduction = gross_income * tax_rate

# Define Superannuation rate
super_rate = 0.1  # superannuation rate is fixed at 10% for all employees. In decimal format, 10% is
# equivalent to 0.10 which is simplified to 0.1

# Calculate the superannuation deduction
super_deduction = gross_income * super_rate

# Calculate the net income, that is the income after deduction of tax and superannuation rate
net_income = gross_income - tax_deduction - super_deduction

# Prints the results to the user
print("Employee Income Summary of", user_name)
print(" Total Income without Tax: $", gross_income)
print(" Income Tax Deduction (20%): $", tax_deduction)
print(" Superannuation Deduction (10%): $", super_deduction)
print(" Total Income after deductions: $", net_income)
