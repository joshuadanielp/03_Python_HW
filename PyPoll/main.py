# Import data from csv file
import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

votes = 0

def candidates(row):

    with open(csvpath, newline="") as csvfile:

# CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=",")
        csv_header = next(csvreader)

        for row in csvreader:
 
# The total number of votes cast
            votes +=1

# A complete list of candidates who received votes
            candidates.value_counts()

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.

print(str(votes))
print(candidates)