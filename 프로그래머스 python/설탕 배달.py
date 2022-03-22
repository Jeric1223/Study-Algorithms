def baekjun():
    n = int(input())
    answer = 0

    while(n>=0):
        if n%5 == 0:
            answer += n//5
            print(answer)
            return
        n= n-3
        answer += 1
    print(-1)

baekjun()