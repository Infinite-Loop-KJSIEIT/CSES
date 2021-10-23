n, m = list(map(int,input().split()))
arr = [list(input()) for i in range(n)]
ans = 0
x = [0, 0, -1, 1]
y = [1, -1, 0, 0]
for i in range(n):
    for j in range(m):
        if arr[i][j] == ".":
            ans += 1
            arr[i][j] = "#"
            stack = [(i, j)]
            while stack:
                cx, cy = stack.pop()
                for k in range(4):
                    tx, ty = cx + x[k], cy + y[k]
                    if -1 < tx < n and -1 < ty < m and arr[tx][ty] != "#":
                        arr[tx][ty] = "#"
                        stack.append((tx, ty))
print(ans)