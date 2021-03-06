# Import OS and CSV
import os 
import csv

# list for the data to go into 
election_list = []

# open the file path 
election_file = os.path.join("Resources", "election_data.csv")

# read the file to begin working with the data
with open(election_file, "r") as csvfile:

    election_reader = csv.reader(csvfile, delimiter=",")

    # skipping the header but putting it in a variable
    header = next(election_reader, None)

    for row in election_reader:
        election_list.append(row)

    # Formatting
    print("Election Results")
    print("---------------------------")

    # Find the total number of votes cast
    total_votes = len(election_list)
    print(f'Total Votes: {total_votes}')

    print("---------------------------")

    # Create a dictionary of candidates who received votes and count their votes
    candidates_votes = {}

    for candidates in election_list:
        if candidates[2] in candidates_votes:
            candidates_votes[candidates[2]] += 1
        else:
            candidates_votes[(candidates[2])] = 1

    # Create another dictionary with candidates and their percentage of votes
    candidates_percent = dict([(key, (value / total_votes) * 100) for key, value in candidates_votes.items()])

    # Find the winner of the election based on popoular vote
    candidate = list(candidates_percent.keys())
    votes = list(candidates_percent.values())
    winner = candidate[votes.index(max(votes))]

    # A final list with both values in it for each candidate
    final_list_candidates = list(candidates_percent.keys())
    final_list_percents = list(candidates_percent.values())
    final_list_votes = list(candidates_votes.values())

    # Print each of the candidates, their percentage of votes, and the number of votes
    i = 0
    for row in final_list_candidates:
        print(f"{final_list_candidates[i]}: {final_list_percents[i]:.2f}% ({final_list_votes[i]})")
        i += 1

    print("---------------------------")

    print(f"Winner: {winner}")

    print("---------------------------")

# file path to write to the analysis file
output_path = os.path.join("Analysis", "PyPoll_output.txt")

# Outputting results to new file
with open(output_path, 'w') as text_file:

    # creating the csv.writer
    csvwriter = csv.writer(csvfile)

    # Outputting all the text into the csv file in the Analysis folder 
    print("Election Results", file = text_file)
    print("---------------------------", file = text_file)

    print(f'Total Votes: {total_votes}', file = text_file)

    print("---------------------------", file = text_file)

    i = 0
    for row in final_list_candidates:
        print(f"{final_list_candidates[i]}: {final_list_percents[i]:.2f}% ({final_list_votes[i]})", file = text_file)
        i += 1

    print("---------------------------", file = text_file)

    print((f"Winner: {winner}"), file = text_file)

    print("---------------------------", file = text_file)
