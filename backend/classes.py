import sqlite_scripts

class gameTop:
    def __init__(self, data, gameID, bookID) :
        # print("CHECK", args)
        gameInfo = args
        self.data = data
        self.gameID = gameID

        return

class gameObj(gameTop):
    # def __init__(self, game, library, book):
    #     self.name = game['name'][0]['@value']
    #     # self.gid = game['@id']
    #     # self.library = library
    #     # self.game = game
    #     self.rid = game['@id']
    #     # self.system = game['link']['rpgmechanic']
    #     # self.rules = rules
    #     self.description = game['description']
    #     # self.publisher = publisher
    #     # self.year = year
    #     self.book = {"book": book['name']['@value'] }
    #     # print("LIBRARY", library)
    #     # print(self.gid)
    #     return
    
    def __init__(self, data, gameID, bookID) :
        super().__init__(data, gameID)

    def checkGame(args):
        check = sqlite_scripts.isPresent(args)
        print(check)
        return check
    
    # def __repr__(self):
    #     return self

    # def __str__(self):
    #     return self

class bookObj(gameTop):
    def __init__(data, gameID, bookID) :
        super().__init__(game)
        return
