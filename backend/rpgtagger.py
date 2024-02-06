# Main code for running the tagger itself.

# Directory/File select
# Begin URL preparation


# Initial Search Program

from apiSearch import broadSearch, narrowSearch, exactSearch
import pdfreader
import configparser
import db.sqlite_scripts
import db.sqlalchemy_models
import classes
from sqlalchemy.orm import sessionmaker
import treelib
args = {}
sel = 0
gameID = ''


systemsObj = db.sqlalchemy_models.System
bookObj = db.sqlalchemy_models.Book
# search and select game
def init():
    singleSearch()
    return


# standard single-book search function
def singleSearch():
    b_loop = False

    while b_loop != True:
        # set initial parameters for broad search
        bmethod = "search"
        bsearch = 0

        # initial search prompt - look for parent game
        bsearchterms = input("Enter RPG name: ")
        bargs = [bmethod, bsearch, bsearchterms]
        bresult = broadSearch(*bargs)

        if (
            int(bresult["@total"]) == 0
        ):  # if total results in response = 0, return to prompt
            print("Hello this failed.")

        else:  # otherwise, set b_loop to True and pass dict filtered to "item"
            broadSearchResults(bresult)
            b_loop = True

        ## TODO: we should add the RPG system search to the database for storage

    # ----- Narrow Prompt Search
    nsearch = 0
    nmethod = "family"

    # provide list of assets related to this game
    nsearchterm = input("Please select game:")
    b_found = bresult["item"][int(nsearchterm)]


    # selectGame = sqlite_scripts.GameDB.isPresent([b_found["@id"], "games"])
    # print("Object!", game_obj)
    nargs = [nmethod, nsearch, int(b_found["@id"])]
    nresult = narrowSearch(*nargs)
    nresult_items = nresult["link"]
    # print(nresult)
    # search SQL database for existing game, and load that data instead

    # gameInfo = db.sqlite_scripts.getGameObj(nresult['@id'])
    gameInfo = []
    # TODO: Make this better, I don't like the hacky way it works.

    system_result = []
    method = ''
    # if gameInfo['game'] == [] :
    #     system_result = nresult
    #     print("New one!")
    #     method = "api"
    # else :
    #     system_result = gameInfo
    #     print("Yessir!")
    #     method = "db"
    
    
    # system_obj = classes.systemObj(system_result, method)

    system =''
    for x in nresult_items :
        if x['@type'] == 'rpgsystem' :
            system = x['@value']

    systemobj = systemsObj(
        system_name = nresult['name'][0]['@value'],
        rid = nresult['@id'],
        system = system,
        description = nresult['description']
    )


    db.sqlalchemy_models.session.add(systemobj)
    db.sqlalchemy_models.session.commit()
    system_gid = systemobj.gid
    print(system_gid)
    # take nresult
    # to provide prompt.
    sel = 0
    for item in nresult_items:
        if item["@type"] == "rpg":
            id = item["@id"]
            name = item["@value"]
            bselect = [name, id]
            print(sel, name)
            # rsearched.append(item)
            sel += 1
    # narrow search prompt from above list.
    esearchterm = input("Please select book:")
    eselected = nresult_items[int(esearchterm)]["@id"], nresult_items[int(esearchterm)]["@value"], "rpgitem"

    eargs = eselected
    eresult = exactSearch(*eargs)

    publishers = []
    designers = []
    artists = []
    producers = []
    for bookData in eresult['link'] :
        if bookData['@type'] == 'rpgpublisher' :
            publishers.append(bookData['@value'])
        if bookData['@type'] == 'rpgdesigner' :
            designers.append(bookData['@value'])
        if bookData['@type'] == 'rpgartist' :
            artists.append(bookData['@value'])
        if bookData['@type'] == 'rpgproducer' :
            producers.append(bookData['@value']),


    book_obj = bookObj(        
        brid = eresult['@id'],
        system_gid = systemobj.gid,
        book_title= eresult['name']['@value'],
        publisher = publishers,
        designers = designers,
        artists = artists,
        producers = producers,
        year = eresult['yearpublished']['@value'],
        description = eresult['description'])

    # print(book_obj)
    db.sqlalchemy_models.session.add(book_obj)
    # print(systemobj in db.sqlalchemy_models.session, )
    db.sqlalchemy_models.session.commit(book_obj)

    # db.sqlalchemy_models.submitBook()
    # submitobject = sqlite_scripts.sqlObject(eresult, bresult)



def broadSearchResults(bresult):
    if int(bresult["@total"]) == 0:
        print("False!")
        return
    else:
        sel = 0
        if isinstance(bresult["item"], list):
            # There are multiple items
            for item in bresult["item"]:
                # print(item)
                id = item["@id"]
                name = item["name"]["@value"]
                # qselect.append(item)
                print(sel, name)
                sel += 1
        else:
            # There is only one item
            item = bresult["item"]
            # print("One item", item)
            id = item["@id"]
            name = item["name"]["@value"]
            # qselect.append(item)
            print(sel, name)
        return
    

init()
