x, y, w, h = map(int,input().split())
MIN = 9999999999
MIN_TYPE = 999999
answer = 0

X_W = w-x
Y_H = h-y

X_0 = x-0
Y_0 = y-0

if X_W < Y_H:
    MIN = X_W
else:
    MIN = Y_H

if X_0 < Y_0:
    MIN_TYPE = X_0
else:
    MIN_TYPE = Y_0

if MIN_TYPE < MIN:
    print(MIN_TYPE)
else:
    print(MIN)
