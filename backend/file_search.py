import read_config
import os
from pathlib import Path
import requests
import xmltodict
import json
import xml
from classes import Directory
import helpers
from flask import session, jsonify
from db.models import System, Library
import globals

def file_list():
    def dict_to_dir(path):
        """Convert directory tree to nested dictionary."""
        p = Path(path)
        node = []
        # node = {p: []}
        try:
            for item in sorted(p.iterdir()):
                if item.is_dir():
                    node.append({"dir": "true", "name": item.name, "path": str(item), "files": dict_to_dir(item)})
                else:
                    node.append({"dir": "false", "name": item.name, "type": item.suffix, "size": item.stat().st_size, "path": str(item)})
        except PermissionError:
            node["error"] = "Access Denied"
        
        return node
        #return results
    
    result = dict_to_dir(globals.scan)
    return result
    