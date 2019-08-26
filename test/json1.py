from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):

    try:
        html = urlopen(url)
    except HTTPError as e:
        return None

    try:
        htmlContent = html.read()
        bsObj = BeautifulSoup(htmlContent, features="html.parser")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

url = "http://www.pythonscraping.com/pages/page1.html"
title = getTitle(url)
if title == None:
    print("Title could not be found")
else:
    print(title)
