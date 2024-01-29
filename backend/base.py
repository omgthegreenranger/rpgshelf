from flask import Flask, request, jsonify, make_response
import pikepdf
import fs
from fs.osfs import OSFS
import os
from flask_cors import CORS
from flask_vite import Vite

app = Flask(__name__)
CORS(app)
vite = Vite()
vite.init_app(app)

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

@app.route('/library', methods=["GET", "POST"])
def library():
    print('path')
    response = make_response( 
        jsonify({'title': meta['dc:title']})
    )
    response.headers.add('access-control-allow-origin', '*')


