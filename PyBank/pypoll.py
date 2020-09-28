import os

import csv

csvpath = os.path.join('PyPoll.csv')

#lists to store data
votes = []
candidates = []
candidate_vote_count = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader) 

    csv_header = next(csvreader)

    print(f"CSV Header: {csv_header}")


    for row in csvreader:
        #Add voters
        votes.append(row[0])

        #Add candidates
        candidates.append(row[2])


    #calculate number of votes
    print ("Number of unique votes = " + str(len(votes)))


# function to get unique values 
def unique(candidates): 
      
    # insert the list to the set 
    list_set = set(candidates) 
    # convert the set to the list 
    unique_list = (list(list_set)) 
    for x in unique_list: 
        print (x)

    unique(candidates)

while candidates == "Correy":

print (len(votes))

while candidates == "Khan":

print (len(votes))

while candidates == "O'Tooley":

print (len(votes))

while candidates == "Li":

print (len(votes))














