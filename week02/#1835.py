# 거꾸로 돌리면서 답을 구할 수 있는 문제

from collections import deque

N = int(input())
dq = deque()
for i in range(N, 0, -1):
    dq.appendleft(i)
    for _ in range(i):
        dq.appendleft(dq.pop())

print(*list(dq))    # dq를 리스트에 집어 넣어서 포인터로 요소만 바로 출력