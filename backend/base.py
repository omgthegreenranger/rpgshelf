from flask import Flask

api = Flask(__name__)

@api.route('/profile')
def my_profile():
    response_body = {
        "name": "Stephen Cardie",
        "about" :"Hello! I'm totally the rockin' dude."
    }

    return response_body