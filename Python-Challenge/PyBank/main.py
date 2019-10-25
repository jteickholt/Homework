import os
import csv

# Define the path to the data within the Resources folder

budget_csv = os.path.join('..','..', '..', 'RU-HOU-DATA-PT-09-2019-U-C', 'Homework', '03-Python', 'Instructions', 'Pybank', 'Resources','budget_data.csv')

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
        total=total + float(row[1])
        nomonths=nomonths+1
        rownum=csvreader.line_num
        if rownum==2:
            prevpl=0
        else:
            change=int(row[1])-prevpl
            totchange=totchange + change
            if change>0 and change>greatinc:
                incmonth=row[0]
                greatinc=change
            if change<0 and change<greatdec:
                decmonth=row[0]
                greatdec=change
    
        prevpl=int(row[1])

        # print(row, change)
        
avgchange=round(totchange/(nomonths - 1),2)

# print(f"The total P/L is {total} and the number of months is {nomonths}")

print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {nomonths}")
print(f"Total: ${total}")
print(f"Average Change: ${avgchange}")
print(f"Greatest Increase in Profits: {incmonth} (${greatinc})")
print(f"Greatest Decrease in Profits: {decmonth} (${greatdec})")

import sys

# f=open('.\pybank.txt', 'w')

f=open('.\practice.txt', 'w')
std=sys.stdout
sys.stdout=f


print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {nomonths}")
print(f"Total: ${total}")
print(f"Average Change: ${avgchange}")
print(f"Greatest Increase in Profits: {incmonth} (${greatinc})")
print(f"Greatest Decrease in Profits: {decmonth} (${greatdec})")

f.close()
sys.stdout=std






    

        







    











