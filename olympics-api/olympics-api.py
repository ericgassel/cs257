#Eric Gassel & Martin Bernard

import sys
import argparse
import flask
import json
import psycopg2

app = flask.Flask(__name__)

def establish_database_connection():
  
    from config import password
    from config import database
    from config import user
    
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
    

def main():

    #connection = establish_database_connection()
    #cursor = connection.cursor()
    
    parser = argparse.ArgumentParser('An Olympics Flask application/API')
    parser.add_argument('host', help='the host on which this application is running')
    parser.add_argument('port', type=int, help='the port on which this application is listening')
    args = parser.parse_args()
    
    app.run(host=args.host, port=args.port, debug=True)
    
    #connection.close()
    
if __name__ == "__main__":
    main()