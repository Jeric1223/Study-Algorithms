n = input()
arr = list(map(int, input().split()))

sosu = 0
for num in arr:
    error = 0
    if num > 2 :
        for i in range(3, num, 2):  # 2부터 n-1까지
            if num % i == 0:
                error += 1  # 2부터 n-1까지 나눈 몫이 0이면 error가 증가
        if error == 0:
            sosu += 1  # error가 없으면 소수.
print(sosu)