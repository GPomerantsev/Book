from flask import Flask, request
from flask_cors import CORS
from flask_pymongo import PyMongo, ObjectId

app = Flask(__name__, static_folder='../../notes/build', static_url_path='/')
app.config["MONGO_URI"] = ""
mongo = PyMongo(app)

CORS(app)

db = mongo.db.notes

@app.route('/', methods=['GET'])
def hello():    
    return ''

@app.route('/notes/', methods = ['POST'])
def createNote():
    db.insert({
        "title": request.json["title"],
        "body": request.json["body"]
    })
    return 'received'

@app.route('/notes/', methods = ['GET'])
def getNotes():
    notes = []
    for note in db.find():
        notes.append({
            "_id": str(ObjectId(note['_id']),
            "title": note['title'],
            "conbody": note['body']
        })
    return 'received'

@app.route('/notes/<id>', methods = ['GET'])
def getNote(id):
    note = db.find_one({'_id': ObjectId(id)}):
    return 'received'

@app.route('/notes/<id>', methods = ['PUT'])
def updateNote():
    db.update_one({'_id': ObjectId(id), {'$set': {
        "title": request.json["title"],
        "main": request.json["main"]
    }}})
    return 'received'

@app.route('/notes/<id>', methods = ['DELETE'])
def deleteNote(id):
    db.delete_one({'_id': ObjectId(id)})
    return 'received'

if __name__ == "__main__":
    app.run(debug=True)
