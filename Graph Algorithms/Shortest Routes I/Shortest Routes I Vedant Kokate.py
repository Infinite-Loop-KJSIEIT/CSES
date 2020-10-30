import heapq
import sys
from collections import defaultdict
def get_ints(): return map(int, sys.stdin.readline().strip().split())

n,m=get_ints()
g=defaultdict(list)
for i in range(m):
    a,b,c=get_ints()
    g[a-1].append((b-1,c))
dis=[10**15]*n
dis[0]=0
Q=[(0,0)]
heapq.heapify(Q)

while Q:
    at,d=(heapq.heappop(Q))
    if d>dis[at]:
        continue
    for loc,disAB in g[at]:
        if d+disAB<dis[loc]:
            dis[loc]=d+disAB
            heapq.heappush(Q,(loc,d+disAB))
print(*dis)
        
          

