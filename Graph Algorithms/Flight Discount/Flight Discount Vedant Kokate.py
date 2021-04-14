import sys
from heapq import *
input=sys.stdin.readline
inf = 10**15
n,m = map(int,input().split())
g=[[] for _ in range(n+1)]
rg=[[] for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    g[a].append((b,c))
    rg[b].append((a,c))
 
df=[inf]*(n+1)
db=[inf]*(n+1)
 
def djk(i,d,e):
    d[i]=0
    q=[(0,i)]
    while q:
        p,a = heappop(q)
        if p==d[a]:
            for b,c in e[a]:
                if d[b]>p+c:
                    d[b]=p+c
                    heappush(q,(d[b],b))
 
djk(1,df,g)
djk(n,db,rg)
 
d = inf
for a in range(1,n+1):
    for b,c in g[a]:
        d = min(d, c//2+df[a]+db[b])
 
print(d)