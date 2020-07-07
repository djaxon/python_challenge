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

#create a set from candidate list

Consol_Candidate=list(set(List))
print(Consol_Candidate)


#create a dictionary of the candidate list



#add number of votes won and % of vote received to dictionary




#if statement for winner





