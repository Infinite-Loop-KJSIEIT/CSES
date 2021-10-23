#import time
#import bisect
#import math
import sys
#import random as r
from collections import defaultdict
from collections import deque
#from heapq import heapify, heappush, heappop 
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def inp_int(): return int(sys.stdin.readline().strip())
def inp_str(): return(sys.stdin.readline().strip())
def out(output): sys.stdout.write(str(output))
def get_strs(): return  sys.stdin.readline().strip().split()
sys.setrecursionlimit(10**6)
 


n,m=get_ints()
g=defaultdict(list)
for i in range(m):
    a,b=get_ints()
    g[a].append(b)
    g[b].append(a)

vis=[True]*(n+1)
vis[1]=False
parent=[-1]*(n+1)
q=[1]
for node in q:
    for secondnode in g[node]:
        if vis[secondnode]:
            parent[secondnode]=node
            vis[secondnode]=False
            q.append(secondnode)
if vis[n]:
    print("IMPOSSIBLE")
else:
    ans=[]
    while n!=-1:
        ans.append(n)
        n=parent[n]
    print(len(ans))
    print(*reversed(ans))

   
