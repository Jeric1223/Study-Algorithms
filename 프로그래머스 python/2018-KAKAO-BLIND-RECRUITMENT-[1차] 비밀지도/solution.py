def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        len_n_bin_str1 = bin(arr1[i]).split('0b')[1].zfill(n)
        len_n_bin_str2 = bin(arr2[i]).split('0b')[1].zfill(n)
        
        result_str = ''
        for j in range(n):
            if len_n_bin_str1[j] == '1' or len_n_bin_str2[j] == '1':
                result_str += '#'
            else:
                result_str += ' '
        
        answer.append(result_str)

    return answer