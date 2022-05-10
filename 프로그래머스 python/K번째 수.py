def solution(array, commands):

    answer = []

    for command_item in commands:
        start = command_item[0] - 1
        end = command_item[1]
        k = command_item[2]
        answer.append(list(sorted(array[start:end]))[k-1])

    return answer