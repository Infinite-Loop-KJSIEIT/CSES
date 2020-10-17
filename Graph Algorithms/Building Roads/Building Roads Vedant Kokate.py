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
 
def dfs(x,vis):
    stack=[x]
    while stack:
        p=stack.pop()
        for i in g[p]:
            if i not in vis.keys():
                stack.append(i)
                vis[i]=1
n,m=get_ints()
g=defaultdict(list)
for i in range(m):
    a,b=get_ints()
    g[a].append(b)
    g[b].append(a)
vis={}
ans=[]
for i in range(1,n+1):
    #print(vis)
    if i not in vis.keys():
        ans+=[i]
        dfs(i,vis)
print(len(ans)-1)
for i in range(len(ans)-1):
    print(ans[i],ans[i+1])
