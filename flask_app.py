import sys
from flask import Flask
from flask import request
import wpr_singapore_bot

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def index_fn():
    return "Thank you for the visit!!"

@app.route("/wpr_singapore_bot", methods = ['GET', 'POST'])
def enablement_bot_fn():
    return wpr_singapore_bot.runme(request)