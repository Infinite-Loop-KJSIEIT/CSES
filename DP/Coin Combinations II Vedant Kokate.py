import sys
input=sys.stdin.readline

m,n=map(int,input().split())
c=list(map(int,input().split()))
c.sort()
mod=10**9+7
dp=[0]*(n+1)
dp[0]=1
for i in c:
    for j in range(i,n+1):
        dp[j]+=dp[j-i]
        dp[j]%=mod
#print(dp)
print(dp[n]%mod)
