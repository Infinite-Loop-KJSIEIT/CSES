import sys
input=sys.stdin.readline

K=25


n,q=map(int,input().split())
st=[[0 for i in range(K+1)]for j in range(n+1)]
a=list(map(int,input().split()))
a.insert(0,0)
n+=1
# print(a)
for i in range(n):
	st[i][0]=a[i]

for j in range(1,K+1):
	i=0
	while i + (1 << j) <= n:
		st[i][j] = st[i][j-1] + st[i + (1 << (j - 1))][j - 1]
		i+=1
# for i in st:
# 	print(i)
for i in range(q):
	L,R=map(int,input().split())
	Sum=0
	for j in range(K,-1,-1):
		if ((1 << j) <= R - L + 1) :
			Sum += st[L][j]
			L += 1 << j
	print(Sum)
	
