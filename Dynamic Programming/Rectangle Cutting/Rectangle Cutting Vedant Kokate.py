import sys
input=sys.stdin.readline
a,b=map(int,input().split())
dp=[[0 for i in range(b+1)]for j in range(a+1)]

for i in range(1,a+1):
	for j in range(1,b+1):
		if i!=j:
			temp=10**6
			for k in range(1,i//2+1):
				val=dp[k][j]+dp[i-k][j]+1
				if temp>val:
					temp=val
			for k in range(1,j//2+1):
				val=dp[i][k]+dp[i][j-k]+1
				if temp>val:
					temp=val
			dp[i][j]=temp
				
print(dp[-1][-1])
