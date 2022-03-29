"""import sys
a,b = map(int,sys.stdin.readline().split())

for i in range(min(a,b), 0, -1):
    if a % i == 0 and b % i == 0:
        print(i)
        break

i = max(a,b)
while True:
    if i % a == 0 and i % b == 0:
        print(i)
        break
    i += 1"""

import math
import sys
a,b = map(int,sys.stdin.readline().split())
print(math.gcd(a,b))
print(math.lcm(a,b))