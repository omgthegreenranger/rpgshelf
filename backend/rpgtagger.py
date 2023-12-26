# Main code for running the tagger itself.

# Directory/File select
# Begin URL preparation


# Initial Search Program

from apiSearch import broadSearch, narrowSearch, exactSearch
import pdfreader
import configparser
import sqlite_scripts

args = {}
sel = 0

# search and select game
def init() :
    singleSearch()
    return

# standard single-book search function
def singleSearch() :
    b_loop = False

    while b_loop is not True:
        #set initial parameters for broad search
        bmethod = "search"
        bsearch = 0

        #initial search prompt - look for parent game
        bsearchterms = input("Enter RPG name: ")
        bargs = [bmethod, bsearch, bsearchterms]
        bresult = broadSearch(*bargs)
        b_total = bresult[0]
        b_results = bresult[1]
        print(b_results)
        if int(b_total[0]) == 0 : # if total results in response = 0, return to prompt
            print("Hello this failed.")
        
        else : # otherwise, set b_loop to True and pass dict filtered to "item"
            b_loop = True
            bresult = b_results['item']


    # ----- Narrow Prompt Search
    nsearch = 0
    nmethod = "family"

        # provide list of assets related to this game

    nsearchterm = input("Please select game:")
    print(bresult[0])
    b_found = bresult[int(nsearchterm)]
    print(b_found['@id'])
    nargs = [nmethod, nsearch, int(b_found['@id'])]
    nresult = narrowSearch(*nargs)
    
        # narrow search prompt from above list.
    esearchterm = input("Please select book:")
    eselected = nresult[int(esearchterm)]["@id"], nresult[int(esearchterm)]['@value']

    eargs = eselected
    eresult = exactSearch(*eargs)
    
    submitobject = sqlite_scripts.sqlObject(eresult, bresult)

    print("*** book object title ***")
    print(submitobject.sqlBook()['@value'])

    print("******", "******")
    print("*****", "*****")
    print("**** Categories ****")
    # print(eresults_categories)

    print("Broad found", b_found)
    # print("Exact found", eselected)

init()