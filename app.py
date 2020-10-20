
from flask import Flask, request, render_template
from flask_cors import CORS

app = Flask(__name__, static_folder='notes/build', static_url_path='')

@app.route('/')
def root():
    return app.send_static_file('index.html')

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

if __name__ == "__app__":
    app.run(debug=True)
