import sys
import math
input=sys.stdin.readline
mod=10**9+7

n=int(input())
sq=math.sqrt(n)
# contri from 1 to sq
i=1
ans=0
while i<=sq:
    ans+=(n//i)*i
    i+=1
# print(ans)
# contri from sq to n/2
i=1
while i<sq:
    l=n//(i+1)+1
    r=n//i
    if l<=sq:
        i+=1
        continue
    Sum=(r-l+1)*(r+l)//2
    # print(Sum,i,l,r)
    ans+=Sum*i
    i+=1
print(ans%mod)