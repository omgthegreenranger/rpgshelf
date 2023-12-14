# Main code for running the tagger itself.

# Directory/File select
# Begin URL preparation


# Initial Search Program

from apiSearch import broadSearch, narrowSearch, exactSearch
import pdfreader
import configparser
import sqlite

args = {}
sel = 0

# search and select game
def init() :
    singleSearch()
    return

# standard single-book search function
def singleSearch() :
    b_loop = False

    while b_loop == False:
        #set initial parameters for broad search
        bmethod = "search"
        bsearch = 0

        #initial search prompt - look for parent game
        bsearchterms = input("Enter RPG name: ")
        bargs = [bmethod, bsearch, bsearchterms]
        bresult = broadSearch(*bargs)
        # print(bresult)
        if int(bresult['@total']) == 0 :
            print("Hello this failed.")
        else :
            b_loop = True
            bresult = bresult['item']


    # with that done, search for specific book to this one file
    # set parameters
    nsearch = 0
    nmethod = "family"
    # narrow search prompt - find the book from the list
    nsearchterm = input("Please select game:")
    b_found = bresult[int(nsearchterm)]
    print(b_found['@id'])
    nargs = [nmethod, nsearch, int(b_found['@id'])]
    nresult = narrowSearch(*nargs)
    
    esearchterm = input("Please select book:")
    eselected = nresult[int(esearchterm)]["@id"], nresult[int(esearchterm)]['@value']

    eargs = eselected
    eresult = exactSearch(*eargs)
    eresult_name = eresult["name"]
    eresult_links = eresult["link"]

    print(eresult_name["@value"])
    
    for x in eresult_links : 
        if x['@type'] == 'rpgcategory' : 
        
            print("Okay", x['@value'])

    print("Broad found", b_found)
    print("Exact found", eselected)

init()