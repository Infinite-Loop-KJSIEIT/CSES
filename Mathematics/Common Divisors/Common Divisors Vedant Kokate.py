import sys
from itertools import permutations
def get_ints(): return map(int, sys.stdin.readline().strip().split())
 
d={}
n=int(input())
ar=list(get_ints())
for i in ar:
    if i not in d.keys():
        d[i]=1
    else:
        d[i]+=1
m=0
for i in range(1,10**6+1):
    count=0
    for j in range(i,10**6+1,i):
        if j in d.keys():
            count+=d[j]
    if count>1 and i>m:
        m=i
print(m)
