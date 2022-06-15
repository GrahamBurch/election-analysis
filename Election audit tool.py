#The data that needs to be retrieved.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won. 
#4. The total number of votes each candidate won.
#5. The winner of the election based on popular vote.

import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Initialize candidate list
candidate_options = []

# Declare empty dictionary for vote counts
candidate_votes = {}

# Initialize a total vote counter
total_votes = 0

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    ## Read and analyze data
    # First, Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and print the header row
    headers = next(file_reader)
    
    # Print each row of the CSV file
    for row in file_reader:
        # Increment total votes
        total_votes += 1

        candidate_name = row[2]

        if candidate_name not in candidate_options:
            # Add candidate's name to candidate list
            candidate_options.append(candidate_name)
            # Start tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's vote count
        candidate_votes[candidate_name] += 1

        # Write the results to our text file
with open(file_to_save, "w") as txt_file:
        # Print the final count to the terminal.
    election_results = (
                f"\nElection Results\n"
                f"-----------------------\n"
                f"Total votes: {total_votes:,}\n"
                f"-----------------------\n"
            )
            
    print(election_results, end="")
            # Save that final vote count to the text file.
    txt_file.write(election_results)

        # Find the percentage of votes for each candidate by looping through the counts.
        # 1. Iterate through the candidate list
    for candidate_name in candidate_votes:
                    # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
                    # 3. Calculate vote percentages
        vote_percentage = float(votes) / float(total_votes) * 100
                    # 4. Print the candidate name and their percentage of votes.
        candidate_results = (f"{candidate_name}: received {vote_percentage:.1f}% or ({votes:,}).\n")

        # Print each candidate, their voter count and percentage to the terminal
        print(candidate_results)
                # TO DO: Print out each candidate's name, vote count and percentage of votes to the terminal.
                #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Save the candidate results to our text file
        txt_file.write(candidate_results)

                # Determine winning vote count and candidate.
                #Determine if the votes for a candidate is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
                    # If true, then set winning_count equal to votes and winning_percent equal to vote_percentage
                    winning_count = votes
                    winning_percentage = vote_percentage
                    # Set the winning_candidate equal to the candidate's name.
                    winning_candidate = candidate_name

    winning_candidate_summary = (
                f"-------------------------\n"
                f"Winner: {winning_candidate}\n"
                f"Winning Vote Count: {winning_count:,}\n"
                f"Total votes: {total_votes:,}\n"
                f"Winning Percentage: {winning_percentage:.1f}%\n"
                f"--------------------------\n")
    print(winning_candidate_summary)

    # Save winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)