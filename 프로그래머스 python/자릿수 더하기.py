def solution(n):
    sum = 0
    while True:
        sum += n%10
        n = n//10
        if(n == 0):
            break;
    
    return sum