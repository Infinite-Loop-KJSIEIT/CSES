import sys 
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m=map(int,input().split())
g=[[]for i in range(n)]
rev_g=[[]for i in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    g[a-1].append(b-1)
    rev_g[b-1].append(a-1)
def dfs(v):
    # print(v,cycle)
    visited[v]=True
    for u in g[v]:

        if not visited[u]:
            dfs(u)
    ans.append(v)

visited=[False]*n
isCycle=False
ans=[]
for i in range(n):
    if not visited[i]:
        dfs(i)
topological_sort=reversed(ans)
count=[0]*n
mod=10**9+7
count[0]=1
for v in topological_sort:
    if len(rev_g[v])==0:
        continue
    for u in rev_g[v]:
        count[v]+=count[u]
    count[v]%=mod
print(count[n-1])