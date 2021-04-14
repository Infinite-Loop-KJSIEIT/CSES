import sys 
def get_ints(): return map(int, sys.stdin.readline().strip().split())
 
 
 
def modinv(a):
 
    if a==1:
        return 1
    return (mod-((mod//a)*modinv(mod%a))%mod+mod)%mod
mod=10**9+7
ch=[0]*26
s=sys.stdin.readline().strip()
n=len(s)
f=[1]*(n+1)
for i in range(2,n+1):
    f[i]=(f[i-1]*i)%mod
ch=[0]*26
 
for i in s:
    ch[ord(i)-ord('a')]+=1
 
ans=f[n]
for i in ch:
    ans*=modinv(f[i])
    ans%=mod
 
print(ans)