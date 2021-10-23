import sys
from typing import Sized
input=sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**6)
I=lambda:list(map(int,sys.stdin.readline().split()))

def dfs1(v):
    # print(v)
    vis[v]=True
    for u in g[v]:
        if not vis[u]:
            dfs1(u)
    order.append(v)


def dfs2(v):
    # print(v)
    vis[v]=True
    for u in rev_g[v]:
        if not vis[u]:
            dfs2(u)
    component.append(v)
                

n,m=I()
g = [[] for i in range(n)]
rev_g = [[] for i in range(n)]
for _ in range(m):
    x,y=I()
    x-=1
    y-=1
    g[x].append(y)
    rev_g[y].append(x)

vis=[False]*n
order = []
for i in range(n):
    if not vis[i]:
        dfs1(i)

order.reverse()

# print(order)

vis=[False]*n
ans=[-1]*n
index = 1
for v in order:
    if not vis[v]:
        component = []
        dfs2(v)
        # print(component)
        for i in component:
            ans[i]=index
        index+=1
print(index-1)
print(*ans)