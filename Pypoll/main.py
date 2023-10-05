import csv

total_votes = 0
list_canidates = " "
percent_vote = 0
total_canidate_vote = 0
election_winner = " "
canidates = set() #empty set to store
# Replace with the actual path of your extracted CSV file
file_path = 'C:/Users/Madelyn Zelaya/Desktop/Starter_Code/PyPoll/Resources/election_data.csv'

with open(file_path, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # skip header row
    for row in reader:
        total_votes += 1 #increments total votes for each row
        canidate = row[2]
        canidates.add(canidate)
        ###
print(f'Total Votes: {total_votes}')
print(f'List of Canidates: {canidates}')