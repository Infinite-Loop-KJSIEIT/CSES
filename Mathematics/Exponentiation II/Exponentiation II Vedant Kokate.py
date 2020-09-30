import sys
from itertools import permutations
def get_ints(): return map(int, sys.stdin.readline().strip().split())
 
n=int(input())
mod=10**9+7
for i in range(n):
    a,b,c=get_ints()
    bc=pow(b,c,mod-1)
    print(pow(a,bc,mod))
