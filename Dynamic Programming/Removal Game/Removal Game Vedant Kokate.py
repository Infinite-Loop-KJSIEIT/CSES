import sys
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
dp=[[0 for i in range(n)]for j in range(n+1)]

for l in range(n-1,-1,-1):
    for r in range(n):
        if l==r:
            dp[l][r]=a[l]
        else:
            dp[l][r]=max(a[l]-dp[l+1][r],a[r]-dp[l][r-1])
print((sum(a)+dp[0][n-1])//2)

