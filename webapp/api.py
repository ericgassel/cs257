'''
    by Eric Gassel and Sam Gloss
    February 23, 2021
'''
import sys
import flask
import json
import config
import psycopg2
import argparse

api = flask.Blueprint('api',__name__)

def establish_database_connection():

    from config import database
    from config import user
    from config import password

    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
    except Exception as e:
        print(e)
        exit()
    
    return connection


def execute_query(cursor, query):
    
    try:
        cursor.execute(query)
    except Exception as e:
        print (e)
        exit()
    
    return cursor.fetchall()

def per_game_convert(stat):
    if stat.lower() == 'ppg':
        stat = 'PTS'
    elif stat.lower() == 'apg':
        stat = 'AST'
    elif stat.lower() == 'rpg':
        stat = 'TRB'
    elif stat.lower() == 'spg':
        stat = 'STL'
    elif stat.lower() == 'bpg':
        stat = 'BLK'
    elif stat.lower() == 'tov':
        stat = 'TOV'
    return stat
    

@api.route('/players/<per_game>/<season>/<month>', strict_slashes=False)
def get_players_per_game(per_game, season, month):
    game_stat = per_game_convert(per_game)
    connection = establish_database_connection()
    cursor = connection.cursor()
    if month == "0":
        query = f'''SELECT player.player, CAST(SUM(player_game.{game_stat}) AS FLOAT)/CAST(COUNT(player_game.{game_stat}) AS FLOAT) as PG,
            COUNT(player_game.MP) AS GP
            FROM game, player, player_game
            WHERE player_game.MP > 0
            AND player.id=player_game.player_id
            AND game.id=player_game.game_id
            AND game.season = %s
            GROUP BY player.player
            ORDER BY PG DESC
            LIMIT 5 '''
        try:
            cursor.execute(query,(season,))
        except Exception as e:
            print (e)
            exit()
        
    else:
        query = f'''SELECT player.player, CAST(SUM(player_game.{game_stat}) AS FLOAT)/CAST(COUNT(player_game.{game_stat}) AS FLOAT) as PG,
            COUNT(player_game.MP) AS GP
            FROM game, player, player_game
            WHERE player_game.MP > 0
            AND player.id=player_game.player_id
            AND game.id=player_game.game_id
            AND game.season = %s
            AND game.month = %s
            GROUP BY player.player
            ORDER BY PG DESC
            LIMIT 5 '''
        try:
            cursor.execute(query,(season,month,))
        except Exception as e:
            print (e)
            exit()
    
   
    

    player_request = flask.request.args.get('player_name')
    
    per_game_list = []
    for row in cursor:
        player=row[0]
        per_game=round(row[1],1)
        if player_request != None:
            if player == player_request:
                per_game_list.append({'name':player,'per_game':per_game})
            continue
        per_game_list.append({'name':player,'per_game':per_game})
    cursor.close()
    connection.close()
    return json.dumps(per_game_list)

@api.route('/teams/') 
def get_team_list():
    query = '''SELECT team FROM team ORDER BY team'''

    connection = establish_database_connection()
    cursor = execute_query(connection.cursor(), query)

    teams_list = []
    for team in cursor:
        teams_list.append(team[0])

    return json.dumps(teams_list)

@api.route('/teams/<per_game>/<season>/<month>', strict_slashes=False) 
def get_team_per_game(per_game, season, month):

    game_stat = per_game_convert(per_game)
    connection = establish_database_connection()
    cursor = connection.cursor()
    cursor_count = connection.cursor()
    
    if month == "0":
        query = f'''SELECT team.team, CAST(SUM(player_game.{game_stat}) AS FLOAT) as sum_points
            FROM game, player, player_game, team
            WHERE player.id=player_game.player_id
            AND game.id=player_game.game_id
            AND team.id=player_game.team_id
            AND game.season= %s
            GROUP BY team.team
            ORDER BY sum_points DESC
            '''

        query_count = '''SELECT team.team, COUNT(DISTINCT game.id) as GP
            FROM game, player_game, team
            WHERE team.id = player_game.team_id
            AND game.id=player_game.game_id
            AND game.season = %s
            GROUP BY team.team
            '''
        try:
            cursor.execute(query,(season,))
        except Exception as e:
            print (e)
            exit()
        try:
            cursor_count.execute(query_count,(season,))
        except Exception as e:
            print (e)
            exit()
    else: 
        query = f'''SELECT team.team, CAST(SUM(player_game.{game_stat}) AS FLOAT) as sum_points
            FROM game, player, player_game, team
            WHERE player.id=player_game.player_id
            AND game.id=player_game.game_id
            AND team.id=player_game.team_id
            AND game.season= %s
            AND game.month = %s
            GROUP BY team.team
            ORDER BY sum_points DESC
            '''

        query_count = '''SELECT team.team, COUNT(DISTINCT game.id) as GP
            FROM game, player_game, team
            WHERE team.id = player_game.team_id
            AND game.id=player_game.game_id
            AND game.season = %s
            AND game.month = %s
            GROUP BY team.team
            '''
        try:
            cursor.execute(query,(season,month,))
        except Exception as e:
            print (e)
            exit()
        try:
            cursor_count.execute(query_count,(season,month,))
        except Exception as e:
            print (e)
            exit()

    
    team_request = flask.request.args.get('team_name')


    count_list = {}
    for row in cursor_count:
        team = row[0]
        count = row[1]
        count_list[team] = {'count':count}

    per_game_list = []
    for row in cursor:
        team=row[0]
        sum_stat = row[1]
        count = count_list[team]
        count = count['count']
        per_game = round(float(sum_stat/count),1)
        if team_request != None:
            if team == team_request:
                per_game_list.append({'name':team,'per_game':per_game})
            continue
        per_game_list.append({'name':team,'per_game':per_game})
        
        
    sorted_pg = sorted(per_game_list, key=lambda k: k['per_game'], reverse=True)

    cursor.close()
    cursor_count.close()
    connection.close()
    
    return json.dumps(sorted_pg)
 
@api.route('/<team>/<season>/<month>', strict_slashes=False)
def return_team_leaders_in_statistic(team, season, month):
    connection = establish_database_connection()
    cursor = connection.cursor()
    if month == "0":
        query_roster = f'''SELECT DISTINCT player.player FROM player, team, player_game, game
                WHERE player.id = player_game.player_id
                AND team.id = player_game.team_id
                AND player_game.game_id = game.id
                AND team.team = %s
                AND game.season = %s
            '''
        try:
            cursor.execute(query_roster,(team,season,))
        except Exception as e:
            print (e)
            exit()
    else:
        query_roster = f'''SELECT DISTINCT player.player FROM player, team, player_game, game
                WHERE player.id = player_game.player_id
                AND team.id = player_game.team_id
                AND player_game.game_id = game.id
                AND team.team = %s
                AND game.season = %s
                AND game.month = %s
            '''
        try:
            cursor.execute(query_roster,(team,season,month,))
        except Exception as e:
            print (e)
            exit()
    
    
    per_game_list = []
    for row in cursor:
        player=row[0]
        per_game_list.append({'name':player})
    cursor.close()
    connection.close()
    return json.dumps(per_game_list)



@api.route('/games/<season>/<month>', strict_slashes=False)
def get_games_list(season, month):
    connection = establish_database_connection()
    cursor = connection.cursor()
    if month == "0":
        query = f'''SELECT home_team, home_score, away_team, away_score, month, day, year 
                FROM game
                WHERE season = %s
                '''
        try:
            cursor.execute(query,(season,))
        except Exception as e:
            print (e)
            exit()

    else:
        query = f'''SELECT home_team, home_score, away_team, away_score, month, day, year 
                FROM game
                WHERE season = %s
                AND month = %s
                '''
        try:
            cursor.execute(query,(season,month,))
        except Exception as e:
            print (e)
            exit()

  
    query_team = '''SELECT id, team FROM team'''

    
    cursor_team = connection.cursor()

   

    try:
        cursor_team.execute(query_team,(season,))
    except Exception as e:
        print (e)
        exit()

    team_request = flask.request.args.get('team_name')

    teams_dict = {}
    for row in cursor_team:
        ID = row[0]
        teams_dict[ID] = {'team':row[1]} 

    games_list = []
    for row in cursor:
        home_team = teams_dict[row[0]]
        home_team = home_team['team']
        home_score = row[1]
        away_team = teams_dict[row[2]]
        away_team = away_team['team']
        away_score = row[3]
        month = row[4]
        day = row[5]
        year = row[6]
        if team_request != None:
            if team_request == home_team or team_request == away_team:
                games_list.append({'home_team':home_team,'home_score':home_score,'away_team':away_team,'away_score':away_score,'month':month,'day':day,'year':year})
            continue
        games_list.append({'home_team':home_team,'home_score':home_score,'away_team':away_team,'away_score':away_score,'month':month,'day':day,'year':year})

    return json.dumps(games_list)




@api.route('/help/')
def return_help_screen():
    #returns the help documentat
    
    return flask.render_template('help.html')


