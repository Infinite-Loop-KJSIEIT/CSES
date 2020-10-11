n = int(input())
act = []
for _ in range(n):
    act.append(list(map(int, input().split())))

act = sorted(act, key=lambda x: x[1])
ans, l = 0, 0
for i in range(n):
    if act[i][0] >= l:
        ans += 1
        l = act[i][1]
print(ans)
