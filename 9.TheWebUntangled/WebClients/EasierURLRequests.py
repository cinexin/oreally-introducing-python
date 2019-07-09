# install 'requests' python module first
import requests
import json

url = 'https://www.googleapis.com/books/v1/volumes?q=isbn:0747532699'
resp = requests.get(url)
print(resp)
js_data = resp.json()
try:
    items = js_data['items']
    volumeInfo = items[0]['volumeInfo']
    print('Title:', volumeInfo['title'])
    print('Authors:', volumeInfo['authors'])
    print('Summary:', volumeInfo['description'])
except:
    print('Error when parsing json data...')
    