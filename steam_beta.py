import requests
from bs4 import BeautifulSoup
import fake_useragent

user = fake_useragent.UserAgent().random
header = {'User-Agent': user}
page = 1
games_found = 0

while True:
    base_url = 'https://store.steampowered.com/search/?hwtype=0&supportedlang=russian%2Cenglish%2Cturkish%2Cvietnamese&tags=492&ndl=1'
    r = requests.get(f'{base_url}&page={page}')

    html = BeautifulSoup(r.content, 'html.parser')
    items = html.select("a.search_result_row")
    if(len(items)):
        for el in items:
            title = el.select('.title')
            if title:
                print(title[0].text.strip())
        page += 1
    else:
        break