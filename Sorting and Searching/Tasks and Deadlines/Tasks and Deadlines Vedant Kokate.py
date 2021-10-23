import sys
from bisect import bisect_right
input=sys.stdin.readline
n=int(input())
a=[]
for i in range(n):a.append(list(map(int,input().split())))
a.sort()
reward=0
f=0
for i in a:
    f+=i[0]
    reward+=i[1]-f
print(reward)


