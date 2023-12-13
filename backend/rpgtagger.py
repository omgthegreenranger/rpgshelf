# Main code for running the tagger itself.

# Directory/File select
# Begin URL preparation


# Initial Search Program

import getFiles
import pdfreader
import configparser
import sqlite

args = {}
sel = 0

# pdfreader.pdfsearch()
# print(pdfreader.qsearchterms)

# search and select game
def init() :
    search()
    return


def search() :
    qmethod = "search"
    rsearch = 1
    #search for game system
    qsearch = 0
    qsearchterms = input("Enter RPG name: ")
    args = [qmethod, qsearch, qsearchterms, rsearch]
    qresult = getFiles.broadSearch(*args)


    # search for specific book
    gsearchterm = input("Please select game:")

    # search and select book - preserve list for have/missing 
    
    nsearch = 0
    nmethod = "family"
    gresult = getFiles.narrowSearch(nmethod, nsearch, qresult[int(gsearchterm)], rsearch)
          
    # gselected = [gresult['item'][int(gsearchterm)]["@id"], rpg_dict['item'][int(gsearchterm)]['name']['@value']]
    # print(sqlite.sqlAdd(qresult, gresult[0], gresult[1]))


# rpg_selector = getFiles.apiSelect()
# print(qresult)


init()