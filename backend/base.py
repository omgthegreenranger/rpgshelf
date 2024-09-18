from flask import Flask, request, jsonify, make_response, session
from flask_caching import Cache
import pikepdf
import fs
from fs.osfs import OSFS
import os
from flask_cors import CORS
from apiSearch import broadSearch, narrowSearch, exactSearch, familyJSON
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
CORS(app)

config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300,
    "ensure_ascii": False
}
app.config.from_mapping(config)
cache = Cache(app)
app.secret_key = os.getenv("SECRET_KEY")

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
        search_result = broadSearch("search", "0", search_string)
    if (search_type == "narrow") :
        search_result = narrowSearch("family", 0, search_string)
    if (search_type == "family") :
        search_result = familyJSON("family", 0, search_string)
    response = make_response(
        #jsonify(search_result)
        search_result
    )
    response.headers.add('access-control-allow-origin', '*')
    return response

@app.route('/db', methods=["GET"])
def db_add():
    submit_details = request.args.get('submit_details')
    print("DETAILS!", request.args.get('submit_details'))
    # response.headers.add('access-control-allow-origin', '*')    
    #print("RESPONSE", response)
    # Add system to database
    return submit_details


# process for API call to get the details of your search:
# 1. search for the broadsearch - this is the system (though we can expand to include the book as well, perhaps)
# 2. select broad System
#   a. provide details of System - this will include the link details.