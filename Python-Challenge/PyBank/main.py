import os
import csv

# Define the path to the data within the Resources folder

budget_csv = os.path.join('..','..', '..', 'RU-HOU-DATA-PT-09-2019-U-C', 'Homework', '03-Python', 'Instructions', 'Pybank', 'Resources','budget_data.csv')




# Read in the CSV file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheaer = next(csvreader)

    total=0
    nomonths=0
    for row in csvreader:
        total=total + float(row[1])
        nomonths=nomonths+1

        if nomonths<30:
            print(row)

    print(f"The total P/L is {total} and the number of months is {nomonths}")



    











