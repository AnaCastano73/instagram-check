# Import Flask
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

import os

# Import date
import datetime

# webpage endpoints
@app.route("/")
def index():
    return render_template("index.html")

"""
# input processor endpoints
@app.route("/process_signup", methods = ['GET', 'POST'])
def process_signup():
return
"""

if __name__ == '__main__':
    app.run(debug=True) # run locally
    # app.run(host="0.0.0.0") # run publicly
