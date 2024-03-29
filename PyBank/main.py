# Import os module that has functions to interact with the file system
import os

# Import module for reading CSV files
import csv

#Append file directory and make a complete file path
csvpath = os.path.join("Downloads","Instructions 6","PyBank", "Resources", "budget_data.csv")

#Initialize variables
mcount = 0; total = 0; PreValue = 0; Diff = 0; DiffMax = 0; DiffMin = 0

#Open and read CSV file
with open(csvpath, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     csv_header = next(csvreader)
     print(f'Financial Analysis'+'\n')
     print(f'----------------------------'+'\n')
     for i in csvreader:
         month = i[0]
         Amount = i[1]
         iAmount = int(Amount)
         Diff =  iAmount - PreValue

#Placeholder to track greatest increase in profits 
         if DiffMax < Diff:
            DiffMax = Diff
            DiffMaxDate = month

#Placeholder to track greatest decrease in profits 
         if DiffMin > Diff:
            DiffMin = Diff
            DiffMinDate = month
            PreValue = iAmount 

# Get total months 
         mcount = mcount + 1
         total += int(Amount) 
 
#The total number of months included in the dataset
print(f'Total Months : {mcount}')

#The total net amount of "Profit/Losses" over the entire period
print(f'Total: $ {total}')

# Greatest increase in profit
print(f'Greatest Increase in Profits: {DiffMaxDate} : ($ {DiffMax})')

# Greatest increase in profit
print(f'Greatest Decrease in Profits: {DiffMinDate} : ($ {DiffMin})')