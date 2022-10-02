from sys import stdin, stdout
import sys 
def get_ints(): return map(int, sys.stdin.readline().strip().split())
#n = stdin.readline()
def find(y):
   # print("y",y)
    l=0
    u=n-1
    while l<=u:
        m=(l+u)//2
        if a[m][0]==y:
            return [True,a[m][1]]
        if a[m][0]>y:
            u=m-1
        else:
            l=m+1
    return [False,-1]
def solve():
    if len(a)==1:
        return [-1,-1]
    for i in range(n):
        if x==2*a[i][0]:
            if a[i-1][0]==x//2:
                return [a[i-1][1]+1,a[i][1]+1]
            else:
                continue
        ans=find(x-a[i][0])
       
       # print(ans,a[i])
        if ans[0]:
            return [a[i][1]+1,ans[1]+1]
    return[-1,-1]
 
n,x=get_ints()
temp=list(get_ints())
a=[]
for i in range(n):
    a.append([temp[i],i])
a.sort()
#print(a)
ans=solve()
if ans[0]==-1:
    print("IMPOSSIBLE")
else:
#print(ans)
    print(ans[0],ans[1])
