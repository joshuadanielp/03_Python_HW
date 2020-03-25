# Import data from csv file
import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

PnL = 0
months = 0
maximum = 0
minimum = 0
difference = []

with open(csvpath, newline="") as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

# Read each row of data after the header
    for row in csvreader:
        
# The total number of months included in the dataset
        months +=1

# The net total amount of "Profit/Losses" over the entire period
        PnL += int(row[1])
        # print(months)
        # print(PnL)
# The average of the changes in "Profit/Losses" over the entire period
        average = PnL/len(row[1])
        print(average)

# The greatest increase in profits (date and amount) over the entire period


# The greatest decrease in losses (date and amount) over the entire period

