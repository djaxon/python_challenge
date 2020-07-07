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

# Consol_Candidate=list(set(List))
# print(Consol_Candidate)

from collections import Counter
a = List
c = Counter(a)
print(c)



# candis = dict()
# summaryList=Consol_Candidate
# for i in summaryList:
#     for k in range(0,List[i]):
#         candis.setdefault(sum(k),[]).append(i)
# print(candis)

#for i in range(0,len(List)):
    



#create a dictionary of the candidate list
#dict(Consol)


#add number of votes won and % of vote received to dictionary




#if statement for winner





