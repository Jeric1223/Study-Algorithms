def solution(strings, n):
    answer = []
    new = []
    for value in strings:
        new.append(value[n] + value)
    new.sort()
    for i in new:
        answer.append(i[1:])
    print(answer)
    return answer