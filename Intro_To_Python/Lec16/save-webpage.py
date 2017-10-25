import requests
url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'
pagetext = requests.get(url)
# pagetext itself returns 200 if successful
#print(pagetext.text)


if __name__ == '__main__':
    with open('obo-t17800628-33.html', 'w') as writefile:
        writefile.write(pagetext.text)