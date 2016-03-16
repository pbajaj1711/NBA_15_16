import csv

#get number of distinct teams
teams = []
with open("box_scores_15.csv", "r") as csvinput:
    reader = csv.reader(csvinput)
    for line in reader:
         if(len(line)!=1):
            team_name = line[1].replace("\n","")
            if(team_name not in teams):
                teams.append(team_name)
            team_name = line[3].replace("\n","")
            if(team_name not in teams):
                teams.append(team_name)

#get team ka data
for team in teams:
    with open("TeamStats/"+team+"_15_16.csv", "w") as csvoutput:
        writer = csv.writer(csvoutput, lineterminator="\n")
        writer.writerow(["Date", "Q1", "Q2", "Q3", "Q4"])
        with open("box_scores_15.csv", "r") as csvinput:
            reader = csv.reader(csvinput)
            for line in reader:
                if(len(line)!=1):
                    if(line[1].replace("\n","") == team):
                        scores = line[2].replace("\n","")
                    elif(line[3].replace("\n","") == team):
                        scores = line[4].replace("\n","")
                    else:
                        continue
                    box_scores = scores[1:-1].split(",")
                    writer.writerow([line[0], box_scores[0], box_scores[1], box_scores[2], box_scores[3]])
                    
        with open("box_scores_16.csv", "r") as csvinput:
            reader = csv.reader(csvinput)
            for line in reader:
                if(len(line)!=1):
                    if(line[1].replace("\n","") == team):
                        scores = line[2].replace("\n","")
                    elif(line[3].replace("\n","") == team):
                        scores = line[4].replace("\n","")
                    else:
                        continue
                    box_scores = scores[1:-1].split(",")
                    writer.writerow([line[0], box_scores[0], box_scores[1], box_scores[2], box_scores[3]])