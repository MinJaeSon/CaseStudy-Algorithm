# 교집합
import sys

input = sys.stdin.readline    # N, M이 백만까지도 들어올 수 있으므로 입력이 오래걸릴 수 있어 빠른 입출력 사용

while True: # 테스트 케이스가 얼마가 들어올지 모르기 때문에 while문 사용
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break

    a = set()
    for _ in range(N):
        a.add(input())

    b = set()
    for _ in range(M):
        b.add(input())

    print(len(a & b))