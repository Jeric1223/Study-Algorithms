# ord() : 아스키코드로 변경 , chr() : 아스키 코드를 string  print(chr(ord(s[0])+n))
def solution(s, n):
    answer = []
    lst = list(''.join(s))
    print(lst)

    for i in lst:
        if i == ' ':
            answer.append(i)
        elif ord(i) >= 65 and ord(i) <= 90:  # 소문자
            if ord(i) + n > 90:  # Z값을 넘으면
                Temp = 90 - ord(i) + n
                answer.append(chr(64 + temp))
            else:
                answer.append(chr(ord(i) + n))
        elif ord(i) >= 97 and ord(i) <= 122:  # 대문자
            if ord(i) + n > 122:  # z값을 넘으면
                temp = 122 - ord(i) + n
                answer.append(chr(96 + temp))
            else:
                answer.append(chr(ord(i) + n))

    return ''.join(answer)