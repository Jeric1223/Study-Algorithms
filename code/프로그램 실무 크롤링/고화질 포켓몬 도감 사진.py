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
    imageDiv = soup.select('#content > div.inner > div.entry-content > div > table > tbody > tr > td:nth-child(3) > figure > span > img')
    poketmonName = soup.select('#content > div.inner > div.entry-content > div > table > tbody > tr > td:nth-child(2)')

    for index in range(1,len(poketmonName)+1):
        if "(2개)" in poketmonName[index].text:
            print(poketmonName[index].text)

        print(poketmonName[index].text[0:-4])
        # if poketmonName[index].text[-1:-5] == "(2개)":
        #     name_list.append(poketmonName[index].text[0:-4])
        # name_list.append(poketmonName[index].text)

    print(poketmonName[1].text)

    for item in map(lambda x: x['src'], imageDiv[:-1]):
        start = time.time()
        print(item)
        # os.system(f"curl {item} > {item.split('/')[-1]}")
        print(time.time() - start)
        # img = Image.open(item.split('/')[-1])
else:
    print(response.status_code)
