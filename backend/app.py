from flask import Flask, request
import requests
import json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)

class Rappartial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    audioFile = db.Column(db.Binary, unique=True)
    analysis = db.Column(db.String())

    def __init__(self, audioFile):
        self.audioFile = audioFile

    def __repr__(self):
        return '<Song %r>' % self.words

class Partialline(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    numSylables = db.Column(db.String())
    words = db.Column(db.String())

@app.route('/')
def newHome():
    return "Lines are random words", 200


@app.route('/newsong', methods=['POST'])
def addNewSong():
    audioFile=request.form['audiofile']
    #newPartial = Rappartial(audioFile)
    #lines = getLines(audioFile)
    return "Lines are random words", 200

#Also consume the id of the song
def modifyLines(newLines):
    ...

def getNextPossibleLine():
    ...

def getSongAudio():
    #consumes nextLine, id of the song
    ...

def getWords(audioFile):
    return "This is a bunch of sample words"

app.run()
