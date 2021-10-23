import sys 
input=sys.stdin.readline
n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
dp=['L']*(n+1)
for i in range(1,n+1):
    for j in a:
        if i-j>=0 and dp[i-j]=='L':
            dp[i]='W'
            break
    # print(dp)

print(''.join(dp[1:]))