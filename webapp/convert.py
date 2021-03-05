#Eric Gassel and Sam Gloss
import csv

def write_dictionaries():
    
    players_dict = {}
    games_dict = {}
    matchups_dict = {}
    game_matchups_dict = {}
    stats_dict = {}
    pgs_dict = {}
    
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
            
            #matchups.csv
            team = row[1]
            oppt = row[2]
            matchup_key = (team, oppt)
            if matchup_key in matchups_dict:
                matchup_value = matchups_dict[matchup_key]
            else:
                matchup_value = {'id': len(matchups_dict)+1}
                matchups_dict[matchup_key] = matchup_value
            matchup_id = matchup_value['id']
            
            #games.csv
            game = row[0]
            year = int(game[11:15])
            month = int(game[15:17])
            day = int(game[17:19])
            home_team=game[20:23]
            if game in games_dict:
                games_value = games_dict[game]
            else:
                games_value = {'id': len(games_dict)+1,'year':year,'month':month,'day':day,'home_team':home_team}
                games_dict[game] = games_value
            game_id = games_value['id']
                
            #games_matchups.csv
            result = row[5]
            team_score = int(row[3])
            opponent_score = int(row[4])
            point_diff = int(row[6])
            games_matchups_key = (matchup_id,game_id)
            if games_matchups_key in game_matchups_dict:
                gm_value = game_matchups_dict[games_matchups_key]
            else:
                gm_value = {'id':len(game_matchups_dict)+1,'result':result,'team_score':team_score,'opponent_score':opponent_score,'point_diff':point_diff}
                game_matchups_dict[games_matchups_key]=gm_value
            game_matchup_id=gm_value['id']
            
            #stats.csv
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
            stats_dict_key = (MP,PTS,FG,FGA,FG3,FG3A,FT,FTA,ORB,DRB,TRB,AST,STL,BLK,TO,PF,plus_minus)
            if stats_dict_key in stats_dict:
                stats_value=stats_dict[stats_dict_key]
            else:
                stats_value = {'id':len(stats_dict)+1}
                stats_dict[stats_dict_key]=stats_value
            stats_id = stats_value['id']
            
            #player_game_statistics.csv
            pgs = (game_matchup_id,player_ID)
            if pgs in pgs_dict:
                pgs_value = pgs_dict[pgs]
            else:
                pgs_value = {'id':len(pgs_dict)+1,'stats':stats_id}
                pgs_dict[pgs]=pgs_value
            
            
    with open('csv-data/players.csv', 'w', newline='') as csvfile:
        players_info = ['id', 'player_name']
        writer = csv.writer(csvfile, delimiter = ',', quotechar='|')
        writer.writerow(players_info)
        for player in players_dict:
            player_list = players_dict[player]
            player_id = player_list['id']
            writer.writerow([player_id, player])
            
    with open('csv-data/games.csv', 'w', newline='') as csvfile:
        games_info = ['id', 'game_id','year','month','day','home_team']
        writer = csv.writer(csvfile, delimiter = ',', quotechar='|')
        writer.writerow(games_info)
        for game in games_dict:
            games_list = games_dict[game]
            game_id = games_list['id']
            year = games_list['year']
            month = games_list['month']
            day = games_list['day']
            home_team=games_list['home_team']
            writer.writerow([game_id, game, year, month,day,home_team])
            
    with open('csv-data/matchups.csv', 'w', newline='') as csvfile:
        matchup_info = ['id', 'team', 'opponent']
        writer = csv.writer(csvfile, delimiter = ',', quotechar='|')
        writer.writerow(matchup_info)
        for (team,oppt) in matchups_dict:
            matchups_list = matchups_dict[(team,oppt)]
            matchup_id = matchups_list['id']
            writer.writerow([matchup_id, team, oppt])
            
    with open('csv-data/games_matchups.csv', 'w', newline='') as csvfile:
        team_game_info = ['id', 'matchup_id', 'game_id', 'result','team_score','opponent_score','point_diff']
        writer = csv.writer(csvfile, delimiter = ',', quotechar='|')
        writer.writerow(team_game_info)
        for (matchup_id,game_id) in game_matchups_dict:
            team_game_list = game_matchups_dict[(matchup_id,game_id)]
            result=team_game_list['result']
            team_score=team_game_list['team_score']
            opponent_score=team_game_list['opponent_score']
            point_diff=team_game_list['point_diff']
            gm_id=team_game_list['id']
            writer.writerow([gm_id, matchup_id, game_id, result, team_score,opponent_score,point_diff])
            
    with open('csv-data/stats.csv', 'w', newline='') as csvfile:
        stats_info = ['id', 'mp','pts','fg','fga','fg3','fg3a','ft','fta','orb','drb','trb','ast','stl','blk','to','pf','plus_minus',]
        writer = csv.writer(csvfile, delimiter = ',', quotechar='|')
        writer.writerow(stats_info)
        for (MP,PTS,FG,FGA,FG3,FG3A,FT,FTA,ORB,DRB,TRB,AST,STL,BLK,TO,PF,plus_minus) in stats_dict:
            stats_list = stats_dict[(MP,PTS,FG,FGA,FG3,FG3A,FT,FTA,ORB,DRB,TRB,AST,STL,BLK,TO,PF,plus_minus)]
            stats_id=stats_list['id']
            writer.writerow([stats_id,MP,PTS,FG,FGA,FG3,FG3A,FT,FTA,ORB,DRB,TRB,AST,STL,BLK,TO,PF,plus_minus])
            
    with open('csv-data/player_game_statistics.csv', 'w', newline='') as csvfile:
        player_game_info = ['id', 'game_matchup_id', 'player_id', 'stats_id']
        writer = csv.writer(csvfile, delimiter = ',', quotechar='|')
        writer.writerow(player_game_info)
        for (game_matchup_id,player_ID) in pgs_dict:
            player_game_list = pgs_dict[(game_matchup_id,player_ID)]
            pgs_id=player_game_list['id']
            stats_id=player_game_list['stats']
            writer.writerow([pgs_id, game_matchup_id,player_ID,stats_id])
    return

def main():
  write_dictionaries()

if __name__ == "__main__":
  main()

