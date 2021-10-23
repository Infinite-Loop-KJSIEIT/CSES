import sys
input=sys.stdin.readline
n,x=map(int,input().split())
a=list(map(int,input().split()))
dp={}
for i in range(n):
    for j in range(i+1,n):
        y=x-a[i]-a[j]
        if y in dp.keys():
            print(i+1,j+1,dp[y][0],dp[y][1])
            sys.exit()
    for j in range(i):
        dp[a[i]+a[j]]=(i+1,j+1)
print("IMPOSSIBLE")



