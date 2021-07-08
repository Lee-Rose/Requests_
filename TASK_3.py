import requests
import time
import json

params = {
    'fromdate': int(time.time())-86400*2,
    'todate': int(time.time()),
    'tagged': 'python',
    'site': 'stackoverflow'
}

headers = {
    'Content-Type': 'application/json'
}

if __name__ == "__main__":
    url = 'http://api.stackexchange.com/2.3/questions'
    result = requests.get(url, headers=headers, params=params)

    data = json.loads(result.text)
    for item in data['items']:
        print(item['title'])

