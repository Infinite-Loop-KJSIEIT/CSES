import sys
input=sys.stdin.readline
def binary():
    l=0
    u=i-1
    while l<u:
        m=(l+u)//2
        if a[m][0]<a[i-1][1]:
            l=m+1
        else :
            u=m-1
    return(min(l,u))
        



n=int(input())
a=[]
for i in range(n):a.append(list(map(int,input().split())))
a.sort(key=lambda x:x[1])
dp=[0]*(n+1)
for i in a:print(i)
for i in range(1,n+1):
    pos=binary()
    print(i,pos,'pos')
    dp[i]=max(dp[i-1],a[i-1][2]+dp[pos])
print(dp)
