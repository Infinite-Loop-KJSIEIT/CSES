import sys
input=sys.stdin.readline

n=int(input())
dp=[10**9]*(n+1)
dp[0]=0
for i in range(1,n+1):
    for c in str(i):
        l=i-ord(c)+48
        if l>=0:
            dp[i]=min(dp[i],dp[l]+1)
print(dp[n])
