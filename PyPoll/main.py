# Dependencies
import os
import csv

#identify variables and lists
Votes=[]
List=[]
Consol_Candidate=[]

#pull election data
election = os.path.join('Resources','election_data.csv')

with open(election) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    for row in csvreader:      
        VoterID=row[0]
        County=row[1]
        Candidate=row[2]
        Votes.append(VoterID)
        List.append(Candidate)

print(f'Election Results')

print(f'------------------------')

#sum votes
TotalVotes=len(Votes)
print(f"Total Votes: " + str(TotalVotes))

print(f'------------------------')

#create a dictionary from candidate list
from collections import Counter
a= List
d= dict(Counter(a))

#loop through list to sum unique names (candidates) to get total numbers (votes)
for names, numbers in d.items():
    print(names,":", round(numbers/TotalVotes*100,3), "% (", numbers, ")")
    

#find winner
Winner=max(set(List),key=List.count)
print(f'------------------------')
print(f'Winner: ' + str(Winner))

# Specify the file to write to
output = os.path.join("analysis", "election_output.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow([f'Election Results'])
    csvwriter.writerow([f'------------------------'])
    csvwriter.writerow([f"Total Votes: " + str(TotalVotes)])
    csvwriter.writerow([f'------------------------'])
    for names, numbers in d.items():
        csvwriter.writerow([names + ": " + str(round(numbers/TotalVotes*100,3)) + "% (" + str(numbers) + ")"])
    csvwriter.writerow([f'------------------------'])
    csvwriter.writerow([f'Winner: ' + str(Winner)])