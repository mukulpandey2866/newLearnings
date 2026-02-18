"""
🏢 Assignment: Employee Data Management (Using Only input() and print())
✅ PART A: Basic Employee Information
Q1. Employee Introduction Program
Write a program that:
Takes Employee Name
Takes Employee ID
Takes Department Name
Takes Company Name
✅ PART B: Salary Calculation
Q2. Monthly Salary Breakdown
Write a program that:

Takes Basic Salary
Takes HRA
Takes Bonus
Calculate :Gross Salary = Basic Salary + HRA + Bonus
✅ PART C: Annual Salary Calculator
Q3. Annual Package Calculation
Take:
Monthly Salary
Calculate:Annual Salary = Monthly Salary * 12
✅ PART D: Salary Deduction
Q4. Net Salary After Deduction
Take:
Employee Name
Basic Salary
Tax Percentage
Calculate:
Tax Amount = (Basic Salary * Tax Percentage) / 100
Net Salary = Basic Salary - Tax Amount
✅ PART E: Overtime Payment
Q5. Overtime Salary Calculator
Take:
Basic Salary
Overtime Hours
Overtime Rate per Hour
Calculate :
Overtime Pay = Overtime Hours * Overtime Rate
Total Salary = Basic Salary + Overtime Pay
Print complete details of Employee in proper formatted way as per your wish

"""


# Q1. Employee Introduction Program
emp_name = input("Enter Employee name: ")
emp_id = input("Enter emp id: ")
dept_name = input("Enter dept name: ")
comp_name = input("Enter company name: ")
print("Emp name: ", emp_name, "Emp id: ", emp_id, "Dept name: ", dept_name, "Company name: ", comp_name)



# Q2 Monthly Salary Breakdown
basic_sal = float(input("Enter basic sal: "))
hra = float(input("Enter HRA: "))
bonus = float(input("Enter bonus: "))
gross_sal = basic_sal + hra + bonus
print(f" Gross salary is: {gross_sal:.3f}")


# Q3 Annual Package Calculation
monthly_sal = float(input("Enter monthly salary: "))
annual_sal = monthly_sal * 12
print("Annual salary is: %.2f" %(annual_sal))


# Q4. Net Salary After Deduction
emp_name = input("Enter Employee name: ")
basic_sal = float(input("Enter basic salary: "))
tax_perc = float(input("Enter tax percentage: "))
tax_amt = (basic_sal * tax_perc) / 100
net_sal= basic_sal - tax_amt
print("Employee Name: {}, Net Salary: {:.2f}".format(emp_name, net_sal))

# Q5. Overtime Salary Calculator
basic_sal = float(input("Enter basic salary: " ))
overtime_hrs = float(input("Enter overtime hours: "))
overtime_rate = float(input("Enter overtime rate per hour: "))
overtime_pay = overtime_hrs * overtime_rate
total_sal = basic_sal + overtime_pay
print("Total Salary is: {total_sal:.3f}")

