import sys 
def get_ints(): return map(int, sys.stdin.readline().strip().split())
 
 
 
def modinv(a):
 
    if a==1:
        return 1
    return (mod-((mod//a)*modinv(mod%a))%mod+mod)%mod
mod=10**9+7
n=int(input())
 
 
d=[0]*(n+1)
d[2]=1
for i in range(3,n+1):
    d[i]=(((d[i-1]+d[i-2])%mod)*(i-1))%mod
print(d[n])