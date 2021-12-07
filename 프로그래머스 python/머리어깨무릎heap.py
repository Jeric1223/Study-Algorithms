import heapq

lst = [2,3,9,4,3,1,2,5]

#시퀀스를 힙으로 변경
heapq.heapify(lst)

h = []

heapq.heappush(h, (7,'jwa'))
heapq.heappush(h, (3,'seo'))
heapq.heappush(h, (1,'shin'))
heapq.heappush(h, (5,'kang'))

heapq.heappop(h)

print(h)