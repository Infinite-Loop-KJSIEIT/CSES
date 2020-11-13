import sys
input=sys.stdin.readline
m,n=map(int, input().split())
H=map(int, input().split())
S=map(int, input().split())
dp=[0]*(n+1)
for h,s in zip(H,S):
	for j in range(n,h-1,-1):
		dp[j]=max(dp[j],dp[j-h]+s)
print(dp[n])
