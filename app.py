# -*- coding:UTF-8 -*-

import requests
import json
import csv
from bs4 import BeautifulSoup


class weatherSpider(object):
    JSON_URL = 'http://www.86pm25.com/'
    html = requests.get(JSON_URL, timeout=10)
    content = html.content
    bf = BeautifulSoup(content)
    texts = bf.find('dl', id='clist').find_all('a')
    f = open('city.txt', 'w')
    cityObj = {}

    for city in texts:
        cityObj['cityname'] = city.get_text()
        cityObj['href'] = 'http://www.86pm25.com/' + city.attrs['href']
        f.write(json.dumps(cityObj, ensure_ascii=False))
        f.write('\n')


if __name__ == '__main__':
    weatherSpider()
