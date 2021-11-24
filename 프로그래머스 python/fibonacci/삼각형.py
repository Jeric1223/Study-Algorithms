n = int(input())
input_arr = []

for i in range(n):
    input_arr.append(int(input()))

def solution(n):
    d = [0] * 101
    d[1] = 1
    d[2] = 1
    d[3] = 1
    d[4] = 2
    d[5] = 2
    d[6] = 3
    if d[n]: return d[n]
    for i in range(7, n+1):
        d[i]=d[i-1]+d[i-5]
    return d[n]

for i in input_arr:
    print(solution(i))
