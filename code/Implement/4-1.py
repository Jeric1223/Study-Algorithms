n = int(input())
wayArr = list(input().split())
space = {}
space['x'] = 1
space['y'] = 1

for i in wayArr:
    if i == 'R' and space['x'] != n:
        space['x'] += 1
    elif i == 'L' and space['x'] != 1:
        space['x'] -= 1
    elif i == 'U' and space['y'] != 1:
        space['y'] -= 1
    elif i == 'D' and space['y'] != n:
        space['y'] += 1

print(f"{space.get('y')} {space.get('x')}")