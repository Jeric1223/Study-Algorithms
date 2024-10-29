dp = [0] * 100

def t(n):
    
    if n == 1:
        dp[n-1] = 1
        return dp[n-1]
    
    if dp[n-1] != 0:
        return dp[n-1]
    
    result = t(n-1)
    while(True):
        result += 1
        
        if '3' in str(result):
            continue
        if result % 3 == 0:
            continue

        else:
            dp[n-1] = result
            break
            
    return dp[n-1]

def solution(n):
    return t(n)