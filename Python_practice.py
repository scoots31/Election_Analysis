counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# Displays all the counties
for county in counties_dict:
    print(county)

# Displays all the counties and voters
for voters in counties_dict.values():
    print(voters)

# Displays all the counties
for county in counties_dict:
    print(counties_dict.get(county))

# Displays counties and voters with text strings    
for county, voters in counties_dict.items():
    print(str(county) + ' county has ' + str(voters) + ' registered voters.')

# Sets the dictionary county inside of the voting data dictionary
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print(county_dict)

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
    print(county_dict['county'])

# using f strings to print out sentences using data
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters. ")


#Multiline f strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes: ,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)

for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters. ")

for i in voting_data:
    print(f"{i['county']} county has {i['registered_voters']:,} registered voters.")
