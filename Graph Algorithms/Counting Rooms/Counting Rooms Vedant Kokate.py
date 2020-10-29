#import time
#import bisect
#import math
import sys
#import random as r
#from collections import defaultdict 
#from heapq import heapify, heappush, heappop 
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def inp_int(): return int(sys.stdin.readline().strip())
def inp_str(): return(sys.stdin.readline().strip())
def out(output): sys.stdout.write(str(output))
def get_strs(): return  sys.stdin.readline().strip().split()
sys.setrecursionlimit(10**6)

a,ans=[],0
n,m=get_ints()
a=[list(inp_str()) for i in range(n)]
r,c=[0,0,1,-1],[1,-1,0,0]
for i in range(n):
    for j in range(m):
        if a[i][j]=='.':
            ans+=1
            stack=[(i,j)]
            while stack:
                x,y=stack.pop()
                a[x][y]='#'
                for k in range(4):
                    R,C=x+r[k],y+c[k]
                    if 0<=R<n and 0<=C<m and a[R][C]=='.':
                        stack+=[(R,C)]
out(str(ans)+"\n")
 
