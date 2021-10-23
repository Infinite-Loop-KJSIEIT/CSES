import sys
input=sys.stdin.readline
from heapq import heapify,heappop,heappush

n,m,k=map(int,input().split())
g=[[]for i in range(n)]
for i in range(m):
    a,b,c=map(int,input().split())
    g[a-1].append((b-1,c))

q=[]
heapify(q)
heappush(q,(0,0))
count=[0]*n
K=k
ans=[]
while k:
    D,node=heappop(q)
    if count[node]<=K:
        count[node]+=1
        if node==n-1:
            k-=1
            ans.append(D)
            # print(D)
        for Node,dist in g[node]:
            heappush(q,(D+dist,Node))

print(*ans)
