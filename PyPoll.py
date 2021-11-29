# Need to retrieve the data

# Importing packages for csv and os
import csv
import os

# Assign a variable for the file to load and the path using os.path and join methods
file_to_load = os.path.join("Resources", "election_results.csv")

# Open the election results and read the file.
with open(file_to_load) as election_data:

# To do: perform analysis.
    print(election_data)

# Close the file.
election_data.close()

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file.
    for row in file_reader:
        print(row)

# Use the open statement to open the file as a text file.
with open(file_to_save, "w") as txt_file:
    # Write some data to the file.
    # Write three counties to the file.
    txt_file.write("Counties in Election\n-------------------------\nArapahoe\nDenver\nJefferson")

# Close the file
txt_file.close()


# 1. Total number of votes cast.
# 2. A complete list of candidates that recieved votes.
# 3. Percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the votes based on popular vote.
