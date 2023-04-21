from flask import Flask, request, jsonify
import pikepdf
import fs
from fs.osfs import OSFS
import os

api = Flask(__name__)

@api.route('/readfile', methods=["POST"])
def read_file():
    pdfPath = request.json['path']
    pdf = pikepdf.open(pdfPath)
    meta = pdf.open_metadata()
    print(meta['dc:title'])
    response = read.jsonify({'title': meta['dc:title']})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response