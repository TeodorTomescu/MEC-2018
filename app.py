# from app import app
from flask import Flask
from flask import render_template, abort, request, jsonify
app = Flask(__name__)

# app.debug = True
from datamuse import datamuse
import json


def predict(word):
    api = datamuse.Datamuse()
    return api.suggest(s=word, max=6)

@app.route('/')
def index():
    essentials = ["Yes", "No", "Help", "Clear"]
    # print (request.args)
    return render_template('index.htm', essentials=essentials)


@app.route('/api/word', methods=['POST']) 
def word():
    print(request.form)
    # if not request.json:
    #     print(request.get_json())
    #     abort(400)
    string = request.form.get("s", False)
    print ("Request String",string)
    # return 0
    predicted = jsonify({'list':predict(string)})
    print(predicted)
    return predicted

if __name__ == '__main__':
    app.run()