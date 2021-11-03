def solution(s):
    answer = []
    dic = {'zero':'0','one': '1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    num = ['0','1','2','3','4','5','6','7','8','9']
    start_index = 0
    end_index = 1
    
    for _ in range(len(s)+1):
        if s[start_index:end_index] in dic:
            answer.append(dic[s[start_index:end_index]])
            start_index += len(s[start_index:end_index])
            end_index+= 1
        else:
            if s[start_index:end_index] in num:
                answer.append(s[start_index:end_index])
                start_index += len(s[start_index:end_index])
            end_index += 1
    
    return int(''.join(answer))