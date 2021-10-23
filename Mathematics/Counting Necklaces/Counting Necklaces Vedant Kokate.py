import math
n,k=map(int,input().split())
def inv(x):
    return pow(x,mod-2,mod)
mod=10**9+7
print((sum(pow(k,math.gcd(i,n),mod) for i in range(1,n+1))*inv(n))%mod)