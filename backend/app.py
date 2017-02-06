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
import audio


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
        self.sentiment = nlp.sentiment_text(self.lyrics.split(" "))

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
        print(request.form)
        if 'file' not in request.files:
            return "failure", 404
        submitted_file = request.files['file']

        times = [int(time) for time in dict(request.form)['times']]

        if submitted_file:
            filename = submitted_file.filename
            print(filename)
            print(os.getcwd())
            submitted_file.save(os.path.join(os.getcwd(), filename))
            fileTrans = transcribe.main(os.path.join(os.getcwd(), filename))
            if fileTrans == None:
                fileTrans = ""
            print(fileTrans)
            p = Rappartial(filename, fileTrans)
            db.session.add(p)

            filenames = audio.main(filename, times)
            lines = []
            for f in filenames:
                fileTrans = transcribe.main(os.path.join(os.getcwd(), f))
                lines.append(fileTrans)
                if fileTrans == None:
                    fileTrans = ""
                print(fileTrans)
                l = Partialline(fileTrans, p)
                db.session.add(l)
            db.session.commit()

            m = {"lines": [p.lyrics], "id": p.id}
            print(m)
            return json.dumps(m), 200
        return "failure", 404

@app.route('/analytics/<song_id>', methods=['GET'])
def getAnalytics(song_id):
    song = Rappartial.query.filter_by(id=song_id).first_or_404()
    lines = song.lyrics
    noob = {"sentiment": nlp.sentiment_text([lines]),
            "keywords": nlp.getKeywords([lines]),
            "syllableArray": [sum(nlp.countSylArray([lines]))],
            "rhymeWords": list(nlp.findRhyme([lines])[:10]),
            "rhymability":nlp.howRhymable([lines])
            #"alliteration":...
            
            }
    print(noob)
    return json.dumps(noob)


#Also consume the id of the song
@app.route('/lyrics/<song_id>', methods=['GET'])
def getLine(song_id):
    song = Rappartial.query.filter_by(id=song_id).first_or_404()
    m = {"lines": [song.lyrics]}
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
    currLyrics = [song.lyrics]
    prevLyrics = [line.lyrics for line in Rappartial.query.filter(id != song_id).all() if len(line.lyrics.split(" ")) >= 2]
    ##prevLyrics = [line.words for line in Partialline.query.filter(sentiment <= 0.5).all() if len(line.words.split(" ")) >= 2]
    print("CurrLyrics :{}".format(currLyrics))
    print("PrevLyrics :{}".format(prevLyrics))
    newLines = nlp.pickMatchingLine(prevLyrics, currLyrics, n=5)
    m = {'newlines': newLines}
    return json.dumps(m)

@app.route('/songs/<song_id>/<newline>', methods=['GET'])
def getSongAudio(song_id, newline):
    #consumes nextLine, id of the song
    song = Rappartial.query.filter_by(id=song_id).first_or_404()
    filename = str(time.time())
    text2speech.text2speech(newline, filename)
    print(song.audioFileName, type(song.audioFileName))
    #fileCombined = str(song.audioFileName)
    fileCombined = filename
    fileCombined = str(time.time())
    print("AUDIO FILE NAME: " + song.audioFileName +" " + filename+".mp3")
    audio.merge([song.audioFileName, filename+".mp3"], fileCombined+".mp3")
    return send_from_directory(os.getcwd(), fileCombined+".mp3")

def getWords(audioFile):
    return "This is a bunch of sample words"

app.run(debug=True)
