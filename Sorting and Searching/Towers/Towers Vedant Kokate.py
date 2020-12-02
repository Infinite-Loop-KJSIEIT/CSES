import sys
from bisect import bisect_right
input=sys.stdin.readline
n=int(input())
towers=[]
for i in list(map(int,input().split())):
    pos=bisect_right(towers,i)
    if pos>=len(towers):
        towers.append(i)
    else:
        towers[pos]=i
print(len(towers))
