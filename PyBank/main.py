# Import data from csv file
import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

PnL = 0
months = 0
maximum = 0
max_month = ""
minimum = 100000000
min_month = ""
previous = 0
sum = 0

with open(csvpath, newline="") as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

# Read each row of data after the header
    for row in csvreader:
 
# The total number of months included in the dataset
        months +=1

# The net total amount of "Profit/Losses" over the entire period
        PnL +=int(row[1])

# The average of the changes in "Profit/Losses" over the entire period
        change = int(row[1]) - previous
        previous = int(row[1])
        if months > 1:
                sum = sum + change

# The greatest increase in profits (date and amount) over the entire period
        if change > maximum:
                maximum = change
                max_month = row[0]

# The greatest decrease in losses (date and amount) over the entire period
        if change < minimum:
                minimum = change
                min_month = row[0]

average = sum/(months - 1)

print("Financial Analysis")
print("-" * 30)
print("Total months: " + str(months))
print("Total: $" + str(PnL))
print("Average change: $" + "{:.2f}".format(average))
print("Greatest increase in profits: " + str(max_month) + " ($" + str(maximum) + ")")
print("Greatest decrease in profits: " + str(min_month) + " ($" + str(minimum) + ")")

output = os.path.join("..", "PyBank", "PyBankOut.txt")
with open(output, 'w') as file:
        file.write("Financial Analysis\n")
        file.write("-" * 30 + "\n")
        file.write("Total months: " + str(months) + "\n")
        file.write("Total: $" + str(PnL) + "\n")
        file.write("Total: $" + str(PnL) + "\n")
        file.write("Average change: $" + "{:.2f}".format(average) + "\n")
        file.write("Greatest increase in profits: " + str(max_month) + " ($" + str(maximum) + ")" + "\n")
        file.write("Greatest decrease in profits: " + str(min_month) + " ($" + str(minimum) + ")")