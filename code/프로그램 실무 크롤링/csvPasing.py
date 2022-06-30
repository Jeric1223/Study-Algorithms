import pymssql
import pandas as pd
import pyodbc

# 기존에 있던 포켓몬 가격정보들 csv 파일을 Pandas로 읽어왔습니다.
df = pd.read_csv('./sealprice.csv')

# 기존에 df에 있는 데이터들에서 랭크 시스템을 추가하기 위해서 기존에 있던 데이터들을 추출하였습니다.
no = df['no'].to_list()
price = df['price'].to_list()
second = df['second'].to_list()

# 포켓몬 랭크를 크롤링 한 데이터
rating = ['Hyper', 'Hyper', 'Hyper', 'Hyper', 'Epic', 'Epic', 'Epic', 'Hyper', 'Epic', 'Epic', 'Epic', 'Epic', 'Rare', 'Rare', 'Rare', 'Rare', 'Rare', 'Rare', 'Rare', 'Rare', 'Epic', 'Norma', 'Norma', 'Rare', 'Rare', 'Rare', 'Rare', 'Hyper', 'Epic', 'Epic', 'Epic', 'Rare', 'Norma', 'Norma', 'Rare', 'Norma', 'Norma', 'Rare', 'Epic', 'Epic', 'Epic', 'Epic', 'Epic', 'Epic', 'Rare', 'Rare', 'Rare', 'Rare', 'Rare', 'Rare', 'Rare', 'Rare', 'Rare', 'Epic', 'Rare', 'Hyper', 'Epic', 'Hyper', 'Epic', 'Rare', 'Rare', 'Epic', 'Epic', 'Rare', 'Rare', 'Rare', 'Epic', 'Epic', 'Epic', 'Rare', 'Rare', 'Rare', 'Rare', 'Rare', 'Rare', 'Rare', 'Rare', 'Rare', 'Rare', 'Rare', 'Epic', 'Epic', 'Epic', 'Epic', 'Rare', 'Epic', 'Rare', 'Rare', 'Rare', 'Rare', 'Epic', 'Epic', 'Rare', 'Rare', 'Rare', 'Hyper', 'Epic', 'Epic', 'Hyper', 'Rare', 'Rare', 'Rare', 'Rare', 'Epic', 'Hyper', 'Rare', 'Rare', 'Rare', 'Rare', 'Rare', 'Rare', 'Rare', 'Hyper', 'Hyper', 'Rare', 'Rare', 'Rare', 'Rare', 'Hyper', 'Epic', 'Epic', 'Rare', 'Rare', 'Rare', 'Epic', 'Epic', 'Rare', 'Epic', 'Epic', 'Hyper', 'Rare', 'Epic', 'Epic', 'Hyper', 'Epic', 'Epic', 'Epic', 'Epic', 'Epic', 'Epic', 'Epic', 'Rare', 'Rare', 'Epic', 'Rare', 'Rare', 'Rare', 'Hyper', 'Hyper', 'Hyper', 'Hyper', 'Epic', 'Epic', 'Hyper', 'Legendary', 'Legendary', 'Legendary', 'Legendary', 'Legendary']

# 데이터프레임을 새로운 데이터들 추가하여 넣었습니다.
df1 = pd.DataFrame({'no': no, \
        'price': price, \
        'second': second, \
        'rating': rating})

# 데이터프레임을 csv파일로 만들었습니다.
df1.to_csv('sealPriceAndRating.csv',encoding='utf-8-sig')
