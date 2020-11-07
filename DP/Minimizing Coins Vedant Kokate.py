import sys
input=sys.stdin.readline

n,m=map(int,input().split())
c=list(map(int,input().split()))

d=[m+1]*(m+1)

d[0]=0
for coins in c:
    for i in range(coins,m+1):
        if d[i]>d[i-coins]+1:
            d[i]=d[i-coins]+1
print(-1 if d[m]==m+1 else d[m])
