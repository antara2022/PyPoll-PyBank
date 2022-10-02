# Creating a Python script that analyzes the votes and helps a small, rural town modernize its vote-counting process

# Import os module
import os

# Import module for reading CSV files
import csv

# Import collections module
import collections
from collections import Counter

# Lists to store data
candidates = []
votes_cast_per_candidate = []

# create a path to the file
csvpath = os.path.join('Resources', 'election_data.csv')

# Open the CSV
with open(csvpath, encoding='utf') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
    
        candidates.append(row[2])

    # Sort the list in alphabetical order
    list_sorted = sorted(candidates)

    # Count votes received per candidate and add to a list
    candidate_count = Counter (list_sorted)
    votes_cast_per_candidate.append(candidate_count.most_common())

    # Calculate the percentage of votes each candidate won
    for item in votes_cast_per_candidate:

        first = format((item[0][1])*100/(sum(candidate_count.values())),'.3f')
        second = format((item[1][1])*100/(sum(candidate_count.values())),'.3f')
        third = format((item[2][1])*100/(sum(candidate_count.values())),'.3f')

# Print out the analysis to the terminal
print("Election Results")
print("----------------------------")
print(f"Total Votes:  {sum(candidate_count.values())}")
print("-------------------------")
print(f"{votes_cast_per_candidate[0][1][0]}: {second}% ({votes_cast_per_candidate[0][1][1]})")
print(f"{votes_cast_per_candidate[0][0][0]}: {first}% ({votes_cast_per_candidate[0][0][1]})")
print(f"{votes_cast_per_candidate[0][2][0]}: {third}% ({votes_cast_per_candidate[0][2][1]})")
print("-------------------------")
print(f"Winner:  {votes_cast_per_candidate[0][0][0]}")
print("-------------------------")

# Specify the text file to export the results to
election_data_results = os.path.join("analysis", "election_data_results.txt")

# Open the file using the "write" mode and specifiy the variable to hold the contents
with open(election_data_results, 'w') as textfile:

    textfile.write("Election Results\n")
    textfile.write("-------------------------\n")
    textfile.write(f"Total Votes:  {sum(candidate_count.values())}\n")
    textfile.write("-------------------------\n")
    textfile.write(f"{votes_cast_per_candidate[0][1][0]}: {second}% ({votes_cast_per_candidate[0][1][1]})\n")
    textfile.write(f"{votes_cast_per_candidate[0][0][0]}: {first}% ({votes_cast_per_candidate[0][0][1]})\n")
    textfile.write(f"{votes_cast_per_candidate[0][2][0]}: {third}% ({votes_cast_per_candidate[0][2][1]})\n")
    textfile.write("-------------------------\n")
    textfile.write(f"Winner:  {votes_cast_per_candidate[0][0][0]}\n")
    textfile.write("-------------------------\n")