#Eric Gassel & Martin Bernard

import sys
import argparse
import flask
import json
import psycopg2

app = flask.Flask(__name__)


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

@app.route('/games')
def get_games():
    connection = establish_database_connection()
    cursor = connection.cursor()
    
    query = 'SELECT * FROM games ORDER BY years ASC'
    games_list = []
    
    try:
        cursor.execute(query)
    except Exception as e:
        print (e)
        exit()
        
    for game in cursor:
        ID = game[0]
        year = game[1]
        season = game[2]
        city = game[3]
        games_list.append({'id': ID, 'year':year, 'season':season, 'city':city})
    
    connection.close()
        
    return json.dumps(games_list)

@app.route('/nocs')
def get_nocs():
    
    connection = establish_database_connection()
    cursor = connection.cursor()

    query = "SELECT abbre, name FROM nocs"

    try:
        cursor.execute(query)
    except Exception as e:
        print (e)
        exit()

    noc_list = []
    for noc in cursor:
        abbreviation = noc[0]
        country = noc[1]
        noc_list.append({'noc':abbreviation, 'country':country})
    
    connection.close()

    return json.dumps(noc_list)

@app.route('/medalists/games/<games_id>')
def get_medals_winner_list(games_id):

    connection = establish_database_connection()
    cursor = connection.cursor()

    query = 'SELECT athlete.id, athlete.name, athlete.sex, events.sports, events.events, athletes_total.medal, games.id, athletes_game.NOC FROM athletes, games, events, athletes_games, athletes_total, noc WHERE athlete_games.athletes_id = athletes_total.athletes_games_id AND athletes.id = athletes_games.athletes_id AND events.id = athletes_total.events_id;'

    try:
        cursor.execute(query)
    except Exception as e:
        print (e)
        exit()
    
    games_list = []
    noc_request = flask.request.args.get('noc')
    
    for game in cursor:
        athlete_id = game[0]
        athlete_name = game[1]
        sex = game[2]
        sport = game[3]
        events = game[4]
        medal = game[5]
        searched_game = game[6]
        noc = game[7]
        if searched_game == games_id:
            games_list.append({'athlete_id':athlete_id, 'athlete_name':athlete_name, 'sex': sex, 'sport':sport, 'event':events, 'medal':medal})
        
        
        connection.close()
        
    return json.dumps(games_list)
    

def main():
    
    parser = argparse.ArgumentParser('An Olympics Flask application/API')
    parser.add_argument('host', help='the host on which this application is running')
    parser.add_argument('port', type=int, help='the port on which this application is listening')
    args = parser.parse_args()
    
    app.run(host=args.host, port=args.port, debug=True)
    
if __name__ == "__main__":
    main()