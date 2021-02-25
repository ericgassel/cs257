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
from config import password
from config import database
from config import user

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

@api.route('/teams/') 
def get_team_list():
    query = 'SELECT team_data.Team_Name ORDER BY team_data.Team_Name ASC'

    connection = establish_database_connection()
    cursor = execute_query(connection.cursor(), query)

    teams_list = []
    for team in cursor:
        teams_list.append(team[0])

    return json.dumps(teams_list)

@api.route('/teams/ppg/') 
def get_team_ppg():

    query = 'SELECT team_data.Team_Name, team_data.PPG FROM team_data ORDER BY team_data.PPG DESC LIMIT 5'

    connection = establish_database_connection()
    cursor = execute_query(connection.cursor(), query)
    
    ppg_list = []
    for team in cursor:
        name = team[0]
        points = team[1]
        ppg_list.append({'name':name, 'points':points})


    return json.dumps(ppg_list)

@api.route('/teams/apg/') 
def get_team_apg():
   
    query = 'SELECT team_data.Team_Name, team_data.APG FROM team_data ORDER BY team_data.APG DESC LIMIT 5'

    connection = establish_database_connection()
    cursor = execute_query(connection.cursor(), query)
    
    apg_list = []
    for team in cursor:
        name = team[0]
        assists = team[1]
        apg_list.append({'name':name, 'assists':assists})


    return json.dumps(apg_list)


