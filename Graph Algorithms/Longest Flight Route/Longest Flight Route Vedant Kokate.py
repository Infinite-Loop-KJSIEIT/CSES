import sys 
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m=map(int,input().split())
g=[[]for i in range(n)]

for i in range(m):
    a,b=map(int,input().split())
    g[a-1].append(b-1)

def dfs(v):
    visited[v]=True
    for u in g[v]:
        if not visited[u]:
            dfs(u)
    ans.append(v+1)

visited=[False]*n
ans=[]
dfs(0)
print(*reversed(ans))