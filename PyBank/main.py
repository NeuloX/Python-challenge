import os
import csv
import sys
#variables 
totalamount = 0
monthcount = 0
getprofit = []
getdate = []
change = []
avgchange = 0
maxchange = 0
minchange = 0
# Path to collect data from the Resources folder
budget_csv = os.path.join('budget_data.csv')

#-----------------------Main--------------------------------------------
# Read in the CSV file
with open(budget_csv, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    #skip the titles
    header = next(csvreader)

    # Loop through the data
    for row in csvreader:
        #transfer to function
        #count months 
        monthcount = monthcount + 1 
        #get total amount 
        totalamount = totalamount + int(row[1])
        #store values in array
        getprofit.append(row[1])
        #store dates in array
        getdate.append(row[0])
    #get the changes for each month add to the change variable as array
    for counter in range(len(getprofit)-1):
        change.append(int(getprofit[counter+1]) - int(getprofit[counter]))
    #get changes
    avgchange = sum(change)/(monthcount-1)
    maxchange = max(change)
    minchange = min(change)
    #get date of changes cross reference the date index to the change index
    for datecount in range(len(getdate)-1):
        #look for the index of greatest increase in change
        if maxchange == change[datecount]:
            maxdate = getdate[datecount+1]
        #look fot the index of greates decrease in change
        if minchange == change[datecount]:
            mindate = getdate[datecount+1]
    #show to terminal
    print ("Financial Analysis")
    print ("--------------------------")
    print (f"Total Months: {monthcount}" )
    print (f"Total Amount: {totalamount}")
    print (f"Average  Change: ${round(avgchange,2)}")
    print (f"Greatest Increase in Profits: {maxdate} ${round(maxchange)}")
    print (f"Greatest Decrease in Profits: {mindate} ${round(minchange)}")
    #save to text file
    sys.stdout = open("result.txt", "a")
    print ("Financial Analysis")
    print ("--------------------------")
    print (f"Total Months: {monthcount}" )
    print (f"Total Amount: {totalamount}")
    print (f"Average  Change: ${round(avgchange,2)}")
    print (f"Greatest Increase in Profits: {maxdate} ${round(maxchange)}")
    print (f"Greatest Decrease in Profits: {mindate} ${round(minchange)}")
    sys.stdout.close
