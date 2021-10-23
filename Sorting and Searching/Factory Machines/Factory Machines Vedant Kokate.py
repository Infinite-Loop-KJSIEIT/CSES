import sys
from bisect import bisect_right
input=sys.stdin.readline
def mac(time):
    val=0
    for i in k:
        val+=time//i
    #print(time,val)
    return val

n,t=map(int,input().split())
k=list(map(int,input().split()))
u=10**18
l=0
while l<u:
    mid=(l+u)//2
    prod=mac(mid)
    if prod<t:
        l=mid+1
    else:
        u=mid
print(max(u,l))

