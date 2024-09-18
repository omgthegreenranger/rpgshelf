import db.sqlite_scripts

#this is the game (i.e. the actual system) being used.

class systemObj():
    def __init__(self, data, method):
        print("Object data", data)
        # print(isinstance(data['name'],list))
        if method == "api" :
            if(isinstance(data['name'],list)) :
                self.name = data['name'][0]['@value']
            else :
                self.name = data['name']['@value']
            self.rid = data['@id']
            self.library = []
            # self.gid = 
            self.system = []
            for x in data['link'] :
                if x['@type'] == 'rpgsystem' :
                    self.system = x['@value']
            self.description = data['description']
            self.image = data['image']
        if method == "db" :
            self.name = data["game"]["name"]
            self.rid = data["game"]["rid"]
            self.library = data['library']
            # self.gid = 
            self.system = data["game"]["system"]
            self.description = data['description']
            self.image = data['image']
        return
    
    def systemGet(self) : # access the system data from the library, if present
        return

    def bookGet(self) : #use this to retrive library for game
        return

    def systemAdd(self, data) : # to add a new game system/create new object
        # this requires all of the data to add the new system.
        return

    def addBook(self, book) : # to add a new book to the object's library
        #print("Here we go!", book)
        publishers = []
        designers = []
        artists = []
        producers = []
        bookName = ""
        for bookData in book['link'] :
            if bookData['@type'] == 'rpgpublisher' :
                publishers.append(bookData['@value'])
            if bookData['@type'] == 'rpgdesigner' :
                designers.append(bookData['@value'])
            if bookData['@type'] == 'rpgartist' :
                artists.append(bookData['@value'])
            if bookData['@type'] == 'rpgproducer' :
                producers.append(bookData['@value'])

        # Do a check in case the book has alternate titles
        # TODO FOR UI: allow for selection of title to use.

        if isinstance(book['name'], list) == True :
            for bookData in book['name'] :
                if bookData['@type'] == 'primary' :
                    bookName = bookData['@value']
        if isinstance(book['name'], list) == False : 
            bookName = book['name']['@value']

        self.library.append(
            {
                "rid" : self.rid,
                "name": bookName,
                "bid": book['@id'],
                #"series": book['seriescode']['@value'].rsplit(" ", 1),
                "publisher": publishers,
                "designers": designers,
                "artists": artists,
                "producers": producers,
                "year": book['yearpublished']['@value'],
                "description": book['description'],
                #"image": book['image'],
                #"thumbnail": book['thumbnail']
            }
        )


        return

# class campaignObj(): #TODO: this is the object created for whatever campaign is being used.
#     return