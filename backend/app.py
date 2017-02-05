from flask import Flask, request
import requests
import json
from flask_sqlalchemy import SQLAlchemy
from pprint import pprint
import os
import transcribe
import nlp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)

class Rappartial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    audioFileName = db.Column(db.String())
    words = db.Column(db.String())
    analysis = db.Column(db.String())
    sentiment = db.Column(db.Float())

    def __init__(self, audioFileName, lyrics):
        self.audioFileName = audioFileName
        self.words = words
        self.sentiment = nlp.sentiment_text(lyrics.split(" "))

    def __repr__(self):
        return '<Song %r>' % self.words

class Partialline(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    numSylables = db.Column(db.String())
    words = db.Column(db.String())
    sentiment = db.Column(db.Float())
    rappartial_id = db.Column(db.Integer, db.ForeignKey('rappartial.id'))
    rappartial = db.relationship('Rappartial', backref=db.backref('lines', lazy='dynamic'))

    def __init__(self, line, rappartial):
        self.words = line
        self.rappartial = rappartial
        self.sentiment = nlp.sentiment_text(words)
        self.numSylables = rappartial.sentiment


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

@app.route('/seed',  methods=['POST'])
def seed():
    data = request.get_json(data['audioFile'])
    fakePartial = Rappartial("", "")
    db.session.add(fakePartial)
    for item in data['seed']:
        newLine = Partialine(item, fakePartial)
        newLine.sentiment = nlp.sentiment_text(item.split(" "))
        db.session.add(newLine)
    db.session.commit()

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
            transcribed = transcribe.main(os.path.join(os.getcwd(), filename))
            print(transcribed)
            p = Rappartial(filename, transcribed)
            db.session.add(p)
            db.session.commit()
            lines = ["line1 is lit", "line2 is lit", "line3 is lit"]
            m = {"lines": [transcribed], "id": p.id}
            return json.dumps(m), 200
        return "failure", 404

#Also consume the id of the song
@app.route('/songs/<song_id>', methods=['POST'])
def modifyLines(song_id):
    song = Rappartial.query.filter_by(id=song_id).first_or_404()
    data = request.get_json(force=True)
    song.words = ','.join(data['lines'])
    db.session.add(song)
    print(data)

    for i in data['lines']:
        l = Partialline(i, song)
        db.session.add(l)
    db.session.commit()
    m = {"lines": [line for line in data['lines']]}
    return json.dumps(m), 200

#Also consume the id of the song
@app.route('/songs/<song_id>/newline', methods=['POST'])
def newlyrics(song_id):
    song = Rappartial.query.filter_by(id=song_id).first_or_404()
    currLyrics = [line.words for line in  song.lines]
    prevLyrics = [line.words for line in Rappartial.query.filter_by(id != song_id).filter( sentiment <= song.sentiment + 0.2 ).filter(sentiment >= song.sentiment - 0.2)]
    print("CurrLyrics :{}".format(currLyrics))
    print("PrevLyrics :{}".format(prevLyrics))

    m = {"lines": [line for line in data['lines']]}
    return json.dumps(m), 200

@app.route('/songs/<song_id>/newline', methods=['POST'])
def getSongAudio():
    #consumes nextLine, id of the song
    ...

def getWords(audioFile):
    return "This is a bunch of sample words"

app.run(debug=True)
