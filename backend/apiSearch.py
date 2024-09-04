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
import helpers

global rpg_json_parse
global rpg_dict
search_path = "https://rpggeek.com/xmlapi2/"
rsearch = 1
searchParams = ["rpg", "rpgitem", "family","thing"]


# this object will be the gameObj itself. We're going to cross to the database and, if it isn't present, add it.
# TODO: add more search options (author, publisher, etc., or do narrow title search)

def broadSearch(*args) :
    print(args)
    search = search_path + args[0]
    args = {"query": args[2], "type": searchParams[0]}
    print("Broad Search Begins")
    rpgg = requests.get(search, params=args)
    # print(rpgg.url)
    rpg_dict = xmltodict.parse(rpgg.text)["items"]
    bsearched = []

    qselect = ''
    # rpg_response = helpers.clean_names(rpg_dict)
    # # export to JSON for testing
    # rpgjson = open("JSONboardtest.json", "w")
    # rpgjson.write(json.dumps(bsearched))
    # rpgjson.close()
    # return qselect, bsearched, rpg_dict
    return rpg_dict

def narrowSearch(args):
    search = search_path + args[0]
    args = {"id" : args[2], "type": searchParams[args[1]]}
    print("Narrow Search Begins")
    rpgg = requests.get(search, params=args)
    #print("Narrow", rpgg.url)
    # print(rpgg.text)
    rpg_dict = xmltodict.parse(rpgg.text)["items"]["item"]
    #rpg_response = helpers.clean_names(rpg_dict)
    rpg_json_parse = json.dumps(rpg_dict)

    # Exported to JSON for a missing list or testing
    # rpgjson = open("JSONnarrowtest.json", "w")
    # rpgjson.write(json.dumps(rsearched))
    # rpgjson.close()
    print(rpg_dict)
    return rpg_dict

def exactSearch(*args) : 
    print("Exact Search begins")
    # TODO: FIX THIS API CALL to match with the others - let's keep it clean, people.
    search = search_path + searchParams[3]
    eargs = {"id" : args[0], type : args[2]}
    e_rpg = requests.get(search, params=eargs)
    print(e_rpg.url)
    e_rpg_dict = xmltodict.parse(e_rpg.text)["items"]["item"]
    print(e_rpg_dict)
    # e_rpg_json_parse = json.dumps(e_rpg_dict)

    # Uncomment this if you want all results exported to JSON for a missing list
    # rpgjson = open("JSONexacttest.json", "w")
    # rpgjson.write(e_rpg_json_parse)
    # rpgjson.close()
    # print(e_rpg_dict)
    return e_rpg_dict

# let's make this script to be able to put the data together into a single JSON for us.

def familyJSON(*args) :
    print("Family search - narrow begins")
    systems = narrowSearch(args)
    print(systems['link'])
    # for book in systems['link'] :
    #     print("HERE IS THE ITEM", book)
    #     asset = exactSearch(book['@id'], "0", "rpgitem")
        
    #     return asset
    systemLibrary = classes.systemObj(systems, "api")
    for book in systems['link'] :
        print("HERE IS THE ITEM", book)
        if(book['@type'] == "rpg"): 
            asset = exactSearch(book['@id'], "0", "rpgitem")
            systemLibrary.addBook(asset)
            print("Exact Search complete", systemLibrary.__dict__)
        else :
            continue
        continue
        
    # args - narrowSearch result in proper form
    # plus each "rpg" link has details from exactSearch
    # JSON format:
    # Item: Name, Image, ID, [Mechanics]


    print("System Object", systemLibrary.__dict__)
    return json.dumps(systemLibrary.__dict__)
