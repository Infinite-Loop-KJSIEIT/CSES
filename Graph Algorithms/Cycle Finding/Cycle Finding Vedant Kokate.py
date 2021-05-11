import sys
input=sys.stdin.readline
n, m = map(int, input().split())
g=[]
for i in range(m):
    a,b,w=map(int,input().split())
    a-=1
    b-=1
    g.append([a,b,w])
d=[0]*n
p=[-1]*n
x=-1


for i in range(n):
    x=-1
    for a,b,w in g:
        if d[a]+w<d[b]:
            d[b]=d[a]+w
            p[b]=a
            x=b
# print(d)
# print(p,x)
if x==-1:
    print("NO")
else:
    
    for i in range(n):
        x=p[x]
    cycle=[]
    v=x
    # print(p[10:])
    while True:
        # print(v)
        cycle.append(v+1)
        if v==x and len(cycle)>1:
            break
        v=p[v]
    cycle=reversed(cycle)
    print("YES")
    print(*cycle)



