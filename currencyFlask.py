from flask import Flask
from flask import render_template
from flask import request
import json



app = Flask(__name__)

with open('data.json') as json_file:
    data = json.load(json_file)


@app.route("/")
def home():
    return render_template("home.html", data=data)





if __name__ =="__main__":
    app.run(debug=True)

