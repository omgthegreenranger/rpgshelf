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
search_path = "https://rpggeek.com/xmlapi2/"
# qmethod = "search"
rsearch = 1
searchParams = ["rpg", "rpgitem", "family","thing"]

# api search params = []

def broadSearch(*args) :
    search = search_path + args[0]
    args = {"query": args[2], "type": searchParams[0]}
    rpgg = requests.get(search, params=args)
    rpg_dict = xmltodict.parse(rpgg.text)["items"]
    # print(rpg_dict['@total'])
    qselect = rpg_dict
    if int(rpg_dict['@total']) == 0 :
        # print("False!")
        return qselect
    else :
        sel = 0
        for item in rpg_dict["item"]:
            id = item["@id"]
            name = item["name"]["@value"]
            # qselect.append(item)
            print(sel, name)
            sel += 1

    return qselect

def narrowSearch(*args):
    print(args[2], searchParams[args[1]])
    search = search_path + args[0]
    args = {"id" : args[2], "type": searchParams[args[1]]}

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

    # Uncomment this if you want all results exported to JSON for a missing list
    # rpgjson = open("JSONtest.json", "w")
    # rpgjson.write(json.dumps(rsearched))
    # rpgjson.close()

    return rsearched

def exactSearch(*args) : 
    print("Exact Search begins", args)

    search = search_path + searchParams[3]
    eargs = {"id" : args[0]}
    e_rpg = requests.get(search, params=eargs)

    e_rpg_dict = xmltodict.parse(e_rpg.text)["items"]["item"]
    e_rpg_json_parse = json.dumps(e_rpg_dict)

    return e_rpg_dict
