import time
import math
import sys 
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def ipi(): return int(sys.stdin.readline().strip())
def ips(): return(sys.stdin.readline().strip())
sys.setrecursionlimit(10**6)
def dfs(x,y):
    a[x][y]="#"
    if x+1<n and a[x+1][y]=='.':
        dfs(x+1,y)
    if x-1>-1 and a[x-1][y]=='.':
        dfs(x-1,y)
    if y+1<m and a[x][y+1]=='.':
        dfs(x,y+1)
    if y-1>-1 and a[x][y-1]=='.':
        dfs(x,y-1)
        
 
n,m=get_ints()
a=[]
for i in range(n):
    s=ips()
    l=[]
    l[:0]=s
    
    a.append(l)
 
count=0
for i in range(n):
    for j in range(m):
        if a[i][j]=='.':
            dfs(i,j)
            count+=1
print(count)
 
