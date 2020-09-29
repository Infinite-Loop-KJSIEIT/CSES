import sys
import math
from sys import stdin
def get_ints(): return map(int, sys.stdin.readline().strip().split())
n=int(input())
#s=stdin.readline()
for _ in range(n):
    x,y=get_ints()
    if x>=y:
        t=x*(x-1)+1
        if x%2==0:
            print(t+x-y)
        else:
            print(t-x+y)
    else:
        t=y*(y-1)+1
        if y%2==0:
            print(t-y+x)
        else:
            print(t+y-x)
