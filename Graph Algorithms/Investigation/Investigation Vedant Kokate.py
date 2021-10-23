from heapq import heapify, heappush, heappop
import sys
input=sys.stdin.readline
mod=10**9+7

n,m=map(int,input().split())
g=[[]for i in range(n)]
for i in range(m):
    a,b,c=map(int,input().split())
    a-=1
    b-=1
    g[a].append((b,c))

heap=[(0,0)]
heapify(heap)

vis=[False]*n
min_dis=[-1]*n
paths=[-1]*n
min_nodes=[-1]*n
max_nodes=[-1]*n
min_dis[0],paths[0],min_nodes[0],max_nodes[0] = 0,1,0,0

while heap:

    weight,cur_node=heappop(heap)
    if vis[cur_node]:        continue
    vis[cur_node]=True

    for node,w in g[cur_node]:

        if vis[node]:continue
        
        if min_dis[node]==-1 or min_dis[node] > min_dis[cur_node]+w:
            min_dis[node] = min_dis[cur_node]+w
            paths[node] = paths[cur_node]
            min_nodes[node] = min_nodes[cur_node]+1
            max_nodes[node] = max_nodes[cur_node]+1
            heappush(heap, (min_dis[node],node))

        elif min_dis[node] == min_dis[cur_node]+w:
            paths[node] += paths[cur_node]
            paths[node]%=mod
            min_nodes[node] = min(min_nodes[cur_node]+1,min_nodes[node])
            max_nodes[node] = max(max_nodes[cur_node]+1,max_nodes[node])
            heappush(heap, (min_dis[node],node))

print(min_dis[-1],paths[-1],min_nodes[-1],max_nodes[-1])

