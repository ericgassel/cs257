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


def execute_query(cursor, query):
    
    try:
        cursor.execute(query)
    except Exception as e:
        print (e)
        exit()
    
    return cursor.fetchall()


@app.route('/games')
def get_games():
    '''
    REQUEST: /games
    
    RESPONSE: a JSON list of dictionaries, each of which represents one Olympic games, sorted by year. Each dictionary in this list will have the following fields.
    
        id -- (INTEGER) a unique identifier for the games in question
        year -- (INTEGER) the 4-digit year in which the games were held (e.g. 1992)
        season -- (TEXT) the season of the games (either "Summer" or "Winter")
        city -- (TEXT) the host city (e.g. "Barcelona")
    '''
    
    query = 'SELECT * FROM games ORDER BY years ASC'
    games_list = []
    
    connection = establish_database_connection()
    cursor = execute_query(connection.cursor(), query)
        
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
    '''
    REQUEST: /nocs

    RESPONSE: a JSON list of dictionaries, each of which represents one National Olympic Committee, alphabetized by NOC abbreviation. Each dictionary in this list will have the following fields.

       abbreviation -- (TEXT) the NOC's abbreviation (e.g. "USA", "MEX", "CAN", etc.)
       name -- (TEXT) the NOC's full name (see the noc_regions.csv file)
    '''

    query = 'SELECT abbre, name FROM nocs'

    connection = establish_database_connection()
    cursor = execute_query(connection.cursor(), query)

    noc_list = []
    for noc in cursor:
        abbreviation = noc[0]
        country = noc[1]
        noc_list.append({'noc':abbreviation, 'country':country})
    
    connection.close()

    return json.dumps(noc_list)

@app.route('/medalists/games/<games_id>')
def get_medals_winner_list(games_id):
    '''
    REQUEST: /medalists/games/<games_id>?[noc=noc_abbreviation]

    RESPONSE: a JSON list of dictionaries, each representing one athlete
    who earned a medal in the specified games. Each dictionary will have the
    following fields.

       athlete_id -- (INTEGER) a unique identifier for the athlete
       athlete_name -- (INTEGER) a unique identifier for the athlete
       athlete_sex -- (TEXT) the athlete's sex as specified in the database ("F" or "M")
       sport -- (TEXT) the name of the sport in which the medal was earned
       event -- (TEXT) the name of the event in which the medal was earned
       medal -- (TEXT) the type of medal ("gold", "silver", or "bronze")

    If the GET parameter noc=noc_abbreviation is present, this endpoint will return only those medalists who were on the specified NOC's team during the specified games.
    '''

    query = f'''SELECT athletes.id, athletes.names, athletes.sex, events.sports, 
        events.events, athletes_total.medal, athletes_games.team
        FROM athletes, events, athletes_total, games, athletes_games
        WHERE games.id = {games_id}
        AND athletes.id = athletes_games.athletes_id
        AND games.id = athletes_games.games_id
        AND athletes_total.events_id = events.id
        AND (athletes_total.medal = 'Gold' OR  athletes_total.medal = 'Silver' OR athletes_total.medal = 'Bronze')
        AND athletes_total.athletes_games_id = athletes_games.id
        ORDER BY events.events;
    '''

    connection = establish_database_connection()
    cursor = execute_query(connection.cursor(), query)
    
    games_list = []
    noc_request = flask.request.args.get('noc')
    
    for game in cursor:
        athlete_id = game[0]
        athlete_name = game[1]
        sex = game[2]
        sport = game[3]
        events = game[4]
        medal = game[5]
        noc = game[6]
        if noc_request != None:
            if noc == noc_request:
                games_list.append({'athlete_id':athlete_id, 'athlete_name':athlete_name, 'sex': sex, 'sport':sport, 'event':events, 'medal':medal})
            continue
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