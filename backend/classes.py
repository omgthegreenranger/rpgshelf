import sqlite_scripts


#this is the game (i.e. the actual system) being used.
class systemObj():
    def __init__(self, data):
        self.name = data['name'][0]['@value']
        self.rid = data['@id']
        self.library = []
        # self.gid = 
        self.system = []
        for x in data['link'] :
            if x['@type'] == 'rpgsystem' :
                self.system = x['@value']
        self.description = data['description']
        return
    
    def systemRetriever(self) : # access the system data from the library, if present
        return

    def bookRetrieve(self) : #use this to retrive library for game
        return

    def addGame(self, data) : # to add a new game system/create new object
        return

    def addBook(self, book) : # to add a new book to the object's library
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
                "rid" : rid,
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

class campaignObj() : #TODO: this is the object created for whatever campaign is being used.
    return