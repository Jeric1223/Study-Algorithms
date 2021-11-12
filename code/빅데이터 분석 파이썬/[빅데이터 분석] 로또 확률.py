import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

n = input() #몇회차 까지 데이터를 수집하겠습니까? 987회가 최대
lotto_num_arr = []

#몇회까지의 데이터 입력 받기
if int(n) > 988:
    print('최대 988회 까지 있습니다')

#데이터 추출하기
for i in range(0,int(n)+1):
    URL = fr'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%A1%9C%EB%98%90+{i}%ED%9A%8C'
    url = URL
    req = requests.get(url)
    if req.status_code == requests.codes.ok: #requests 성공시
        soup = BeautifulSoup(req.text, 'lxml')
        num = soup.find_all("span", {"class" : "num"}) #로또 번호 묶음
        for i in num: #로또 번호 추출
            lotto_num_arr.append(int(i.get_text()))
    else:
        print('fail nn')

odd_even_arr = [0,0]
for i in lotto_num_arr: #로또 홀수 짝수 배열로
    if i % 2 == 0:
        odd_even_arr[1] += 1
    else:
        odd_even_arr[0] += 1

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = '홀수', '짝수'
sizes = [odd_even_arr[0], odd_even_arr[1]]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax1.set_title(f"1회부터 {n}회까지 로또 홀수 짝수 비율")

plt.show()

