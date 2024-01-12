import sqlite_scripts

class gameTop:
    def __init__(self, args) :
        print("CHECK", args)
        gameInfo = sqlite_scripts.getGameObj(args['@id'])
        self.game = gameInfo['game']
        self.library = gameInfo['library']
        return

class gameObj(gameTop):
    def __init__(self, game):
        super().__init__(game)
        print("ARGS", game)
        # super().__init_(gameTop)
        self.name = game['name']
        # self.gid = gid
        self.rid = game['@id']
        self.system = system
        self.rules = rules
        self.description = description
        self.publisher = publisher
        self.year = year
        return
    
    def checkGame(args):
        check = sqlite_scripts.isPresent(args)
        print(check)
        return check

class bookObj(gameObj):
    def __init__(self, bid, brid, type, description, path, image) :
        return
