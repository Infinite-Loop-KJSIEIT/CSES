import sys
input=sys.stdin.readline
n=int(input())
a=[True]*n
count=0
i=0
ans=[]
while count<n:
    
    if a[i]:
        j=i+1
        while not a[j%n]:
            j+=1
            j%=n
        j%=n
        a[j]=False
        count+=1
        
        ans.append(j+1)
        i=j
    i+=1
    i%=n
print(*ans)

    