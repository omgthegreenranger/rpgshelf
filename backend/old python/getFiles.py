# GetFiles.py will search the selected directory and produce a list of files in the directory
# It will also split the names from the extension and remove any hyphens in order to do a file search.
# If RPGGeek allows for accessing cover images, perhaps search by image recognition - prepare first-page image for search.

#try for Git submit.

import urllib
import requests
import xmltodict
import json
import xml

global rpg_json_parse
global rpg_dict
qmethod = "search"
qsearch = 0

def apiSearch(args):

    qparams = ["rpg", "rpgitem", "family"]
    # print("Please provide search parameters\n------------------")
    qsearchterms = input("Enter RPG name: ")

    qtype = qparams[qsearch]

    args = {"query": qsearchterms, "type": qtype}
    print(args)

    rpgg = requests.get("https://rpggeek.com/xmlapi2/search", params = args)
    # root = ET.fromstring(rpgg.content)
    rpg_dict = xmltodict.parse(rpgg.text)['items']
    rpg_json_parse = json.dumps(rpg_dict)

    # selector = 
    qselect = {"name" : [], "sid" : []}
    qselect_list['sel'] = qselect
    sel = 1

    for item in rpg_dict['item']:
        id = item['@id']
        name = item['name']['@value']
        qselect['selector'].append(sel)
        qselect_list['name'].append(name)
        qselect['sid'].append(id)
        # print(sel, name)
        sel += 1

        # print(id,name)
       
    return(qselect)



    rpgjson = open("JSONtest.json","w")
    rpgjson.write(rpg_json_parse)
    rpgjson.close()
    return(rpg_dict)


# def apiRetrieve():
#     rpgg = requests.get("https://rpggeek.com/xmlapi2/thing", params = args)
#     rpgparse = xmltodict.parse(rpgg.text)
#     print(json.dumps(rpgparse))

# def apiSelect(rpg_dict):
#     data = result['item']
#     print(data)
#     qselect = {"selector" : [], "name" : [], "sid" : []}
#     sel = 1
#     for item in data.items:

#         print(id, name)
#         print(data.items['name']['@value'])
#         print(data.items['@id'])
#         qselect("selector").append(i)
#         qselect("name").append(i['name']['@value'])
#         qselect.append(i, a, b)
#         print(qselect)
#         sel += 1

# apiSearch()
# apiSelect()

