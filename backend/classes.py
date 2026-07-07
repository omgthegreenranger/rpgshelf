import db.sqlite_scripts
import globals
import json
#this is the game (i.e. the actual system) being used.

class systemObj():
    def __init__(self, data, method):
        print("Object data", data['name'])
        print(isinstance(data['name'],list))
        if method == "api" :
            if(isinstance(data['name'],list)) :
                self.name = data['name'][0]['@value']
            else :
                self.name = data['name']['@value']
            self.rid = data['@id']
            self.library = data['link']
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
    
    # def systemGet(self) : # access the system data from the library, if present
        return

    # def bookGet(self) : #use this to retrive library for game
        return

    # def systemAdd(self, data) : # to add a new game system/create new object
        # this requires all of the data to add the new system.
        return

    # def addBook(self, book) : # to add a new book to the object's library
    #     #print("Here we go!", book)
    #     publishers = []
    #     designers = []
    #     artists = []
    #     producers = []
    #     bookName = ""
    #     for bookData in book['link'] :
    #         if bookData['@type'] == 'rpgpublisher' :
    #             publishers.append(bookData['@value'])
    #         if bookData['@type'] == 'rpgdesigner' :
    #             designers.append(bookData['@value'])
    #         if bookData['@type'] == 'rpgartist' :
    #             artists.append(bookData['@value'])
    #         if bookData['@type'] == 'rpgproducer' :
    #             producers.append(bookData['@value'])

    #     # Do a check in case the book has alternate titles
    #     # TODO FOR UI: allow for selection of title to use.

    #     if isinstance(book['name'], list) == True :
    #         for bookData in book['name'] :
    #             if bookData['@type'] == 'primary' :
    #                 bookName = bookData['@value']
    #     if isinstance(book['name'], list) == False : 
    #         bookName = book['name']['@value']

    #     self.library.append(
    #         {
    #             "rid" : self.rid,
    #             "name": bookName,
    #             "bid": book['@id'],
    #             #"series": book['seriescode']['@value'].rsplit(" ", 1),
    #             "publisher": publishers,
    #             "designers": designers,
    #             "artists": artists,
    #             "producers": producers,
    #             "year": book['yearpublished']['@value'],
    #             "description": book['description'],
    #             #"image": book['image'],
    #             #"thumbnail": book['thumbnail']
    #         }
    #     )

        #return
# class campaignObj(): #TODO: this is the object created for whatever campaign is being used.
#     return



class Book() : # to add a new book to the object's library
    def __init__(self, data):
        print("Here we go!", data)
        publishers = []
        designers = []
        artists = []
        producers = []
        bookName = ""
        for bookData in data['link'] :
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

        if isinstance(data['name'], list) == True :
            for bookData in data['name'] :
                if bookData['@type'] == 'primary' :
                    bookName = bookData['@value']
        if isinstance(data['name'], list) == False : 
            bookName = data['name']['@value']

        self.library.append(
            {
                "rid" : self.rid,
                "name": bookName,
                "bid": data['@id'],
                #"series": book['seriescode']['@value'].rsplit(" ", 1),
                "publisher": publishers,
                "designers": designers,
                "artists": artists,
                "producers": producers,
                "year": data['yearpublished']['@value'],
                "description": data['description'],
                "image": data['image'],
                "thumbnail": data['thumbnail']
            }
        )
        return

class Directory(): #for the file searching
    def __init__(self, data):
        print(data, "THIS IS THE DATA")
            # parent_root = str("/home/shaggy/Documents/RPG_Library/Gamma World")
        parent_root = globals.scan
        # files = Path(globals.scan).walk(top_down=True, on_error=print)
        # results = DirectoryTree(files)
        # results = []
        # print(files)
        for root, dirs, files in data:
            if(str(root) == parent_root):
                filenames = []
                for file in files:
                    filenames.append(str(root) + "/" + file)
                dirnames = []
                for direc in dirs:
                    dirnames.append(str(root) + "/" + direc)
                self.name = str(root.name)
                self.parent = str(root.parent)
                # results.append({str(root.name):{"Subdirs": dirnames, "Files": filenames }})
        print(self)    
        return