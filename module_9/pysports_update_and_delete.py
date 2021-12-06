import mysql.connector 
from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "MySQLIsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database".format(config["user"], config["host"], config["database"]))

    cursor = db.cursor()

    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM players INNER JOIN team ON players.team_id = team.team_id;")

    player = cursor.fetchall()

    print("-- DISPLAYING PLAYERS AFTER DELETE --")

    for players in player:
        print("Player ID: {}".format(players[0]))
        print("First Name: {}".format(players[1]))
        print("Last Name: {}".format(players[2]))
        print("Team Name: {}".format(players[3]))
        print("")
    
    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    db.close()