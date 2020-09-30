import sys
import math
from sys import stdin
def get_ints(): return map(int, sys.stdin.readline().strip().split())
 
n=int(input())
a=list(get_ints())
a.sort()
ans=1
for i in range(1,n):
    if a[i]!=a[i-1]:
        ans+=1
print(ans)
