def solution(num):
    input_value = num;
    i = 0
    while input_value != 1:
        if(i >= 500) :
            i = -1
            break
        i += 1
        if(input_value%2 == 0):
            input_value = input_value//2
        else:
            input_value = input_value*3+1
            
    answer = i
    return answer