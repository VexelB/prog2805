import requests
import webbrowser
import pprint
url = 'https://api.thecatapi.com/v1/images/search'
headers={'x-api-key':'60ad62fb-7f4d-4a48-8bde-1539b3cd3339'}
try:
    response = requests.get(url, headers = headers)
    #pprint.pprint(response.json())
    #print()
    webbrowser.open(response.json()[0].get('url'))
except Exception as e:
    print(e)
