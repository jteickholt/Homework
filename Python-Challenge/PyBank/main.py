import os
import csv

# Define the path to the data within the Resources folder

budget_csv = os.path.join('..','..', '..', 'RU-HOU-DATA-PT-09-2019-U-C', 'Homework', '03-Python', 'Instructions', 'Pybank', 'Resources','budget_data.csv')

#define several variable and set initial values

total=0
nomonths=0
change=0
rownum=0
numpos=0
poschange=0
avgchange=0.0
totchange=0
greatinc=0
incmonth=''
greatdec=0
decmonth=''


# Read in the CSV file

with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheaer = next(csvreader)

    for row in csvreader:
        #create variables to hold total P/L and total number of months.  Also define rownum to more simply
        #refer to the row for use later
        total=total + float(row[1])
        nomonths=nomonths+1
        rownum=csvreader.line_num
        #for first row, there is not previous P/L
        if rownum==2:
            prevpl=0
        #for other rows, defind the change in P/L and accumulate the total change
        # Also test to to see if the row contains a bigger increase or decease than previous
        # which then store the increase/decrease and the month-yr    
        else:
            change=int(row[1])-prevpl
            totchange=totchange + change
            if change>0 and change>greatinc:
                incmonth=row[0]
                greatinc=change
            if change<0 and change<greatdec:
                decmonth=row[0]
                greatdec=change
        #set the previous P/L to be used in next loop
        prevpl=int(row[1])

       
#average change is total change divided by months -1 since there is no change in the first month       
avgchange=round(totchange/(nomonths - 1),2)

# print the results in the desired format

print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {nomonths}")
print(f"Total: ${total}")
print(f"Average Change: ${avgchange}")
print(f"Greatest Increase in Profits: {incmonth} (${greatinc})")
print(f"Greatest Decrease in Profits: {decmonth} (${greatdec})")

#change the standard output to a text file and
# print the results in the desired format

import sys

# f=open('.\pybank.txt', 'w')

f=open('.\pybankresults.txt', 'w')
std=sys.stdout
sys.stdout=f

print()
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {nomonths}")
print(f"Total: ${total}")
print(f"Average Change: ${avgchange}")
print(f"Greatest Increase in Profits: {incmonth} (${greatinc})")
print(f"Greatest Decrease in Profits: {decmonth} (${greatdec})")

#make sure to close the file and change the standar output back to the screeen
f.close()
sys.stdout=std






    

        







    











