from flask import Flask, request, jsonify
import pikepdf
import fs

api = Flask(__name__)

@app.route('/readfile', methods=["POST"])
def add_guide():
    title = request.json['title']