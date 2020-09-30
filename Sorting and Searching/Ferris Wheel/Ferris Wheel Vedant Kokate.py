import sys
import math
from sys import stdin
def get_ints(): return map(int, sys.stdin.readline().strip().split())
#s=stdin.readline()
 
n,k=get_ints()
a=list(get_ints())
a.sort()
i=0
j=n-1
d=0
while i<j:
    if a[i]+a[j]<=k:
        d+=1
        i+=1
        
    j-=1
print(n-d)
 
    
    
    
