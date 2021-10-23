import sys
input=sys.stdin.readline
def score(x,y):
    ans=0
    check=set()
    check.add((x,x+1))
    check.add((x-1,x))
    check.add((y,y+1))
    check.add((y-1,y))
    for (a,b) in check:
        if 1<=a<=n and 1<=b<=n and pos[a]>pos[b]:
            ans+=1 
   
    return ans
n,m=map(int,input().split())
a=list(map(int,input().split()))
pos=[0]*(n+1)
for i in range(n):
    pos[a[i]]=i
ans=1

for i in range(2,n+1):
    if pos[i]<pos[i-1]:
        ans+=1

for q in range(m):
    
    x,y=map(int,input().split())
    x-=1
    y-=1
    Score=score(a[x],a[y])*-1
    temp=a[x]
    a[x]=a[y]
    a[y]=temp
    pos[a[x]]=x
    pos[a[y]]=y
    Score+=score(a[x],a[y])
    ans+=Score
    print(ans)


    