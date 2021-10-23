import sys
input=sys.stdin.readline
dp=[[0]*2 for i in range(10**6+1)]
dp[1][0]=1
dp[1][1]=1
mod=10**9+7
for i in range(2,10**6+1):
    dp[i][0]=(dp[i-1][0]*4+dp[i-1][1])%mod
    dp[i][1]=(dp[i-1][0]+dp[i-1][1]*2)%mod
for t in range(int(input())):
    n=int(input())
    print((dp[n][0]+dp[n][1])%mod)
# print('done')