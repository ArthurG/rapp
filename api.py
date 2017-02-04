import flask
import nlp
import json
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/analysis', methods=['POST'])
def performAnalysis():
	data = request.get_json(force=True)
	lines = data['lines']
	noob = json.dumps({"Sentiment": nlp.sentiment_text(lines),
		"Most frequent word": nlp.getKeywords(lines),
		"Syllables array": nlp.countSylArray(lines),
		"Words that Rhyme": nlp.findRhyme(lines)})
	print noob
	return noob

@app.route('/generateline', methods=['POST'])
def generateLine():
	data = request.get_json(force=True)
	curLines = data['cur_lines']
	prevLines = data['prev_lines']
	return json.dumps({"Generated Line": nlp.pickMatchingLine(prevLines,curLines)})

app.run()

