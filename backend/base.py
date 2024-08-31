from flask import Flask, request, jsonify, make_response
import pikepdf
import fs
from fs.osfs import OSFS
import os
from flask_cors import CORS
from apiSearch import broadSearch, narrowSearch, exactSearch
#from flask_vite import Vite

app = Flask(__name__)
CORS(app)
#vite = Vite()
#vite.init_app(app)

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

@app.route('/search', methods=["GET"])
def search():
    search_type = request.args.get('search_type')
    search_string = request.args.get('search_string')
    print(search_type, search_string)
    search_result = broadSearch("search", "0", search_string)
    print(search_result)
    response = make_response(
        jsonify(search_result)
    )
    response.headers.add('access-control-allow-origin', '*')
    return response
