
import os
import csv

# Define the path to the data within the Resources folder

election_csv = os.path.join('..','..', '..', 'RU-HOU-DATA-PT-09-2019-U-C', 'Homework', '03-Python', 'Instructions', 'Pypoll', 'Resources','election_data.csv')

# define a candidate list and a vote list

candlist=[]
votelist=[]
listcount=1

# Read in the CSV file
with open(election_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
   
    for row in csvreader:
        rownum=csvreader.line_num
        if rownum==2:
            candlist.append(row[2])
            votelist.append(1)
        else:
            inlist = 0
            for i in range(0 , listcount):
                if row[2]==candlist[i]:
                    inlist = 1
                    votelist[i]=int(votelist[i]) + int(1)
            if inlist == 0:    
                candlist.append(row[2])
                votelist.append(1)
                listcount = listcount + 1


totalvotes=0

# Why doesn't the for loop below work?
# for i in votelist: 

for i in range(len(votelist)):
   totalvotes = totalvotes + int(votelist[i])

# sort the candidates by number of votes.  they are already in the correct order
# but this code would fix it if they weren't

candlist, votelist=zip(*sorted(zip(candlist,votelist), key=lambda pair: pair[1], reverse=True))






        
            



     


