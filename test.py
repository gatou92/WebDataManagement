import requests
import urllib

parameters = {
    'somevar': 123456789
}
url = 'http://localhost:9090/path/final/?' + urllib.urlencode(parameters)
response = requests.get(url)
flickr_json = response.json()

print flickr_json
