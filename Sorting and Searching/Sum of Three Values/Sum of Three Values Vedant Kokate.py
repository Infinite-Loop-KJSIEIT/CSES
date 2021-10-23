import sys
input=sys.stdin.readline
n,x=map(int,input().split())
a=list(map(int,input().split()))
d={}
pos={}
for j in range(n):
    i=a[j]
    pos[a[j]]=j
    if i in d.keys():
        d[i]+=1
    else:
        d[i]=1
for i in range(n):
    #print(i,d[a[i]])
    d[a[i]]-=1
    for j in range(i):
        d[a[j]]-=1
        if x-a[i]-a[j] in d.keys() and d[x-a[i]-a[j]]>0:
            print(i+1,j+1,pos[x-a[i]-a[j]]+1)
            sys.exit()
        d[a[j]]+=1
    d[a[i]]+=1
print("IMPOSSIBLE")



