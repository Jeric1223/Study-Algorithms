import requests
from bs4 import BeautifulSoup
import ssl
from urllib.request import urlopen
from io import BytesIO
from PIL import Image
import os
import time

url = 'https://mdma.co.kr/%ED%8F%AC%EC%BC%93%EB%AA%AC2022/'

list_arr = []

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    imageDiv = soup.select('div > img')

    for item in map(lambda x: x['src'], imageDiv[:-1]):
        # time check
        start = time.time()
        # curl 요청
        os.system(f"curl {item} > {item.split('/')[-1]}")
        # 이미지 다운로드 시간 체크
        print(time.time() - start)
        # 저장 된 이미지 확인
        img = Image.open(item.split('/')[-1])
else :
    print(response.status_code)
