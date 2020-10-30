import sys 
input = sys.stdin.readline
n,m,q=map(int, input().split())
g=[10**15]*(250000)
for i in range(m):
    a,b,c=map(int, input().split())
    a,b=a-1,b-1
    g[a+b*500]=g[b+a*500]=min(c,g[a+b*500])
for i in range(n):g[i+i*500]=0
for k in range(n):
    for i in range(n):
        opt1=g[i+k*500]
        if k==i or opt1==10**15:
            continue
        for j in range(n):
            g[i+j*500]=min(g[i+j*500],opt1+g[k+j*500])
ans=[]
for i in range(q):
    a,b=map(int, input().split())
    a,b=a-1,b-1
    ans.append(g[a+b*500] if g[a+b*500]<10**15 else -1)
for i in ans:
    print(i)
