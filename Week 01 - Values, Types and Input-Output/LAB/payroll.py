"""Calculate and print an employee payroll statement."""

employee_name = input("Employee name: ")
hours_worked = float(input("Hours worked: "))
hourly_rate = float(input("Hourly rate (£): "))
federal_tax_rate = float(input("Federal tax rate (%): "))
state_tax_rate = float(input("State tax rate (%): "))

gross_pay = hours_worked * hourly_rate
federal_withholding = gross_pay * federal_tax_rate / 100
state_withholding = gross_pay * state_tax_rate / 100
net_pay = gross_pay - federal_withholding - state_withholding

print(f"Employee: {employee_name}")
print(f"Gross pay: £{gross_pay:.2f}")
print(f"Federal withholding: £{federal_withholding:.2f}")
print(f"State withholding: £{state_withholding:.2f}")
print(f"Net pay: £{net_pay:.2f}")
