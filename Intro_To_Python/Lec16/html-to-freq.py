import requests, obo
url= 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'
pagetext= requests.get(url)
HTML = pagetext.text
text = obo.stripTags(HTML).lower() # make lower case
wordlist = obo.stripNonAlphaNum(text) # convert to list of words, no punctuation
dictionary = obo.wordListToFreqDict(wordlist) # add words, counts to dictionary
sorteddict= obo.sortFreqDict(dictionary) # sort word list by frequency
for s in sorteddict: print(str(s))