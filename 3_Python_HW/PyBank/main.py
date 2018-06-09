import pandas as pd
import os

budget_data = os.path.join("Resources", "budget_data_1.csv")
df = pd.read_csv(budget_data)

total_months = len(df.axes[0])
total_revenue = df['Revenue'].sum()
avg_revenue = round(df['Revenue'].mean())
greatest_revenue_increase = df.loc[df['Revenue'].idxmax()]
greatest_revenue_decrease = df.loc[df['Revenue'].idxmin()]

f = open('PyBank.txt','w')
f.write("Financial Analysis\n"
"----------------------------\n"
"Total Months: " + str(total_months) + "\n"
"Total Revenue: $" + str(total_revenue) + "\n"
"Average Revenue Change: $" + str(avg_revenue) + "\n"
"Greatest Increase in Revenue: " + greatest_revenue_increase['Date'] + " ($" + str(greatest_revenue_increase['Revenue']) + ")" + "\n"
"Greatest Decrease in Revenue: " + greatest_revenue_decrease['Date'] + " ($" + str(greatest_revenue_decrease['Revenue']) + ")")
f.close()

print("Financial Analysis\n"
"----------------------------\n"
"Total Months: " + str(total_months) + "\n"
"Total Revenue: $" + str(total_revenue) + "\n"
"Average Revenue Change: $" + str(avg_revenue) + "\n"
"Greatest Increase in Revenue: " + greatest_revenue_increase['Date'] + " ($" + str(greatest_revenue_increase['Revenue']) + ")" + "\n"
"Greatest Decrease in Revenue: " + greatest_revenue_decrease['Date'] + " ($" + str(greatest_revenue_decrease['Revenue']) + ")")

