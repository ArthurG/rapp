from flask import Flask, request
import requests
import json
from flask_sqlalchemy import SQLAlchemy
from pprint import pprint
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)

class Rappartial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    audioFileUrl = db.Column(db.String())
    analysis = db.Column(db.String())

    def __init__(self, audioFile):
        self.audioFileUrl = audioFileUrl

    def __repr__(self):
        return '<Song %r>' % self.words

class Partialline(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    numSylables = db.Column(db.String())
    words = db.Column(db.String())
    rappartial_id = db.Column(db.Integer, db.ForeignKey('rappartial.id'))
    rappartial = db.relationship('Rappartial', backref=db.backref('lines', lazy='dynamic'))

    def __init__(self, line, rappartial):
        self.words = line
        self.rappartial = rappartial
        ##self.numSylables



@app.route('/')
def newHome():
    return "Lines are random words", 200


def addNewSong():
    data = request.get_json(force=True)
    print(data)
    partial = Rappartial(data['audioFile'])
    db.session.add(partial)
    db.session.commit()
    #Do something to get the lines and save it


#File extension checking
def allowed_filename(filename):
    return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

@app.route('/newsong', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.get_json())
        print(request.files)
        if 'file' not in request.files:
            return "failure", 404

        submitted_file = request.files['file']
        if submitted_file:
            filename = submitted_file.filename
            print(filename)
            print(os.getcwd())
            submitted_file.save(os.path.join(os.getcwd(), filename))
            lines = ["line1 is lit", "line2 is lit", "line3 is lit"]
            m = {"lines": lines}
            return json.dumps(m), 200
        return "failure", 404

#Also consume the id of the song
@app.route('/songs/<song_id>')
def modifyLines(song_id):
    song = Rappartial.filter_by(id=song_id).first_or_404()
    data = request.get_json(force=True)
    song.lines = []
    db.session.add(song)
    for i in data['line']:
        l = Partialline(line, song)
        db.session.add(l)
    db.session.commit()
    m = {"lines": song.lines}
    return json.dumps(m), 200


def getNextPossibleLine():
    ...

def getSongAudio():
    #consumes nextLine, id of the song
    ...

def getWords(audioFile):
    return "This is a bunch of sample words"

app.run(debug=True)
