import sqlite3
import json

sqlcon = sqlite3.connect("rpgshelf.db")
cur = sqlcon.cursor()

# Don't forget to add in the check whether the game or book is already added
# def sqlPrepare(*args) :
    
class sqlObject :
    def __init__(self, bookData, gameData) :
        self.bookData = bookData,
        self.gameData = gameData

    def sqlBook(self):
        print(json.dumps(self.bookData['item']))
        links = self.bookData['link']
        categories = []
        publishers = []
        artists = []
        designers = []
        producers = []
        book = { 
            # 'name': bookData["name"]["@value"],
            'categories': categories,
            'publishers': publishers,
            'designers': designers,
            'artists': artists,
            'producers': producers}

        for link in links :         
            if link['@type'] == 'rpgcategory' : 
                categories.append(link['@value'])
            if link['@type'] == 'rpgpublisher' :
                publishers.append(link['@value'])
            if link['@type'] == 'rpgartist' :
                artists.append(link['@value'])
            if link['@type'] == 'rpgdesigner' :
                designers.append(link['@value'])
            if link['@type'] == 'rpgproducers' :
                producers.append(link['@value'])

    def printBook(self):
        print(self.bookData)

class sqlGame(sqlObject):
    def __init__(self, gameData) :
        super().__init_(gameData)
        self.gameData = gameData

    # def printGame(self):
    #     print(self)


# def sqlAdd(game, book, library) :
#     print("Game", game)
#     print("Book", book)
#     print("Library", library)
#     res = cur.execute("SELECT  FROM sqlite_master")
#     print(res.fetchall())
    
#     return
    

# CREATE TABLE games(gid, name, rid, system, rules, publisher, year)
# CREATE TABLE library(gid, bid, brid, type, path, image)