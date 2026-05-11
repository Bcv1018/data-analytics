# Unpacking sales perormance list using for loop

# Total sales before addition
total_sales = 0

# List of sales performance
sales_data = [
 ('Marcus Webb', 'East', 4250.00),
 ('Priya Sharma', 'West', 5875.50),
 ('DeShawn Carter', 'East', 3100.75),
 ('LaTonya Rivers', 'South', 6420.00),
 ('Bob Nguyen', 'West', 4980.25),
]
 
# For loop to unpack sales performance list, highlight top performers, and give total sales overall
for name, region, sales in sales_data:
    total_sales += sales + sales
    print(f"\n{name} ({region}): {sales:.2f}")
    if sales > 5000:
        print(f"^ Top performer!")
        print(f"Total Sales: ${total_sales}")
    