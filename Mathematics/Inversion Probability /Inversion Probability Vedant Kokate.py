import sys 
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
ans=0
for i in range(n):
    for j in range(i):
        if a[j]<=a[i]:
            ans+=(a[j]*(a[j]-1)//2)/(a[i]*a[j])
        else:
            ans+=(a[i]*(a[i]-1)//2 + (a[j]-a[i])*a[i])/(a[i]*a[j])
print(f"{ans:.6f}")

