import time
import bisect
import math
import sys
import random as r
from collections import defaultdict 
from heapq import heapify, heappush, heappop 
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def inp_int(): return int(sys.stdin.readline().strip())
def inp_str(): return(sys.stdin.readline().strip())
def out(output): sys.stdout.write(str(output))
def get_strs(): return  sys.stdin.readline().strip().split()
sys.setrecursionlimit(10**6)
 
def bfs(x,vis):
    stack=[x]
    vis[1]=1
    while stack:
        #print(ans)
        #print(stack)
        #print(vis)
        p=stack.pop(0)
        if p==n:
            return
        for i in g[p]:
            if i not in vis.keys():
                stack.append(i)
                ans[i]+=ans[p]+" "+str(i)
                vis[i]=1
n,m=get_ints()
g=defaultdict(list)
for i in range(m):
    a,b=get_ints()
    g[a].append(b)
    g[b].append(a)
vis={}
ans=["" for i in range(n+1)]
bfs(1,vis)
 
if len(ans[n]):
    print((len(ans[n]))//2+1)
    
    print(str(1)+ans[n])
else:
    print("IMPOSSIBLE")
