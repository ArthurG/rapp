import nltk
from nltk.misc.sort import *
from nltk.corpus import treebank
import RhymeBrain

import operator
import random

import curses 
from curses.ascii import isdigit 
import nltk
from nltk.corpus import cmudict 
import functools

import json

# Constant lexicon dictionary from NLTK
d = cmudict.dict()

def countsylManual(word):
  numVowels = 0
  for v in ['a','e','i','o','u']: numVowels += word.count(v)
  return numVowels

def countsyl(word): 
  word = word.lower()
  if not(word in d): return countsylManual(word)
  numSyl = 0
  for y in d[word][0]: # Use first pronunciation
    if isdigit(str(y)[-1]):
      numSyl += 1
  return numSyl

def nthLastSyl(word, n, ind=0):
  word = word.lower()
  #print word #DEBUG
  if not(word in d): return ""
  word = d[word][ind]
  if n > len(word): return ""
  #print str(word[-n]) #DEBUG
  return str(word[-n])

def wordRhyme(a, b, aind = 0, bind = 0):
  for i in range(1, 6): # Max rhyming value is 5
    if nthLastSyl(a, i, aind) != nthLastSyl(b, i, bind):
      return i-1
  return 5


#def tokenize(sentence):
 # return nltk.word_tokenize(sentence)

# Somehow return some kinda analytics
# Probably useless
#def process(sentence):
 # print sentence
  #tokens = tokenize(sentence)
  #tagged = nltk.pos_tag(tokens)
  #entities = nltk.chunk.ne_chunk(tagged)
  #return entities

def getSylArray(sentence):
  return map(countsyl, sentence.split(' '))


#
# Returns a multi-dimensional array of syllables
# Format: ['I am happy hahaha'] => [[1,1,2,3]]
#
def syllabizeArray(arr):
  i = []
  for s in arr:
    i.append(getSylArray(s))
  return i

#
# Returns array of total number of syllables in each sentence
# 
def countSylArray(arr):
  return list(map(lambda n:functools.reduce(lambda x, y: x+y, n), syllabizeArray(arr)))

#
# Returns a number (0-5) of how well two sentences rhyme
#
def isRhyme(arr):
  if len(arr) < 2: return None # Not enough args
  return wordRhyme(arr[0].split(' ')[-1], arr[1].split(' ')[-1])

#
# Returns overall score of rhymability
#
def howRhymable(arr):
  if len(arr) % 2 == 1: arr.pop()
  score = 0
  for i in range(0, len(arr)-1):
    score += isRhyme(arr[i:i+2])
  return score


#
# Return a possible rhyming word
#
def findRhyme(arr):
  #| Fuck Doing this by hand |#
  #toMatch = nthLastSyl(word, 1)
  #for l in list(map(chr, range(97, 123))): # traverse alphabet
   # w = l + word[1:]
    #if w in d: return w
  #return False
  word = arr[-1].split(' ')[-1]
  return map(lambda x: str(x['word']) ,RhymeBrain.getRhymes(word))

#
# Analyze sentiment for given array of sentences
#
def sentiment_text(arr): 
  sent = RhymeBrain.analyzeSentiment(' '.join(arr))
  return sent.get('results', -1)

#
# Extracts keywords from text snippet
#
def getKeywords(arr):
  entries = RhymeBrain.findSalient(' '.join(arr))['entities']
<<<<<<< HEAD
  if len(entries) <= 0:
      return ""
=======
  if len(entries) < 1: return None
>>>>>>> b4c78e7c297e2ebc22d7d21ec27c8bd422d8da97
  topPhrase = entries[0]
  for i in entries:
    if i['salience'] > topPhrase['salience']: topPhrase = i
  return topPhrase['name']

#
# Returns a possible rhyming line
#
def pickMatchingLine(prev, cur, n=1):
  linesArray = []
  for i in range(0, n):
    ind = random.randint(0, len(prev)-1)
    choice = prev[ind]
    if isRhyme([choice, cur[-1]]): return choice
    pr = findRhyme(cur)
    ind = random.randint(0, len(pr)-1)
    linesArray.append(' '.join(choice.split(' ')[:-1]) + ' ' + pr[ind])
  return linesArray

#
# Splits a rap into an array of lines
#
def splitIntoLines(rap):
  RhymeBrain.splitRap(rap)


if __name__ == '__main__':
  pass
  #DEBUG
  #print syllabizeArray(["bitches for days aren't my type man lol", "Rapping everyday nomsayin"])
  #print countsylManual('quintessential')
  #print isRhyme(['Thank mister mongoose','I like yahoos'])
  #print countSylArray(['One syllable', 'Two syllables'])
  #print findRhyme('make')
  #print sentiment_text(['I love you', 'bitches', 'lol'])
  #print getKeywords(["The quick brown fox jumps over the lazy dog"])
  #print pickMatchingLine(["This does not rhyme"], ["Make me a cake"], 5)
  #print howRhymable(["I make", "on a lake", "a cake", "I bake"])
