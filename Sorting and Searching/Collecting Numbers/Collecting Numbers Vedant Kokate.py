import sys
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
pos=[0]*(n+1)
for i in range(n):
    pos[a[i]]=i
ans=1
#print(pos)
for i in range(2,n+1):
    if pos[i]<pos[i-1]:
        ans+=1
print(ans)
    