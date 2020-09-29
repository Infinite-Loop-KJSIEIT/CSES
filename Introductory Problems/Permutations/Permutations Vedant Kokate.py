import sys
import math
from sys import stdin
def get_ints(): return map(int, sys.stdin.readline().strip().split())
n=int(input())
#s=stdin.readline()
if n==3 or n==2:
    print("NO SOLUTION")
elif n==4:
    print("2 4 1 3")
else:
    a=1
    b=math.ceil(n/2)+1
    for i in range(n):
        if i%2==0:
            print(a,end=" ")
            a+=1
        else:
            print(b,end=" ")
            b+=1
    
