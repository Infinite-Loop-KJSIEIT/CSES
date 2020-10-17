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
 
def check():
    for i,l in g.items():
        for j in l:
            if col[i]==col[j]:
                return "IMPOSSIBLE"
    ans=""
    for i in range(1,n+1):
        ans+=str(col[i]+1)+" "
    return ans[:-1]
        
 
def dfs(x,c):
    if x in vis.keys():
        return
    vis[x]=1
    col[x]=c
    for i in g[x]:
        if i not in vis.keys():
            dfs(i,1-c)
        
n,m=get_ints()
g=defaultdict(list)
for i in range(m):
    a,b=get_ints()
    g[a].append(b)
    g[b].append(a)
vis={}
col=[0 for i in range(n+1)]
for i in range(1,n+1):
    if i not in vis.keys():
        dfs(i,0)
print(check())
    
