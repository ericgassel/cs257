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
    

@api.route('/players/<per_game>/<season>', strict_slashes=False)
def get_players_per_game(per_game, season):
    
    game_stat = per_game_convert(per_game)
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
    
    connection = establish_database_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(query,(season,))
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

@api.route('/teams/<per_game>/<season>', strict_slashes=False) 
def get_team_per_game(per_game, season):
    game_stat = per_game_convert(per_game)
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

    connection = establish_database_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(query,(season,))
    except Exception as e:
        print (e)
        exit()
    
    cursor_count = connection.cursor()
    try:
        cursor_count.execute(query_count,(season,))
    except Exception as e:
        print (e)
        exit()


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
        per_game_list.append({'name':team,'per_game':per_game})
        
        
    sorted_pg = sorted(per_game_list, key=lambda k: k['per_game'], reverse=True)

    cursor.close()
    cursor_count.close()
    connection.close()
    
    return json.dumps(sorted_pg)
 


@api.route('/games/<season>', strict_slashes=False)
def get_games_list(season):

    query = f'''SELECT home_team, home_score, away_team, away_score, month, day, year 
                FROM game
                WHERE season = %s
                '''

    connection = establish_database_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(query,(season,))
    except Exception as e:
        print (e)
        exit()

    games_list = []
    for row in cursor:
        home_team = row[0]
        home_score = row[1]
        away_team = row[2]
        away_score = row[3]
        month = row[4]
        day = row[5]
        year = row[6]
        games_list.append({'home_team':home_team,'home_score':home_score,'away_team':away_team,'away_score':away_score,'month':month,'day':day,'year':year})

    return json.dumps(games_list)


@api.route('/help/')
def return_help_screen():
    #returns the help documentat
    
    return flask.render_template('help.html')


