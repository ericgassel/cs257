#Eric Gassel and Sam Gloss
import csv

def write_dictionaries():
    
    players_dict = {}
    games_dict = {}
    team_dict = {}
    stats_dict = {}
    
    with open('csv-data/nba_data.csv', newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter =',', quotechar= '|')
        next(reader)
        for row in reader:
            
            #players.csv
            player = row[7]
            if player in players_dict:
                players_value = players_dict[player]
            else:
                players_value = {'id':len(players_dict)+1}
                players_dict[player]=players_value
            player_ID = players_value['id']
            
            #team.csv
            team = row[1]
            if team in team_dict:
                team_value = team_dict[team]
            else:
                team_value = {'id':len(team_dict)+1}
                team_dict[team] = team_value
            team_id = team_value['id']
            
            #game.csv
            game = row[0]
            year = int(game[11:15])
            month = int(game[15:17])
            day = int(game[17:19])
            home_team=game[20:23]
            if home_team == "ATL":
                if team == "Atlanta Hawks":
                    home_team = team
                    away_team = row[2]
            if home_team == "BKN":
                if team == "Brooklyn Nets":
                    home_team = team
                    away_team = row[2]
            if home_team == "BOS":
                if team == "Boston Celtics":
                    home_team = team
                    away_team = row[2]
            if home_team == "CHA":
                if team == "Charlotte Hornets":
                    home_team = team
                    away_team = row[2]
            if home_team == "CHI":
                if team == "Chicago Bulls":
                    home_team = team
                    away_team = row[2]
            if home_team == "CLE":
                if team == "Cleveland Cavaliers":
                    home_team = team
                    away_team = row[2]
            if home_team == "DAL":
                if team == "Dallas Mavericks":
                    home_team = team
                    away_team = row[2]
            if home_team == "DEN":
                if team == "Denver Nuggets":
                    home_team = team
                    away_team = row[2]
            if home_team == "DET":
                if team == "Detroit Pistons":
                    home_team = team
                    away_team = row[2]
            if home_team == "GSW":
                if team == "Golden State Warriors":
                    home_team = team
                    away_team = row[2]
            if home_team == "HOU":
                if team == "Houston Rockets":
                    home_team = team
                    away_team = row[2]
            if home_team == "IND":
                if team == "Indiana Pacers":
                    home_team = team
                    away_team = row[2]
            if home_team == "LAC":
                if team == "Los Angeles Clippers":
                    home_team = team
                    away_team = row[2]
            if home_team == "LAL":
                if team == "Los Angeles Lakers":
                    home_team = team
                    away_team = row[2]
            if home_team == "MEM":
                if team == "Memphis Grizzlies":
                    home_team = team
                    away_team = row[2]
            if home_team == "MIA":
                if team == "Miami Heat":
                    home_team = team
                    away_team = row[2]
            if home_team == "MIL":
                if team == "Milwaukee Bucks":
                    home_team = team
                    away_team = row[2]
            if home_team == "MIN":
                if team == "Minnesota Timberwolves":
                    home_team = team
                    away_team = row[2]
            if home_team == "NOP":
                if team == "New Orleans Pelicans":
                    home_team = team
                    away_team = row[2]
            if home_team == "NYK":
                if team == "New York Knicks":
                    home_team = team
                    away_team = row[2]
            if home_team == "OKC":
                if team == "Oklahoma City Thunder":
                    home_team = team
                    away_team = row[2]
            if home_team == "ORL":
                if team == "Orlando Magic":
                    home_team = team
                    away_team = row[2]
            if home_team == "PHI":
                if team == "Philadelphia 76ers":
                    home_team = team
                    away_team = row[2]
            if home_team == "PHX":
                if team == "Phoenix Suns":
                    home_team = team
                    away_team = row[2]
            if home_team == "POR":
                if team == "Portland Trail Blazers":
                    home_team = team
                    away_team = row[2]
            if home_team == "SAC":
                if team == "Sacramento Kings":
                    home_team = team
                    away_team = row[2]
            if home_team == "SAS":
                if team == "San Antonio Spurs":
                    home_team = team
                    away_team = row[2]
            if home_team == "TOR":
                if team == "Toronto Raptors":
                    home_team = team
                    away_team = row[2]
            if home_team == "UTA":
                if team == "Utah Jazz":
                    home_team = team
                    away_team = row[2]
            if home_team == "WAS":
                if team == "Washington Wizards":
                    home_team = team
                    away_team = row[2]
                    
            if isinstance(home_team,str):
                away_team = team
                home_team = row[2]
                
            if game in games_dict:
                games_value = games_dict[game]
            else:
                games_value = {'id': len(games_dict)+1,'home_team':home_team,'away_team':away_team,'year':year,'month':month,'day':day}
                games_dict[game] = games_value
            game_id = games_value['id']
            
            
                
            #player_games.csv
            mp = float(row[8])
            MP = int(mp)
            FG = int(row[9])
            FGA = int(row[10])
            FG3 = int(row[11])
            FG3A = int(row[12])
            FT = int(row[13])
            FTA = int(row[14])
            ORB = int(row[15])
            DRB = int(row[16])
            TRB = int(row[17])
            AST = int(row[18])
            STL = int(row[19])
            BLK = int(row[20])
            TO = int(row[21])
            PF = int(row[22])
            plus_minus = int(row[23])
            PTS = int(row[24])
            #stats_dict_key = (MP,PTS,FG,FGA,FG3,FG3A,FT,FTA,ORB,DRB,TRB,AST,STL,BLK,TO,PF,plus_minus)
            stats_dict_key = (player_ID, game_id)
            if stats_dict_key in stats_dict:
                stats_value=stats_dict[stats_dict_key]
            else:
                stats_value = {'id':len(stats_dict)+1, 'team_id': team_id, 'MP':MP,'PTS':PTS,'FG':FG,'FGA':FGA,'FG3':FG3,'FG3A':FG3A,'FT':FT,'FTA':FTA,'ORB':ORB,'DRB':DRB,'TRB':TRB,'AST':AST,'STL':STL,'BLK':BLK,'TO':TO,'PF':PF,'plus_minus':plus_minus}
                stats_dict[stats_dict_key]=stats_value
            stats_id = stats_value['id']

            
    with open('csv-data/players.csv', 'w', newline='') as csvfile:
        players_info = ['id', 'player_name']
        writer = csv.writer(csvfile, delimiter = ',', quotechar='|')
        writer.writerow(players_info)
        for player in players_dict:
            player_list = players_dict[player]
            player_id = player_list['id']
            writer.writerow([player_id, player])
            
    with open('csv-data/games.csv', 'w', newline='') as csvfile:
        games_info = ['id', 'home_team','away_team','year','month','day']
        writer = csv.writer(csvfile, delimiter = ',', quotechar='|')
        writer.writerow(games_info)
        for game in games_dict:
            games_list = games_dict[game]
            game_id = games_list['id']
            year = games_list['year']
            month = games_list['month']
            day = games_list['day']
            home_team=games_list['home_team']
            away_team=games_list['away_team']
            writer.writerow([game_id, home_team,away_team, year, month,day])
            
    with open('csv-data/team.csv', 'w', newline='') as csvfile:
        matchup_info = ['id', 'team']
        writer = csv.writer(csvfile, delimiter = ',', quotechar='|')
        writer.writerow(matchup_info)
        for team in team_dict:
            matchups_list = team_dict[team]
            matchup_id = matchups_list['id']
            writer.writerow([matchup_id, team])

            
    with open('csv-data/players_games.csv', 'w', newline='') as csvfile:
        stats_info = ['id','player_id','game_id','team_id', 'mp','pts','fg','fga','fg3','fg3a','ft','fta','orb','drb','trb','ast','stl','blk','to','pf','plus_minus',]
        writer = csv.writer(csvfile, delimiter = ',', quotechar='|')
        writer.writerow(stats_info)
        for (player_ID,game_id) in stats_dict:
            stats_list = stats_dict[(player_ID,game_id)]
            team_id = stats_list['team_id']
            stats_id=stats_list['id']
            MP = stats_list['MP']
            PTS = stats_list['PTS']
            FG = stats_list['FG']
            FGA = stats_list['FGA']
            FG3 = stats_list['FG3']
            FG3A = stats_list['FG3A']
            FT = stats_list['FT']
            FTA = stats_list['FTA']
            ORB = stats_list['ORB']
            DRB = stats_list['DRB']
            TRB = stats_list['TRB']
            AST = stats_list['AST']
            STL = stats_list['STL']
            BLK = stats_list['BLK']
            TO = stats_list['TO']
            PF = stats_list['PF']
            plus_minus = stats_list['plus_minus']
            writer.writerow([stats_id,player_id,game_id,team_id,MP,PTS,FG,FGA,FG3,FG3A,FT,FTA,ORB,DRB,TRB,AST,STL,BLK,TO,PF,plus_minus])


def main():
  write_dictionaries()

if __name__ == "__main__":
  main()

