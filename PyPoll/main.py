# Import data from csv file
import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

votes = 0
candidates = {}

with open(csvpath, newline="") as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
 
# The total number of votes cast
        votes +=1

# A complete list of candidates who received votes
        if row[2] not in candidates:
                candidates[row[2]] = 0
        else:
                candidates[row[2]] = candidates[row[2]] + 1

print("Election Results")
print("-" * 30)
print("Total Votes: " + str(votes))
print("-" * 30)

# The percentage of votes each candidate won
# The total number of votes each candidate won

total = sum(candidates.values())

for name, vote in candidates.items():
         pct = vote * 100 / total
         pct_round = round(pct,3)
         print(str(name) + ": " + str(pct_round) + "% " + "(" + str(vote) + ")")

# The winner of the election based on popular vote.
def winner():
        v = list(candidates.values())
        k = list(candidates.key())
        return k[v.index(max(v))]

print("-" * 30)
print("Winner: ")
print("-" * 30)



# Loop through the dictionary, print out the key (name) and the value (count)


# output = os.path.join("..", "PyPoll", "PyPollOut.txt")
# with open(output, 'w') as file:
#         file.write("Election Results\n")
#         file.write("-" * 30 + "\n")
#         file.write("Total months: " + str(months) + "\n")
#         file.write("Total: $" + str(PnL) + "\n")
#         file.write("Total: $" + str(PnL) + "\n")
#         file.write("Average change: $" + "{:.2f}".format(average) + "\n")
#         file.write("Greatest increase in profits: " + str(max_month) + " ($" + str(maximum) + ")" + "\n")
#         file.write("Greatest decrease in profits: " + str(min_month) + " ($" + str(minimum) + ")")