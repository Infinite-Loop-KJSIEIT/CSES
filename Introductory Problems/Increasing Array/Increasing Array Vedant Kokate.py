import sys
from sys import stdin
def get_ints(): return map(int, sys.stdin.readline().strip().split())
n=int(input())
#s=stdin.readline()
a=list(get_ints())
ans=0
for i in range(1,n):
    if a[i]<a[i-1]:
        ans+=a[i-1]-a[i]
        a[i]=a[i-1]
print(ans)
        
