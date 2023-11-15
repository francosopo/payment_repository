import flask
import json
import utils
import random

from flask import request
app = flask.Flask(__name__)

@app.route("/token", methods=['GET'])
def get_token():
    return json.dumps({
        "status": 200,
        "message": "Here is your token",
        "token": f"{utils.getToken()}"
    })
    
@app.route("/payment", methods=["POST"])
def doPayment():
    if not 'Authorization' in request.headers.keys():
        return json.dumps({
            "status": 400,
            "message": "Provide a token",
            "details": "Provide a token"
        })
    
    token = request.headers["Authorization"].split(" ")[1]
    if (not utils.isValidToken(token)):
        return json.dumps({
            "status": 400,
            "message": "Invalid token",
            "details": "Token is no valid"
        })
    r = random.random()

    if (r < 0.5):
        return json.dumps({
            "status": 500,
            "message": "Something went wrong",
            "details": "Cannot process your request",
        })
    else:
        return json.dumps({
            "status": 200,
            "message": "Done successfully",
            "details": "Everything went good"
        })
    