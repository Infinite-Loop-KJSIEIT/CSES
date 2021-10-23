
import sys
input=sys.stdin.readline
n,m=map(int, input().split())
x=list(map(int, input().split()))
mod=10**9+7
dp=[[0 for i in range(m+1)]for j in range(n)]
for i in range(n):
	if i==0:
		dp[i][x[i]]=1 if x[i]!=0 else 0
		if x[i]==0:
			for j in range(1,m+1):
				dp[i][j]=1
	elif x[i]==0:
		for j in range(1,m+1):
			dp[i][j]=dp[i-1][j]
			dp[i][j]%=mod
			if j>0:
				dp[i][j]+=dp[i-1][j-1]
				dp[i][j]%=mod
			if j<m:
				dp[i][j]+=dp[i-1][j+1]
				dp[i][j]%=mod
	else:
		dp[i][x[i]]=dp[i-1][x[i]]
		dp[i][x[i]]%=mod
		dp[i][x[i]]+=dp[i-1][x[i]-1]
		dp[i][x[i]]%=mod
		if x[i]<m:
			dp[i][x[i]]+=dp[i-1][x[i]+1]
			dp[i][x[i]]%=mod
		
print(sum(dp[n-1])%mod)
