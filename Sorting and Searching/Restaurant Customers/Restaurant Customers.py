import sys
import bisect
import math
from sys import stdin
def get_ints(): return map(int, sys.stdin.readline().strip().split())
 
 
#s=stdin.readline()
n=int(input())
a=[]
b=[]
for _ in range(n):
    x,y=get_ints()
    a.append(x)
    b.append(y)
 
a.sort()
b.sort()
#print(a,b)
i=0
j=0
m=0
Max=0
while i<n and j<n:
  #  print(i,j)
    if a[i]<b[j]:
      #  print("here")
        i+=1
        m+=1
    elif a[i]>a[j]:
        j+=1
        m-=1
    else:
        i+=1
        j+=1
    if m>Max:
        Max=m
print(Max)
