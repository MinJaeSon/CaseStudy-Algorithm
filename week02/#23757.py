# 우선순위 큐- max-heap 사용 : O(nlogn)
from heapq import heappush, heappop # 간단하게 사용하는 방법 2 : import heapq as hq

N, M = map(int, input().split())
max_heap = []
for c in map(int, input().split()):
    heappush(max_heap, -c)   # 파이썬은 max-heap을 지원하지 않으므로 부호를 바꿔서 최대힙 사용
    # ex. [-4, -3, -2, -1]
ans = 1
for w in map(int, input().split()):
    gift = -heappop(max_heap)    # heappop -> 가장 작은 원소(ex. -4)가 pop됨
    if w > gift:
        ans = 0
        break
    else:
        heappush(max_heap, -(gift - w)) # 넣을 땐 다시 -처리

print(ans)