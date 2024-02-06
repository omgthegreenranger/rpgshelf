# GetFiles.py will search the selected directory and produce a list of files in the directory
# It will also split the names from the extension and remove any hyphens in order to do a file search.
# If RPGGeek allows for accessing cover images, perhaps search by image recognition - prepare first-page image for search.

# try for Git submit.

import urllib
import requests
import xmltodict
import json
import xml
import db.sqlite_scripts
import classes
import db.sqlalchemy_models

global rpg_json_parse
global rpg_dict
search_path = "https://rpggeek.com/xmlapi2/"
rsearch = 1
searchParams = ["rpg", "rpgitem", "family","thing"]


# this object will be the gameObj itself. We're going to cross to the database and, if it isn't present, add it.
# TODO: add more search options (author, publisher, etc., or do narrow title search)

def broadSearch(*args) : # current args: 
    # - method (search, family, thing)
    # - search (digit for searchParams)
    # - searchitems(terms for searching *SEARCH METHOD ONLY*)
    
    search = search_path + args[0]
    args = {"query": args[2], "type": searchParams[0]}
    rpgg = requests.get(search, params=args)
    print(rpgg.url)
    rpg_dict = xmltodict.parse(rpgg.text)["items"]
    bsearched = []

    qselect = ''

    # # export to JSON for testing
    # rpgjson = open("JSONboardtest.json", "w")
    # rpgjson.write(json.dumps(bsearched))
    # rpgjson.close()
    # return qselect, bsearched, rpg_dict
    return rpg_dict

def narrowSearch(*args):
    search = search_path + args[0]
    args = {"id" : args[2], "type": searchParams[args[1]]}

    rpgg = requests.get(search, params=args)
    rpg_dict = xmltodict.parse(rpgg.text)["items"]["item"]
    rpg_json_parse = json.dumps(rpg_dict)

    # Exported to JSON for a missing list or testing
    # rpgjson = open("JSONnarrowtest.json", "w")
    # rpgjson.write(json.dumps(rsearched))
    # rpgjson.close()
    # print(rpg_dict)
    return rpg_dict

def exactSearch(*args) : 
    print("Exact Search begins")
    search = search_path + searchParams[3]
    eargs = {"id" : args[0], type : args[2]}
    e_rpg = requests.get(search, params=eargs)
    e_rpg_dict = xmltodict.parse(e_rpg.text)["items"]["item"]
    e_rpg_json_parse = json.dumps(e_rpg_dict)

    # Uncomment this if you want all results exported to JSON for a missing list
    # rpgjson = open("JSONexacttest.json", "w")
    # rpgjson.write(e_rpg_json_parse)
    # rpgjson.close()
    # print(e_rpg_dict)
    return e_rpg_dict
