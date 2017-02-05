import requests
from gtts import gTTS


def text2speech(text, file):
	tts = gTTS(text=text, lang='en')
	tts.save(file + '.mp3')

if __name__ == '__main__':
	text2speech("With Monica Lewinsky feelin' on his, nutsack", 'popcorn')
