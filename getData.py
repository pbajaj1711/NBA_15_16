import copper
import pandas as pd
import requests
from bs4 import BeautifulSoup

copper.path = "../"
url = 'http://espn.go.com/nba/teams'
r = requests.get(url)

soup = BeautifulSoup(r.text)
tables = soup.find_all('ul', class_='medium-logos')

teams = []
prefix_1 = []
prefix_2 = []
teams_urls = []
for table in tables:
    lis = table.find_all('li')
    for li in lis:
        info = li.h5.a
        teams.append(info.text)
        url = info['href']
        teams_urls.append(url)
        prefix_1.append(url.split('/')[-2])
        prefix_2.append(url.split('/')[-1])


dic = {'url': teams_urls, 'prefix_2': prefix_2, 'prefix_1': prefix_1}
teams = pd.DataFrame(dic, index=teams)
teams.index.name = 'team'
print(teams)
teams.to_csv('teams')


import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime, date

year = 2015
BASE_URL = 'http://espn.go.com/nba/team/schedule/_/name/{0}/year/{1}/{2}'

f = open("games_15", "w")
match_id = []
dates = []
home_team = []
home_team_score = []
visit_team = []
visit_team_score = []

for index, row in teams.iterrows():
    _team, url = index, row['url']
    r = requests.get(BASE_URL.format(row['prefix_1'], year, row['prefix_2']))
    table = BeautifulSoup(r.text).table
    for row in table.find_all('tr')[1:]: # Remove header
        columns = row.find_all('td')
        try:
            _home = True if columns[1].li.text == 'vs' else False
            #print _home
            _other_team = columns[1].find_all('a')[1].text
            _score = columns[2].a.text.split(' ')[0].split('-')
            _won = True if columns[2].span.text == 'W' else False

            match_id.append(columns[2].a['href'].split('?id=')[1])
            home_team.append(_team if _home else _other_team)
            visit_team.append(_team if not _home else _other_team)
            d=""
            d = datetime.strptime(columns[0].text, '%a, %b %d')
            dates.append(date(year, d.month, d.day))

            hs = 0
            vs = 0
            if _home:
                if _won:
                    home_team_score.append(_score[0])
                    hs = _score[0]
                    visit_team_score.append(_score[1])
                    vs = _score[1]
                else:
                    home_team_score.append(_score[1])
                    hs = _score[1]
                    visit_team_score.append(_score[0])
                    vs = _score[0]
            else:
                if _won:
                    home_team_score.append(_score[1])
                    hs = _score[1]
                    visit_team_score.append(_score[0])
                    vs = _score[0]
                else:
                    home_team_score.append(_score[0])
                    hs = _score[0]
                    visit_team_score.append(_score[1])
                    vs = _score[1]
            if(d.month ):
                f.write(str(columns[2].a['href'].split('?id=')[1])+","+str(date(year, d.month, d.day))+","+str(_team if _home else _other_team)+","+str(hs)+","+str(_team if not _home else _other_team)+","+str(vs)+"\n")
        except Exception as e:
            pass # Not all columns row are a match, is OK
            # print(e)
f.close()



import copper
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime, date
import time
copper.path = '../..'


BASE_URL = 'http://espn.go.com/nba/boxscore?gameId={0}'

ids_done = []
with open("box_scores_15.csv", "a") as csvoutput:
    writer = csv.writer(csvoutput, lineterminator="\n")
    f = open("games_15", "r")
    for line in f:
        index = line.split(",")[0]
        date = line.split(",")[1]
        if(index not in ids_done):
            ids_done.append(index)
            print(index)
            time.sleep(10)
            request = requests.get(BASE_URL.format(index))
            table = BeautifulSoup(request. text).find('table', class_="miniTable")
            if(table != None):
                body = table.find_all('tbody')
                td = body[0].find_all('td')
                team_1 = str(td[0])[22:-5]
                scores_1 = [int(str(td[1])[4:-5]), int(str(td[2])[4:-5]), int(str(td[3])[4:-5]), int(str(td[4])[4:-5])]
                ptr = (len(td)-12)/2
                team_2 = str(td[ptr+6])[22:-5]
                scores_2 = [int(str(td[ptr+7])[4:-5]), int(str(td[ptr+8])[4:-5]), int(str(td[ptr+9])[4:-5]), int(str(td[ptr+10])[4:-5])]
                writer.writerow([date, team_1, scores_1, team_2, scores_2])
            else:
                writer.writerow([str(index)])
    f.close()
    
ids_done = []
with open("box_scores_16.csv", "w") as csvoutput:
    writer = csv.writer(csvoutput, lineterminator="\n")
    f = open("games_16", "r")
    for line in f:
        index = line.split(",")[0]
        date = line.split(",")[1]
        if(index not in ids_done):
            ids_done.append(index)
            print(index)
            time.sleep(7)
            request = requests.get(BASE_URL.format(index))
            table = BeautifulSoup(request. text).find('table', class_="miniTable")
            if(table != None):
                body = table.find_all('tbody')
                td = body[0].find_all('td')
                team_1 = str(td[0])[22:-5]
                scores_1 = [int(str(td[1])[4:-5]), int(str(td[2])[4:-5]), int(str(td[3])[4:-5]), int(str(td[4])[4:-5])]
                ptr = (len(td)-12)/2
                team_2 = str(td[ptr+6])[22:-5]
                scores_2 = [int(str(td[ptr+7])[4:-5]), int(str(td[ptr+8])[4:-5]), int(str(td[ptr+9])[4:-5]), int(str(td[ptr+10])[4:-5])]
                writer.writerow([date, team_1, scores_1, team_2, scores_2])
            else:
                writer.writerow([str(index)])
    f.close()