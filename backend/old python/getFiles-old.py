# GetFiles.py will search the selected directory and produce a list of files in the directory
# It will also split the names from the extension and remove any hyphens in order to do a file search.
# If RPGGeek allows for accessing cover images, perhaps search by image recognition - prepare first-page image for search.

#try for Git submit.

import urllib
import requests
import xmltodict
import json
import xml
import pdfreader

qmethod = "search"

def apiSearch(args):

    qparams = {1: "rpgitem", 2: "rpg", 3: "family"}
    print("Please provide search parameters\n------------------")
    #qsearchterms = input("Enter search terms: ")
    
    for i,n in qparams.items():
        print(i, n.capitalize())

    stype = input("Select search type: ")
    qtype = qparams[int(stype)]

    args = {"query": pdfreader.qsearchterms, "type": qtype}
    print(args)

    rpgg = requests.get("https://rpggeek.com/xmlapi2/search", params = args)

    global rpg_json_parse
    global rpg_dict_parse
    rpg_dict_parse = xmltodict.parse(rpgg.text)
    print(rpg_json_parse.items)
    rpg_json_parse = json.dumps(xmltodict.parse(rpgg.text))

    # rpgjson = open("JSONtest.json","w")
    # rpgjson.write(json.dumps(rpg_dict_parse))
    # rpgjson.close()
    # print(rpg_dict_parse)

def apiRetrieve():
    rpgg = requests.get("https://rpggeek.com/xmlapi2/thing", params = args)
    rpgparse = xmltodict.parse(rpgg.text)
    print(json.dumps(rpgparse))

def apiSelect():
    data = json.load(rpg_json_parse['items']['item'])
    qselect = {"selector" : [], "name" : [], "sid" : []}
    sel = 0
    for name in data['name']:

        print(id, name)
        print(rpg_json_parse['items']['item']['name']['@value'])
        print(rpg_json_parse['items']['item']['@id'])
        qselect("selector").append(i)
        qselect("name").append(i['name']['@value'])
        qselect.append(i, a, b)
        print(qselect)
        sel += 1

# apiSearch()
# apiSelect()