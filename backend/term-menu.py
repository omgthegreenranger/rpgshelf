from simple_term_menu import TerminalMenu
from apiSearch import broadSearch, narrowSearch, exactSearch, familyJSON
from dotenv import load_dotenv
import file_search
import classes
import read_config
import json

def file_explorer():
        get_files = file_search.file_list()
        # print("Get the list of files from folder")
        return get_files

def file_menu(lvl, list):
    for entry in list:
        if(entry["dir"] == "true"):
            print("Directory: ", entry['name'])
        else:
            print("File: ", entry['name'])

def menu(options):
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()

    if (options[menu_entry_index] == "Search Files"):
        lvl = ''
        list = file_explorer()
        print("Level!", lvl)
        file_menu(lvl, list)

    return options[menu_entry_index]

#    print(f"You have selected {options[menu_entry_index]}!")\

if __name__ == "__main__":
    options = ["Search Files", "Create System", "Add Book"]
    reply = menu(options)
    print("Hello!", reply)