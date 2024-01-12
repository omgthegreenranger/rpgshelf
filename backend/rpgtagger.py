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

        ## we should add the RPG system search to the database for storage

    # ----- Narrow Prompt Search
    nsearch = 0
    nmethod = "family"

    # provide list of assets related to this game
    # print(bresult["item"])
    nsearchterm = input("Please select game:")
    b_found = bresult["item"][int(nsearchterm)]

    # put details of 

    # print("DETAILS", game_details)

    # selectGame = sqlite_scripts.GameDB.isPresent([b_found["@id"], "games"])
    # print("Object!", game_obj)
    nargs = [nmethod, nsearch, int(b_found["@id"])]
    nresult = narrowSearch(*nargs)
    # print(nresult)
    nresult_items = nresult["link"]
    
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
    # print(eselected)
    eargs = eselected
    eresult = exactSearch(*eargs)
    # print(eresult)

    game_obj = classes.gameObj(nresult, nresult_items, eresult)
    print(game_obj.__dict__)
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
