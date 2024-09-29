import sqlite3
import json
import classes
import sqlalchemy
from flask import session

sqlcon = sqlite3.connect("rpgshelf.db")
cur = sqlcon.cursor()


# Don't forget to add in the check whether the game or book is already added
# def sqlPrepare(*args) :

def getGameObj(args) :
    gameInfo = cur.execute("SELECT * FROM games WHERE rid = ?", (args,)).fetchall()
    try :
        libraryInfo = cur.execute("SELECT * FROM library WHERE gid = ?", (str(gameInfo['gid']),))
    except : 
        libraryInfo = []

    # print(gameInfo)
    # print(libraryInfo)
    return {"game": gameInfo, "library": libraryInfo}



def isPresent(args):
    # this is the "exists checker" where True is present.
    
    print("Here!", args['@id'])
    exec = cur.execute(
        "SELECT * FROM games WHERE rid = ?", (str(args['@id']),)
    ).fetchall()
    if exec == []:
        return False
    elif exec != []:
        return True

def addGame(args):
    # this adds the game to the games database
    print(args)
    print("*** Adding to database")
    add = cur.execute("INSERT INTO games (gid,name,rid,system,rules,description,publisher,year) VALUES (?,?,?,?,?,?,?,?)")
    return

def addSystem(*args) :
    # Add the system to the database and start load of all books.
    print(systemLibrary.__dict__)
    print("System Add \n", args)
    confirm = "Confirmed"
    return confirm


