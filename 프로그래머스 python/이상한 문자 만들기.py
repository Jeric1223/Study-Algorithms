def solution(s):
    str = ''
    arr = list(s.split(' '))
    temp_arr = []
    new_arr = []
    sum = 0
    
    for i in arr:
        i_len = len(i)
        for j in range(i_len):
            if(j % 2 == 0):
                temp_arr.append(i[j].upper()) 
            else:
                temp_arr.append(i[j].lower())
        new_arr.append(''.join(temp_arr))
        temp_arr = []
        
    return ' '.join(new_arr)