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

@api.route('/players/ppg/')
def get_players_ppg():
    query = 'SELECT players.player, SUM(stats.PTS), COUNT(stats.PTS) FROM players, stats, player_game_statistics, games WHERE players.id=player_game_statistics.players_id AND stats.id=player_game_statistics.stats_id AND games.year=2020 GROUP BY players.player ORDER BY SUM(stats.PTS)/COUNT(stats.PTS) DESC LIMIT 10'

    connection = establish_database_connection()
    cursor = execute_query(connection.cursor(), query)

    ppg_list = []
    for row in cursor:
        player=row[0]
        ppg=round(float(row[1])/row[2],2)
        ppg_list.append({'player':player,'ppg':ppg})

    return json.dumps(ppg_list)

@api.route('/teams/') 
def get_team_list():
    query = 'SELECT DISTINCT team FROM matchups ORDER BY team'

    connection = establish_database_connection()
    cursor = execute_query(connection.cursor(), query)

    teams_list = []
    for team in cursor:
        teams_list.append(team[0])

    return json.dumps(teams_list)

@api.route('/teams/ppg/') 
def get_team_ppg():

    query = 'SELECT DISTINCT matchups.team, AVG(stats.PTS) FROM players, games_matchups, matchups, stats, player_game_statistics, games WHERE players.id=player_game_statistics.players_id AND games.year=2020 AND games_matchups.id = player_game_statistics.games_matchups_id GROUP BY matchups.team LIMIT 20'
    #query = 'SELECT DISTINCT team, SUM(PTS) FROM matchups, stats, players, games_matchups, player_game_statistics, games WHERE players.id = player_game_statistics.players_id AND games.id=games_matchups.games_id AND games_matchups.id = player_game_statistics.games_matchups_id AND stats.id=player_game_statistics.stats_id AND games.year = 2020 GROUP BY team LIMIT 20'

    connection = establish_database_connection()
    cursor = execute_query(connection.cursor(), query)
    
    ppg_list = []
    for row in cursor:
        team = row[0]
        points = row[1]
        ppg_list.append({'team':team,'points':points})


    return json.dumps(ppg_list)

@api.route('/teams/apg/') 
def get_team_apg():
   
    query = 'SELECT DISTINCT matchups.team, AVG(SUM(stats.AST)) FROM matchups, stats, player_game_statistics, games WHERE players.id=player_game_statistics.players_id AND games.year=2020 AND games_matchups.id = player_game_statistics.games_matchups_id ORDER BY team'
    connection = establish_database_connection()
    cursor = execute_query(connection.cursor(), query)
    
    apg_list = []
    for row in cursor:
        team = row[0]
        assists = team[1]
        apg_list.append({'team':name, 'team':assists})

    return json.dumps(apg_list)

@api.route('/games/')
def get_games_list():
    query = 'SELECT team, opponent, team_score, opponent_score, month, day, year FROM games, games_matchups, matchups WHERE games.id=games_matchups.games_id AND matchups.id=games_matchups.matchups_id AND games.year=2020'
    connection = establish_database_connection()
    cursor = execute_query(connection.cursor(), query)

    games_list = []
    for row in cursor:
        team = row[0]
        opponent = row[1]
        team_score = row[2]
        opponent_score = row[3]
        month = row[4]
        day = row[5]
        year = row[6]
        check = {'team':team,'opponent':opponent,'team_score':team_score,'opponent_score':opponent_score,'month':month,'day':day,'year':year}
        check2 = {'team':opponent,'opponent':team,'team_score':opponent_score,'opponent_score':team_score,'month':month,'day':day,'year':year}
        if check not in games_list:
            if check2 not in games_list:
                games_list.append({'team':team,'opponent':opponent,'team_score':team_score,'opponent_score':opponent_score,'month':month,'day':day,'year':year})

    return json.dumps(games_list)

@api.route('/players/<player_name>/')
def get_player_names(player_name):

    search_word = "%" + player_name + "%"
    query = "SELECT players.player, DISTINCT matchups.team FROM players, matchups, player_game_statistics WHERE players.player LIKE %s AND players.id=player_game_statistics.player_id AND matchups.id = player_game_statistics.matchups_id"
    
    connection = establish_database_connection()

    cursor = connection.cursor()

    try:
        cursor.execute(query,search_word)
    except Exception as e:
        print (e)
        exit()

    player_list = []
    for row in cursor:
        player=row[0]
        team=row[1]
        player_list.append({'player':player,'team':team})

    return json.dumps(player_list)


@api.route('/help/')
def return_help_screen():
    #returns the help documentat
    
    return flask.render_template('help.html')

