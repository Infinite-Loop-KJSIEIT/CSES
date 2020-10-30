#import time
#import bisect
#import math
import sys
#import random as r
from collections import defaultdict 
#from heapq import heapify, heappush, heappop 
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def inp_int(): return int(sys.stdin.readline().strip())
def inp_str(): return(sys.stdin.readline().strip())
def out(output): sys.stdout.write(str(output))
def get_strs(): return  sys.stdin.readline().strip().split()
sys.setrecursionlimit(10**6)
from collections import defaultdict 

def dfs(x):
        for e in g[x]:
                if p[e]<0:
                        p[e]=x
                        dfs(e)
                elif e!=p[x]:
                        #print(e,x,p)
                        ans=[e]
                        while x!=p[e]:
                                ans.append(x)
                                x=p[x]
                        print(len(ans))
                        print(*ans)
                        raise SystemExit
                                


n,m=get_ints()
g=defaultdict(list)
for i in range(m):
        a,b=get_ints()
        g[a].append(b)
        g[b].append(a)
p=[-1]*(n+1)

for x in range(1,n+1):
        if p[x]==-1:
                p[x]=0
                dfs(x)
print("IMPOSSIBLE")
