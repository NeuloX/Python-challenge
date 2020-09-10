import os
import sys
import csv

totalvotes = 0.0
khantotal = 0.0
kper = 0.0
correytotal = 0.0
cper = 0.0
litotal = 0.0
lper = 0.0
otoototal = 0.0 
otper = 0.0
votelist = []


#data file path
votes = os.path.join("election_data.csv")
#open file for reading 
with open(votes,"r") as votecsv:
    csvreader = csv.reader(votecsv, delimiter=",")
    header = next(csvreader)
    #count total votes for each candidates
    for row in csvreader:
        totalvotes = totalvotes + 1
        if row[2] == "Khan":
            khantotal = khantotal + 1
        elif row[2] == "Correy":
            correytotal= correytotal + 1
        elif row[2] == "Li":
            litotal = litotal + 1
        else:
            otoototal = otoototal + 1
    #get the pecentage of each totals
    kper = (khantotal/totalvotes)*100
    votelist.append(kper)
    cper = (correytotal/totalvotes)*100
    votelist.append(cper)
    lper = (litotal/totalvotes)*100
    votelist.append(lper)
    otper = (otoototal/totalvotes)*100
    votelist.append(otper)
    #get winner
    maxvote = max(votelist)
    #check who won
    if maxvote == kper:
        winner ="Khan"
    elif maxvote == cper:
        winner = "Correy"
    elif maxvote == lper:
        winner = "Li"
    else:
        winner = "O'Tooley"



    #print output
    #format(variable,".3f") displays the float variable into 3 decimal places
    print("Election Results")
    print(f"Total Votes: {totalvotes}")
    print("---------------------------")
    print(f"Khan: {format(kper,'.3f')}% ({khantotal})")
    print(f"Correy: {format(cper,'.3f')}% ({correytotal})")
    print(f"Li: {format(lper,'.3f')}% ({litotal})")
    print(f"O'Tooley: {format(otper,'.3f')}% ({otoototal})")
    print("---------------------------")
    print(f"Winner: {winner}")
    print("---------------------------")
    #print to text file
    sys.stdout = open("result.txt", "a")
    print("Election Results")
    print(f"Total Votes: {totalvotes}")
    print("---------------------------")
    print(f"Khan: {format(kper,'.3f')}% ({khantotal})")
    print(f"Correy: {format(cper,'.3f')}% ({correytotal})")
    print(f"Li: {format(lper,'.3f')}% ({litotal})")
    print(f"O'Tooley: {format(otper,'.3f')}% ({otoototal})")
    print("---------------------------")
    print(f"Winner: {winner}")
    print("---------------------------")
    sys.stdout.close