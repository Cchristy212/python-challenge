from cmath import inf
import csv
import os

#Variables
total_months = 0
net_total = 0
prev_month_amount = 0
greatest_increase = 0
increase_month = None
greatest_decrease = inf
decrease_month = None
change_list = []

#Creates a cvs path to the python working window and prints the whole list for profit and months
Filepath = os.path.join("Pybank", "Resources", 'budget_data.csv')
with open (Filepath) as budgetdata:
    data = csv.reader(budgetdata)
    header=next(data)
   
   #Creating the Net total adding up the months and total
    for i, row in enumerate(data):
        total_months += 1
        amount = int(row[1])
        change = amount - prev_month_amount
        if i > 0: change_list.append(change)
        net_total += amount
        if change > greatest_increase:
            greatest_increase = change
            increase_month = row[0]
        elif change < greatest_decrease:
            greatest_decrease = change
            decrease_month = row[0]

        prev_month_amount = amount


#For output
print("Financial Analysis")
print("-----------------------------")
print(f'Total Months: {total_months}')
print(f"Total: ${net_total}")
print(f"Average Change: ${sum(change_list) / len(change_list)}")
print(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})")
print(f"Greats Decrease in Profits: {decrease_month} (${greatest_decrease})")

#output to a txt file
with open("file.txt", "w") as file.write:
    file = open("output.txt","w")
    file.write("Financial Analysis\n")
    file.write("-----------------------------\n")
    file.write(f'Total Months: {total_months}\n')
    file.write(f"Total: ${net_total}\n")
    file.write(f"Average Change: ${sum(change_list) / len(change_list)}\n")
    file.write(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})\n")
    file.write(f"Greats Decrease in Profits: {decrease_month} (${greatest_decrease})\n")
