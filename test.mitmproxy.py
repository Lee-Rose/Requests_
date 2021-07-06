import requests

proxies = {'https': 'http://localhost:8080',
           }

requests.get('https://habr.ru', proxies=proxies, verify=False)
