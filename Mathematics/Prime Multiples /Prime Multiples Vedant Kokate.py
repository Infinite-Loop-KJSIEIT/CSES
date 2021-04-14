import sys
import math
input=sys.stdin.readline
n,k=map(int,input().split())
p=list(map(int,input().split()))
ans=0
for i in range(1,1<<k):
    prod=1
    cnt=0
    for j in range(k):
        if i&(1<<j):
            prod*=p[j]
            cnt+=1
    if cnt%2:
        ans+=n//prod
    else:
        ans-=n//prod
print(ans)




