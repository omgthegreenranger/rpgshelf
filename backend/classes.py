import sqlite_scripts


#this is the game (i.e. the actual system) being used.
class systemObj():
    def __init__(self, data):
        self.name = data['name'][0]['@value']
        self.gid = data['@id']
        self.library = []
        # self.rid = game['@id']
        self.system = []
        for x in data['link'] :
            if x['@type'] == 'rpgsystem' :
                self.system = x['@value']
        self.description = data['description']
        return
    
    def addBook(self, book) :
        publishers = []
        designers = []
        artists = []
        producers = []
        for bookData in book['link'] :
            if bookData['@type'] == 'rpgpublisher' :
                publishers.append(bookData['@value'])
            if bookData['@type'] == 'rpgdesigner' :
                designers.append(bookData['@value'])
            if bookData['@type'] == 'rpgartist' :
                artists.append(bookData['@value'])
            if bookData['@type'] == 'rpgproducer' :
                producers.append(bookData['@value'])
        self.library.append(
            [{
                "name": book['name']['@value'],
                "bid": book['@id'],
                "publisher": publishers,
                "designers": designers,
                "artists": artists,
                "producers": producers,
                "year": book['yearpublished'],
                "description": book['description']
            }
            ]
        )


        return

    def checkGame(args):
        check = sqlite_scripts.isPresent(args)
        print(check)
        return check
    

# this class is for the book itself - we'll link it to the game class.
class bookObj():
    def __init__(self, data, gameID) :
        
        return
