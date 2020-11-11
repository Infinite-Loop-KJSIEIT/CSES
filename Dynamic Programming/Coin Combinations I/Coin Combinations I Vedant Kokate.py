import sys
input=sys.stdin.readline

m,n=map(int,input().split())
c=list(map(int,input().split()))
c.sort()
mod=10**9+7
dp=[0]*(n+1)
dp[0]=1
for i in range(1,n+1):
    for x in c:
        if x>i:
            break
        dp[i]+=dp[i-x]
        dp[i]%=mod
#print(dp)
print(dp[n]%mod)
