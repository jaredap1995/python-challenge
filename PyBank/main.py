import csv
import numpy as np

filepath="/Users/jaredperez/python-challenge/PyBank/budget_data.csv"

total_months=0
net_total=0
values=[]



with open(filepath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        values.append(row)
        # Increment the total number of months
        total_months += 1

        # Add the profit/loss amount to the net total
        net_total += int(row[1])

values=np.asarray(values)
months=values[:,0]

flat=[int(i) for i in values[:,1]]
flat=np.asarray(flat)
flat=np.diff(flat)

month_1=np.argmax(flat)
month_2=np.argmin(flat)

argmax=months[month_1+1]
argmin=months[month_2+1]

average_change=np.mean(flat)
max_change=np.max(flat)
min_change=np.min(flat)

# Print the results
print("Total Months: ", total_months)
print("Net Total Profit/Loss: $", net_total)
print("Average Change: ", average_change)
print('Max Change in Profits: ', argmax, max_change)
print("Min Change in Profits: ", argmin, min_change)

f=open("output.txt", "w")
print("Total Months: ", total_months, file=f)
print("Net Total Profit/Loss: $", net_total, file=f)
print("Average Change: ", average_change, file=f)
print('Max Change in Profits: ', argmax, max_change, file=f)
print("Min Change in Profits: ", argmin, min_change, file=f)