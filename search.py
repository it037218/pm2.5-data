# -*- coding:UTF-8 -*-
import json
from bs4 import BeautifulSoup
import requests


def weatherSpider():
    file_object = open('city.txt', 'r')
    try:
        all_cities = file_object.readlines()

        for city in all_cities:
            city_data = json.loads(city.strip())
            cityname = city_data['cityname']
            href = city_data['href']
            findData(href)

    finally:
        file_object.close()


def findData(data_url):
    html = requests.get(data_url, timeout=10)
    bf = BeautifulSoup(html.content)

if __name__ == '__main__':
    weatherSpider()
