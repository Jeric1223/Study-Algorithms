import csv

with open('data.csv','r') as file:
    data = csv.reader(file,delimiter=',')
    arr = []
    for row in data:
        arr.append(row[0:5])
        print(row[0:5])
    print(len(arr))