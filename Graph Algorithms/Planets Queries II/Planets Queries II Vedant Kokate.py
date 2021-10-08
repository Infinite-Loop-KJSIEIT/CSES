import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
I=lambda:list(map(int,sys.stdin.readline().split()))

def get(x,y):
    if (y < 0): return 0
    for i in range(lim):
        if y&(1<<i):
            x=dp[i][x]
    return(x)

def dfs(u):
    stack=[u]
    while stack:
        last=stack[-1]
        vis[last]=True
        Next=dp[0][last]
        if not vis[Next]:
            stack.append(Next)
        else:
            stack.pop()
            h[last]=h[Next]+1

lim=20
n,q=I()
dp=[[0,*I()]]
vis=[False]*(n+1)
h=[0]*(n+1)
for i in range(lim):
    temp=dp[-1]
    dp.append([temp[j] for j in temp])

for i in range(1,n+1):
    if not(h[i]):
        dfs(i)

# print(*h)
for _ in range(q):
    u,v=I()
    x = get(u, h[u])
    # print('x',x)
    if (get(u, h[u] - h[v]) == v):
        print(h[u] - h[v])  
    elif (get(x, h[x] - h[v]) == v):
        print( h[x] - h[v] + h[u]) 
    else:
        print(-1)

