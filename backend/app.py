from flask import Flask, request , send_from_directory
import requests
import json
from flask_sqlalchemy import SQLAlchemy
from pprint import pprint
import os
import transcribe
import nlp
import text2speech
import time

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)

class Rappartial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    audioFileName = db.Column(db.String())
    lyrics = db.Column(db.String())
    analysis = db.Column(db.String())
    sentiment = db.Column(db.Float())

    def __init__(self, audioFileName, lyrics):
        self.audioFileName = audioFileName
        self.lyrics = lyrics
        self.sentiment = nlp.sentiment_text(lyrics.split(" "))

    def __repr__(self):
        return '<Song %r>' % self.lyrics

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
        self.sentiment = rappartial.sentiment
        self.numSylables = nlp.countSylArray([line])[0]


@app.route('/')
def newHome():
    return "Lines are random words", 200

@app.route('/seed',  methods=['POST'])
def seed():
    data = request.get_json(force=True)
    print(data)
    fakePartial = Rappartial("", "")
    db.session.add(fakePartial)
    for item in data['seed']:
        print(item)
        newLine = Partialline(item, fakePartial)
        newLine.sentiment = nlp.sentiment_text([item])
        db.session.add(newLine)
        db.session.commit()
    db.session.commit()
    return "success"

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
            if transcribed == None:
                transcribed = ""
            p = Rappartial(filename, transcribed)
            db.session.add(p)
            db.session.commit()
            lines = ["line1 is lit", "line2 is lit", "line3 is lit"]
            m = {"lines": [transcribed], "id": p.id}
            return json.dumps(m), 200
        return "failure", 404

#Also consume the id of the song
@app.route('/songsGet/<song_id>', methods=['GET'])
def getLine(song_id):
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
    newLines = pickMatchingLine(prevLyrics, currLyrics, n=5)
    m = {'newlines': newLines}
    return json.dumps(m)

@app.route('/songs/<song_id>/<newline>', methods=['GET'])
def getSongAudio(song_id, newline):
    #consumes nextLine, id of the song
    song = Rappartial.query.filter_by(id=song_id).first_or_404()

    print("name: '{}'".format(song.lyrics + " " + newline))
    filename = str(time.time())
    text2speech.text2speech(song.lyrics + " " + newline, filename)
    return send_from_directory(os.getcwd(), filename+".mp3")

def getWords(audioFile):
    return "This is a bunch of sample words"

app.run(debug=True)
