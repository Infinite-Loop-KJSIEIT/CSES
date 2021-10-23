import math
import sys 
input=sys.stdin.readline
# def get_ints(): return map(int, sys.stdin.readline().strip().split())
def mul(a,b):
    r=[[INF for i in range(n)]for j in range(n)]
    for j in range(n):
        for k in range(n):
            for l in range(n):
                r[j][k]=min(r[j][k],(a[j][l]+b[l][k]))
    return r
        
    
 
def modpow(x,pw):
    if pw==1:return x
    u=modpow(x,pw//2)
    u=mul(u,u)
    if pw%2: u=mul(u,x)
    return u  

n,m,k=map(int,input().split())
# mod=10**9+7
INF=10**18+1
g=[[INF for i in range(n)]for j in range(n)]
for i in range(m):
    x,y,z=map(int,input().split())
    g[x-1][y-1]=min(g[x-1][y-1],z)
    
ans=modpow(g,k)[0][n-1]
if ans>=INF:print(-1)
else: print(ans)
 