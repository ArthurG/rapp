import nltk
from nltk.misc.sort import *
from nltk.corpus import treebank
#from indicoio.custom import Collection

import curses 
from curses.ascii import isdigit 
import nltk
from nltk.corpus import cmudict 

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
  print word
  if not(word in d): return ""
  word = d[word][ind]
  if n > len(word): return ""
  print str(word[-n]) #DEBUG
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
  return map(lambda n:reduce(lambda x, y: x+y, n), syllabizeArray(arr))

#
# Returns a number (0-5) of how well two sentences rhyme
#
def isRhyme(arr):
  if len(arr) < 2: return None # Not enough args
  return wordRhyme(arr[0].split(' ')[-1], arr[1].split(' ')[-1])

#
# Return a possible rhyming word
#
def findRhyme(word):
  toMatch = nthLastSyl(word, 1)
  # Under construction

if __name__ == '__main__':
  #DEBUG
  #print syllabizeArray(["bitches for days aren't my type man lol", "Rapping everyday nomsayin"])
  #print countsylManual('quintessential')
  #print isRhyme(['Thank mister caboose','I like goose'])
  print countSylArray(['One syllable', 'Two syllables'])
