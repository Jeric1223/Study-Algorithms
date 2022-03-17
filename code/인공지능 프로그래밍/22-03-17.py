import numpy as np

#다차원 행렬
(2,3,4)
c = np.array([[1,2],[3,4],[5,6]])
d = np.array([[1,2,3],[4,5,6]])
print(c.shape)
k = np.matmul(c,d)
print(k.shape, k)


legendV = 5
z = k*legendV
print(z)

#단순 배열 생성 명령
a = np.zeros(5)
print(a)

#초기화하지않은 배열 생성
g = np.empty((4,3))
print(g)

#numpy의 range : arange()
print(np.arange(10))
print(np.arange(3,21,2))
print(np.linspace(0,100,5))
print(np.linspace(0,100,5, endpoint=False)) #끝값 포함 x
print(c.T)
# 나는 문어 꿈을 꾸는 문어 꿈속에서 나는 무엇이든지 될 수 있어
# qodufdml zmrl qusgud
yas = np.arange(12)
aas = yas.reshape(3,4)
aas[0][0] = 100
print(aas)
aas = aas.flatten()
aas = aas[:, np.newaxis]
print(aas)

a1 = np.ones((2,3))
a2 = np.zeros((2,2))

print(np.hstack([a1,a2]))
zq = np.array([[0,1,2], [3,4,5]])
print(np.tile(zq,2))

m = np.arange(3)
n = np.arange(5)
m,n = np.meshgrid(m,n)
print([list(zip(m,n))] for m,n in zip(m,n))