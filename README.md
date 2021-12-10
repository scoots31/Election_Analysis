# Election_Analysis

## Overview of Election Audit
A Colorado Board of Election has requested an election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.
6. Determine the total number of votes and percentages for each county.
7. Determine the county that had the largest voter turnout.

### Resources
– Data Source: election_results.csv
– Software: Python 3.6.7, Visual Studio Code, 1.62.3

## Election Audit Results
The analysis of the election show that:

* There were 369,711 votes cast in the election.
* The candidates were:
    * Charles Casper Stockham
    * Diana DeGette
    * Raymon Anthony Doane
* The candidate results were:
    * Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
    * Diana DeGette received 73.8% of the vote and 272,892 number of votes.
    * Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
* The winner of the election was:
    * Diana DeGette received 73.8% of the vote and 272,892 number of votes.
* The counties in the congressional election were:
    * Jefferson had 10.5 percent of the votes with 38,855 ballots cast.
    * Denver had 82.8 percent of the votes with 306,055 ballots cast.
    * Arapahoe had 6.7 percent of the votes with 24,801 ballots cast.
* The county with the largest voter turnout:
    * Denver

![Screen Shot 2021-12-10 at 9 08 24 AM](https://user-images.githubusercontent.com/93485455/145600097-cdd8b530-9904-4f1d-9c2c-76eae6983d21.png)

    
## Election Audit Summary

Further analysis could be performed on the existing dataset by modifying the script to count the votes for each candidate by the county the ballot was cast. By using a conditional statement we can isolate votes for a candidate AND the county it came from into a list. This analysis would provide further insight where each candidate's support originated from in the overall vote turnout.

For a broader use of this code, we could create dictionaries with all the existing counties and congressional district assignments to create a lookup that would allow the script to be utilized for any election in Colorado. With additional requirement gathering we could modify the script to injest election data, determine the district the ballots are assigned, and run the analysis providing results for any congressional election in Colorado.
