#Eric Gassel and James Marlin

import csv

def write_dictionaries():
    
  
    athletes_dict = {}
    games_dict = {}
    athletes_games_dict = {}
    event_dict = {}
    athlete_total_dict = {}
        
    with open('athlete_events.csv', newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter =',', quotechar= '|')
        next(reader)
        for row in reader:

            #Dictionary for athletes.csv
            ID = int(row[0])
            names = row[1]
            sex = row[2]
            weight = row[4]
            if ID not in athletes_dict:
                athletes_dict[ID] = {'names':names, 'sex':sex, 'weight': weight}
            athlete_id = ID

          #Dictionary for games.csv
            year = int(row[9])
            season = row[10]
            city = row[11]
            games_key = (year, season)
            if games_key in games_dict:
                games_value = games_dict[games_key]
            else:
                games_value = {'id': len(games_dict) +1, 'city':city}
                games_dict[games_key] = games_value
            games_id = games_value['id']


          #Dictionary for athletes_games.csv
            team = row[6]
            noc = row[7]
            athletes_games_key = (athlete_id, games_id)
            if athletes_games_key in athletes_games_dict:
                athlete_games_value = athletes_games_dict[athletes_games_key]
            else:
                athletes_games_value = {'id': len(athletes_games_dict) +1, 'team':team, 'noc':noc}
                athletes_games_dict[athletes_games_key] = athletes_games_value
            athletes_games_id = athletes_games_value['id']
        
          #Dictionary for events.csv
            sports = row[12]
            events = row[13]          
            if events in event_dict:
                events_value = event_dict[events]
            else:
                events_value = {'id': len(event_dict) +1, 'sports': sports}
                event_dict[events] = events_value
            events_id = events_value['id']

          #Dictionary for athlete_total
            medal = row[14]
            athlete_total_key = (athletes_games_id, events_id)
            if athlete_total_key in athlete_total_dict:
                athlete_total_value = athlete_total_dict[athlete_total_key]
            else:
                athlete_total_value = {'id': len(athlete_total_dict), 'medal':medal}
                athlete_total_dict[athlete_total_key] = athlete_total_value
            athlete_total_id = athlete_total_value['id']

          
  
    with open('athletes.csv', 'w', newline='') as csvfile:
        field_names_athletes = ['id', 'names', 'sex', 'weight']
        writer = csv.writer(csvfile, delimiter = ',', quotechar='|')
        writer.writerow(field_names_athletes)
        for ID in athletes_dict: 
            athlete_list = athletes_dict[ID]
            name = athlete_list['names']
            sex = athlete_list['sex']
            weight = athlete_list['weight']
            writer.writerow([ID, name, sex, weight])

    with open('games.csv', 'w', newline='') as csvfile:
        field_names_games = ['id','year','season','city']
        writer = csv.writer(csvfile, delimiter = ',', quotechar='|')
        writer.writerow(field_names_games)
        for (year, season) in games_dict:
            games_list = games_dict[(year, season)]
            games_id = games_list['id']
            city = games_list['city']
            writer.writerow([games_id, year, season, city])

    with open('events.csv','w',newline='') as csvfile:
        field_names_events = ['id','events','sports']
        writer = csv.writer(csvfile, delimiter = ',', quotechar='|')
        writer.writerow(field_names_events)
        for events in event_dict:
            event_list = event_dict[events]
            sports = event_list['sports']
            event_id = event_list['id']
            writer.writerow([event_id, events,sports])


    with open('athletes_games.csv', 'w', newline='') as csvfile:
        field_names_athletes_games = ['id','athlete_id', 'games_id','team','NOC']
        writer = csv.writer(csvfile, delimiter = ',', quotechar='|')
        writer.writerow(field_names_athletes_games)
        for (athlete_id, games_id) in athletes_games_dict:
            athlete_games_list = athletes_games_dict[(athlete_id, games_id)]
            athlete_games_id = athlete_games_list['id']
            team = athlete_games_list['team']
            noc = athlete_games_list['noc']
            writer.writerow([athlete_games_id, athlete_id, games_id, team, noc])

    with open('athletes_total.csv', 'w', newline='') as csvfile:
        field_names_athlete_total = ['id', 'athletes_games_id', 'events_id', 'medal']
        writer = csv.writer(csvfile, delimiter = ',', quotechar='|')
        writer.writerow(field_names_athlete_total)
        for (athletes_games_id, events_id) in athlete_total_dict:
            athlete_total_list = athlete_total_dict[(athletes_games_id, events_id)]
            medal = athlete_total_list['medal']
            athlete_total_id = athlete_total_list['id']
            writer.writerow([athlete_total_id, athletes_games_id, events_id, medal])
    return

def main():
  write_dictionaries()

if __name__ == "__main__":
  main()