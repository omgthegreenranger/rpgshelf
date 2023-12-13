# GetFiles.py will search the selected directory and produce a list of files in the directory
# It will also split the names from the extension and remove any hyphens in order to do a file search.
# If RPGGeek allows for accessing cover images, perhaps search by image recognition - prepare first-page image for search.

# try for Git submit.

import urllib
import requests
import xmltodict
import json
import xml

global rpg_json_parse
global rpg_dict
qmethod = "search"
rsearch = 1
searchParams = ["rpg", "rpgitem", "family"]

# api search params = []

def broadSearch(*args) :
    search = "https://rpggeek.com/xmlapi2/" + args[0]
    args = {"query": args[2], "type": searchParams[args[1]]}
    rpgg = requests.get(search, params=args)
    rpg_dict = xmltodict.parse(rpgg.text)["items"]
    qselect = []
    sel = 0
    for item in rpg_dict["item"]:
        id = item["@id"]
        name = item["name"]["@value"]
        qselect.append([item["@id"], item["name"]["@value"]])
        print(sel, name)
        sel += 1

    return qselect

def narrowSearch(*args):
    print(args[2][0], searchParams[args[1]])
    search = "https://rpggeek.com/xmlapi2/" + args[0]
    args = {"id" : args[2][0], "type": searchParams[args[1]]}

    rpgg = requests.get(search, params=args)
    rpg_dict = xmltodict.parse(rpgg.text)["items"]["item"]["link"]
    rpg_json_parse = json.dumps(rpg_dict)
    rsearched = []
    sel = 0
    for item in rpg_dict:
        if item["@type"] == "rpg" :
            id = item["@id"]
            name = item["@value"]

            bselect = [name, id]
            print(sel, name)
            rsearched.append(item)
            sel += 1

    bsearchterm = input("Please select game:")
    bselected = [rpg_dict[int(bsearchterm)]["@id"], rpg_dict[int(bsearchterm)]['@value']]
    # print(bselected)
    # print("Search", rsearched)

    rpgjson = open("JSONtest.json", "w")
    rpgjson.write(json.dumps(rsearched))
    rpgjson.close()

    return bselected, rsearched

def exactSearch(*args) : 
    
    return
