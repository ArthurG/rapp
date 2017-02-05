import requests

API_KEY = 'AIzaSyB1kj40JT0ZsO8pVF3xP06PL4dxvK941ZQ' #GOogle
INDICO_KEY = 'cf251f38d815e4f0296541946aa93774'

def getRhymes(word):
	r = requests.get('http://rhymebrain.com/talk?function=getRhymes&word=' + word)
	return r.json() # Array of rhyming words

def analyzeSentiment(text):
	payload = {"data": text}
	headers = {'X-apikey': INDICO_KEY}
	r = requests.post('https://apiv2.indico.io/sentiment',
		json=payload, headers=headers)
	return r.json()

def findSalient(text):
	payload = {"encodingType": "UTF8", "document": {"type": "PLAIN_TEXT", "content": text}}
	r = requests.post('https://language.googleapis.com/v1/documents:analyzeEntities?key=' + API_KEY,
		json=payload)
	return r.json()

def splitRap(r):
	payload = {"encodingType": "UTF8", "document": {"type": "PLAIN_TEXT","content": r}}
	r = requests.post('https://language.googleapis.com/v1/documents:analyzeSyntax?key=' + API_KEY,
		json=payload)
	return r.json()

#if __name__ == '__main__':
	#print getRhymes('duck')
	#print analyzeSentiment('i love lucy')
