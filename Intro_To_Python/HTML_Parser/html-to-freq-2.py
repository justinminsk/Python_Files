import requests, obo
url= 'http://literature.org/authors/shelley-mary/frankenstein/chapter-01.html'
pagetext= requests.get(url)
HTML = pagetext.text
text = obo.stripTags(HTML).lower() # convert to lower case
fullwordlist= obo.stripNonAlphaNum(text) # only words, into list
wordlist = obo.removeStopwords(fullwordlist, obo.stopwords) # remove common useless words
dictionary = obo.wordListToFreqDict(wordlist) # add words and counts to dictionary
sorteddict= obo.sortFreqDict(dictionary) # sort word list by frequency


if __name__ == '__main__':
    for s in sorteddict: print(str(s))