import requests
from bs4 import BeautifulSoup

list_arr = []

url = 'https://www.fnnews.com/candidateCompare?can_1=1&can_2=2'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.select('div.cell.c_cell.ft_16w')
    for title in titles:
        list_arr.append(title.get_text())
else :
    print(response.status_code)

print(list_arr)