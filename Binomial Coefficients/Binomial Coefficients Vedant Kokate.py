import sys
from itertools import permutations
def get_ints(): return map(int, sys.stdin.readline().strip().split())
 
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
 
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
mod=10**9+7
ar=[1]*(10**6+1)
for i in range(1,10**6+1):
    ar[i]=ar[i-1]*i%mod
 
t=int(input())
for _ in range(t):
    n,c=get_ints()
    print(ar[n]%mod*pow(ar[n-c],mod-2,mod)%mod*pow(ar[c],mod-2,mod)%mod)
