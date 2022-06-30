import requests
from bs4 import BeautifulSoup
import ssl
from urllib.request import urlopen
from io import BytesIO
from PIL import Image
import os
import time

url = 'https://meta-house.tistory.com/323'

list_arr = []
name_list = []

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    # image를 추출할 select와 이름을 추출할 select
    imageDiv = soup.select('#content > div.inner > div.entry-content > div > table > tbody > tr > td:nth-child(3) > figure > span > img')
    poketmonName = soup.select('#content > div.inner > div.entry-content > div > table > tbody > tr > td:nth-child(2)')

    # 추출한 poketmonName 리스트를 반복문을 통해서 가공하는 코드
    for index in range(1,len(poketmonName)+1):

        # (2개)라는 데이터의 속성을 알기위해서 테스트 코드
        if "(2개)" in poketmonName[index].text:
            print(poketmonName[index].text)

        print(poketmonName[index].text[0:-4])
        # 포켓몬 씰중에 중복되는 포켓몬 들이 있기 때문에 만약에 (2개)라고 되어있으면 (2개)라는 부분을 삭제하는 코드
        if poketmonName[index].text[-1:-5] == "(2개)":
            name_list.append(poketmonName[index].text[0:-4])
        name_list.append(poketmonName[index].text)

    print(poketmonName[1].text)
else:
    print(response.status_code)
