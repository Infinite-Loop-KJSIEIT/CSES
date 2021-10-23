import time
import bisect
import math
import sys
import random as r
from copy import copy, deepcopy
from collections import defaultdict
from heapq import heapify, heappush, heappop
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def inp_int(): return int(sys.stdin.readline().strip())
def inp_str(): return(sys.stdin.readline().strip())
def out(output): sys.stdout.write(str(output))
def get_strs(): return  sys.stdin.readline().strip().split()
sys.setrecursionlimit(10**6)
 
INF = 10**10
def negcycle():
    #for i in dist: print(i)
    for i in range(n):
        for a,b,c in g:
            if dist[a]+c<dist[b]:
                dist[b]=-INF
    if dist[n]==-INF:
        return -1
    else:
        return dist[n]*-1
 
def floydWarshall(dist):
    for k in range(n):
        for a,b,c in g:
            dist[b]= min(dist[b] ,dist[a]+ c)
 
 
n,m=get_ints()
 
dist=[INF]*(n+1)
dist[1]=0
g=[]
for i in range(m):
    a,b,c=get_ints()
    g.append((a,b,-c))
floydWarshall(dist)
x=negcycle()
print( x  )
