import urllib.request as url_req
from urllib.parse import quote
import json

url = 'https://www.googleapis.com/books/v1/volumes?q=isbn:0747532699'
conn = url_req.urlopen(url)
data = conn.read()
print(data)
content_type = conn.getheader('Content-Type')
print(content_type)

# let's try to parse it with json...
try:
    str_data = data.decode('utf8')
    js_data = json.loads(str_data)
    items = js_data['items']
    volumeInfo = items[0]['volumeInfo']
    print('Authors:', volumeInfo['authors'])
except:
    print('Error when parsing json data...')