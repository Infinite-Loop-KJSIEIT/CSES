import sys
input=sys.stdin.readline
from heapq import heapify, heappush, heappop
sys.setrecursionlimit(10**6)
I=lambda:list(map(int,sys.stdin.readline().split()))

n,m=I()
g=[[]for i in range(n+1)]
for _ in range(m):
    a,b,c=I()
    g[a].append((b,c))
    g[b].append((a,c))
# print(g)

heap=[]
heapify(heap)
vis={}
for node,cost in g[1]:
    heappush(heap,(cost,node))
vis[1]=True
ans=0
while len(vis)<n and len(heap)>0:
    cost,node = heappop(heap)
    if node not in vis:
        ans += cost
        for node2,cost2 in g[node]:
            heappush(heap,(cost2,node2))
        vis[node]=True
if len(vis)==n:
    print(ans)
else:
    print("IMPOSSIBLE")