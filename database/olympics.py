#Author: Eric Gassel

import argparse
import psycopg2

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
 

def get_parsed_arguments():
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-anoc', '--athletes_from_noc', nargs = 1, type = str, metavar = '', help = 'Returns a list of the names of all the athletes from a specified NOC')
    parser.add_argument('-gnoc', '--gold_medals_from_noc', action = 'store_true', help = 'Returns a list of all the NOCs and the number of gold medals they have won, in decreasing order of the number of gold medals')
    parser.add_argument('-la', '--lightest_athletes', action = 'store_true', help = 'Returns a list of the 30 lightest athletes')
    
    args = parser.parse_args()
    
    return args


def execute_athletes_from_noc_query(cursor, noc):
    
    query = 'SELECT athletes.names FROM athletes, athletes_games   WHERE athletes.id = athletes_games.athletes_id AND athletes_games.NOC = %s'
  
    try:
        cursor.execute(query, (noc,))
    except Exception as e:
        print (e)
        exit()
    
    print('======All athletes that have competed in the following NOC: {} ======'.format(noc))
    for row in cursor:
        print('-', row[0])
    print()
    
    return

def execute_gold_medals_from_noc(cursor):
    
    query = 'SELECT athletes_games.NOC, COUNT(athletes_total.medal) FROM athletes_games, athletes_total WHERE athletes_games.id = athletes_total.athletes_games_id AND athletes_total.medal = %s GROUP BY athletes_games.NOC ORDER BY COUNT(athletes_total.medal) ASC;'
    
    try:
        cursor.execute(query, ('Gold',))
    except Exception as e:
        print(e)
        exit()
        
    print('====== All NOCs ordered by the number of gold medals won ======')
    for row in cursor:
        print(row[0], ' - ', row[1])
    print()
    
    return

def execute_lightest_athletes(cursor):
    
    query = 'SELECT athletes.names, athletes.weight FROM athletes ORDER BY athletes.weight LIMIT 30'
    
    try:
        cursor.execute(query)
    except Exception as e:
        print(e)
        exit()
    
    print('====== The thirty lightest athletes ======')
    for row in cursor:
        print(row[0], ' - ', row[1])
    print()
    
    return

def main():

    connection = establish_database_connection()
    cursor = connection.cursor()
    args = get_parsed_arguments()
    
    if args.athletes_from_noc != None:
        execute_athletes_from_noc_query(cursor, args.athletes_from_noc)
    if args.gold_medals_from_noc:
        execute_gold_medals_from_noc(cursor)
    if args.lightest_athletes:
        execute_lightest_athletes(cursor)
        
    connection.close()
    

if __name__ == "__main__":
    main()

