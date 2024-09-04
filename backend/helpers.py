import classes;
# from apiSearch import narrowSearch, exactSearch

def clean_names(data):
    print(data)
    for item in data['name'] :
        print("Item", item)
    return data

def familyJSON(*args) :
    systems = narrowSearch(nargs)
    asset = exactSearch(eargs)

    # args - narrowSearch result in proper form
    # plus each "rpg" link has details from exactSearch
    # JSON format:
    # Item: Name, Image, ID, [Mechanics]


    print(data)
    return data