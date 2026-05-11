# calculation for gross pay given pay rate and hours worked

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