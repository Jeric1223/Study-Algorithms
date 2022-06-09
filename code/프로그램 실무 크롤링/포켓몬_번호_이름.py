import requests
from bs4 import BeautifulSoup
import ssl
from urllib.request import urlopen
from io import BytesIO
from PIL import Image
import os
import time

url = 'https://pokemon.fandom.com/ko/wiki/%EC%A0%84%EA%B5%AD%EB%8F%84%EA%B0%90/1%EC%84%B8%EB%8C%80'
list_arr = []
response = requests.get(url)
poketmon_list = []
poketmon_number = []

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    #포켓몬 정보 리스트 크롤링 but 이로치는 뻄
    requirementsTd = soup.select('#mw-content-text > div > table > tbody > tr > td:nth-child(1)')
    poketmonName = soup.select('#mw-content-text > div > table > tbody > tr> td:nth-child(4) > a')

    for index, item in enumerate(requirementsTd):
        #이로치 빼는 코드
        if item.text != "\xa0\n":
            poketmon_number.append(int(item.text[1:-1]))
            poketmon_list.append(poketmonName[index].text)

    print(poketmon_list)
    print(poketmon_number)

else :
    print(response.status_code)
