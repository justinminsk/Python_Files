import requests, obo
url= 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'
pagetext= requests.get(url)

HTML = pagetext.text

print(obo.stripTags(HTML))