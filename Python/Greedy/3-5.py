n, k = map(int, input().split())

count = 0
while True:
   n = n//k if n%k == 0 else n-1
   count += 1
   if n == 1:
       break
print(count)
