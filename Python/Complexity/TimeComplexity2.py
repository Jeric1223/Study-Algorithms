#수행 시간 측정 소스 코드
from random import randint
import time
start_time = time.time() #측정 시작

# 프로그램 소스코드
end_time = time.time() #측정 종료
print("time:", end_time - start_time) #수행 시간 출력

# 선택 정렬과 기본 정렬 라이브러리의 수행 시간 비교

# 배열에 10,000개의 정수를 삽입
array= []
for _ in range(10000):
    array.append(randint(1,100)) # 1부터 100사이의 랜덤함 정수

# 선택 정렬 프로그램 성능 측정
start_time = time.time()

#선택 정렬 프로그램 소스코드
for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i + 1,len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스와프

end_time = time.time() #측정 종료
print("선택 정렬 성능 측정:",end_time - start_time) #수행 시간 출력

#배열을 다시 무작위 데이터로 초기화
array= []
for _ in range(10000):
    array.append(randint(1,100)) # 1부터 100사이의 랜덤함 정수

# 선택 정렬 프로그램 성능 측정
start_time = time.time()

array.sort()

end_time = time.time() #측정 종료
print("기본 정렬 라이브러리 성능 측정: ", end_time-start_time) #수행 시간 출력

#가독성을 해치지 않는 선에서 최대한 복잡도가 낮게 프로그램을 작성해야한다.