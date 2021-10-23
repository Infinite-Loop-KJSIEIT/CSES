import sys
input=sys.stdin.readline
n= int(input())
half=n*(n+1)//2
if half%2==1:
    print(0)
    sys.exit()
half//=2
mod=10**9+7
dp=[0]*(half+1)
dp[0]=1
for i in range(1,n):
    for j in range(half,i-1,-1):
        dp[j]+=dp[j-i]
        dp[j]%=mod
    
#print(dp)
print(dp[half]%mod)
