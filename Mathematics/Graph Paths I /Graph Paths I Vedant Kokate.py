import math
import sys 
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def mul(a,b):
    r=[[0 for i in range(n)]for j in range(n)]
    for j in range(n):
        for k in range(n):
            for l in range(n):
                r[j][k]=(r[j][k]+(a[j][l]*b[l][k])%mod)%mod
    return r
        
    
 
def modpow(x,pw):
    if pw==0:
        r=[[0 for i in range(n)]for j in range(n)]
        for i in range(n):
            r[i][i]=1
        return r
    u=modpow(x,pw//2)
    u=mul(u,u)
    if pw%2==1: u=mul(u,x)
    return u
 
n,m,k=get_ints()
mod=10**9+7
g=[[0 for i in range(n)]for j in range(n)]
for i in range(m):
    x,y=get_ints()
    g[x-1][y-1]+=1
    
print(modpow(g,k)[0][n-1])
 