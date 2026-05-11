# Calculate federal tax based on annual gross income and filing status

# taxes based on weekly gross income
pay_rate = int(input("What is your pay hourly? "))
hours_worked = int(input("How many hours did you work this week? "))
overtime_hours = float(input("Did you work overtime if so how many hours? "))


if overtime_hours > 0:
    regular_pay = pay_rate * hours_worked
    overtime_rate = pay_rate * 1.5
    overtime_pay = overtime_hours * overtime_rate
    gross_pay = regular_pay + overtime_pay
    reason = "you had overtime and worked over 40 hours"
elif hours_worked == 40:
    gross_pay = pay_rate * hours_worked
    reason = "you worked exactly 40 hours"
elif hours_worked < 40:
    gross_pay = pay_rate * hours_worked
    reason = "you worked under 40 hours"

print(f"""
      \nYour pay rate is ${pay_rate} per hour 
      \nyou worked {(hours_worked + overtime_hours):.0f} hours 
      \nyour gross pay is ${gross_pay:.2f} becuase {reason} 
""")

# taxes based on annual gross income and filing status
annual_gross_pay = (gross_pay * 52)
filing_status = input("Are you filing single or joint? ")


if filing_status == "single":
    if annual_gross_pay < 12000:
        tax_rate = .05
    elif annual_gross_pay < 24999.99:
        tax_rate = .1
    elif annual_gross_pay <= 25000 or 74999.99:
        tax_rate = .15
    else:
        tax_rate = .2

if filing_status == "joint":
    if annual_gross_pay < 12000:
        tax_rate = .0
    elif annual_gross_pay < 24999.99:
        tax_rate = .06
    elif annual_gross_pay <= 25000 or 74999.99:
        tax_rate = .11
    else:
        tax_rate = .2

tax_withheld = gross_pay * tax_rate
net_pay = gross_pay - tax_withheld


print(f"You worked {hours_worked} hours this period")
print(f"Becasue you earn ${pay_rate} per hour, your gross weekly pay is ${gross_pay}")
print(f"Your tax withholding for the week is ${tax_withheld}")
print(f"Your net pay is ${net_pay}")