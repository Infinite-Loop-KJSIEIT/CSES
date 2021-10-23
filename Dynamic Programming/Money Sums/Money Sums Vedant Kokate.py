import sys
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
dp=[False]*(10**5+1)
dp[0]=True
for i in range(n):
    cur=a[i]
    for j in range(10**5,cur-1,-1):
        if dp[j-cur]:dp[j]=True
ans=[]
for i in range(1,10**5+1):
    if dp[i]:ans.append(i)
print(len(ans))
print(*ans)

