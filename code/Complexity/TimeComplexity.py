# 1-1
array = [3,5,1,2,4] #5개의 데이터(N == 5)
summary = 0 # 합계를 저장할 변수

# 모든 데이터를 하나씩 확인하며 합계를 계산
for x in array:
    summary += x

print(summary) #시간 복잡도를 O(N)이라고 표현

# 1-2
a=5
b=7
print(a+b) #시간 복잡도 O(1)

# 1-3
array = [3,5,1,2,4] #5개의 데이터(N = 5)

for i in array:
    for j in array:
        temp = i * j
        print(temp) #시간 복잡도 O(N^2)
