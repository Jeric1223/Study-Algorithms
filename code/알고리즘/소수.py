"""n = int(input())

for i in range(n+1):
    result = True
    if i < 2:
        result = False
    for j in range(2,i):
        if i % j == 0:
            result = False
    if result:
        print(i, end=" ")"""

A,B = map(int,input().split())
n = B
a = [False,False] + [True]*(n-1)
primes=[]
answer = []

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(i*i, n+1, i):
        a[j] = False

for i in primes:
    if i >= A and i <= B:
        print(i)

