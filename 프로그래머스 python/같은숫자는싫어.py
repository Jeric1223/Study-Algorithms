arr = list(map(int, input().split()))
#temp에는 인덱스 arr 실제값

def solution(arr):
    answer = []
    temp = []
    i = 0
    while True:
        if i >= len(arr)-1:
            break;
        if arr[i] == arr[i+1]:
            temp.append(i)
        i += 1
    cnt = 0
    for i in range(arr.__len__()):
        if cnt < temp.__len__() :
            if i == temp[cnt]:
                cnt += 1
                continue
        answer.append(arr[i])

    return answer;

print(solution(arr))

