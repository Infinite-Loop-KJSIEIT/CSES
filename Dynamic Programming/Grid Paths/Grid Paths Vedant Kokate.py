import sys
input=sys.stdin.readline
n=int(input())
mod=10**9+7
dp=[[0 for i in range(n)] for j in range(n)]
dp[0][0]=1
 
for i in range(n):
    s=input()
    for j in range(n):
        if s[j]=='.':
            if i>0:
                dp[i][j]+=dp[i-1][j]
                dp[i][j]%=mod
            if j>0:
                dp[i][j]+=dp[i][j-1]
                dp[i][j]%=mod
        else:
            dp[i][j]=0
print(dp[n-1][n-1])
