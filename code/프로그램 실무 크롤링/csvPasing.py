import pymssql
import pandas as pd
import pyodbc

df = pd.read_csv('./sealprice.csv')

no = df['no'].to_list()
price = df['price'].to_list()
second = df['second'].to_list()
rating = ['Hyper', 'Hyper', 'Hyper', 'Hyper', 'Epic', 'Epic', 'Epic', 'Hyper', 'Epic', 'Epic', 'Epic', 'Epic', 'Rare', 'Rare', 'Rare', 'Rare', 'Rare', 'Rare', 'Rare', 'Rare', 'Epic', 'Norma', 'Norma', 'Rare', 'Rare', 'Rare', 'Rare', 'Hyper', 'Epic', 'Epic', 'Epic', 'Rare', 'Norma', 'Norma', 'Rare', 'Norma', 'Norma', 'Rare', 'Epic', 'Epic', 'Epic', 'Epic', 'Epic', 'Epic', 'Rare', 'Rare', 'Rare', 'Rare', 'Rare', 'Rare', 'Rare', 'Rare', 'Rare', 'Epic', 'Rare', 'Hyper', 'Epic', 'Hyper', 'Epic', 'Rare', 'Rare', 'Epic', 'Epic', 'Rare', 'Rare', 'Rare', 'Epic', 'Epic', 'Epic', 'Rare', 'Rare', 'Rare', 'Rare', 'Rare', 'Rare', 'Rare', 'Rare', 'Rare', 'Rare', 'Rare', 'Epic', 'Epic', 'Epic', 'Epic', 'Rare', 'Epic', 'Rare', 'Rare', 'Rare', 'Rare', 'Epic', 'Epic', 'Rare', 'Rare', 'Rare', 'Hyper', 'Epic', 'Epic', 'Hyper', 'Rare', 'Rare', 'Rare', 'Rare', 'Epic', 'Hyper', 'Rare', 'Rare', 'Rare', 'Rare', 'Rare', 'Rare', 'Rare', 'Hyper', 'Hyper', 'Rare', 'Rare', 'Rare', 'Rare', 'Hyper', 'Epic', 'Epic', 'Rare', 'Rare', 'Rare', 'Epic', 'Epic', 'Rare', 'Epic', 'Epic', 'Hyper', 'Rare', 'Epic', 'Epic', 'Hyper', 'Epic', 'Epic', 'Epic', 'Epic', 'Epic', 'Epic', 'Epic', 'Rare', 'Rare', 'Epic', 'Rare', 'Rare', 'Rare', 'Hyper', 'Hyper', 'Hyper', 'Hyper', 'Epic', 'Epic', 'Hyper', 'Legendary', 'Legendary', 'Legendary', 'Legendary', 'Legendary']


df1 = pd.DataFrame({'no': no, \
        'price': price, \
        'second': second, \
        'rating': rating})

df1.to_csv('sealPriceAndRating.csv',encoding='utf-8-sig')
