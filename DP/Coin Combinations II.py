import sys
from itertools import permutations
def get_ints(): return map(int, sys.stdin.readline().strip().split())
n,target=get_ints()
mod=10**9+7
c=list(get_ints())
dp=[[0 for j in range(target+1)]for i in range(n+1)]

dp[0][0]=1
for i in range(1,n+1):
    for j in range(target+1):
        dp[i][j]=dp[i-1][j]
        if j-c[i-1]>=0:
            dp[i][j]+=dp[i][j-c[i-1]]
            dp[i][j]%=mod
print(dp[n][target])

