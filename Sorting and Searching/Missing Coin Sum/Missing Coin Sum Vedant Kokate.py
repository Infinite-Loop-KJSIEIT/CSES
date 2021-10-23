import sys
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
a.sort()
Sum=1
for i in range(n):
    if a[i]<=Sum:
        Sum+=a[i]
    else:
        break
print(Sum)
