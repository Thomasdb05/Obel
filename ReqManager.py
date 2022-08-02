import requests 

def getHTTP(url):
    response = requests.get(url)
    pageText = response.text