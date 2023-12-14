import sqlite3

sqlcon = sqlite3.connect("rpgshelf.db")
cur = sqlcon.cursor()

# Don't forget to add in the check whether the game or book is already added

def sqlAdd(game, book, library) :
    print("Game", game)
    print("Book", book)
    print("Library", library)
    res = cur.execute("SELECT  FROM sqlite_master")
    print(res.fetchall())
    
    return
    

# CREATE TABLE games(gid, name, rid, system, rules, publisher, year)
# CREATE TABLE library(gid, bid, brid, type, path, image)