def solution(n):
    arr = []
    answer = ''
    input_value = n;
    input_len = len(str(input_value))
    for _ in range(input_len):
        arr.append(n%10)
        n = n//10
    arr.sort(reverse=True)
    for i in arr:
        answer += str(i)
    answer = int(answer)
    return answer