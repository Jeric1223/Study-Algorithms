# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

check_list = ['S', 'S', 'S', 'A', 'A', 'S', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'C', 'C', 'B', 'B', 'B', 'B', 'S', 'A', 'A', 'A', 'B', 'C', 'C', 'B', 'C', 'C', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'S', 'A', 'S', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'S', 'A', 'A', 'S', 'B', 'B', 'B', 'B', 'A', 'S', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'S', 'S', 'B', 'B', 'B', 'B', 'S', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'S', 'B', 'A', 'A', 'S', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'S', 'S', 'S', 'S', 'A', 'S', 'S', 'SS', 'SS', 'SS', 'SS', 'SS']
rating_arr = []

url = 'https://guri-guri.tistory.com/371'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    Rating = soup.select('table > tbody > tr > td:nth-child(3)')

    for index,item in enumerate(check_list):
        rating_arr.append(item)
        if index == 0 or index == 4 or index == 8 or index == 136 or index == 147 or index == 157:
            rating_arr.append(item)

else:
    print(response.status_code)

print(rating_arr, '\n', len(rating_arr))








