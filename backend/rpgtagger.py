# Main code for running the tagger itself.

# Directory/File select
# Begin URL preparation


# Initial Search Program

from apiSearch import broadSearch, narrowSearch, exactSearch
import pdfreader
import configparser
import db.sqlite_scripts
import classes

args = {}
sel = 0
gameID = ''

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
    
    # search SQL database for existing game, and load that data instead

    gameInfo = db.sqlite_scripts.getGameObj(nresult['@id'])
#     gameInfo = {
#   "game": {
#   "name": "Star Trek Adventures",
#   "rid": "37049",
#   "system": "2d20 System"
#   },
#   "library": [
#     [
#       {
#         "name": "Deep Space Nine Player Characters",
#         "bid": "261888",
#         "publisher": [
#           "Modiphius Entertainment"
#         ],
#         "designers": [
#           "Nathan Dowdell",
#           "Jacob Ross"
#         ],
#         "artists": [
#           "Matthew Comben"
#         ],
#         "producers": [
#           "Salwa Azar",
#           "Chris Birch",
#           "Michal E. Cross",
#           "Steve Daldry",
#           "Sam Webb"
#         ],
#         "year": "2018",
#         "description": "From publisher blurb:&#10;&#10;This PDF contains statistics for the crew and residents of Deep Space 9, including Captain Sisko, Major Kira Nerys, Lt. Commander Worf, Chief Miles O'Brien, Lieutenant Jadzia Dax, Dr. Julian Bashir, Constable Odo, Quark, and Elim Garak as well as the game statistics for the Deep Space 9 and the U.S.S. Defiant, and rules for Changelings and Ferengi as playable species.&#10;&#10;"
#       }
#     ]
#   ],
#   "system": [],
#   "description": "Description from the publisher:&#10;&#10;Star Trek Adventures uses the Modiphius 2d20 game system (Mutant Chronicles, Infinity, Conan, John Carter of Mars) designed by Jay Little (Star Wars: Edge of the Empire, X-Wing Miniatures Game). Modiphius is also sculpting an accompanying Star Trek miniature figure line, the first to be produced in seventeen years. Resin and metal 32mm-scale hobby figures will feature classic Star Trek characters and crews, boarding parties, and away teams. Geomorphic tile maps of burning Federation ships, mysterious colonies and embattled Klingon cruisers will set the scene for dramatic new voyages in the Final Frontier.&#10; Under license by CBS Consumer Products, Star Trek Adventures is slated for a mid-2017 release and the playtest crews will be listed in the Star Trek Adventures book manifest.&#10;&#10;"
# }

    # TODO: Make this better, I don't like the hacky way it works.

    system_result = []
    method = ''
    if gameInfo['game'] == [] :
        system_result = nresult
        print("New one!")
        method = "api"
    else :
        system_result = gameInfo
        print("Yessir!")
        method = "db"
    
    system_obj = classes.systemObj(system_result, method)

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
    book_obj = system_obj.addBook(eresult)
    print(system_obj.__dict__)
    # submitobject = sqlite_scripts.sqlObject(eresult, bresult)

    # print("*** book object title ***")
    # print(submitobject.sqlBook()['@value'])

    # print("******", "******")
    # print("*****", "*****")
    # print("**** Categories ****")
    # # print(eresults_categories)

    # print("Broad found", b_found)
    # # print("Exact found", eselected)


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
