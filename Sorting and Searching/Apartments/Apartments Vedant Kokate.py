import sys
import math
from sys import stdin
def get_ints(): return map(int, sys.stdin.readline().strip().split())
#s=stdin.readline()
 
n,m,k=get_ints()
a=list(get_ints())
b=list(get_ints())
a.sort()
b.sort()
#print(a)
#print(b)
i=j=ans=0
while i<n and j<m:
   # print(i,j)
    if abs(a[i]-b[j])<=k:
        ans+=1
        i+=1
        j+=1
    else:
        if a[i]>b[j]:
            j+=1
        else:
            i+=1
print(ans)
    
 
    
    
