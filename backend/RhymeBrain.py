import requests

API_KEY = 'AIzaSyB1kj40JT0ZsO8pVF3xP06PL4dxvK941ZQ'

def getRhymes(word):
	r = requests.get('http://rhymebrain.com/talk?function=getRhymes&word=' + word)
	return r.json() # Array of rhyming words

def analyzeSentiment(text):
	payload = {"encodingType": "UTF8","document": {"type": "PLAIN_TEXT","content": text}}
	r = requests.post('https://language.googleapis.com/v1/documents:analyzeSentiment?key=' + API_KEY,
		json=payload)
	return r.json()

def splitRap(r):
	payload = {"encodingType": "UTF8", "document": {"type": "PLAIN_TEXT","content": r}}
	r = requests.post('https://language.googleapis.com/v1/documents:analyzeSyntax?key=' + API_KEY,
		json=payload)
	return r.json()

if __name__ == '__main__':
	#print getRhymes('duck')
	print analyzeSentiment('i love lucy')