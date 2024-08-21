# Import os and CSV
import os
import csv

# lists to store data for name of candidates, votes each candidate received, and percent votes per candidate
name_candidate_list = []
votes_candidate = []
percent_votes_candidate = []

# set initial value for total number of votes
votes_total = 0

# open and read the csv file
election_data_csv = os.path.join("Resources", "election_data.csv")

with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    #read the header row
    csv_header = next(csv_file)
    # read through the row; calculate total votes 
    for row in csv_reader:
        votes_total = votes_total + 1
        
     # setting the list for candidate name and votes each candidate received       
        if row[2] not in name_candidate_list:
            name_candidate_list.append(row[2])
            index = name_candidate_list.index(row[2])
            votes_candidate.append(1)
            
        else:
            index = name_candidate_list.index(row[2])
            votes_candidate[index] = votes_candidate[index] + 1   
            
    # calculate percent votes per candidate, and candidate with the most popular vote    
    for votes in votes_candidate:
        percent_votes = (votes/votes_total)*100
        percent_votes_candidate.append(percent_votes)
        
    popular_vote = max(votes_candidate)
    index = votes_candidate.index(popular_vote)
    winner = name_candidate_list[index] 
    
    # print statments            
    print("Election Results" + "\n")
    print("----------------------------" + "\n")
    print(f"Total Votes: {votes_total}" + "\n")
    print("----------------------------" + "\n")
    
    for i in range(len(name_candidate_list)):
        print(name_candidate_list[i] + ":" + " " + str("%.3f" % (percent_votes_candidate[i])) + "% (" + str(votes_candidate[i]) + ")" + "\n")
    print("----------------------------" + "\n")
    print(f"Winner: {winner}" + "\n")
    print("----------------------------")
    
    # analysis output as text
    output_path = os.path.join("Analysis", "analysis.txt")
    
    with open(output_path, "w") as txtfile:
        txtfile.write("Election Results" + "\n" + "\n")
        txtfile.write("----------------------------" + "\n" + "\n")
        txtfile.write(f"Total Votes: {votes_total}" + "\n" + "\n")
        txtfile.write("----------------------------" + "\n" + "\n")
    
        for i in range(len(name_candidate_list)):
            txtfile.write(name_candidate_list[i] + ":" + " " + str("%.3f" % (percent_votes_candidate[i])) + "% (" + str(votes_candidate[i]) + ")" + "\n" + "\n")
        txtfile.write("----------------------------" + "\n" + "\n")
        txtfile.write(f"Winner: {winner}" + "\n" + "\n")
        txtfile.write("----------------------------")
           
    
    