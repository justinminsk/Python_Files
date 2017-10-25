import requests
url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'
pagetext = requests.get(url) # entire page to string pagetext


if __name__ == '__main__':
    # pagetext itself returns 200 if successful
    print(pagetext.text)