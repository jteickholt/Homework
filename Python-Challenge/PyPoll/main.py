
import os
import csv

# Define the path to the data within the Resources folder

election_csv = os.path.join('..','..', '..', 'RU-HOU-DATA-PT-09-2019-U-C', 'Homework', '03-Python', 'Instructions', 'Pypoll', 'Resources','election_data.csv')

# define a candidate list and a vote list and a list count that will hold the # of items in list

candlist=[]
votelist=[]
listcount=1

# Read in the CSV file
with open(election_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
   
   #for the first row, I will append the candidates name to the list and append 1 vote to the votelist
    
    for row in csvreader:
        rownum=csvreader.line_num
        if rownum==2:
            candlist.append(row[2])
            votelist.append(1)

        #for other rows, I first check to see if the current candidate is already on the list
        #if they are, I add a vote
        #if they are note, I append the name to the candidate list and append 1 to the votelist

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


# I then add up the number of votes across the candidates

totalvotes=0

for i in range(len(votelist)):
    totalvotes = totalvotes + int(votelist[i])

#I also define the percentage of votes for each candidate

percvote=[]
percvotei=0.000
for i in range(len(votelist)):
    percvotei=round((float(votelist[i])/totalvotes)*100 , 3)
    percvote.append(percvotei)


# sort the candidates by number of votes.  they are already in the correct order in our data,
# but this code would fix it if they weren't

candlist, votelist=zip(*sorted(zip(candlist,votelist), key=lambda pair: pair[1], reverse=True))

#print results in desired format

print()
print("Election Results")
print()
print("_"*20)
print()
print(f"Total Votes: {totalvotes}")
print("_"*20)
print()

for i in range(len(candlist)): 
    print(f"{candlist[i]} : {percvote[i]}% ({votelist[i]})")
print()
print("_"*20)
print()
print(f"Winner: {candlist[0]}")
print()
print("_"*20)

#change the standard output to print to a text file
#print results in desired format

import sys

# f=open('.\pybank.txt', 'w')

f=open('.\pypollresults.txt', 'w')
std=sys.stdout
sys.stdout=f

#print output
print()
print("Election Results")
print()
print("_"*20)
print()
print(f"Total Votes: {totalvotes}")
print("_"*20)
print()

for i in range(len(candlist)): 
    print(f"{candlist[i]} : {percvote[i]}% ({votelist[i]})")
print()
print("_"*20)
print()
print(f"Winner: {candlist[0]}")
print()
print("_"*20)

#make sure to close the file and change the standard output back to the screeen

f.close()
sys.stdout=std







        
            



     


