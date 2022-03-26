arr = []
answer=[]

while True:
    n = input()
    if n == "0":
        break
    else:
        arr.append(n)

for value in arr:
    if value == value[::-1]:
        answer.append('yes')
    else:
        answer.append('no')

print(*answer, sep='\n')
