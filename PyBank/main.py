import os
import csv
#variables 
totalamount = 0
monthcount = 0
# Path to collect data from the Resources folder
budget_csv = os.path.join('budget_data.csv')

#-----------------------Main--------------------------------------------
# Read in the CSV file
with open(budget_csv, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    header = next(csvreader)

    # Loop through the data
    for row in csvreader:
        #transfer to function
        #count months 
        monthcount = monthcount + 1 
        totalamount = totalamount + int(row[1])
        
    
    print ("Financial Analysis")
    print ("--------------------------")
    print (f"Total Months: {monthcount}" )
    print (f"Total Amount: {totalamount}")


