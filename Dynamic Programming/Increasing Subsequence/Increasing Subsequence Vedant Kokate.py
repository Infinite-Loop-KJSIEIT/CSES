import sys
from bisect import bisect_left
input=sys.stdin.readline
n= int(input())
a=list(map(int,input().split()))

dp=[0]*n
st=0
end=0
for i in range(n):
    cur=a[i]
    if cur>dp[end-1]:
        dp[end]=cur
        end+=1
    else:
        pos=bisect_left(dp,cur,st,end)
        dp[pos]=cur
print(end)

