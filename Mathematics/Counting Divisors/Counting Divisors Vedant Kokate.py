import sys
from itertools import permutations
def get_ints(): return map(int, sys.stdin.readline().strip().split())
 
a=[1]*(10**6+1)
for i in range(1,10**6+1):
    for j in range(i*2,10**6+1,i):
        a[j]+=1
 
n=int(input())
for _ in range(n):
    x=int(input())
    print(a[x])
