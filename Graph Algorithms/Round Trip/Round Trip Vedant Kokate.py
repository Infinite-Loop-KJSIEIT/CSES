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
        #print(x)
        q=[x]
        while q:
                #print(q)
                #print(p)
                cur=q.pop()
                for node in g[cur]:
                        if p[node]==-1 and p[cur]!=node:
                                p[node]=cur
                                q.append(node)
                                break
                        else:
                                print(cur,node)
                                if p[cur]!=node:
                                        ans=[node,cur]
                                        while cur!=node:
                                                cur=p[cur]
                                                ans.append(cur)
                                        print(len(ans))
                                        print(*ans)
                                        return True
        
        print("IMPOSSIBLE")
        return False


n,m=get_ints()
g=defaultdict(list)
q=[1]
for i in range(m):
        a,b=get_ints()
        g[a].append(b)
        g[b].append(a)
p=[-1]*(n+1)
for i in range(1,n+1):
        if p[i]==-1:
                
                if dfs(i):
                        break
