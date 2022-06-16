# election-analysis

## Overview
A Colorado Board of Elections has asked us to certify a recent election. There are 5 key pieces of information to collect:
  1) The total number of votes cast in the election.
  2) A complete list of candidates who received a vote.
  3) The percentage of the total votes held by each candidate respectively.
  4) The total number of votes held by each candidate.
  5) The final winner of the election.

These final outcomes should then be written to the text file 'election_analysis.txt'. 

## Resources
-- voting data: election_results.csv
-- software: Python 3.8.2 and CSV 1.68.1.

## Summary 
Our analysis showed that:
  1) Using the code:
     for row in file_reader:
        total_votes += 1
     There were 369,711 total votes.
     
  2) Using the code:
  
   candidate_name = row[2]
   
   if candidate_name not in candidate_options:
   
       candidate_options.append(candidate_name)
       
       candidate_votes[candidate_name] = 0
       
   candidate_votes[candidate_name] += 1
   
   The 3 candidates which received votes were: Charles Casper Stockham, Raymon Anthony Doane and Diana DeGette.
   
  3) Using the code:
  
   for candidate_name in candidate_votes:
   
       votes = candidate_votes[candidate_name]
       
       vote_percentage = float(votes) / float(toatl_votes) * 100
       
       candidate_results = (f"{candidate_name}: received {vote_percentage:.1f}% or ({votes:,}).\n")
       
       print(candidate_results)
       
   We find that:
   
   Stockham received 23% of the vote;
   Doane received 3.1%;
   Degette received 73.8% of the vote.
   
  4) With the same for-loop from #2 above, we find that:
    
     Stockham received 85,213 total votes;
     Doane received 11,606 total votes;
     DeGette received 272,892 total votes.
     
  5) With this conditional statement:
   
   if (votes > winning_count) and (vote_percentage > winning_percentage):
   
       winning_count = votes
       
       winning_percentage = vote_percentage
       
       winning_candidate = candidate_name
       
  We initialized a candidate_votes dictionary to hold each candidate's name as keys and their votes received as values 

## Challenge Overview
This challenge requested an additional 3 pieces of information about the election:
  1) The total turnout of votes from each county.
  2) Each county's percentage of the total votes.
  3) The county with the highest turnout.

## Results
-- There were 369,711 total votes cast in the election.

-- Jefferson County had 38,855 votes or 10.5% of the grand total; Arapahoe County had 24,801 votes or 6.7% of the grand total; and Denver County had 306,055 votes or 82.8% of the grand total. 

-- Denver County had, by far, the largest vote turnout.

-- Three candidates received votes in the election: Charles Casper Stockham, Diana DeGette and Raymon Anthony Doane. Stockham received 85,213 votes or 23% of the grand total; Doane received 11,606 votes or 3.1% of the grand total; and DeGette received 272,892 votes or 73.8% of the grand total.

-- DeGette won the election with 73.8% (272,892) of the total vote. 

## Challenge Summary

This script could be modified to apply to other kinds of elections, such as local and federal. Instead of holding variables for county, we would create variables that described things such as ZIP code or school district at the local level. For a federal election, tracking votes at the county level would likely be impractical so our loops would need to instead extract things such as a voters' state of residence. 
