import sys
import math
input=sys.stdin.readline
mod=10**9+7
n=int(input())
p=[]
k=[]
for i in range(n):
    a,b=map(int,input().split())
    p.append(a)
    k.append(b)


COD=SOD=POD=COD2=1
for i in range(n):
    # Count of divisors
    COD*=(k[i]+1)
    COD%=mod
    # Sum of Divisors
    x=pow(p[i],k[i]+1,mod)-1
    y=pow(p[i]-1,mod-2,mod)
    SOD*=(x*y)%mod
    # print('sod',SOD,i)
    SOD%=mod
    # Product of Divisors
    POD=pow(POD,k[i]+1,mod)*pow(pow(p[i],k[i]*(k[i]+1)//2,mod),COD2,mod)
    POD%=mod
    COD2 = COD2 * (k[i] + 1) % (mod - 1)
print(COD,SOD,POD)

