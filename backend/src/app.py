from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World</h1>'

@app.route('/notes/', methods = ['POST'])
def createNote():
    print(request.json)
    return 'received'

@app.route('/notes/', methods = ['GET'])
def getNotes():
    return 'received'

@app.route('/notes/<id>', methods = ['PUT'])
def updateNote():
    return 'received'

@app.route('/notes/<id>', methods = ['GET'])
def deleteNote():
    return 'received'

if __name__ == "__main__":
    app.run(debug=True)
