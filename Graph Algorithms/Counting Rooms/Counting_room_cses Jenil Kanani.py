ans = 0
n, m = map(int, input().split())
arr = [list(input()) for i in range(n)]
x = [-1, 0, 1, 0]
y = [0, 1, 0, -1]
def dfs(i,j):
    stack = [(i,j)]
    while stack:
        cx, cy = stack.pop()
        for i in range(4):
            if -1 < cx + x[i] < n and -1 < cy + y[i] < m:
                if arr[cx + x[i]][cy + y[i]] == "." :
                    arr[cx + x[i]][cy + y[i]] = "#" 
                    stack.append((cx + x[i],cy + y[i]))
            else:
                arr[cx][cy] = "#" 
for i in range(n):
    for j in range(m):
        if arr[i][j] == ".":
            arr[i][j] = "#"
            dfs(i,j)
            ans += 1
print(ans)
