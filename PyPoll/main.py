import csv

# set the file path of the CSV file
csv_file_path = "/Users/jaredperez/Python-Challenge/PyPoll/resources/election_data.csv"

# create a dictionary to store candidate names and their vote counts
candidate_votes = {}

# initialize variables to keep track of the total votes and the winning candidate
total_votes = 0
winning_candidate = ""
winning_votes = 0

# read the CSV file and loop through each row
with open(csv_file_path, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    # skip the header row if there is one
    next(csv_reader, None)
    for row in csv_reader:
        # add 1 to the total vote count for each row
        total_votes += 1
        # get the candidate name from the row
        candidate_name = row[2]
        # check if the candidate is already in the dictionary
        if candidate_name in candidate_votes:
            # add 1 to the candidate's vote count
            candidate_votes[candidate_name] += 1
        else:
            # initialize the candidate's vote count to 1
            candidate_votes[candidate_name] = 1

total_votes
candidate_votes



# print the total number of votes cast
print("Total Votes: " + str(total_votes))

# calculate and print the percentage of votes each candidate won and their total vote count
for candidate in candidate_votes:
    vote_count = candidate_votes[candidate]
    vote_percentage = round((vote_count / total_votes) * 100, 2)
    print(f"{candidate}: {vote_percentage}% ({vote_count})")
# check if the candidate has more votes than the current winning candidate
    if vote_count > winning_votes:
        winning_candidate = candidate
        winning_votes = vote_count

# print the winner of the election based on popular vote
print("Winner: " + winning_candidate)


f=open("output_2.txt", "w")
print("Total Votes: " + str(total_votes), file=f)
print("-------------------------------------------------", file=f)
for candidate in candidate_votes:
    vote_count = candidate_votes[candidate]
    vote_percentage = round((vote_count / total_votes) * 100, 2)
    print(f"{candidate}: {vote_percentage}% ({vote_count})", file=f)
print("---------------------------------------------------", file=f)
print("Winner: " + winning_candidate, file=f)
