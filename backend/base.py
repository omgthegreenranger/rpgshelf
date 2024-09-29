from flask import Flask, request, jsonify, make_response, session
from flask_caching import Cache
import pikepdf
import fs
from fs.osfs import OSFS
import os
from flask_cors import CORS
from apiSearch import broadSearch, narrowSearch, exactSearch, familyJSON
from dotenv import load_dotenv
from db.sqlite_scripts import addSystem
from flask_sqlalchemy import SQLAlchemy
import classes

load_dotenv()

app = Flask(__name__)
CORS(app)

config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300,
    "ensure_ascii": False,
    "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory"
}
app.config.from_mapping(config)
cache = Cache(app)
app.secret_key = os.getenv("SECRET_KEY")
db = SQLAlchemy(app)


@app.route('/readfile', methods=["POST"])
def read_file():
    print('path')
    pdfPath = request.json['path']
    pdf = pikepdf.open(pdfPath)
    meta = pdf.open_metadata()
    response = make_response( 
        jsonify({'title': meta['dc:title']})
    )
    response.headers.add('access-control-allow-origin', '*')
    return response

@app.route('/search', methods=["GET", "POST"])
def search():
    search_type = request.args.get('search_type')
    search_string = request.args.get('search_string')
    print("API is called", search_type, search_string)
    if (search_type == "system") :        
        search_result = [broadSearch("search", "0", search_string), False]
    if (search_type == "narrow") :
        narrowResult = narrowSearch("family", 0, search_string)
        object_cached = system_object_cache(narrowResult, "system")
        search_result = [narrowResult, object_cached]
    # if (search_type == "family") :
    #    search_result = [familyJSON("family", 0, search_string), False]
    #    print(systemData)
    # print(object_cached)
    response = make_response(
        #jsonify(search_result)
        search_result
    )
    response.headers.add('access-control-allow-origin', '*')
    return response

# @app.route('/db', methods=["GET"])
#@cache.cached(timeout=300, key_prefix='System')
def system_object_cache(submit_details, submit_type):
    print("Result!")
    systemData = request.args.get('submit_details')
    submit_type = request.args.get('submit_type')
    print(submit_type)
    submit_result = True
    print("Result **********", submit_result)
    # submit_response = addSystem(submit_details); 

    # Add system to database
    # response = make_response(
    #     submit_result
    # )
    # response.headers.add('access-control-allow-origin', '*')   
 
    return submit_result

@app.route('/db', methods=["GET"])
# Gets confirmation of the book selection - send the global object.
def db_add():
    submitData = request.args.get('select_details')
    select_type = request.args.get('select_type')
    #print("DETAILS!", request.args.get('select_details'), select_type)
    addSystem(submitData); 
    # Add system to database
    response = make_response(
         select_type
     )
    response.headers.add('access-control-allow-origin', '*')   

    return response

# process for API call to get the details of your search:
# 1. search for the broadsearch - this is the system (though we can expand to include the book as well, perhaps)
# 2. select broad System
#   a. provide details of System - this will include the link details.