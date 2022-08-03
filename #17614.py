N = int(input())
ans = 0
for i in range(1, N+1):
    for j in str(i):
        if j in '369':
            ans += 1

print(ans)