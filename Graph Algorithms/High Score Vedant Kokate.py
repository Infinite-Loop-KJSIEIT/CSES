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
def negcycle(dist):
    #for i in dist: print(i)
    for i in range(n):
        if dist[i][i]<0 and dist[i][n-1]<10**9 and dist[0][i]<10**9:
            return -1
    return dist[0][n-1]*-1

def floydWarshall(dist):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j] ,dist[i][k]+ dist[k][j])


n,m=get_ints()

dist=[[INF for i in range(n)]for j in range (n)]
for i in range(n):dist[i][i]=0
for i in range(m):
    a,b,d=get_ints()
    dist[a-1][b-1]=d*-1
    #dist[b-1][a-1]=d*-1


floydWarshall(dist)
x=negcycle(dist)
print( x if x!=10**10 else -1 )

