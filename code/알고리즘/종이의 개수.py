n = int(input())
mylist=[list(map(int, input().split())) for _ in range(n)]

print(mylist)

def solve(x,y,n):
    if same(x,y,n):
        cnt[a[x][y]]