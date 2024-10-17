# PyPoll
# Import necessary modules
import csv
import os

# Files to load and output
resource_file = os.path.join("Resources", "election_data.csv")  # Input file path
analysis_file = os.path.join("Analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0 # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidates_votes = { 
    "candidate" : [],
    "vote_count" : []
}

# Open the CSV file and process it
with open(resource_file) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes = total_votes + 1

        # Get the candidate's name from the row
        name = row[2]

        # If the candidate is not already in the candidate list, add them
        if name not in (candidates_votes["candidate"]):
            candidates_votes["candidate"].append(name)
            candidates_votes["vote_count"].append(0) #add a vote counter for each candidate

        # Add a vote to the candidate's count
        index = int(candidates_votes["candidate"].index(name))
        votes = (candidates_votes["vote_count"][index])
        votes = votes + 1
        candidates_votes["vote_count"][index] = votes

   
# Open a text file to save the output
with open(analysis_file, "w") as txt_file:

    # Print the total vote count (to terminal)
    output = (f'''--------------------------------
Total Votes: {total_votes}
--------------------------------''')
    print(".") #this is just for formatting
    print(output)
    
    # Write the total vote count to the text file
    txt_file.write(output)
    
    # Creates variables to track index of each candidate and the vote count for the winner
    index = 0
    winner_count = 0

    # Loop through the candidates to determine vote percentages and identify the winner
    for name in candidates_votes["candidate"]:

        # Get the vote count and calculate the percentage
        percent = ((candidates_votes["vote_count"][index])/total_votes)*100

        # Update the winning candidate if this one has more votes
        if int(candidates_votes["vote_count"][index]) > winner_count:
            winner_count = int(candidates_votes["vote_count"][index])

        # Print and save each candidate's vote count and percentage
        output = (f"{candidates_votes['candidate'][index]}: {percent:.3f}% ({candidates_votes['vote_count'][index]})")
        print(f'{output}')
        txt_file.write(f'''
{output}''')
        
        index = index + 1 #advances index variable so we look at the next candidate and vote count

    # Generate and print the winning candidate summary
    index = int(candidates_votes["vote_count"].index(winner_count))
    winner = (candidates_votes["candidate"][index])
    output = (f'''--------------------------------
Winner: {winner}
--------------------------------''')
    print(output)
   
    # Save the winning candidate summary to the text file

    txt_file.write(f'''
{output}''')