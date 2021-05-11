import sys
input=sys.stdin.readline
n,k=map(int,input().split())
a=list(map(int,input().split()))
start=max(a)
end=sum(a)
ans=-1
while start<=end:
    mid=(start+end)//2
    subsum=0
    numofSubArrays=1
    for i in range(n):
        if subsum+a[i]>mid:
            subsum=a[i]
            numofSubArrays+=1
        else:
            subsum+=a[i]
    if numofSubArrays<=k:
        ans=mid
        end=mid-1
    else:
        start=mid+1
print(ans)

