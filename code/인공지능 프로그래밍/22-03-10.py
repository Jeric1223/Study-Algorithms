import pandas as pd
import numpy as np

#numpy, pandas 설치 확인
#print(np.__version__)
#print( pd.__version__ )


#emumerate 함수
list1 = ['인덱스 1', '인덱스 2', '인덱스 3']

for index, value in enumerate(list1):
    print(index, value)

#파일 입출력
with open("./파일입출력.txt", "w") as file:
    file.write("it's legend file open in python")

#lamda 함수
sum = lambda x,y : x+y
print(sum(10,30))

#map 함수
# def power(n):
#     return n*n

# nlist = map(power,[1,2,3,4,5]))
# list(nlist)

list3 = map(lambda x: x*x, [1,2,3,4,5])
print(list(list3))

#가변 매개변수
def value_times(times, *values):
    for value in values:
        print(times*value)
print(value_times(3,1,2,3,4,5))

#기본 매개변수
def value_time(value, times=2):
    print(times * value)
value_time(3,5)
value_time(3)

#키워드 매개변수
def value_test(*values, times=2):
    for value in values:
        print(times * value)
value_test(1,2,3,4, times=100)

# 배열 np.array
import numpy as np

a = np.array([i for i in range(1,11)])
print(a)
print(type(a))

#백터화 연산
a = np.array([1,2,3])
b = np.array([10,20,30])
print(2*a+b)
print(a==2)

#다차원 배열
(2,3,4)
c = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[13,14,15,16],[17,18,19,20],[21,22,23,24]]])
print(c)
print(c.shape)

#인덱싱
a2 = np.array([0,1,2,3,4,5,6,7,8,9])
#idx = np.array([True,False,True,False,True,False,True,False,True])
idx = np.array([2,2,2,1,1,1,0,0,0])
print(a2[idx])


#dtype 지정
x= np.array([1,2,3], dtype='f8')
print(x.dtype)
print(x[0] + x[1])

#다차원 배열
(2,3,4)
c = np.array([[1,2],[3,4],[5,6]])
d = np.array([[1,2,3],[4,5,6]])
print(c,d)
print(c.shape, d.shape)\ASDasd
