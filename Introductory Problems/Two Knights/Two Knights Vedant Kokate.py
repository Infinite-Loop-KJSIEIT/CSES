import sys
import math
from sys import stdin
def get_ints(): return map(int, sys.stdin.readline().strip().split())
 
def solve(x):
    return (x*x*(x*x-1))//2-4*(x-2)*(x-1)
 
n=int(input())
for i in range(1,n+1):
    print(solve(i))
    
