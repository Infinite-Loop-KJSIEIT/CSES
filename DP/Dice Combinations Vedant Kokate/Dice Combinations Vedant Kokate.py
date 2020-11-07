import sys
input=sys.stdin.readline

n=int(input())
mod=10**9+7
dp=[0]*(n+1)
dp[0]=1
for i in range(1,n+1):
    for x in range(1,7):
        if x>i:
            break
        dp[i]+=dp[i-x]
        dp[i]%=mod
#print(dp)
print(dp[n]%mod)
