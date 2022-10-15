N, M = map(int, input().split())
m = []
for _ in range(N):
    m.append(list(input()))

ans = 0
r, c = [0, 0, 1, -1], [1, -1, 0, 0]
for i in range(N):
    for j in range(M):
        if m[i][j] == '.':
            ans += 1
            stack = [(i, j)]
            while stack:
                x, y = stack.pop()
                m[x][y] = '#'
                for k in range(4):
                    R, C = x + int(r[k]), y + int(c[k])
                    if 0 <= R < N and 0 <= C < M and m[R][C] == '.':
                        stack += [(R, C)]

print(ans)
