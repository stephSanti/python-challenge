import csv

total_votes = 0
list_canidates = " "
percent_vote = 0
total_canidate_vote = 0
election_winner = " "
canidates = { } #empty dictionary to store canidate name and vote count

file_path = 'C:/Users/Madelyn Zelaya/Desktop/Starter_Code/PyPoll/Resources/election_data.csv'

with open(file_path, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # skip header row
    for row in reader:
        total_votes += 1 #increments total votes for each row
        canidate = row[2]

        if canidate in canidates:
            canidates[canidate] += 1
        else:
            canidates[canidate] = 1
print(" Election Results " )
print('------------------------')
print(f'Total Votes: {total_votes}')
print('------------------------')
election_winner = max(canidates, key = canidates.get) # Get Election Winner

for canidate, votes in canidates.items():
    percent_vote = (votes / total_votes) * 100
    print(f'{canidate}: {percent_vote:.2f}% ({votes})')
print('------------------------')
print(f'Winner: {election_winner}')
print('------------------------')

#Export to text
with open('election_data.txt', 'w') as f:
    f.write("Election Results\n")
    f.write('------------------------\n')
    f.write(f'Total Votes: {total_votes}\n')
    f.write('------------------------\n')
    election_winner = max(canidates, key = canidates.get) # Get Election Winner

    for canidate, votes in canidates.items():
        percent_vote = (votes / total_votes) * 100
        f.write(f'{canidate}: {percent_vote:.2f}% ({votes})\n')
        f.write('------------------------\n')

    f.write(f'Winner: {election_winner}\n')
    f.write('------------------------\n')
