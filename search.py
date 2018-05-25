# -*- coding:UTF-8 -*-
import json
from bs4 import BeautifulSoup
import requests
import re
import redis


def weatherSpider():
    file_object = open('city.txt', 'r')
    try:
        all_cities = file_object.readlines()

        for city in all_cities:
            city_data = json.loads(city.strip())
            cityname = city_data['cityname']
            href = city_data['href']
            city_content = findData(href, cityname)
            r = redis.Redis(host='localhost', port=6379, db=0)
            # print(r)
            r.set(cityname, city_content)
            print(r.get(cityname))
    finally:
        file_object.close()


def findData(data_url, cityname):
    content_data = {}
    data_url = 'http://www.86pm25.com/city/anshan.html'
    html = requests.get(data_url, timeout=10)
    bf = BeautifulSoup(html.content, 'lxml')
    time = bf.find('div', class_='remark')
    time_text = time.get_text()
    mode = re.compile(r'\d+')
    txt = mode.findall(time_text)
    content_data['year'] = txt[0]  # 年
    content_data['month'] = txt[1]  # 月
    content_data['day'] = txt[2]  # 日
    content_data['hour'] = txt[3]  # 时
    content_data['city'] = cityname  # 城市

    pm_details = []
    print(cityname)
    pm = bf.find('div', class_='weilai').find_all('table')[0]

    if pm:
        pm = pm.find_all('tr')
        for pm_1 in pm:
            pm_detail_obj = {}

            if pm.index(pm_1) > 0:
                pm_detail = pm_1.find_all('td')
                pm_detail_obj['qu'] = pm_detail[0].get_text()
                pm_detail_obj['value'] = pm_detail[3].get_text()
                pm_details.append(pm_detail_obj)
    content_data['data'] = pm_details

    return content_data


if __name__ == '__main__':
    weatherSpider()
