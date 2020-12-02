import sys
input=sys.stdin.readline
n=int(input())
t=list(map(int,input().split()))
s=sum(t)
m=max(t)
print(m*2 if m>s-m else s)


