import csv
import os

#The total number of votes
total_votes = 0

candidate_selection = []
candidate_votes = {}

#Creates a path to the file in the different folder
Filepath = os.path.join("PyPoll", "Resources", 'election_data.csv')
#Open election data and read the file
with open (Filepath) as election_data:
    #Read the file ojects
    data = csv.reader(election_data)
    #Print header Row
    header=next(data)

    #Each row
    for row in data:
        #total vote count
        total_votes += 1
        #print candidate from each row
        candidate_name =row[2]
        
        #if there is a name that isnt on the list them add
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name]["votes"] += 1
        else:
            candidate_votes[candidate_name] = {"votes": 1, "percent": 0}

winner = ""
winner_votes = 0
winning_percentage = 0
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]["votes"]
    vote_percentage = round(votes / total_votes * 100, 2)
    candidate_votes[candidate_name]["percent"] = vote_percentage

    if votes > winner_votes:
        winner_votes = votes
        winner = candidate_name
        winning_percentage = vote_percentage

print(
    "Election Results\n",
    "------------------\n",
    f"Total Votes: {total_votes}"
)
print("--------------------")
for candidate_name in candidate_votes:
    print(f'{candidate_name}: {candidate_votes[candidate_name]["percent"]}% ({candidate_votes[candidate_name]["votes"]})')
print("--------------------")
print(f'Winner: {winner}')


# export text file of results
output = "output.txt"
with open("output","w") as file:

    file.write (
        f'''Election Results
------------------
Total Votes: {total_votes}\n'''
        )
    file.write("--------------------\n")
    for candidate_name in candidate_votes:
        file.write(f'{candidate_name}: {candidate_votes[candidate_name]["percent"]}% ({candidate_votes[candidate_name]["votes"]})\n')
    file.write("--------------------\n")

    file.write(f'Winner: {winner}')

