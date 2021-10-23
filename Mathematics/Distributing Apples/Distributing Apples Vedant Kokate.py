import sys 
def get_ints(): return map(int, sys.stdin.readline().strip().split())
 
 
 
def modinv(a):
 
    if a==1:
        return 1
    return (mod-((mod//a)*modinv(mod%a))%mod+mod)%mod
mod=10**9+7
n,m=get_ints()
 
f=[1]*(2*10**6+1)
for i in range(2,2*10**6+1):
    f[i]=(f[i-1]*i)%mod
#print(f[:10])
ans=f[n+m-1]*modinv(f[n-1])%mod
ans*=modinv(f[m])
ans%=mod
print(ans)