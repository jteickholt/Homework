
import os
import csv

# Define the path to the data within the Resources folder

election_csv = os.path.join('..','..', '..', 'RU-HOU-DATA-PT-09-2019-U-C', 'Homework', '03-Python', 'Instructions', 'Pypoll', 'Resources','election_data.csv')



# Read in the CSV file
with open(election_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheaer = next(csvreader)
    
    for row in csvreader:
        rownum=csvreader.line_num
        if rownum<10:
            print(row)


  