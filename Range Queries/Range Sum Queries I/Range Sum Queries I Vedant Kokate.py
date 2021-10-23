import sys
input=sys.stdin.readline
n,q=map(int,input().split())
a=list(map(int,input().split()))
a.insert(0,0)
for i in range(1,n+1):
	a[i]+=a[i-1]
for i in range(q):
	x,y=map(int,input().split())
	print(a[y]-a[x-1])
