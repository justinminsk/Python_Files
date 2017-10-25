import requests, obo
url= 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'
pagetext= requests.get(url)
HTML = pagetext.text
text = obo.stripTags(HTML).lower() # convert to lower case
fullwordlist= obo.stripNonAlphaNum(text) # only words, into list
wordlist = obo.removeStopwords(fullwordlist, obo.stopwords) # remove common useless words
dictionary = obo.wordListToFreqDict(wordlist) # add words and counts to dictionary
sorteddict= obo.sortFreqDict(dictionary) # sort word list by frequency
for s in sorteddict: print(str(s))