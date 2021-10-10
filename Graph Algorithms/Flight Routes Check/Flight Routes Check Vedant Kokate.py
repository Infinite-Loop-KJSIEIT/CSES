import sys
from typing import Sized
input=sys.stdin.readline
from heapq import heapify, heappush, heappop
sys.setrecursionlimit(10**6)
I=lambda:list(map(int,sys.stdin.readline().split()))

def dfs(g,rev):
    vis={}
    stack=[0]
    while stack and len(vis)<n:
        cur = stack.pop()
        vis[cur]= True

        for adj in g[cur]:
            if adj not in vis:
                stack.append(adj)

    if len(vis)==len(g):
        return "YES"
    else:
        for i in range(n):
            if i not in vis:
                if rev == False:
                    return f"1 {i+1}"
                else:
                    return f"{i+1} 1"
    


 
  
n,m=I()
g = [[] for i in range(n)]
rev_g = [[] for i in range(n)]
for _ in range(m):
    x,y=I()
    x-=1
    y-=1
    g[x].append(y)
    rev_g[y].append(x)

ans = dfs(g, False)
if ans == "YES":
    ans = dfs(rev_g, True)
    if ans =="YES":
        print(ans)
    else:
        print("NO")
        print(ans)

else:
    print("NO")
    print(ans)