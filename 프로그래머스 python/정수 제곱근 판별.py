import math

def solution(n):
    answer = ''
    input_value = math.sqrt(n)
    new_value = 0
    if(input_value - int(input_value) == 0):
        new_value = int(input_value) + 1
        answer = new_value ** 2
    else :
        answer = -1
    return answer