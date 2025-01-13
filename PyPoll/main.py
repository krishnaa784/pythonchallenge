import csv

# File paths
# File paths
input_file = 'C:/Users/preit/OneDrive/Desktop/pythonchallenge/PyPoll/Resources/election_data.csv'
output_file = 'C:/Users/preit/OneDrive/Desktop/pythonchallenge/PyPoll/election_results.txt'


# Initialize variables
total_votes = 0
candidate_votes = {}

# Read the election data
with open(input_file, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)

    for row in csvreader:
        # Count the total votes
        total_votes += 1
        candidate = row['Candidate']

        # Count votes for each candidate
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Calculate percentages and find the winner
winner = ""
max_votes = 0
results = []

for candidate, votes in candidate_votes.items():
    # Calculate the percentage of votes for each candidate
    percentage = (votes / total_votes) * 100
    results.append(f"{candidate}: {percentage:.1f}% ({votes})")

    # Determine the winner
    if votes > max_votes:
        max_votes = votes
        winner = candidate

# Prepare the output
output = [
    "Election Results",
    "-------------------------",
    f"Total Votes: {total_votes}",
    "-------------------------"
]
output.extend(results)
output.append("-------------------------")
output.append(f"Winner: {winner}")
output.append("-------------------------")

# Print the output
for line in output:
    print(line)

# Save results to a text file
with open(output_file, 'w') as txtfile:
    for line in output:
        txtfile.write(line + "\n")