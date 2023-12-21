# Main code for running the tagger itself.

# Directory/File select
# Begin URL preparation


# Initial Search Program

from apiSearch import broadSearch, narrowSearch, exactSearch
import pdfreader
import configparser
import sqlite_scripts
import classes

args = {}
sel = 0


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
            int(bresult[2]["@total"]) == 0
        ):  # if total results in response = 0, return to prompt
            print("Hello this failed.")

        else:  # otherwise, set b_loop to True and pass dict filtered to "item"
            b_loop = True
            bresult = bresult[1]

        ## we should add the RPG system search to the database for storage

    # ----- Narrow Prompt Search
    nsearch = 0
    nmethod = "family"

    # provide list of assets related to this game

    nsearchterm = input("Please select game:")
    b_found = bresult[int(nsearchterm)]

    game_obj = classes.gameObj(b_found)
    # selectGame = sqlite_scripts.GameDB.isPresent([b_found["@id"], "games"])
    print("OBject!", game_obj)
    nargs = [nmethod, nsearch, int(b_found["@id"])]
    nresult = narrowSearch(*nargs)

    # narrow search prompt from above list.
    esearchterm = input("Please select book:")
    eselected = nresult[int(esearchterm)]["@id"], nresult[int(esearchterm)]["@value"]

    eargs = eselected
    eresult = exactSearch(*eargs)

    # submitobject = sqlite_scripts.sqlObject(eresult, bresult)

    # print("*** book object title ***")
    # print(submitobject.sqlBook()['@value'])

    # print("******", "******")
    # print("*****", "*****")
    # print("**** Categories ****")
    # # print(eresults_categories)

    # print("Broad found", b_found)
    # # print("Exact found", eselected)


init()
