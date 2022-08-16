import csv
import numpy as np

with open('data.csv','r') as file:
    data = csv.reader(file,delimiter=',')
    """header = next(data)
    print(type(header))"""
    maxArr = []
    arr = []
    for row in data:
        arr.append(row[0:5])
        if row[4] == '':
            row[4] = -99
        maxArr.append(float(row[4]))

    maxvalue = max(maxArr)
    maxIndex = maxArr.index(maxvalue)
    print(f'서울 {arr[maxIndex][0]} 일에 역대급 최고온도 {maxvalue}')