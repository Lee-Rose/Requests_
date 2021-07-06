import requests
from pprint import pprint

def search_herous():
    _access_token_html = 2619421814940190
    url = f'https://superheroapi.com/api/{_access_token_html}/search/'
    heroes = ['Hulk', 'Captain_America', 'Thanos']
    max_intel = 0
    max_name = ''
    for hero in heroes:
        url_hero = url + hero
        #pprint(url_hero)  #проверка ссылок на каждого героя
        resp = requests.get(url_hero)
        intel_hero = int(resp.json()['results'][0]['powerstats']['intelligence'])
        #print(f'{intel_hero}, {hero}') #здесь видим нужные данные
        if intel_hero > max_intel:
            max_intel = intel_hero
            max_name = hero
    print(max_name, max_intel)





def get_status():

    response = requests.get('https://superheroapi.com/')
    if response.status_code == 200:
        print('True')
        print(response.text)

search_herous()


