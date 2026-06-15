# import urllib
import read_config
import os
from pathlib import Path
import requests
import xmltodict
import json
import xml
import classes
import helpers
from flask import session
from db.models import System, Library
#from base import g

def file_list():
    paths = read_config.import_config('Paths')
    scan = paths["scanpath"]
    library = paths['librarypath']
    returns = []
    files = Path(scan).iterdir()
    print(files)
    for file in files:
        # returns.append(file.stat())
        if file.is_dir():
            print("Dir")
            returns.append({"Name": file.name, "Type": "directory"})
        if file.is_file():
            print("File")
            returns.append({"Name": file.name, "Type": "file"})
    print(returns)
    return returns
    