def solution(dartResult):
    answer = 0
    dartResultStringList = list(dartResult)
    group_list = []
    score_dict = {'S': 1, 'D': 2, 'T': 3}
    start_index = 0
    
    for index, string in enumerate(dartResultStringList):
        if string in ['S', 'D', 'T']:
            # 이번 인덱스가 마지막이 아니고 다음 인덱스에 * 또는 #이 들어가는 경우
            # start_index를 설정하는 이유는 10의 자리수가 올 수 있기 때문에
            if index != len(dartResultStringList)-1 and dartResultStringList[index+1] in ['*','#']:
                group_list.append(dartResultStringList[start_index:index+2])
                start_index=index+2
            else:
                group_list.append(dartResultStringList[start_index:index+1])
                start_index = index+1
                
    for index, item in enumerate(group_list):
        # S D T의 인덱스를 구하는 변수
        # 구하는 이유는 점수가 10의 자리일 경우에 처리하기 위해
        find_number_last_index = min((item.index(char) for char in ['S', 'D', 'T'] if char in item), default=-1)
        print(item, find_number_last_index)
        score = int(''.join(item[0:find_number_last_index])) ** score_dict[item[find_number_last_index]]
        print(f'frist score: {score}')
        print(item)
        
        # 현재 점수에 * 또는 # 확인
        if find_number_last_index != len(item)-1:
            if '*' in item:
                score = score * 2
            else:
                score = score * -1
        print(f'second score: {score}')
        
        # 다음 점수에 *이 있는 경우 확인 및 처리
        if index != len(group_list)-1:
            if len(group_list[index+1]) == 3 and group_list[index+1][2] in ['*']:
                # 2배
                score = score*2
        print(f'thrid score: {score}')
                
        answer += score
                
    return answer