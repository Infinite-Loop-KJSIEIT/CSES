import sys
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
mod=[0]*n
 
sum=0
ans=0
for i in a:
    sum+=i
    mod[sum%n]+=1
for i in mod:
    ans+=i*(i-1)//2
print(ans+mod[0])