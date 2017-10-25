import requests, obo

url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

pagetext = requests.get(url)
HTML = pagetext.text
wordlist = HTML.split()
text = obo.stripTags(HTML).lower() # convert to lower case
#wordlist = text.split()
wordlist = obo.stripNonAlphaNum(text) # RegEx and split done together
print(wordlist[0:150])